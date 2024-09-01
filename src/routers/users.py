from fastapi import APIRouter, Request, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates

from globals import users_dao
from .auth import get_current_user

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.post("/register", status_code=201)
async def register(request: Request):
    form_data = await request.form()
    username = form_data.get("username")
    password = form_data.get("password")
    if users_dao.get_user_by_username(username):
        return JSONResponse(status_code=200, content={"message": "User already registered, please login to continue."})
    users_dao.add_user(username, password)
    return JSONResponse(status_code=200, content={"message": "User registered successfully, please login."})


@router.get("/portfolio")
async def get_user_portfolio(
        token: str = Depends(get_current_user)
):
    username = token.username

    try:
        portfolio = users_dao.show_mutual_funds(username)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

    return {
        "portfolio": portfolio
    }
