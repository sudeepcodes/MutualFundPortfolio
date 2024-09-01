import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from auth import router as auth_router
from funds import router as funds_router
from users import router as users_router

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

# Existing routes here...
app.include_router(auth_router, prefix="/auth")
app.include_router(funds_router, prefix="/funds")
app.include_router(users_router, prefix="/users")


@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.get("/", response_class=HTMLResponse)
@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


@app.get("/portfolio", response_class=HTMLResponse)
async def render_portfolio_page(request: Request):
    # Just render the HTML template; portfolio data will be loaded via JavaScript
    return templates.TemplateResponse("portfolio.html", {"request": request})


if __name__ == '__main__':
    uvicorn.run(app)
