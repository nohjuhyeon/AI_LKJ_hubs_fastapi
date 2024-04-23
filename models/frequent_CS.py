from typing import Optional, List
from beanie import Document, Link
from bson import ObjectId 

class FAQ_list(Document):
    _id : ObjectId
    question : Optional[str] = None 
    answer : Optional[str] = None
    class Settings:
        name = "frequent_CS"
