from pydantic import BaseModel
from typing import Optional
from enum import Enum

class PeriodNum(str, Enum):
    six = "六期"
    seven = "七期"
    eight = "八期"
    admin = "管理员"

class Department(str, Enum):
    data_science = "数据科学"
    Full_stack = "全栈"
    CPU_OS = "CPU&OS"
    JAVA = "JAVA"

class Student(BaseModel):
    name: str
    position: Optional[str] = None
    awards: Optional[str] = "0"
    account: str
    pwd: str
    periodNum: PeriodNum
    department: Department

class AwardsInfo(BaseModel):
    account: str = "0"
    name: str
    awards: str = None
    experience: str = None

class UpdateResponseModel(BaseModel):
    message: str
    position: str
    
class PositionUpdate(BaseModel):
    position: str

class UserInfo(BaseModel):
    account: str
    pwd: str