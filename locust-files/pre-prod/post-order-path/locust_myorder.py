import csv
import random
import warnings
import os

from locust import HttpUser, task, between

LINK = "/index.php/customers/order/myorders"
header = {
    "cookie": '''ga=GA1.2.1915765794.1656325597; _gcl_au=1.1.2100115229.1656325597; _gid=GA1.2.1005279687.1661250102; cartsynch=0; IsLab=0; PHPSESSID=ksk7b002og5sdgain1lvsacth2; GuestUserID=ksk7b002og5sdgain1lvsacth2; cookie_consent=Y; cisession_in_com=159d47f6e81697c048affd0613d46931; csrf=9; UIVAL=AQcPfVZaGQRtExc%3D; browserPopUpData=["ksk7b002og5sdgain1lvsacth2","2022-08-24T03:12:50.111Z"]; isPanIndia=N; LocationSkipped=0; auth_token=authentic; profileUpdated=Y; PanIndiaStateName=West+Bengal; PanIndiaStateCode=WB; PanIndiaStateID=35; PanIndiaCityName=Kolkata; PanIndiaCityID=806; WHId=1; userLocation=West+Bengal; UserLocationPincode=700001; DeliveryDateVal=We will serve you soon; DeliveryDateCallTime=1661312241348''',

    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}
body = {
    "orderType": "O",
    "pageNo": 1,
    "recordPerPage": 10
}
class MyOrder(HttpUser):
    host = os.getenv('TARGET_URL', 'https://fkhp-preprod-fe.sastasundar.com')

    def on_start(self):
        warnings.filterwarnings("ignore")
        self.client.verify = False

    @task
    def sasta_sundar_search_query(self):
        response = self.client.post(LINK, headers=header, data=body)
        # print(response.text)


