from concurrent import futures
import logging

import grpc
import sys
sys.path.append("protos")
import vaja_pb2
import vaja_pb2_grpc
sys.path.append("configs")
import config

class VajaService(vaja_pb2_grpc.VajaService):

    def VajaFunc(self, request, context):
        print('Recive data:'+request.name)
        return vaja_pb2.VajaReply(result='Vaja:%s' % request.name)

    def VajaStream(self, request_iterator, context):
        for new_data in request_iterator:
            print('Stream Recive data:'+new_data.check+':'+new_data.data)
        print('End Stream.')
        return vaja_pb2.VajaReply(result='Vaja:stream')

    def VajaBiStream(self, request_iterator, context):
        for new_data in request_iterator:
            print('BiStream Recive data:'+new_data.check+':'+new_data.data)
            yield vaja_pb2.StreamData(check='1',data=new_data.data+' ok')
        print('End BiStream.')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    vaja_pb2_grpc.add_VajaServiceServicer_to_server(VajaService(), server)
    server.add_insecure_port('[::]:'+str(config.vaja))
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()