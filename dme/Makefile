# Makefile

GOPATH		= ../../../../../..
GW		= $(shell go list -f '{{ .Dir }}' -m github.com/grpc-ecosystem/grpc-gateway)
APIS		= $(shell go list -f '{{ .Dir }}' -m github.com/gogo/googleapis)
INCLUDE		= -I. -I${GW} -I${APIS} -I${GOPATH} -I../edgeprotogen
BUILTIN		= Mgoogle/protobuf/timestamp.proto=github.com/gogo/protobuf/types,Mgoogle/protobuf/empty.proto=github.com/gogo/protobuf/types,Mgoogle/api/annotations.proto=github.com/gogo/googleapis/google/api,Mgoogle/protobuf/field_mask.proto=github.com/gogo/protobuf/types,Mgoogle/protobuf/descriptor.proto=github.com/golang/protobuf/protoc-gen-go/descriptor

build:
	protoc ${INCLUDE} --gomex_out=plugins=grpc+mex,${BUILTIN}:. *.proto
	protoc ${INCLUDE} --grpc-gateway_out=${BUILTIN}:. *.proto
	# swagger annotations for REST APIs
	# go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger
	protoc ${INCLUDE} --swagger_out=logtostderr=true,allow_merge=true,merge_file_name=app-client:. *.proto
