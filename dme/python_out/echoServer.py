from concurrent import futures
import time
import math
import logging

import grpc

import app_client_pb2
import app_client_pb2_grpc

se_event_doit = True
port = 50051

class MatchEngineApiServicer(app_client_pb2_grpc.MatchEngineApiServicer):
    """Provides methods that implement functionality of route guide server."""

    def __init__(self):
   		return

    def RegisterClient(self, request, context):
        return app_client_pb2.RegisterClientReply()

    def FindCloudlet(self, request, context):
    	return app_client_pb2.FindCloudletReply()

    def VerifyLocation(self, request, context):
        return app_client_pb2.VerifyLocationReply()

    def PlatformFindCloudlet(self, request, context):
        return app_client_pb2.FindCloudletReply()

    def GetLocation(self, request, context):
        return app_client_pb2.GetLocationReply()

    def AddUserToGroup(self, request, context):
    	return app_client_pb2.DynamicLocGroupReply()

    def GetAppInstList(self, request, context):
    	return app_client_pb2.AppInstListReply()

    def GetFqdnList(self, request, context):
    	return app_client_pb2.FqdnListReply()

    def GetAppOfficialFqdn(self, request, context):
    	return app_client_pb2.AppOfficialFqdnReply()

    def GetQosPositionKpi(self, request, context):
    	return app_client_pb2.QosPositionKpiReply()

    # Now, finally, stream request, stream reply:
    def SendEdgeEvent(self, request_iterator, context):
        print("Hi!")
        # It's just going to ignore request_iterator (ServerEdgeEvent stream)
        while se_event_doit:
        	yield app_client_pb2.ClientEdgeEvent()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    app_client_pb2_grpc.add_MatchEngineApiServicer_to_server(
        MatchEngineApiServicer(), server)
    #server.add_insecure_port('[::]:50051')
    
    # read in key and certificate
    with open('server.key', 'rb') as f:
        private_key = f.read()
    with open('server.crt', 'rb') as f:
        certificate_chain = f.read()

    server_credentials = grpc.ssl_server_credentials(
      ((private_key, certificate_chain,),))

    server.add_secure_port('[::]:50051', server_credentials)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
