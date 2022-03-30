from concurrent import futures
import logging

import grpc
import sys
sys.path.append("protos")
import chatbot_pb2
import chatbot_pb2_grpc
sys.path.append("configs")
import config

import vajaClient

class ChatService(chatbot_pb2_grpc.ChatService):

    def ChatFunc(self, request, context):
        return chatbot_pb2.ChatReply(result=vajaClient.vajaClient(request.name))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chatbot_pb2_grpc.add_ChatServiceServicer_to_server(ChatService(), server)
    server.add_insecure_port('[::]:'+str(config.chatbot))
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()