OUT_DIR=/home/wxf/grpc_prj/medium/web_grpc_app3
python -m grpc_tools.protoc -I . --python_out=${OUT_DIR} --grpc_python_out=${OUT_DIR} service.proto

# -I
# Specify the directory in which to search for imports.
# https://stackoverflow.com/questions/57909401/what-are-the-command-line-arguments-passed-to-grpc-tools-protoc

# 