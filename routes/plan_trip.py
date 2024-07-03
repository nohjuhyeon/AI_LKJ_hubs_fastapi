from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from utils.paginations import Paginations
from typing import Optional
from beanie import PydanticObjectId
from routes.chat_bot import reco_tour,reco_theme
import datetime
router = APIRouter()

templates = Jinja2Templates(directory="templates/")


from models.user_list import User_list 
from databases.connections import Database
from models.reserve_transfer import transfer_car_list,transfer_train_list,transfer_bus_list,transfer_airport_list,tour_list, transfer_total_list
from models.reserve_dorm import Reserve_dorm
from models.tour_plan import reco_trip_plan,reco_trip_add
collection_transfer_car_list = Database(transfer_car_list)
collection_transfer_train_list = Database(transfer_train_list)
collection_transfer_bus_list = Database(transfer_bus_list)
collection_transfer_airport_list = Database(transfer_airport_list)
collection_transfer_total_list = Database(transfer_total_list)
collection_reco_trip_plan = Database(reco_trip_plan)
collection_tour_list = Database(tour_list)
collection_reco_trip_add = Database(reco_trip_add)
collection_reserve_dorm = Database(Reserve_dorm)

collection_user_list = Database(User_list)

# 여행 계획 추천

@router.get("/reco_trip_plan") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    region = dict(request._query_params)['arrive']
    datediff = (datetime.datetime.strptime(dict(request._query_params)['arrive_date'],'%Y-%m-%d') - datetime.datetime.strptime(dict(request._query_params)['depart_date'],'%Y-%m-%d')).days+1
    concept_list = reco_theme(region,datediff)
    concept_list.append('상관없음')
    return templates.TemplateResponse(name="plan_trip/reco_trip_plan.html", context={'request':request,
                                                                                     'concept_list' : concept_list,'tour_list':tour_list,'datediff':datediff})

## 여행 계획

@router.get("/trip_plan")
async def list_post(request:Request):
    await request.form()
    datediff = int(dict(request._query_params)['datediff'])
    print(dict(await request.form()))
    
    theme = dict(request._query_params)['concept_list'][int(dict(request._query_params)['trip_concept'])-1]
    if theme == '상관없음':
        theme = ''
    region = dict(request._query_params)['arrive']
    datediff = int(dict(request._query_params)['datediff'])

    dict_answer = reco_tour(region,theme,datediff)

    tour_list =[]
    for i in range(3):
        try:
            for day in list(dict_answer.keys()):
                day_list = []
                for i in dict_answer[day]:
                    dict_attraction = {}
                    dict_attraction['attraction'] = i.split(' : ')[0]
                    dict_attraction['region'] = i.split(' : ')[1]
                    dict_attraction['info'] = i.split(' : ')[2]
                    day_list.append(dict_attraction)
                tour_list.append(day_list)
            break
        except:
            tour_list = []
            pass
    if len(tour_list) != 0:
        reco_add_list = await collection_reco_trip_add.get_all()
        pass
        return templates.TemplateResponse(name="plan_trip/trip_plan.html", context={'request':request,
                                                                                'tour_list': tour_list,
                                                                                'reco_add_list': reco_add_list,'datediff':datediff})
    else:
        return templates.TemplateResponse(name="plan_trip/trip_plan_fail.html", context={'request':request})



@router.get("/reserve_transfer") # 펑션 호출 방식
@router.get("/reserve_transfer/{page_number}") # 펑션 호출 방식
async def list_get(request:Request, page_number: Optional[int]=1):
    transfer_type = dict(request._query_params)
    await request.form()
    conditions = {} 
    try :
        search_word = transfer_type["transfer"]
    except:
        search_word = None
    if search_word:     # 검색어 작성
        conditions = {"transfer_cate" : { '$regex': search_word}}
    total_list_pagination, pagination = await collection_transfer_total_list.getsbyconditionswithpagination(conditions
                                                                     ,page_number)
    return templates.TemplateResponse(name="plan_trip/reserve_transfer.html", context={'request':request,
                                                                                           'total_list':total_list_pagination,
                                                                                           'pagination':pagination})



@router.get("/reserve_dorm") # 펑션 호출 방식
@router.get("/reserve_dorm/{page_number}") # 펑션 호출 방식
async def list_get(request:Request, page_number: Optional[int]=1):
    dorm_type = dict(request._query_params)
    await request.form()
    conditions = { }
    try :
        search_word = dorm_type["dorm_cate"]
    except:
        search_word = None
    if search_word:     # 검색어 작성
        conditions = {"dorm_cate" : { '$regex': search_word}}
    check_dorm = []
    added_items=[]
    for i in range(len(dorm_type)):
        pass
        if str(i+1) in dorm_type.keys():
            if dorm_type[str(i+1)] not in added_items:
                added_items.append(dorm_type[str(i+1)])
                dorm_element = await collection_reserve_dorm.get(dorm_type[str(i+1)])
                check_dorm.append(dorm_element)
    print(check_dorm)
    dorm_list_pagination, pagination = await collection_reserve_dorm.getsbyconditionswithpagination(conditions
                                                                     ,page_number)
    return templates.TemplateResponse(name="plan_trip/reserve_dorm.html", context={'request':request,
                                                                                           'list_dorm':dorm_list_pagination,
                                                                                           'pagination':pagination,
                                                                                           'check_dorm':check_dorm,
                                                                                           'added_items':added_items})
@router.get("/reserve_tour") # 펑션 호출 방식
@router.get("/reserve_tour/{page_number}") # 펑션 호출 방식
async def tour_post(request:Request, page_number: Optional[int]=1):
    tour_type = dict(request._query_params)
    await request.form()
    conditions = {}
    check_tour = []
    added_items=[]
    for i in range(len(tour_type)):
        pass
        if str(i+1) in tour_type.keys():
            if tour_type[str(i+1)] not in added_items:
                added_items.append(tour_type[str(i+1)])
                tour_element = await collection_tour_list.get(tour_type[str(i+1)])
                check_tour.append(tour_element)
    print(check_tour)

    print(dict(await request.form()))
    tour_list_pagination, pagination = await collection_tour_list.getsbyconditionswithpagination(conditions
                                                                     ,page_number)
    return templates.TemplateResponse(name="plan_trip/reserve_tour.html", context={'request':request,
                                                                                           'tour_list':tour_list_pagination,
                                                                                           'pagination':pagination,
                                                                                           'check_tour':check_tour,
                                                                                           'added_items':added_items})

@router.get("/reserve_dorm_test") # 펑션 호출 방식
async def list_get(request:Request):
    dorm_type = dict(request._query_params)
    dorm_list = await collection_reserve_dorm.get_all()
    await request.form()
    conditions = { }
    try :
        search_word = dorm_type["dorm_cate"]
    except:
        search_word = None
    if search_word:     # 검색어 작성
        conditions = {"dorm_cate" : { '$regex': search_word}}
    dorm_list = await collection_reserve_dorm.getsbyconditions(conditions
                                                                     )    # pagenumber = 1
    dorm_dict_list = [module.dict() for module in dorm_list]
    return templates.TemplateResponse(name="plan_trip/reserve_dorm_test.html", context={'request':request,
                                                                                           'list_dorm':dorm_dict_list})


@router.post("/reserve_transfer") # 펑션 호출 방식
@router.post("/reserve_transfer/{page_number}") # 펑션 호출 방식
async def list_post(request:Request, page_number: Optional[int]=1):
    transfer_type = dict(await request.form())
    form_data = await request.form()

    conditions = {} 
    try :
        search_word = transfer_type["transfer"]
    except:
        search_word = None
    if search_word:     # 검색어 작성
        conditions = {"transfer_cate" : { '$regex': search_word}}
    total_list_pagination, pagination = await collection_transfer_total_list.getsbyconditionswithpagination(conditions
                                                                     ,page_number)
    return templates.TemplateResponse(name="plan_trip/reserve_transfer.html", context={'request':request,
                                                                                           'total_list':total_list_pagination,
                                                                                           'form_data':form_data,
                                                                                           'pagination':pagination})



@router.post("/reserve_dorm") # 펑션 호출 방식
@router.post("/reserve_dorm/{page_number}") # 펑션 호출 방식
async def list_post(request:Request, page_number: Optional[int]=1):
    dorm_type = dict(await request.form())
    form_data = await request.form()

    conditions = { }
    try :
        search_word = dorm_type["dorm_cate"]
    except:
        search_word = None
    if search_word:     # 검색어 작성
        conditions = {"dorm_cate" : { '$regex': search_word}}
    check_dorm = []
    added_items=[]
    for i in range(len(dorm_type)):
        pass
        if str(i+1) in dorm_type.keys():
            if dorm_type[str(i+1)] not in added_items:
                added_items.append(dorm_type[str(i+1)])
                dorm_element = await collection_reserve_dorm.get(dorm_type[str(i+1)])
                check_dorm.append(dorm_element)
    print(check_dorm)
    dorm_list_pagination, pagination = await collection_reserve_dorm.getsbyconditionswithpagination(conditions
                                                                     ,page_number)
    return templates.TemplateResponse(name="plan_trip/reserve_dorm.html", context={'request':request,
                                                                                           'list_dorm':dorm_list_pagination,
                                                                                           'pagination':pagination,
                                                                                           'form_data':form_data,
                                                                                           'check_dorm':check_dorm,
                                                                                           'added_items':added_items})
@router.post("/reserve_tour") # 펑션 호출 방식
@router.post("/reserve_tour/{page_number}") # 펑션 호출 방식
async def tour_post(request:Request, page_number: Optional[int]=1):
    tour_type = dict(await request.form())
    form_data = await request.form()
    conditions = {}
    check_tour = []
    added_items=[]
    for i in range(len(tour_type)):
        pass
        if str(i+1) in tour_type.keys():
            if tour_type[str(i+1)] not in added_items:
                added_items.append(tour_type[str(i+1)])
                tour_element = await collection_tour_list.get(tour_type[str(i+1)])
                check_tour.append(tour_element)
    print(check_tour)

    print(dict(await request.form()))
    tour_list_pagination, pagination = await collection_tour_list.getsbyconditionswithpagination(conditions
                                                                     ,page_number)
    return templates.TemplateResponse(name="plan_trip/reserve_tour.html", context={'request':request,
                                                                                           'tour_list':tour_list_pagination,
                                                                                           'pagination':pagination,
                                                                                           'form_data':form_data,
                                                                                           'check_tour':check_tour,
                                                                                           'added_items':added_items})

@router.post("/reserve_dorm_test") # 펑션 호출 방식
async def list_post(request:Request):
    dorm_type = dict(await request.form())
    dorm_list = await collection_reserve_dorm.get_all()
    form_data = await request.form()
    conditions = { }
    try :
        search_word = dorm_type["dorm_cate"]
    except:
        search_word = None
    if search_word:     # 검색어 작성
        conditions = {"dorm_cate" : { '$regex': search_word}}
    dorm_list = await collection_reserve_dorm.getsbyconditions(conditions
                                                                     )    # pagenumber = 1
    dorm_dict_list = [module.dict() for module in dorm_list]
    return templates.TemplateResponse(name="plan_trip/reserve_dorm_test.html", context={'request':request,
                                                                                        'form_data':form_data,
                                                                                           'list_dorm':dorm_dict_list})


# 여행 계획 추천
@router.post("/reco_trip_plan") # 펑션 호출 방식
async def list_post(request:Request):
    dict(await request.form())
    form_data = await request.form()

    region = dict(form_data)['arrive']
    datediff = (datetime.datetime.strptime(dict(form_data)['arrive_date'],'%Y-%m-%d') - datetime.datetime.strptime(dict(form_data)['depart_date'],'%Y-%m-%d')).days+1
    concept_list = reco_theme(region,datediff)
    concept_list.append('상관없음')
    return templates.TemplateResponse(name="plan_trip/reco_trip_plan.html", context={'request':request,
                                                                                     'form_data':form_data,
                                                                                     'concept_list' : concept_list,'tour_list':tour_list,'datediff':datediff})

@router.post("/trip_plan")
async def list_post(request:Request):
    form_data = await request.form()

    datediff = int(dict(form_data)['datediff'])
    
    theme = dict(form_data)['concept_list'].split(',')[int(dict(form_data)['trip_concept'])-1]
    if theme == '상관없음':
        theme = ''
    region = dict(form_data)['arrive']
    datediff = int(dict(form_data)['datediff'])

    dict_answer = reco_tour(region,theme,datediff)

    tour_list =[]
    for i in range(3):
        try:
            for day in list(dict_answer.keys()):
                day_list = []
                for i in dict_answer[day]:
                    dict_attraction = {}
                    dict_attraction['attraction'] = i.split(' : ')[0]
                    dict_attraction['region'] = i.split(' : ')[1]
                    dict_attraction['info'] = i.split(' : ')[2]
                    day_list.append(dict_attraction)
                tour_list.append(day_list)
            break
        except:
            tour_list = []
            pass
    if len(tour_list) != 0:
        reco_add_list = await collection_reco_trip_add.get_all()
        pass
        return templates.TemplateResponse(name="plan_trip/trip_plan.html", context={'request':request,
                                                                                'tour_list': tour_list,
                                                                                'form_data':form_data,
                                                                                'reco_add_list': reco_add_list,'datediff':datediff})
    else:
        return templates.TemplateResponse(name="plan_trip/trip_plan_fail.html", context={'request':request,'form_data':form_data})
