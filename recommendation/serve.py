import grpc
from concurrent import futures
import recommend_pb2
import recommend_pb2_grpc


class Recommendation(recommend_pb2_grpc.RecomServicer):

    def __init__(self):
        self.booksdata = [
            {
                "title": "Harry Potter",
                "author": "J.K Rowling",
                "isbn": 1122343452
            },
            {
                "title":"To kill a mocking bird",
                "author":"Harper lee",
                "isbn": 1122343451
            },
            {
                "title":"Pride and Prejudices",
                "author":"Jane Austen",
                "isbn": 1122343458
            }
        ]

    def GetRecommendation(self, request, context):

        userId = request.userid

        if userId:
            bookObjList = recommend_pb2.BookList()

            for item in self.booksdata:
                bookObj = bookObjList.book.add()
                bookObj.title = item["title"]
                bookObj.author = item["author"]
                bookObj.isbn = item["isbn"]
                print(bookObj)
               

        return bookObjList


def server():

    srvr = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    recommend_pb2_grpc.add_RecomServicer_to_server(Recommendation(),srvr)
    srvr.add_insecure_port("[::]:50052")
    print("LISTENING TO PORT 50052")
    srvr.start()
    srvr.wait_for_termination()

if __name__== '__main__':
    server()

    