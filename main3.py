from fastapi import APIRouter, HTTPException, FastAPI
from pydantic import BaseModel


class UserDetails(BaseModel):
    name: str
    mail_id: str


class User(UserDetails):
    id: int


router = APIRouter(
    prefix="/user",
    tags=["Users"],
)

users: dict[int, User] = {}

app = FastAPI()

app.include_router(router)

@router.post(
    "/create_details/{user_id}",
    response_model=User,
    status_code=201,
)
async def create_user_details(
    user_id: int,
    details: UserDetails,
):
    if user_id in users:
        raise HTTPException(
            status_code=409,
            detail="A user with this ID already exists",
        )

    user = User(
        id=user_id,
        name=details.name,
        mail_id=details.mail_id,
    )

    users[user_id] = user
    return user


@router.get(
    "/details/{user_id}",
    response_model=User,
)
async def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return users[user_id]


@router.put(
    "/update_details/{user_id}",
    response_model=User,
)
async def update_user_details(
    user_id: int,
    details: UserDetails,
):
    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    updated_user = User(
        id=user_id,
        name=details.name,
        mail_id=details.mail_id,
    )

    users[user_id] = updated_user
    return updated_user