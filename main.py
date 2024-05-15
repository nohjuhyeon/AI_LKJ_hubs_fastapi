from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from apscheduler.schedulers.background import BackgroundScheduler

from dotenv import load_dotenv
import openai
import os
import re

# Models
from models.plan_trip import ReserveTransferTotal, ReserveDorm, ReserveTour
from models.admin_notice import Admin_notice_list
from models.frequent_CS import FAQ_list
from models.data_chart import data_attraction, data_concept_search, data_consume, data_consume_transition, data_trend_search
from models.user_list import User_list

# Routes
from routes.admin import router as admin_router
from routes.mypage import router as second_router
from routes.plan_trip import router as users_router
from routes.consult import router as consult_router
from routes.consult_api import router as consult_api_router
from routes.plan_trip_api import router as plan_trip_api_router
from routes.event import router as event_router
from routes.detailed_region import router as detailed_router

load_dotenv()

app = FastAPI()

# Middleware 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files 설정
app.mount("/css", StaticFiles(directory="resources/css/"), name="static_css")
app.mount("/images", StaticFiles(directory="resources/images/"), name="static_images")

templates = Jinja2Templates(directory="templates/")

# MongoDB 초기화
@app.on_event("startup")
async def on_startup():
    mongo_url = os.getenv("DATABASE_URL")
    client = AsyncIOMotorClient(mongo_url)
    try:
        # MongoDB 서버 상태 확인
        await client.server_info()
    except Exception as e:
        print("MongoDB 서버에 연결할 수 없습니다:", e)
        raise HTTPException(status_code=500, detail="MongoDB 서버에 연결할 수 없습니다.")
    
    database = client["AI_LKJ"]
    await init_beanie(
        database,
        document_models=[
            ReserveTransferTotal,
            ReserveDorm,
            ReserveTour,
            Admin_notice_list,
            FAQ_list,
            data_attraction,
            data_concept_search,
            data_consume,
            data_consume_transition,
            data_trend_search,
            User_list,
        ],
    )

    # 스케줄러 초기화 (비활성화된 상태)
    # scheduler = BackgroundScheduler()
    # scheduler.start()

# 라우터 포함
app.include_router(admin_router, prefix="/admin")
app.include_router(second_router, prefix="/mypage")
app.include_router(users_router, prefix="/plan_trip")
app.include_router(consult_router, prefix="/consult")
app.include_router(consult_api_router, prefix="/consult_api")
app.include_router(plan_trip_api_router, prefix="/plan_trip_api")
app.include_router(event_router, prefix="/event")
app.include_router(detailed_router, prefix="/detailed_region")

# 메인 페이지
@app.get("/")
async def main_get(request: Request):
    return templates.TemplateResponse("main.html", {'request': request})

@app.post("/")
async def main_post(request: Request):
    await request.form()
    return templates.TemplateResponse("main.html", {'request': request})

# 로그인 페이지
@app.get("/login")
async def login_get(request: Request):
    user_list = await User_list.find_all().to_list()
    return templates.TemplateResponse("login.html", {
        'request': request,
        'user_list': user_list
    })

# 로그인 확인
@app.post("/login_check")
async def login_check(request: Request):
    form_data = await request.form()
    user_list = await User_list.find_all().to_list()
    email_list = [user.user_email for user in user_list]
    password_list = [user.user_password for user in user_list]

    if form_data["login_email"] in email_list:
        user_index = email_list.index(form_data["login_email"])
        if password_list[user_index] == form_data["login_password"]:
            return templates.TemplateResponse("login_complete.html", {
                'request': request,
                'user_dict': user_list[user_index]
            })
        else:
            return templates.TemplateResponse("login_fail.html", {'request': request})
    else:
        return templates.TemplateResponse("login_fail.html", {'request': request})

# 회원가입 완료
@app.post("/login_insert")
async def login_insert(request: Request):
    form_data = await request.form()
    user_list = await User_list.find_all().to_list()
    email_list = [user.user_email for user in user_list]
    name_list = [user.user_name for user in user_list]

    if form_data["user_email"] in email_list:
        return templates.TemplateResponse("insert_email_error.html", {'request': request})
    elif form_data["user_password"] != form_data["password_check"]:
        return templates.TemplateResponse("insert_password_error.html", {'request': request})
    elif form_data["user_name"] in name_list:
        return templates.TemplateResponse("insert_name_error.html", {'request': request})
    else:
        new_user = User_list(**form_data)
        await new_user.insert()
        return templates.TemplateResponse("insert_interesting_region.html", {
            'request': request,
            'user_dict': form_data
        })

# 커뮤니티 페이지
@app.get("/community")
async def community_get(request: Request):
    return templates.TemplateResponse("community.html", {'request': request})

@app.post("/community")
async def community_post(request: Request):
    await request.form()
    return templates.TemplateResponse("community.html", {'request': request})

# 회원가입 페이지
@app.get("/insert")
async def insert_get(request: Request):
    return templates.TemplateResponse("insert.html", {'request': request})

@app.post("/insert")
async def insert_post(request: Request):
    await request.form()
    return templates.TemplateResponse("insert.html", {'request': request})

# OpenAI API 설정
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# OpenAI 테마 추천
def recommend_themes(destination):
    prompt = f"As a travel planner, create three broad travel themes suitable for a trip to {destination}, such as 'Gastronomy', 'Nature & Relaxation', 'Cultural Exploration'. Please focus on broad categories only, without any descriptions about the themes, and avoid any season-related themes. All responses should be translated into Korean."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": "You are a travel planner, and your responses must be in Korean, focusing solely on broad themes."},
                {"role": "user", "content": prompt}
            ]
        )
        themes_text = response['choices'][0]['message']['content'].strip()
        themes = re.split(r'\b[1-3][.)] ', themes_text)
        return [theme.strip() for theme in themes if theme.strip()]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/plan_trip/reco_themes/", response_class=HTMLResponse)
async def reco_themes(request: Request):
    form_data = await request.form()
    destination = form_data.get('arrive')
    themes = recommend_themes(destination)
    return templates.TemplateResponse("plan_trip/reco_themes.html", {
        'request': request,
        'themes': themes,
        'destination': destination,
        'depart': form_data.get('depart'),
        'transfer_mem': form_data.get('transfer_mem'),
        'depart_date': form_data.get('depart_date'),
        'arrive_date': form_data.get('arrive_date')
    })

# OpenAI detailed itinerary recommendation
def generate_itinerary(departure, destination, people, theme, start_date, end_date):
    detailed_prompt = f"""
    As a travel planner, create a detailed itinerary for {people} people traveling from {departure} to {destination} from {start_date} to {end_date}. 
    Include the following details:
    - Theme: {theme}
    - Recommended activities for morning, afternoon, and evening each day.
    - Cultural sites and dining options that are popular among locals.
    - Transportation advice between locations within the destination.
    Please structure all responses in an HTML table format that can be styled with CSS, with separate rows for morning, afternoon, and evening activities each day. Each activity should be detailed and the table should be ready for professional presentation in a web interface. Ensure that all responses are accurately provided and translated into Korean.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": "You are a travel planner."},
                {"role": "user", "content": detailed_prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/plan_trip/trip_itinerary/", response_class=HTMLResponse)
async def plan_trip(request: Request):
    form_data = await request.form()
    itinerary = generate_itinerary(
        departure=form_data.get('depart'),
        destination=form_data.get('destination'),
        people=form_data.get('transfer_mem'),
        theme=form_data.get('theme'),
        start_date=form_data.get('depart_date'),
        end_date=form_data.get('arrive_date')
    )
    return templates.TemplateResponse("plan_trip/trip_itinerary.html", {'request': request, 'itinerary': itinerary})
