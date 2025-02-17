import time
import grpc


class TimingInterceptor(grpc.aio.ServerInterceptor):
    async def intercept_service(self, continuation, handler_call_details):
        """Intercept each RPC call to measure its execution time."""
        start_time = time.time()
        received_at = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        response = await continuation(handler_call_details)
        elapsed_time = time.time() - start_time
        print(f"{received_at} RPC {handler_call_details.method} took {elapsed_time:.6f} seconds")
        return response