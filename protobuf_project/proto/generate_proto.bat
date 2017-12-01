cd proto_source
for %%i in (*.proto) do (
"../protoc.exe" -I=./ --cpp_out=../proto_result %%i
)