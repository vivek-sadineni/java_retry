# -*- coding: utf-8 -*-

"""
This contains to load test of Url-Mapping of gRPC call with locust.
"""

import time
import uuid

import grpc
from locust import task
from locust import User
from locust import TaskSet

from gateway.clients.WalletService_pb2_grpc import WalletServiceStub
from gateway.models.app.AppInfo_pb2 import AppInfo
from gateway.models.device.DeviceInfo_pb2 import DeviceInfo
from gateway.requests.WalletUnlinkRequest_pb2 import WalletUnlinkRequest
from gateway.responses.WalletUnlinkResponse_pb2 import WalletUnlinkResponse
from mapi.MetadataClientInterceptor import MetadataClientInterceptor


class TesterClient:

    def __init__(self):
        self.host = "34.100.234.141:80"
        self.interceptors = [MetadataClientInterceptor()]

    def unlink_account(self, request: WalletUnlinkRequest) -> WalletUnlinkResponse:
        stub = WalletServiceStub(grpc.intercept_channel(grpc.insecure_channel(self.host), *self.interceptors))
        stub.unlinkAccount(request=request)


class PerfTaskSet(TaskSet):

    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task
    def unlink_account(self):
        req_data = WalletUnlinkRequest(appInfo=self.get_app_info(), deviceInfo=self.get_device_info(),
                                        mobileNumber="9811371549", walletType=0)
        self.locust_request_handler("unlink_account", req_data)

    def get_app_info(self):
        return AppInfo(appType=2, appVersion="1")

    def get_device_info(self):
        return DeviceInfo(deviceId="11514df1934cf6e6acf178afe1918bce", deviceIP="0.0.0.0")
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
            "unlink_account": self.client.unlink_account
        }
        if grpc_name not in req_func_map:
            raise ValueError(f"gRPC name not supported [{grpc_name}]")
        return req_func_map[grpc_name]


class TesterUser(User):
    tasks = [PerfTaskSet]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = TesterClient()
