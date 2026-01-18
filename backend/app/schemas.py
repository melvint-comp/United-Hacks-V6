from pydantic import BaseModel
from typing import List, Dict, Any

class Message(BaseModel):
    sender: str
    text: str

class ChatRequest(BaseModel):
    messages: List[Message]

class AnalysisResponse(BaseModel):
    tone: Dict[str, Any]
    empathy: Dict[str, Any]
    balance: Dict[str, Any]
