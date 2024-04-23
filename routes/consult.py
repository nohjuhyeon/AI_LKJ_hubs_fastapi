from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi import Query
from databases.connections import Database
from typing import Optional
from datetime import datetime
import requests

router = APIRouter()

templates = Jinja2Templates(directory="templates/")

from databases.connections import Database

from models.frequent_CS import FAQ_list
collection_FAQ_list = Database(FAQ_list)
from models.admin_notice import Admin_notice_list
collection_admin_notice_list = Database(Admin_notice_list)
from models.one_on_one_CS import One_on_one_CS_list
collection_one_on_one_CS_list = Database(One_on_one_CS_list)
from models.data_chart import data_attraction, data_concept_search, data_consume,data_consume_transition,data_trend_search
collection_data_attraction=Database(data_attraction)
collection_data_concept_search=Database(data_concept_search)
collection_data_consume=Database(data_consume)
collection_data_consume_transition=Database(data_consume_transition)
collection_data_trend_search=Database(data_trend_search)


## 공지 사항
@router.post("/user_notice") # 펑션 호출 방식
@router.post("/user_notice/{page_number}")
async def list_post(request: Request, page_number: Optional[int] = 1):
    print(dict(await request.form()))
    conditions = {}
    notice_pagination, pagination = await collection_admin_notice_list.getsbyconditionswithpagination(conditions, page_number, records_per_page=10)  
    return templates.TemplateResponse(name="consult/user_notice.html", context={'request': request, "notices": notice_pagination, 'pagination': pagination})

@router.get("/user_notice") # 펑션 호출 방식
@router.get("/user_notice/{page_number}")
async def list_get(request: Request, page_number: Optional[int] = 1):
    print(dict(await request.form()))
    conditions = {}
    notice_pagination, pagination = await collection_admin_notice_list.getsbyconditionswithpagination(conditions, page_number, records_per_page=10)  
    return templates.TemplateResponse(name="consult/user_notice.html", context={'request': request, "notices": notice_pagination, 'pagination': pagination})

## 자주 묻는 질문 페이지
@router.post("/frequent_CS")
async def frequent_cs_post(request:Request):
    form_data = await request.form()
    print(dict(form_data))
    faqs = await collection_FAQ_list.get_all()
    return templates.TemplateResponse(name="consult/frequent_CS.html", context={'request':request, 'faqs':faqs})

@router.get("/frequent_CS")
async def frequent_cs_get(request:Request):
    faqs = await collection_FAQ_list.get_all()
    return templates.TemplateResponse(name="consult/frequent_CS.html", context={'request':request, 'faqs':faqs})

## 1대1 문의 메인페이지
@router.post("/one_on_one_CS_main")  # 펑션 호출 방식
@router.post("/one_on_one_CS_main/{page_number}")  # 펑션 호출 방식
async def list_post(request: Request, page_number: Optional[int] = 1):
    print(dict(await request.form()))
    conditions = {}
    qna_list_pagination, pagination = await collection_one_on_one_CS_list.getsbyconditionswithpagination(conditions, page_number, records_per_page=6)  
    return templates.TemplateResponse(name="consult/one_on_one_CS_main.html", context={'request': request, "qnas": qna_list_pagination, 'pagination': pagination})


@router.get("/one_on_one_CS_main")  # 펑션 호출 방식
@router.get("/one_on_one_CS_main/{page_number}")  # 펑션 호출 방식
async def list_get(request: Request, page_number: Optional[int] = 1):
    print(dict(await request.form()))
    conditions = {}
    qna_list_pagination, pagination = await collection_one_on_one_CS_list.getsbyconditionswithpagination(conditions, page_number, records_per_page=6)  
    return templates.TemplateResponse(name="consult/one_on_one_CS_main.html", context={'request': request, "qnas": qna_list_pagination, 'pagination': pagination})

## 1대1 문의 페이지
@router.post("/one_on_one_CS") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="consult/one_on_one_CS.html", context={'request':request})

@router.get("/one_on_one_CS") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="consult/one_on_one_CS.html", context={'request':request})

## 1대1 문의 페이지 제출 및 리디렉션
@router.post("/inquiryForm")
async def create_inquiry(request: Request):
    form_data = await request.form()
    user_info = dict(form_data)

    user_info['date'] = datetime.now().strftime("%Y-%m-%d")

    # MongoDB에서 현재 가장 높은 inquiryNumber 찾기
    results = await One_on_one_CS_list.find().sort("-inquiryNumber").to_list(1)
    if results:
        last_inquiry = results[0]
    else:
        last_inquiry = None

    if last_inquiry:
        user_info['inquiryNumber'] = last_inquiry.inquiryNumber + 1
    else:
        user_info['inquiryNumber'] = 1

    # 데이터 유효성 검사 및 저장
    inquiry = One_on_one_CS_list(**user_info)
    await inquiry.create()

    # 사용자를 1대1 상담 메인 페이지로 리디렉션
    return RedirectResponse(url="/consult/one_on_one_CS_main", status_code=303)

## 카카오톡 상담
@router.post("/kakaotalk_CS")
@router.get("/kakaotalk_CS")
async def kakaotalk_CS(request: Request):
    access_token = "Kuah5OooBvqo_gpRWE075RorCj1vn8ZYkucKKwynAAABjgy4pJ-oblpFv_zasg"  # 실제 액세스 토큰으로 바꿔주세요

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get("https://kapi.kakao.com/v2/api/talk/memo/default/send", headers=headers)

    return templates.TemplateResponse("template.html", context={'request':request, 'response': response.json()})



## 데이터 현황 차트
@router.post("/data_chart") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="consult/data_chart.html", context={'request':request})

@router.get("/data_chart") # 펑션 호출 방식
async def list_post(request:Request):
    if len(dict(request._query_params))>0:
        select_region = dict(request._query_params)['select_region']
    else:
        select_region = "서울"
    await request.form()
    print(dict(await request.form()))

    # 월별 방문객 수 
    visitor_conditions = {"destination_type" : { '$regex': '전체'}}
    visitor_list = await collection_data_concept_search.getsbyconditions(visitor_conditions)
    visitor_list = [module.dict() for module in visitor_list]
    dict_visitor = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0}
    for i in range(len(visitor_list)):
        if visitor_list[i]['region'] == select_region:
            dict_visitor[str(visitor_list[i]['std_month'])] = dict_visitor[str(visitor_list[i]['std_month'])]  + visitor_list[i]['destination_search']/4

    # 유형별 목적지 검색량
    concept_conditions = {"destination_type": { "$ne": "전체" }}
    dict_concept={'숙박':0, '음식':0, '기타관광':0, '쇼핑':0, '문화관광':0, '역사관광':0, '자연관광':0, '체험관광':0, '레저스포츠':0}
    concept_list = await collection_data_concept_search.getsbyconditions(concept_conditions)
    concept_list = [module.dict() for module in concept_list]
    for k in range(len(concept_list)):
        if concept_list[k]['region'] == select_region:
            dict_concept[concept_list[k]["destination_type"]] = dict_concept[concept_list[k]["destination_type"]] +  concept_list[k]['destination_search']/4

    # 월별 관광 소비 추이 이거
    consume_transition = {"industry_major_cate" : { '$ne': '전체'}}
    consume_transition_list = await collection_data_consume_transition.getsbyconditions(consume_transition)
    consume_transition_list = [module.dict() for module in consume_transition_list]
    consume_transition_column = ['운송업', '여행업', '숙박업', '식음료업', '여가서비스업', '쇼핑업']
    list_consume_transition = [{'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0},
                               {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0},
                               {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0},
                               {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0},
                               {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0},
                               {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0}]
    for x in range(len(consume_transition_list)):
        if consume_transition_list[x]['region'] == select_region:
            list_consume_transition[consume_transition_column.index(consume_transition_list[x]['industry_major_cate'])][str(consume_transition_list[x]['std_month'])] = list_consume_transition[consume_transition_column.index(consume_transition_list[x]['industry_major_cate'])][str(consume_transition_list[x]['std_month'])]+ consume_transition_list[x]['consumption_amount']/4
        pass
    
    # 월별 키워드 검색량
    trend_list = await collection_data_trend_search.get_all()
    trend_list = [module.dict() for module in trend_list]
    tour_trend_column = ['레포츠', '휴식/힐링', '기타', '미식', '체험']
    list_month_trend = [{'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0},
                        {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0},
                        {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0},
                        {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0},
                        {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0}]
    for j in range(len(trend_list)):
        if trend_list[j]['region'] == select_region:
            list_month_trend[tour_trend_column.index(trend_list[j]['tour_trend'])][str(trend_list[j]['std_month'])] =list_month_trend[tour_trend_column.index(trend_list[j]['tour_trend'])][str(trend_list[j]['std_month'])] + trend_list[j]['num_mention']/4
        pass
    
    # 관광소비 유형
    dict_consume={'쇼핑업':0, '숙박업':0, '식음료업':0, '여가서비스업':0, '여행업':0, '운송업':0}
    consume_list = await collection_data_consume.get_all()
    consume_list = [module.dict() for module in consume_list]
    for y in range(len(consume_list)):
        if consume_list[y]['region'] == select_region:
            dict_consume[consume_list[y]["industry_major_cate"]] = dict_consume[consume_list[y]["industry_major_cate"]] +  consume_list[y]['consumption_amount']/4

    return templates.TemplateResponse(name="consult/data_chart.html", context={'request':request, 'dict_visitor':dict_visitor,'dict_concept':dict_concept,'list_month_trend':list_month_trend,'consume_list':consume_list,'list_consume_transition':list_consume_transition, 'dict_consume':dict_consume, 'selected_region':select_region})