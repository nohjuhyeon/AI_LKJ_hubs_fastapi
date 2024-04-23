from pydantic import BaseModel, Field
from typing import Optional, List
from beanie import Document, Link
from bson import ObjectId     

class Inquiry(Document):
    userName: Optional[str] = None
    userEmail: Optional[str] = None
    password: Optional[str] = None
    inquiryContent: Optional[str] = None
    date: Optional[str] = None
    title: Optional[str] = None
    inquiryNumber: Optional[int] = None

    class Settings:
        name = "one_on_one_CS"
