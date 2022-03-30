import grpc
import sys
sys.path.append("protos")
import vaja_pb2
import vaja_pb2_grpc
sys.path.append("configs")
import config

def vajaClient(nameInput):
    with grpc.insecure_channel('localhost:'+str(config.vaja)) as channel:
        stub = vaja_pb2_grpc.VajaServiceStub(channel)
        response = stub.VajaFunc(vaja_pb2.VajaRequest(name=nameInput))
    return "Vaja client received: " + response.result