from pydantic import BaseModel,EmailStr,field_validator
from datetime import datetime
from pydantic_core.core_schema import FieldValidationInfo

class UserBase(BaseModel):
    email: str
    class Config:
        orm_mode = True

# class CreateUser(UserBase):
#     nickname:str
#     password:str

class CreateUserResponse(UserBase):
    nickname:str
    id:int

class UserInfo(UserBase):
    nickname:str
    created_at : datetime
    follower: int
    following:int
    id:int

class Token(BaseModel):
    access_token: str
    token_type: str
    email: str
    id:int

class CreateUser(BaseModel):
    nickname: str
    password1: str
    password2: str
    email: EmailStr

    @field_validator('nickname', 'password1', 'password2', 'email')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

    @field_validator('password2')
    def passwords_match(cls, v, info: FieldValidationInfo):
        if 'password1' in info.data and v != info.data['password1']:
            raise ValueError('비밀번호가 일치하지 않습니다')
        return v