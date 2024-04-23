from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from utils.paginations import Paginations
from typing import Optional
from beanie import PydanticObjectId

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
@router.post("/reco_trip_plan") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    concept_tour = await collection_reco_trip_plan.get_all()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="plan_trip/reco_trip_plan.html", context={'request':request,
                                                                                     'concept_list' : concept_tour})

@router.get("/reco_trip_plan") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    concept_tour = await collection_reco_trip_plan.get_all()
    concept_list = []
    check_concept_list = []
    for i in range(len(concept_tour)):
        if concept_tour[i].concept_name in check_concept_list:
            pass
        else:
            concept_list.append(concept_tour[i])
            check_concept_list.append(concept_tour[i].concept_name)
            pass
    print(dict(await request.form()))
    return templates.TemplateResponse(name="plan_trip/reco_trip_plan.html", context={'request':request,
                                                                                     'concept_list' : concept_list})

## 여행 계획
@router.post("/trip_plan") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="plan_trip/trip_plan.html", context={'request':request})

@router.get("/trip_plan")
async def list_post(request:Request):
    await request.form()
    dict(request._query_params)
    print(dict(await request.form()))
    tour_plan_list = await collection_reco_trip_plan.get_all()
    tour_list = []
    for i in range(len(tour_plan_list)):
        if tour_plan_list[i].concept_number == dict(request._query_params)["trip_concept"]:
            tour_list.append(tour_plan_list[i])
    print(tour_list) 
    reco_add_list = await collection_reco_trip_add.get_all()
    pass
    return templates.TemplateResponse(name="plan_trip/trip_plan.html", context={'request':request,
                                                                                'tour_list': tour_list,
                                                                                'reco_add_list': reco_add_list})


@router.get("/reserve_transfer") # 펑션 호출 방식
@router.get("/reserve_transfer/{page_number}") # 펑션 호출 방식
async def list_get(request:Request, page_number: Optional[int]=1):
    transfer_type = dict(request._query_params)
    await request.form()
    conditions = {} 
    try :
        search_word = transfer_type["transfer_cate"]
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


