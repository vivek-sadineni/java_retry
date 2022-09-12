import time

import sonora.client

from locust import task
from locust import User
from locust import TaskSet

from gateway.clients.FetchClient_pb2_grpc import FetchClientStub
from gateway.requests.FetchPageRequest_pb2 import FetchPageRequest
from gateway.responses.FetchResponse_pb2 import FetchResponse
from gateway.models.app.AppInfo_pb2 import AppInfo
from gateway.models.device.DeviceInfo_pb2 import DeviceInfo
from gateway.models.user.UserInfo_pb2 import UserInfo
from mapi.MetadataClientInterceptor import MetadataClientInterceptor

header_object = {
    # "content-type": "application/grpc-web+proto",
    "x-client": "mapi",
    "x-cookie":
     "_fbp=fb.1.1661241781083.484329401; isPanIndia=Y; cartsynch=0; WHId=10; UserLocationPincode=560103; PanIndiaCityName=Bangalore; userLocation=Karnataka; PanIndiaStateName=Karnataka; PanIndiaStateCode=KA; PanIndiaCityID=20122; LocationSkipped=0; IsLab=0; PanIndiaStateID=16; GuestUserID=mqob8uq649jh1ittvdhji0lck2; PHPSESSID=mqob8uq649jh1ittvdhji0lck2; sspl_csrf=d7ef3d98fbf0431e9818149341b8c5bc; UIVAL=DQIFew%3D%3D; cisession_in_com=7a010de3d0b7e0762927106327eed042; moe_uuid=47bebdc0-0cd9-42f0-ba95-0fc120549170",
    "x-csrf-test-name": "d7ef3d98fbf0431e9818149341b8c5bc",
    "x-timestamp": "142433",
    "x-user-agent":
     "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.3"
}


class FetchClient:

    def fetch(self, request: FetchPageRequest) -> FetchResponse:
        interceptors = [MetadataClientInterceptor()]
        # with sonora.client.insecure_web_channel(
        #         f"https://fkhp-gw.nl-demo.com/"
        # ) as channel:
        #     channel = grpc.intercept_channel(channel, *interceptors)
            # print("request for gateway")
        # print(request)
        stub = FetchClientStub(
            sonora.client.insecure_web_channel(
                f"https://fkhp-gw.nl-demo.com/fkhp.gateway.layer.client.FetchClient/fetch")).fetch
        resp, call = stub.with_call(request=request, timeout=100000, metadata=header_object)
        print("printing request and response")
        print(request)
        print(call)
        print(resp)


class PerfTaskSet(TaskSet):

    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task
    def fetch(self):
        req_data = FetchPageRequest(path="/home-page", appInfo=self.get_app_info(),
                                    deviceInfo=self.get_device_info(),
                                    userInfo=self.get_user_info(), request=self.get_request(), fetchPageReactionType=8)
        self.locust_request_handler("fetch", req_data)

    def get_app_info(self):
        req_data = AppInfo(appVersion="1", appType=2)
        return req_data

    def get_device_info(self):
        return DeviceInfo(deviceId="4d118b7af5cd52f54b60ade9f6523160", deviceIP="0.0.0.0")

    def get_user_info(self):
        return UserInfo(accountId="", userType="New", loggedIn="LOGGED_IN", org="FKH")

    def get_request(self):
        return {
            "userId": "",
            "appVersion": "1",
            "deviceId": "4d118b7af5cd52f54b60ade9f6523160",
            "csrf": "dde6e7944df8451fb369c7446b1492ac"
        }

    def locust_request_handler(self, grpc_name, req_data):
        req_func = self._get_request_function(grpc_name)
        start = time.time()
        result = None
        try:
            result = req_func(req_data)
        except Exception as e:
            total = int((time.time() - start) * 1000)
            self.user.environment.events.request_failure.fire(
                request_type="grpc", name=grpc_name, response_time=total, response_length=0, exception=e)
        else:
            total = int((time.time() - start) * 1000)
            self.user.environment.events.request_success.fire(
                request_type="grpc", name=grpc_name, response_time=total, response_length=0)
        return result

    def _get_request_function(self, grpc_name):
        req_func_map = {
            "fetch": self.client.fetch,
        }
        if grpc_name not in req_func_map:
            raise ValueError(f"gRPC name not supported [{grpc_name}]")
        return req_func_map[grpc_name]


class TesterUser(User):
    tasks = [PerfTaskSet]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = FetchClient()
