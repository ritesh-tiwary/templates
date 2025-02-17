python -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. service.proto
echo "Generated protocol buffer code."