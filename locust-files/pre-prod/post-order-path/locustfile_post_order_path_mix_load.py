import csv
import random
import warnings
import os

from locust import HttpUser, task, between
from requests.auth import HTTPDigestAuth

"""
fetch profile - 31.7
myorder - 32
cart checkout -  64
create address - 3.5
order success info - 5.2
create order - 5
total = 32 + 32 + 64 + 4 + 5 + 5 = 142
"""

fetch_profile_header = {
    "cookie": '''ga=GA1.2.1915765794.1656325597; _gcl_au=1.1.2100115229.1656325597; _gid=GA1.2.1005279687.1661250102; cartsynch=0; IsLab=0; PHPSESSID=ksk7b002og5sdgain1lvsacth2; GuestUserID=ksk7b002og5sdgain1lvsacth2; cookie_consent=Y; cisession_in_com=159d47f6e81697c048affd0613d46931; csrf=9; UIVAL=AQcPfVZaGQRtExc%3D; browserPopUpData=["ksk7b002og5sdgain1lvsacth2","2022-08-24T03:12:50.111Z"]; isPanIndia=N; LocationSkipped=0; auth_token=authentic; profileUpdated=Y; PanIndiaStateName=West+Bengal; PanIndiaStateCode=WB; PanIndiaStateID=35; PanIndiaCityName=Kolkata; PanIndiaCityID=806; WHId=1; userLocation=West+Bengal; UserLocationPincode=700001; DeliveryDateVal=We will serve you soon; DeliveryDateCallTime=1661312241348''',

    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}

my_order_header = {
    "cookie": '''ga=GA1.2.1915765794.1656325597; _gcl_au=1.1.2100115229.1656325597; _gid=GA1.2.1005279687.1661250102; cartsynch=0; IsLab=0; PHPSESSID=ksk7b002og5sdgain1lvsacth2; GuestUserID=ksk7b002og5sdgain1lvsacth2; cookie_consent=Y; cisession_in_com=159d47f6e81697c048affd0613d46931; csrf=9; UIVAL=AQcPfVZaGQRtExc%3D; browserPopUpData=["ksk7b002og5sdgain1lvsacth2","2022-08-24T03:12:50.111Z"]; isPanIndia=N; LocationSkipped=0; auth_token=authentic; profileUpdated=Y; PanIndiaStateName=West+Bengal; PanIndiaStateCode=WB; PanIndiaStateID=35; PanIndiaCityName=Kolkata; PanIndiaCityID=806; WHId=1; userLocation=West+Bengal; UserLocationPincode=700001; DeliveryDateVal=We will serve you soon; DeliveryDateCallTime=1661312241348''',

    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}
my_order_body = {
    "orderType": "O",
    "pageNo": 1,
    "recordPerPage": 10
}

cart_checkout_body_get_otp = {
    "RequestHeader": {
        "AppType": "N",
        "AppVersion": "4.0.4",
        "AppVersionCode": "109",
        "DeviceId": "f21e21e1-a1bd-4b9e-a620-6da754085a9e",
        "DeviceDensity": "440",
        "DeviceDensityType": "xhdpi",
        "DeviceHeight": "2160",
        "DeviceWidth": "1080",
        "DeviceName": "Google Pixel 4a",
        "DeviceOsInfo": "12",
        "NetworkInfo": "Wifi",
        "AccessToken": "PDWZ5pStjE"
    },
    "RequestURI": {
        "Section": "regenerateOtp"
    },
    "Params": {
        "MobileNo": "9051026063",
        "UserIP": "",
        "UserAgent": "Dalvik/2.1.0 (Linux; U; Android 12; Pixel 4a Build/SQ1A.220205.002)",
        "CampaignId": "",
        "warehouseId": "",
        "PanIndia": "0",
        "Latitude": "",
        "Longitude": "",
        "Pincode": ""
    }
}

cart_checkout_body_verify_otp = {
    "RequestHeader": {
        "AppType": "N",
        "AppVersion": "4.0.4",
        "AppVersionCode": "109",
        "DeviceId": "f21e21e1-a1bd-4b9e-a620-6da754085a9e",
        "DeviceDensity": "440",
        "DeviceDensityType": "xhdpi",
        "DeviceHeight": "2160",
        "DeviceWidth": "1080",
        "DeviceName": "Google Pixel 4a",
        "DeviceOsInfo": "12",
        "NetworkInfo": "Wifi",
        "AccessToken": "PDWZ5pStjE"
    },
    "RequestURI": {
        "Section": "verifyOtp"
    },
    "Params": {
        "MobileNo": "9051026063",
        "OTP": "32529",
        "UserIP": "",
        "UserAgent": "Dalvik/2.1.0 (Linux; U; Android 12; Pixel 4a Build/SQ1A.220205.002)",
        "CampaignId": "",
        "IsLocationRequired": "Y",
        "LocationData": {
            "Pincode": "",
            "StateId": "",
            "StateName": "",
            "StateCode": "",
            "CityId": "",
            "CityName": "",
            "LocationSkipped": ""
        }
    }
}

header_cart_checkout = {
    "Content-Type": "application/json",
    "apptype": "N",
    "appversion": "4.0.5",
    "appversioncode": "109",
    "deviceid": "f21e21e1-a1bd-4b9e-a620-6da754085a9e",
    "userid": "5108874",
    "pincode": "700156",
    "is_panindia": "0",
    "warehouse_id": "1"
}

order_success_body = {
    "orderids": "8933318847"
}

order_success_header = {
    "Apptype": "N",
    "Appversion": "4.0.4",
    "Appversioncode": "109",
    "Deviceid": "81653dce-0dd2-4201-8916-4aecbdd89269",
    "Devicedensity": "320",
    "Devicedensitytype": "xhdpi",
    "Deviceheight": "1184",
    "Devicewidth": "768",
    "Devicename": "Unknown Google Nexus 4",
    "Deviceosinfo": "5.1",
    "Networkinfo": "Wifi",
    "Accesstoken": "PDWZ5pStjE",
    "Refdeviceid": "4dd29c0f2f8d1842",
    "Userid": "4937724",
    "Pincode": "700120",
    "Is_panindia": "0",
    "Warehouse_id": "1",
    "Content-Type": "application/json",
    "Content-Length": "25",
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "okhttp/5.0.0-alpha.2"

}

header_ca = {
    "cookie": '''ga=GA1.2.1915765794.1656325597; _gcl_au=1.1.2100115229.1656325597; _gid=GA1.2.1005279687.1661250102; cartsynch=0; IsLab=0; PHPSESSID=ksk7b002og5sdgain1lvsacth2; GuestUserID=ksk7b002og5sdgain1lvsacth2; cookie_consent=Y; cisession_in_com=159d47f6e81697c048affd0613d46931; csrf=9; UIVAL=AQcPfVZaGQRtExc%3D; browserPopUpData=["ksk7b002og5sdgain1lvsacth2","2022-08-24T03:12:50.111Z"]; isPanIndia=N; LocationSkipped=0; auth_token=authentic; profileUpdated=Y; PanIndiaStateName=West+Bengal; PanIndiaStateCode=WB; PanIndiaStateID=35; PanIndiaCityName=Kolkata; PanIndiaCityID=806; WHId=1; userLocation=West+Bengal; UserLocationPincode=700001; DeliveryDateVal=We will serve you soon; DeliveryDateCallTime=1661312241348''',

    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}
body_ca = {
    "add_name": "Ashutosh Kaushik",
    "add_address": "173, JR layout, Harlur Road, Banglore",
    "add_landmark": "Udaan",
    "add_pin": 560102,
    "add_area": 159096,
    "user_address_type": "O"
}

device_id = "f21e21e1-a1bd-4b9e-a620-6da754085a9e"

body_cart_checkout = {"products": [{"product_id": "9841", "quantity": 1, "ref_id": ""}]}
smallcase_char = "abcdefghijklmnopqrstuvwxyz"


class PostOrderPathMixLoad(HttpUser):
    SEARCH_QUERIES = []

    def get_mobile_number(self):
        no = ""
        for i in range(0, 10):
            x = random.randint(5, 9)
            no = no + str(x)
        return no

    def get_device_id(self):
        id = ""
        for ch in device_id:
            if 'a' <= ch <= 'z':
                id = id + random.choice(smallcase_char)
            elif '1' <= ch <= '9':
                id = id + str(random.randint(1, 9))
            else:
                id = id + ch;
        # print(id)
        return id;

    def on_start(self):
        warnings.filterwarnings("ignore")
        self.client.verify = False
        self.cart_checkout_body_get_otp["Params"]["MobileNo"] = self.get_mobile_number()
        self.cart_checkout_body_get_otp["RequestHeader"]["DeviceId"] = self.get_device_id()
        self.body_verify_otp["Params"]["MobileNo"] = self.cart_checkout_body_get_otp["Params"]["MobileNo"]
        self.body_verify_otp["RequestHeader"]["DeviceId"] = self.cart_checkout_body_get_otp["RequestHeader"]["DeviceId"]
        self.header_cart_checkout["deviceid"] = self.cart_checkout_body_get_otp["RequestHeader"]["DeviceId"]
        self.login()

    def login(self):
        response = self.client.post(
            "https://fkhp-preprod-api.sastasundar.com/sastasundar/customer/rest_customer/postData",
            json=cart_checkout_body_get_otp)
        print(response.text)
        if response.status_code == 200:
            # print(response.text)
            json_response = response.json()
            self.body_verify_otp["Params"]["OTP"] = json_response["ResponseData"]["data"]
            response = self.client.post(
                "https://fkhp-preprod-api.sastasundar.com/sastasundar/customer/rest_customer/postData",
                json=cart_checkout_body_verify_otp
            )
            print(response.text)
            json_response = response.json()
            if json_response["ResponseData"].get("data", {}) != {}:
                print(response.text)
                self.header_cart_checkout["userid"] = str(json_response["ResponseData"]["data"]["UserId"])
            print("Logged In")

    @task
    def fetch_profile(self):
        self.client.post("https://fkhp-preprod-fe.sastasundar.com/index.php/customers/user/fetchProfile",
                         headers=fetch_profile_header)
        self.client.post("https://fkhp-preprod-fe.sastasundar.com/index.php/customers/order/myorders",
                         headers=my_order_header, data=my_order_body)
        self.client.post("https://preprod-fkhapi.sastasundar.com/checkout",
                         headers=self.header_cart_checkout,
                         json=cart_checkout_body_get_otp)
        self.client.post("https://preprod-fkhapi.sastasundar.com/orderinfo/ordersuccessinfo",
                         headers=order_success_header, json=order_success_body, auth=HTTPDigestAuth('admin', '1234'))
        self.client.post("https://preprod-fkhapi.sastasundar.com/orderinfo/createorder",
                         headers=self.header_cart_checkout)
        self.client.post("/index.php/webapi/cartuserapp/create_address", headers=header_ca, data=body_ca)
