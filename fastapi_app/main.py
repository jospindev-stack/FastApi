
import sys, os
from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.templating import Jinja2Templates
import uvicorn
from dash_app import app as app_dash
import requests

# Désactivation des routes docs/redoc/openapi pour éviter la redirection automatique
app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

# Chemins absolus pour les templates et fichiers statiques
templates_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "templates"))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "static"))

# Servir les fichiers statiques
app.mount("/static", StaticFiles(directory=static_dir), name="static")
# Initialiser le moteur de templates Jinja2
templates = Jinja2Templates(directory=templates_dir)

# URL API externe 
EXTERNAL_API_URL = "https://weather1003.azurewebsites.net/info"

def get_external_info():
    try:
        response = requests.get(EXTERNAL_API_URL)
        return response.json()
    except Exception:
        return {
            "date": "N/A",
            "time": "N/A",
            "weather": {
                "city": "Unknown",
                "temperature": "N/A",
                "description": "N/A"
            }
        }

# Utilisateur en mémoire 
users = {"admin": "password"}

@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    info = get_external_info()
    return templates.TemplateResponse("home.html", {"request": request, "info": info})

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    info = get_external_info()
    return templates.TemplateResponse("login.html", {"request": request, "info": info})

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    if username in users and users[username] == password:
        response = RedirectResponse(url='/dashboard', status_code=302)
        response.set_cookie(key="Authorization", value="Bearer Token", httponly=True)
        return response
    info = get_external_info()
    return templates.TemplateResponse("login.html", {"request": Request, "error": "Invalid credentials", "info": info})

@app.get("/logout")
async def logout():
    response = RedirectResponse(url='/login')
    response.delete_cookie('Authorization')
    return response

# Montée de l'application Dash sous /dashboard
app.mount("/dashboard", WSGIMiddleware(app_dash.server))

# Exécution locale uniquement
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8021, workers=1)