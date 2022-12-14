import random
import warnings
import os

from locust import HttpUser, task
import json

header_object = {
    "Host": "fkhapi.sastasundar.com",
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
     "Content-Length": "63",
     "Accept-Encoding": "gzip, deflate",
     "User-Agent": "okhttp/5.0.0-alpha.2"
}
data_object = {
    "products":[
        {
            "id":"21813",
            "qty":1,
            "p_type":"O",
            "ref_id":""
        }
    ]
}


class AddToCart(HttpUser):
    host = os.getenv('TARGET_URL', 'https://fkhapi.sastasundar.com')
    product_ids = []

    def fetch_product_ids(self):
        f = open('../../productId.json')
        data = json.load(f)
        for product in data['items']:
            self.product_ids.append(product['ProductId'])

    def on_start(self):
        warnings.filterwarnings("ignore")
        self.fetch_product_ids()
        self.client.verify = False

    @task
    def sasta_sundar_search_query(self):
        data_object['products'][0]['id'] = random.choice(self.product_ids)
        self.client.post("/basket", json=data_object, auth=None, headers=header_object)
