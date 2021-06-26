Here we defined an RPC service that exposes a method called Hello that 
takes as argument a request with a name attribute and returns a response 
with a message attribute. We then need to compile the proto file to a more 
usable python module by running the following:

```
pip install grpcio grpcio-tools
```


```
OUT_DIR=/home/wxf/grpc_prj/medium/web_grpc_app3
python -m grpc_tools.protoc --python_out=${OUT_DIR} --grpc_python_out=${OUT_DIR} service.proto
```

https://stackoverflow.com/questions/57909401/what-are-the-command-line-arguments-passed-to-grpc-tools-protoc