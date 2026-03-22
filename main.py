from fastapi import FastAPI,Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates  


tab = FastAPI()

tab.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {
        "id": 1,
        "author": "Dr. Amina Yusuf",
        "content": "Hypertension is a common condition that can lead to serious complications if left untreated.",
        "title": "Understanding High Blood Pressure (Hypertension)",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Dr. Michael Okafor",
        "content": "Diabetes affects how your body processes blood sugar and requires careful management.",
        "title": "What You Need to Know About Diabetes",
        "date_posted": "April 21, 2025",
    },
    {
        "id": 3,
        "author": "Dr. Sarah Johnson",
        "content": "Malaria is transmitted through mosquito bites and is preventable with proper measures.",
        "title": "Malaria Prevention and Treatment",
        "date_posted": "April 22, 2025",
    },
    {
        "id": 4,
        "author": "Dr. Chinedu Eze",
        "content": "A balanced diet and regular exercise are key to maintaining a healthy heart.",
        "title": "Tips for a Healthy Heart",
        "date_posted": "April 23, 2025",
    },
    {
        "id": 5,
        "author": "Dr. Fatima Bello",
        "content": "Vaccination is one of the most effective ways to prevent infectious diseases.",
        "title": "The Importance of Vaccines",
        "date_posted": "April 24, 2025",
    }
]   


@tab.get("/", include_in_schema=False)
@tab.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title":"Home"},)

@tab.get("/api/posts")
def get_posts():  
    return posts