from fastapi import APIRouter, Depends, Form, HTTPException, status
from fastapi import Request
from fastapi.responses import JSONResponse

from globals import mutual_fund_dao, users_dao
from routers.auth import get_current_user

router = APIRouter()


@router.get("/", response_class=JSONResponse)
async def get_all_funds(token: str = Depends(get_current_user)):
    fund_names = mutual_fund_dao.get_all_fund_family_names()
    return JSONResponse(status_code=200, content={"funds": fund_names})


@router.post("/select", response_class=JSONResponse)
async def select_fund(request: Request, fund_name: str = Form(...), token: str = Depends(get_current_user)):
    matching_funds = mutual_fund_dao.get_fund_family_by_name(fund_name)
    return JSONResponse(status_code=200, content={"funds": matching_funds})


@router.post("/buy", response_class=JSONResponse)
async def buy_fund(
        request: Request,
        fund_name: str = Form(...),
        units: int = Form(...),
        token: str = Depends(get_current_user)
):
    username = token['username']  # Fetch current user from token

    if not fund_name or units <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid fund_id or units"
        )

    fund_exists = mutual_fund_dao.get_mutual_fund_by_name(fund_name)
    if not fund_exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Mutual fund not found"
        )

    try:
        users_dao.purchase_mutual_fund(username, fund_name, units)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Mutual fund purchased successfully"}
    )
