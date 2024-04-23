from fastapi import APIRouter, Request, Form
from starlette.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from beanie import PydanticObjectId
from typing import Optional
from utils.paginations import Paginations
from datetime import datetime
router = APIRouter()

templates = Jinja2Templates(directory="templates/")

from models.admin_notice import Admin_notice_list
from models.user_list import User_list
from databases.connections import Database
collection_admin_notice_list = Database(Admin_notice_list)
collection_user_list = Database(User_list)


## 메인
@router.post("/") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="admin/admin_main.html", context={'request':request})

@router.get("/") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="admin/admin_main.html", context={'request':request})

## 관리자 로그인 
@router.post("/admin_login")
async def list_post(request:Request) :
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="admin/admin_login.html", context={'request':request})

@router.get("/admin_login")
async def list_post(request:Request) :
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="admin/admin_login.html", context={'request':request})

## 공지 관리
@router.post("/notice") # 펑션 호출 방식
async def list_post(request:Request):
    # MongoDB에서 공지사항 데이터 가져오기
    notices = await collection_admin_notice_list.get_all() # 메서드를 사용하여 모든 공지사항을 가져옴
    # print(notices)
    # 템플릿에 데이터 전달하여 HTML 페이지 렌더링
    return templates.TemplateResponse("admin/admin_notice.html" , context={"request": request, "notices": notices} )

## 공지 관리
@router.get("/notice") # 펑션 호출 방식
@router.get("/notice/{page_number}") # 펑션 호출 방식
async def list_get(request:Request, page_number: Optional[int]=1):
    await request.form()
    conditions = {}
    notices_list_pagination, pagination = await collection_admin_notice_list.getsbyconditionswithpagination(conditions
                                                                     ,page_number)
    # MongoDB에서 공지사항 데이터 가져오기
    # notices = await collection_admin_notice_list.get_all() # 메서드를 사용하여 모든 공지사항을 가져옴
    # print(notices)
    # 템플릿에 데이터 전달하여 HTML 페이지 렌더링
    return templates.TemplateResponse("admin/admin_notice.html" , context={"request": request,
                                                                           "notices": notices_list_pagination,
                                                                            'pagination': pagination})

## 공지사항 수정 업데이트
@router.post("/notice_update") # 펑션 호출 방식
@router.post("/notice_update/{page_number}") # 펑션 호출 방식
async def list_post(request:Request, page_number: Optional[int]=1):
    # MongoDB에서 공지사항 데이터 가져오기
    await request.form()
    form_data = dict(await request.form())
    update_fields = {}
    conditions = {}
    update_fields['title'] = form_data['title']
    update_fields['writer'] = form_data['writer']
    update_fields['date'] = form_data['date']
    update_fields['content'] = form_data['content']
    
    await collection_admin_notice_list.update_one(form_data['id'], update_fields)
    notices_list_pagination, pagination = await collection_admin_notice_list.getsbyconditionswithpagination(conditions
                                                                     ,page_number)
    # 템플릿에 데이터 전달하여 HTML 페이지 렌더링
    return templates.TemplateResponse(name="admin/admin_notice.html" , context={"request": request, 
                                                                                "notices": notices_list_pagination,
                                                                                'pagination': pagination})


## 공지사항 삭제
@router.post("/notice_delete") # 펑션 호출 방식
@router.post("/notice_delete/{page_number}") # 펑션 호출 방식
async def list_post(request:Request, page_number: Optional[int]=1):
    # MongoDB에서 공지사항 데이터 가져오기
    await request.form()
    form_data = dict(await request.form())
    notices_id = form_data.get('id')
    print(form_data)
    conditions = {}
    await collection_admin_notice_list.delete_one(notices_id)
    notices_list_pagination, pagination = await collection_admin_notice_list.getsbyconditionswithpagination(conditions
                                                                     ,page_number)

    # 템플릿에 데이터 전달하여 HTML 페이지 렌더링
    return templates.TemplateResponse(name="admin/admin_notice.html" , context={"request": request, 
                                                                                "notices": notices_list_pagination,
                                                                                'pagination': pagination})

@router.get("/notice") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    notices = await collection_admin_notice_list.get_all() # 메서드를 사용하여 모든 공지사항을 가져옴
    # print(notices)
    return templates.TemplateResponse(name="admin/admin_notice.html", context={'request':request, 'notices': notices})

## 공지사항 내용 보기
@router.get("/admin_notice_content/{object_id}")
async def get_notice_content(request : Request, object_id: PydanticObjectId) :
    # notice_id를 기반으로 데이터베이스에서 공지사항 내용을 가져옴
    notices = await collection_admin_notice_list.get(object_id)
    print(notices)
    return templates.TemplateResponse(name="admin/admin_notice_content.html", context={'request' : request, 'notices' : notices})

## 공지사항 내용 보기
@router.post("/admin_notice_content/{object_id}")
async def post_notice_content(request : Request, object_id: PydanticObjectId) :
    # notice_id를 기반으로 데이터베이스에서 공지사항 내용을 가져옴
    notices = await collection_admin_notice_list.get(object_id)
    print(notices)
    return templates.TemplateResponse(name="admin/admin_notice_content.html", context={'request' : request, 'notices' : notices})

    
## 공지사항 글쓰기
@router.get("/admin_notice_write")
async def get_notice_write(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="admin/admin_notice_write.html", context={'request':request})

@router.post("/admin_notice_write")
async def post_notice_write(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="admin/admin_notice_write.html", context={'request':request})

## 게시물 내용 관리
@router.post("/contents") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="admin/admin_contents.html", context={'request':request})

@router.get("/contents") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="admin/admin_contents.html", context={'request':request})


## 새로운 게시물 추가
@router.post("/notice_add")
@router.post("/notice_delete/{page_number}")
async def add_notice(request : Request, page_number: Optional[int]=1):
    notice_dict = dict(await request.form())
    print(dict(await request.form()))
    conditions = {}
    add_notice = Admin_notice_list(**notice_dict)
    await collection_admin_notice_list.save(add_notice)
    notices = await collection_admin_notice_list.get_all()
    notices_list_pagination, pagination = await collection_admin_notice_list.getsbyconditionswithpagination(conditions
                                                                     ,page_number)
    return templates.TemplateResponse(name="admin/admin_notice.html" , context={"request": request, 
                                                                                "notices": notices_list_pagination,
                                                                                'pagination': pagination})


## 회원 관리
@router.post("/users") # 펑션 호출 방식
async def user_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    users = await collection_user_list.get_all()
    return templates.TemplateResponse(name="admin/admin_users.html", context={'request':request, 'users':users})

@router.get("/users") # 펑션 호출 방식
@router.get("/users/{page_number}") # 펑션 호출 방식
async def user_get(request:Request, page_number: Optional[int]=1):
    await request.form()
    print(dict(await request.form()))
    conditions = {}
    users_list_pagination, pagination = await collection_user_list.getsbyconditionswithpagination(conditions
                                                                     ,page_number)
    return templates.TemplateResponse(name="admin/admin_users.html", context={'request':request,
                                                                              'users' : users_list_pagination,
                                                                              'pagination' : pagination})

