import grpc
from concurrent import futures
import user_pb2_grpc
import user_pb2

class Authenticate(user_pb2_grpc.AuthServicer):

    def __init__(self):
        self._username = "Johndoe"
        self._passwd = "somerandompass"
    
    #implementing Authenticate method provided by gRPC
    def Authenticate(self, request, context):

        print(request.username)
        print(request.passwd)

        resp_obj = user_pb2.AuthResponseData()
        resp_obj.username = "JohnDoe"
        resp_obj.authenticated = True

        return resp_obj


def serve():

    """
    server function to server the gRPC auth services
    """

    srvr = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_AuthServicer_to_server(Authenticate(),srvr)
    srvr.add_insecure_port("[::]:50051")
    print("AUTH SERVICE LISTENING TO PORT 50051")
    srvr.start()
    srvr.wait_for_termination()


if __name__ == '__main__':

    serve()