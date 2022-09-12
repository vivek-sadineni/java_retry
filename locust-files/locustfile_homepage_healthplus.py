import csv
import random
import warnings
import os

from locust import FastHttpUser, task, between



class SastaSundarCheckout(FastHttpUser):
    host = os.getenv('TARGET_URL', 'https://healthplus.flipkart.com/')
    network_timeout = 15.0
    connection_timeout = 15.0
    def on_start(self):
        warnings.filterwarnings("ignore")
        self.client.verify = False

    @task
    def sasta_sundar_search_query(self):
        self.client.get("/")
