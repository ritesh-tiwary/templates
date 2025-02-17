import grpc
import asyncio
import service_pb2_grpc
import service_servicer
import service_interceptor


options = [
    ('grpc.so_reuseport', 1),
    ('grpc.tcp_min_rto_ms', 1000),
    ('grpc.keepalive_time_ms', 10000), # 10 sec ping
    ('grpc.keepalive_timeout_ms', 1000), # 1 sec timeout
    ('grpc.http2.max_pings_without_data', 0),
    ('grpc.keepalive_permit_without_calls', 1),
    ('grpc.max_concurrent_streams', 100),
    ('grpc.max_connection_idle_ms', 30000), # 30 sec idle timeout
    ('grpc.max_send_message_length', 10 * 1024 * 1024),
    ('grpc.max_receive_message_length', 10 * 1024 * 1024)
]

async def serve():
    server = grpc.aio.server(interceptors=[service_interceptor.TimingInterceptor()], options=options)
    service_pb2_grpc.add_ServiceServicer_to_server(service_servicer.ServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    print("🚀 gRPC server running on port 50051")
    try:
        await server.wait_for_termination()
    except asyncio.CancelledError:
        try:
            await server.stop(0)
        except asyncio.CancelledError:
            print("Server Stopped!!")

if __name__ == "__main__":
    asyncio.run(serve())