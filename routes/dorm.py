from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from motor.motor_asyncio import AsyncIOMotorClient
import math

client = AsyncIOMotorClient('mongodb://192.168.10.240:27017/')
db = client['AI_LKJ']
collection = db['reserve_dorm']

templates = Jinja2Templates(directory='templates/plan_trip/reserve_dorm.html')

ITEMS_PER_PAGE = 9

async def get_data(page):
    skip = (page - 1) * ITEMS_PER_PAGE
    data = await collection.find().skip(skip).limit(ITEMS_PER_PAGE).to_list(ITEMS_PER_PAGE)
    return data

async def get_pagination_info(page):
    total_items = await collection.count_documents({})
    total_pages = math.ceil(total_items / ITEMS_PER_PAGE)
    has_previous = page > 1
    has_next = page < total_pages
    return {'total_items': total_items, 'total_pages': total_pages, 'has_previous': has_previous, 'has_next': has_next, 'current_page': page}

async def reserve_dorm(request):
    page = int(request.path_params['page'])
    data = await get_data(page)
    pagination_info = await get_pagination_info(page)
    return templates.TemplateResponse('plan_trip/reserve_dorm.html', {'request': request, 'data': data, 'pagination': pagination_info})

routes = [
    Route('/reserve_dorm/{page}', endpoint=reserve_dorm, methods=['GET']),
]

app = Starlette(debug=True, routes=routes)
