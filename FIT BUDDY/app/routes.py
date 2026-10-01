from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@router.get("/health")
async def health():
    return {
        "status": "healthy"
    }


@router.get("/plan")
async def plan(request: Request):

    name = request.query_params.get("name")
    age = request.query_params.get("age")
    goal = request.query_params.get("goal")

    if name and age and goal:
        return templates.TemplateResponse(
            request=request,
            name="result.html",
            context={
                "name": name,
                "age": age,
                "goal": goal
            }
        )

    return templates.TemplateResponse(
        request=request,
        name="plan.html"
    )
@router.post("/...")
async def create_plan(request: Request):
    # code here

    name = form.get("name")
    age = form.get("age")
    goal = form.get("goal")

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "name": name,
            "age": age,
            "goal": goal
        }
    )   