import grpc
import fastapi
import contextlib
import service_pb2
import service_pb2_grpc


options=[("grpc.enable_retries", 1),
         ("grpc.max_retry_attempts", 3),
         ("grpc.use_local_subchannel_pool", 1),
         ("grpc.lb_policy_name", "round_robin")]

grpc_to_http_status = {
        grpc.StatusCode.OK: 200,
        grpc.StatusCode.CANCELLED: 499,
        grpc.StatusCode.UNKNOWN: 500,
        grpc.StatusCode.INVALID_ARGUMENT: 400,
        grpc.StatusCode.DEADLINE_EXCEEDED: 504,
        grpc.StatusCode.NOT_FOUND: 404,
        grpc.StatusCode.ALREADY_EXISTS: 409,
        grpc.StatusCode.PERMISSION_DENIED: 403,
        grpc.StatusCode.RESOURCE_EXHAUSTED: 429,
        grpc.StatusCode.FAILED_PRECONDITION: 400,
        grpc.StatusCode.ABORTED: 409,
        grpc.StatusCode.OUT_OF_RANGE: 400,
        grpc.StatusCode.UNIMPLEMENTED: 501,
        grpc.StatusCode.INTERNAL: 500,
        grpc.StatusCode.UNAVAILABLE: 503,
        grpc.StatusCode.DATA_LOSS: 500,
        grpc.StatusCode.UNAUTHENTICATED: 401,
    }

@contextlib.asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    channel = grpc.aio.insecure_channel("localhost:50051", options=options)
    stub = service_pb2_grpc.ServiceStub(channel)
    app.state.grpc_stub = stub
    print("INFO:\t  Service channel created.")
    yield

    # Cleanup
    await channel.close()
    print("INFO:\t  Service channel closed.")


app = fastapi.FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Application is running."}

@app.get("/{name}")
async def get_message(name: str):
    try:
        response = await app.state.grpc_stub.GetMessage(service_pb2.RequestMessage(name=name))
        return {"message": response.message}
    except grpc.aio.AioRpcError as e:
        raise fastapi.HTTPException(status_code=grpc_to_http_status.get(e.code()), detail=e.details())