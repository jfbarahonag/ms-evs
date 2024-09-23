from fastapi import APIRouter

from app.services.evaluation_service import EvaluationService

router = APIRouter(prefix="/evs")

@router.get("")
def hello_world():
    return EvaluationService.hello_world()

@router.post("/request")
def handle_request_reception():
    return EvaluationService.hello_world()