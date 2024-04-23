from fastapi import FastAPI               
app = FastAPI()

from databases.connections import Settings
from beanie import PydanticObjectId
from apscheduler.schedulers.background import BackgroundScheduler
from seleniums.kto9suk9suk_scraping import kto9suk9suk_scraping
from seleniums.yeomi_scraping import yeomi_scraping
# from sample_function import message_print, job_print
import datetime

settings = Settings()
@app.on_event("startup")
async def init_db():
    await settings.initialize_database()
    scheduler = BackgroundScheduler()
    scheduler.add_job(kto9suk9suk_scraping, trigger='cron', hour=0, minute=0)    
    scheduler.add_job(kto9suk9suk_scraping, trigger='cron', hour=4, minute=0)    
    scheduler.add_job(kto9suk9suk_scraping, trigger='cron', hour=8, minute=0)    
    scheduler.add_job(kto9suk9suk_scraping, trigger='cron', hour=12, minute=0)    
    scheduler.add_job(kto9suk9suk_scraping, trigger='cron', hour=16, minute=0)    
    scheduler.add_job(kto9suk9suk_scraping, trigger='cron', hour=20, minute=0)    
    scheduler.add_job(yeomi_scraping, trigger='cron', hour=2, minute=0)
    scheduler.add_job(yeomi_scraping, trigger='cron', hour=6, minute=0)
    scheduler.add_job(yeomi_scraping, trigger='cron', hour=10, minute=0)
    scheduler.add_job(yeomi_scraping, trigger='cron', hour=14, minute=0)
    scheduler.add_job(yeomi_scraping, trigger='cron', hour=18, minute=0)
    scheduler.add_job(yeomi_scraping, trigger='cron', hour=22, minute=0)

# 스케줄러 시작
    scheduler.start()

from routes.admin import router as admin_router                   
from routes.mypage import router as second_router
from routes.plan_trip import router as users_router
from routes.consult import router as consult_router
from routes.event import router as event_router
from routes.detailed_region import router as detailed_router

app.include_router(admin_router, prefix="/admin")
app.include_router(second_router, prefix="/mypage")
app.include_router(users_router, prefix="/plan_trip")
app.include_router(consult_router, prefix="/consult")
app.include_router(event_router, prefix="/event")
app.include_router(detailed_router, prefix="/detailed_region")

from fastapi import Request                                
from fastapi.templating import Jinja2Templates              
from databases.connections import Database

from models.user_list import User_list # 컬랙션을 연결하고, 컬렉션에 저장/불러오기 하는 방법 
collection_user_list = Database(User_list)
from models.reserve_transfer import transfer_car_list
collection_transfer_car_list = Database(transfer_car_list)


from fastapi.middleware.cors import CORSMiddleware             
app.add_middleware(
    CORSMiddleware,            
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi.staticfiles import StaticFiles
# # url 경로(url에서 입력해야 하는 주소), 자원 물리 경로(directory; 실제 경로), 프로그래밍 측면(key의 이름 지정)
app.mount("/css", StaticFiles(directory="resources\\css\\"), name="static_css")
app.mount("/images", StaticFiles(directory="resources\\images\\"), name="static_images")



templates = Jinja2Templates(directory="templates/")    

# 메인 페이지로 이동
@app.get("/")                     
async def main_get(request:Request):
    print(dict(request._query_params))
    return templates.TemplateResponse("main.html",{'request':request})

@app.post("/")                      
async def main_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse("main.html",{'request':request})

# 로그인 페이지로 이동
@app.get("/login")                     
async def login_get(request:Request):
    print(dict(request._query_params))
    user_list = await collection_user_list.get_all()
    
    print(user_list)
    list_user_id = []
    list_user_email = []
    list_user_pswd = []
    for i in range(len(user_list)):
        list_user_id.append(dict(user_list[i])["id"])
        list_user_email.append(dict(user_list[i])["user_email"])
        list_user_pswd.append(dict(user_list[i])["user_password"])
    print(list_user_id)
    print(list_user_email)
    print(list_user_pswd)
    pass
    return templates.TemplateResponse("login.html",{'request':request,
                                                    'user_id':list_user_id,
                                                    'user_email': list_user_email,
                                                    'user_pswd': list_user_pswd})

# @app.post("/login")
# async def login_post(request:Request):
#     await request.form()
#     print(dict(await request.form()))
#     return templates.TemplateResponse(name="users/list.html", context={'request':request})


# 로그인 확인 페이지로 이동
@app.post("/login_check")
async def login_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    user_list = await collection_user_list.get_all()
    print(user_list)
    email_list = []
    password_list = []
    for i in range(len(user_list)):
        email_list.append(user_list[i].user_email)
        password_list.append(user_list[i].user_password)
    print(email_list)
    if dict(await request.form())["login_email"] in email_list: 
        user_index = email_list.index(dict(await request.form())["login_email"])
        if password_list[user_index] == dict(await request.form())["login_password"]:
            link = "login_complete.html"  
            user_dict = user_list[user_index]
            return templates.TemplateResponse(name=link, context={'request':request,
                                                                  'user_dict' : user_dict})
        else:
            link = "login_fail.html"
            return templates.TemplateResponse(name=link, context={'request':request})

    else:
        link = "login_fail.html"
        return templates.TemplateResponse(name=link, context={'request':request})

# 회원가입 완료시 
@app.post("/login_insert")                      
async def login_insert_post(request:Request):
    user_dict = dict(await request.form())
    print(dict(await request.form()))
    user_list = await collection_user_list.get_all()
    list_user_email = []
    list_user_name = []
    for i in range(len(user_list)):
        list_user_email.append(dict(user_list[i])["user_email"])
        list_user_name.append(dict(user_list[i])["user_name"])
    pass
    if user_dict["user_email"] in list_user_email :     
        return templates.TemplateResponse("insert_email_error.html",{'request':request})
    elif user_dict["user_password"] != user_dict["password_check"]:
        return templates.TemplateResponse("insert_password_error.html",{'request':request})
    elif user_dict["user_name"] in list_user_name:
        return templates.TemplateResponse("insert_name_error.html",{'request':request})
        
    else:
        user = User_list(**user_dict)
        await collection_user_list.save(user)
        return templates.TemplateResponse("insert_interesting_region.html",{'request':request,
                                                                  'user_dict' : user_dict}) # login.html

# 커뮤니티 페이지로 이동
@app.get("/community")                     
async def community_get(request:Request):
    print(dict(request._query_params))
    return templates.TemplateResponse("community.html",{'request':request})

@app.post("/community")                      
async def community_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse("community.html",{'request':request})

# 회원가입 페이지로 이동
@app.get("/insert")                     
async def insert_get(request:Request):
    print(dict(request._query_params))
    return templates.TemplateResponse("insert.html",{'request':request})

@app.post("/insert")                      
async def insert_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse("insert.html",{'request':request})
