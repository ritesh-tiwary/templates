import service_pb2
import service_pb2_grpc


class ServiceServicer(service_pb2_grpc.ServiceServicer):
    async def GetMessage(self, request, context):
        return service_pb2.ResponseMessage(message=f"Hello, {request.name}!")