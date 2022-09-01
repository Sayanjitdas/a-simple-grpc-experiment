import grpc
import user_pb2 as u_pb2
import user_pb2_grpc as u_pb2_grpc
import recommend_pb2 as r_pb2
import recommend_pb2_grpc as r_pb2_grpc

def auth_gRPC(username: str,passwd:str):

    """
    the adpater function to call authenticate rpc
    method on auth service 
    """
    channel = grpc.insecure_channel("localhost:50051")
    auth_func = u_pb2_grpc.AuthStub(channel=channel)

    auth_payload = u_pb2.AuthRequestData()
    auth_payload.username = username
    auth_payload.passwd = passwd

    return auth_func.Authenticate(auth_payload)


def recommend_gRPC(userid: int):

    """
    the adpater function to call authenticate rpc
    method on auth service
    """

    channel = grpc.insecure_channel("localhost:50052")
    recom_func = r_pb2_grpc.RecomStub(channel)

    recom_payload = r_pb2.User()
    recom_payload.userid = userid

    return recom_func.GetRecommendation(recom_payload)

if __name__ == '__main__':

    print(auth_gRPC("JohnDoe","somerandompass"))
    print(recommend_gRPC(12345))