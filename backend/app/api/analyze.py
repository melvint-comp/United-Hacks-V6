from fastapi import APIRouter
from app.schemas import ChatRequest, AnalysisResponse
from app.core.tone import analyze_tone
from app.core.empathy import analyze_empathy
from app.core.balance import analyze_balance

router = APIRouter()

@router.post("/", response_model = AnalysisResponse)
def analyze_chat(request: ChatRequest):
    messages = request.messages

    tone = analyze_tone(messages)
    empathy = analyze_empathy(messages)
    balance = analyze_balance(messages)

    return AnalysisResponse(
        tone = tone,
        empathy = empathy,
        balance = balance
    )
