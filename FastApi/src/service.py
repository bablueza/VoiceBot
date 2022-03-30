from fastapi import APIRouter
from typing import Optional

router = APIRouter()

import grpc
import sys
sys.path.append("../protos")
import chatbot_pb2
import chatbot_pb2_grpc
sys.path.append("../configs")
import config

def chatBotClient(input):
    with grpc.insecure_channel('localhost:'+str(config.chatbot)) as channel:
        stub = chatbot_pb2_grpc.ChatServiceStub(channel)
        response = stub.ChatFunc(chatbot_pb2.ChatRequest(name=input))
    return "Chat client received: " + response.result

@router.get("/route")
def read_service(name:Optional[str] = None):
    return {"Route to": name,"ret":chatBotClient(name)}