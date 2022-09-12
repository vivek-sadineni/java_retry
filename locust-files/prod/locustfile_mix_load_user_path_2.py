import csv
import random
import warnings
import os

from locust import HttpUser, task, between




header1 = {"cookie": '''T=TI164922685845700296292883240291767363571549416617245158015905844352; Network-Type=4g; pxcts=96d08337-b573-11ec-94f4-5458434c6246; _pxvid=96d07630-b573-11ec-94f4-5458434c6246; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; _gcl_au=1.1.1577513354.1654787934; cartsynch=0; InitForMob=false; prescriptionId=; PHPSESSID=dr7as2hgeviuao2us520jsg172; addressTypName=; LocationSkipped=0; MembershipId=null; CardStatus=null; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19211%7CMCMID%7C03547093981926272024322102480078472856%7CMCAAMLH-1660416624%7C12%7CMCAAMB-1660416624%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1659819024s%7CNONE%7CMCAID%7CNONE; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Afurniture%25253Abeds-more%25253Abeds%25253Apr%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.flipkart.com%25252Fflipkart-perfect-homes-sonore-engineered-wood-single-box-bed%25252Fp%25252Fitmdf04030a1%2526ot%253DA; SN=VIE02AEDFBEC394CEAA205AC62FD28F9F4.TOKE66E39E4860E41F28A6CDA258044B284.1659811945.LO; S=d1t19BlFgIjVCAwETdj8/P09NPz1rksS+D9G0TQQXYDqpdumcxd+UZuTm90FRDOBqzM5T7VBylLvvgA7I2PJXE/U1AA==; GuestUserID=dr7as2hgeviuao2us520jsg172; profileUpdated=N; lab_booking_count=null; cookie_consent=Y; myorderpagevisitFK=Y; _ga=GA1.1.101759026.1654787985; uToken=eY2dFgvvxzo:APA91bEO2zGb9ccy67ljZtSS1XsxNGPfYCRgBlrCOQkMCUmQ4IKLk_ZBMfyuHnSTWbxY0qkYWyRCcL4xiuH0l9GqVubOTvY_HU_js1u_LhmJ8hB6hRgUWIfph-o6zzhIq5NRGogarjxS; browserPopUpData=["dr7as2hgeviuao2us520jsg172","2022-08-30T08:38:10.881Z"]; SellerHBContact=9330803080; PanIndiaStateName=Karnataka; PanIndiaStateCode=KA; PanIndiaStateID=16; PanIndiaCityName=Bangalore; PanIndiaCityID=20122; WHId=10; userLocation=Karnataka; isPanIndia=Y; IsLab=0; UserLocationPincode=560102; WHIdCreationDate=1661850625362; SellerAddline=SY.+No.-+95%2C+Block+-+C%2C+Ground+Floor%2C+P.B.Road%2C+Dasanapura%2C+Tal+-+Nelamangala; SellerCity=Bengaluru; SellerStateName=562162; SellerPinCode=Karnataka; SellerFASSAILicenceNo=11222012000002; SellerJoiningDate=1+month; sspl_csrf=75ec21446ff5ca33168ed802cde2d5cf; cisession_in_com=b1caf316286650f423247cbed7762a9f; UIVAL=AgAAdV1bEwVtExI%3D; revisedCart=Y; addressId=; _ga_PXT3VW5F62=GS1.1.1661859630.19.1.1661859658.32.0.0; pagerefresh=N''',}
header2 = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://healthplus.flipkart.com",
            "referer": "https://healthplus.flipkart.com/",
            "sec-ch-ua": '''"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"''',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "Android",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36"
        }
header_login = {'authority': 'healthplus.flipkart.com', 'accept': 'application/json, text/plain, */*', 'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7', 'cookie': 'T=TI164922685845700296292883240291767363571549416617245158015905844352; pxcts=96d08337-b573-11ec-94f4-5458434c6246; _pxvid=96d07630-b573-11ec-94f4-5458434c6246; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; cartsynch=0; InitForMob=false; prescriptionId=; LocationSkipped=0; MembershipId=null; CardStatus=null; profileUpdated=N; lab_booking_count=null; cookie_consent=Y; myorderpagevisitFK=Y; _ga=GA1.1.101759026.1654787985; uToken=eY2dFgvvxzo:APA91bEO2zGb9ccy67ljZtSS1XsxNGPfYCRgBlrCOQkMCUmQ4IKLk_ZBMfyuHnSTWbxY0qkYWyRCcL4xiuH0l9GqVubOTvY_HU_js1u_LhmJ8hB6hRgUWIfph-o6zzhIq5NRGogarjxS; PanIndiaStateName=Karnataka; PanIndiaStateCode=KA; PanIndiaStateID=16; PanIndiaCityName=Bangalore; PanIndiaCityID=20122; WHId=10; userLocation=Karnataka; isPanIndia=Y; UserLocationPincode=560102; pagerefresh=N; revisedCart=Y; CampId=88044NfYd3Bvh1XSgupY; searchTxt=; addressTypName=; IsLab=null; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19241%7CMCMID%7C03547093981926272024322102480078472856%7CMCAAMLH-1663010343%7C12%7CMCAAMB-1663010343%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1662412743s%7CNONE%7CMCAID%7CNONE; SN=VI7F750F1184AD4050BFE2B9FF9E47DF3F.TOK345F9C5008D24E7BA8C2664FC3964F30.1662409859.LO; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Agreen-soul-zodiac-pro-high-back-ergonomic-chair-home-office-wfh-seat-slider-premium-mesh-office-adjustable-arm-chair%25253Ap%25253Aitm0dce3d575abc4%2526pidt%253D1%2526oid%253DfunctionEr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT; S=d1t19OU5JPz8GaD9QOj9hPz9eP7zYFo6UGWLj7ZyEZgq7i6Fuk/nOdJiJj9fID1AFisS3wBtLmmcTQ2JlvzHuX0LSWA==; Network-Type=4g; sspl_csrf=3a5321192e04b0b3262f9ee8f411daca; _gcl_au=1.1.760732449.1662657146; DeliveryDateVal=Earliest Delivery in 3 day(s); DeliveryDateCallTime=1662657145437; cisession_in_com=1979f7c688dd0012a2f71a896239c1b8; browserPopUpData=[null,"2022-09-08T17:12:35.785Z"]; WHIdCreationDate=1662657159134; PHPSESSID=bg1aaa2ln1d3rqpo3nq3gaas16; GuestUserID=bg1aaa2ln1d3rqpo3nq3gaas16; UIVAL=AgAAdV1bEwVrEBA%3D; addressId=; _ga_PXT3VW5F62=GS1.1.1662657159.25.1.1662657181.38.0.0', 'origin': 'https://healthplus.flipkart.com', 'referer': 'https://healthplus.flipkart.com//', 'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.3'}

header_myorder = {'authority': 'healthplus.flipkart.com', 'accept': 'application/json, text/plain, */*', 'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7', 'cookie': 'T=TI164922685845700296292883240291767363571549416617245158015905844352; pxcts=96d08337-b573-11ec-94f4-5458434c6246; _pxvid=96d07630-b573-11ec-94f4-5458434c6246; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; cartsynch=0; InitForMob=false; prescriptionId=; LocationSkipped=0; MembershipId=null; CardStatus=null; profileUpdated=N; lab_booking_count=null; cookie_consent=Y; myorderpagevisitFK=Y; _ga=GA1.1.101759026.1654787985; uToken=eY2dFgvvxzo:APA91bEO2zGb9ccy67ljZtSS1XsxNGPfYCRgBlrCOQkMCUmQ4IKLk_ZBMfyuHnSTWbxY0qkYWyRCcL4xiuH0l9GqVubOTvY_HU_js1u_LhmJ8hB6hRgUWIfph-o6zzhIq5NRGogarjxS; PanIndiaStateName=Karnataka; PanIndiaStateCode=KA; PanIndiaStateID=16; PanIndiaCityName=Bangalore; PanIndiaCityID=20122; userLocation=Karnataka; isPanIndia=Y; UserLocationPincode=560102; pagerefresh=N; CampId=88044NfYd3Bvh1XSgupY; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19241%7CMCMID%7C03547093981926272024322102480078472856%7CMCAAMLH-1663010343%7C12%7CMCAAMB-1663010343%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1662412743s%7CNONE%7CMCAID%7CNONE; SN=VI7F750F1184AD4050BFE2B9FF9E47DF3F.TOK345F9C5008D24E7BA8C2664FC3964F30.1662409859.LO; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Agreen-soul-zodiac-pro-high-back-ergonomic-chair-home-office-wfh-seat-slider-premium-mesh-office-adjustable-arm-chair%25253Ap%25253Aitm0dce3d575abc4%2526pidt%253D1%2526oid%253DfunctionEr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT; S=d1t19OU5JPz8GaD9QOj9hPz9eP7zYFo6UGWLj7ZyEZgq7i6Fuk/nOdJiJj9fID1AFisS3wBtLmmcTQ2JlvzHuX0LSWA==; Network-Type=4g; _gcl_au=1.1.760732449.1662657146; browserPopUpData=[null,"2022-09-08T17:12:35.785Z"]; PHPSESSID=bg1aaa2ln1d3rqpo3nq3gaas16; GuestUserID=bg1aaa2ln1d3rqpo3nq3gaas16; WHId=1; success_page_orderids=25238742543; sspl_csrf=1a9254d989af450dd92b8e3bf2d79a73; DeliveryDateVal=Earliest Delivery in 3 day(s); DeliveryDateCallTime=1662711314917; cisession_in_com=7c0c6d05b3783e910ba141c875c36cbd; addressTypName=; UIVAL=AgAAdV1bEwJmExE%3D; revisedCart=Y; WHIdCreationDate=1662711351923; IsLab=0; addressId=0; searchTxt=; _ga_PXT3VW5F62=GS1.1.1662711323.28.1.1662711366.17.0.0', 'origin': 'https://healthplus.flipkart.com', 'referer': 'https://healthplus.flipkart.com/customers/dashboard/myorders', 'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.3'}

class SastaSundarSearch(HttpUser):
    host = os.getenv('TARGET_URL', 'https://search.sastasundar.com')


    def on_start(self):
        warnings.filterwarnings("ignore")
        self.client.verify = False

    @task
    def sasta_sundar_search_query(self):
        var = random.randint(0, 79 + 15 + 45 + 47 + 76 + 64 + 80 + 47 + 1 + 80 + 19 + 88 + 5 + 1)
        if var <= 79:
            self.client.get("https://healthplus.flipkart.com/index.php/webapi/location/get_delivery_date", headers={"cookie": '''T=TI164922685845700296292883240291767363571549416617245158015905844352; Network-Type=4g; pxcts=96d08337-b573-11ec-94f4-5458434c6246; _pxvid=96d07630-b573-11ec-94f4-5458434c6246; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; _gcl_au=1.1.1577513354.1654787934; cartsynch=0; InitForMob=false; prescriptionId=; PHPSESSID=dr7as2hgeviuao2us520jsg172; addressTypName=; LocationSkipped=0; MembershipId=null; CardStatus=null; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19211%7CMCMID%7C03547093981926272024322102480078472856%7CMCAAMLH-1660416624%7C12%7CMCAAMB-1660416624%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1659819024s%7CNONE%7CMCAID%7CNONE; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Afurniture%25253Abeds-more%25253Abeds%25253Apr%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.flipkart.com%25252Fflipkart-perfect-homes-sonore-engineered-wood-single-box-bed%25252Fp%25252Fitmdf04030a1%2526ot%253DA; SN=VIE02AEDFBEC394CEAA205AC62FD28F9F4.TOKE66E39E4860E41F28A6CDA258044B284.1659811945.LO; S=d1t19BlFgIjVCAwETdj8/P09NPz1rksS+D9G0TQQXYDqpdumcxd+UZuTm90FRDOBqzM5T7VBylLvvgA7I2PJXE/U1AA==; GuestUserID=dr7as2hgeviuao2us520jsg172; profileUpdated=N; lab_booking_count=null; cookie_consent=Y; myorderpagevisitFK=Y; _ga=GA1.1.101759026.1654787985; uToken=eY2dFgvvxzo:APA91bEO2zGb9ccy67ljZtSS1XsxNGPfYCRgBlrCOQkMCUmQ4IKLk_ZBMfyuHnSTWbxY0qkYWyRCcL4xiuH0l9GqVubOTvY_HU_js1u_LhmJ8hB6hRgUWIfph-o6zzhIq5NRGogarjxS; browserPopUpData=["dr7as2hgeviuao2us520jsg172","2022-08-30T08:38:10.881Z"]; SellerHBContact=9330803080; PanIndiaStateName=Karnataka; PanIndiaStateCode=KA; PanIndiaStateID=16; PanIndiaCityName=Bangalore; PanIndiaCityID=20122; WHId=10; userLocation=Karnataka; isPanIndia=Y; IsLab=0; UserLocationPincode=560102; WHIdCreationDate=1661850625362; SellerAddline=SY.+No.-+95%2C+Block+-+C%2C+Ground+Floor%2C+P.B.Road%2C+Dasanapura%2C+Tal+-+Nelamangala; SellerCity=Bengaluru; SellerStateName=562162; SellerPinCode=Karnataka; SellerFASSAILicenceNo=11222012000002; SellerJoiningDate=1+month; sspl_csrf=75ec21446ff5ca33168ed802cde2d5cf; cisession_in_com=b1caf316286650f423247cbed7762a9f; UIVAL=AgAAdV1bEwVtExI%3D; revisedCart=Y; addressId=; _ga_PXT3VW5F62=GS1.1.1661859630.19.1.1661859658.32.0.0; pagerefresh=N''',
           }, data={'wh': '10', 'panindia': '0', 'pincode': '560102', 'page': 'CA', 'csrf_test_name': '75ec21446ff5ca33168ed802cde2d5cf', 'fkh_deviceid': ''})
        elif var <= 79 + 15:
            self.client.get("https://healthplus.flipkart.com/index.php/webapi/order/lastOrderDetails",
                        headers = {'authority': 'ealthplus.flipkart.com', 'accept': 'pplication/json, text/plain, */*', 'accept-language': 'n-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7', 'cookie': '=TI164922685845700296292883240291767363571549416617245158015905844352; pxcts=96d08337-b573-11ec-94f4-5458434c6246; _pxvid=96d07630-b573-11ec-94f4-5458434c6246; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; cartsynch=0; InitForMob=false; prescriptionId=; LocationSkipped=0; MembershipId=null; CardStatus=null; profileUpdated=N; lab_booking_count=null; cookie_consent=Y; myorderpagevisitFK=Y; _ga=GA1.1.101759026.1654787985; uToken=eY2dFgvvxzo:APA91bEO2zGb9ccy67ljZtSS1XsxNGPfYCRgBlrCOQkMCUmQ4IKLk_ZBMfyuHnSTWbxY0qkYWyRCcL4xiuH0l9GqVubOTvY_HU_js1u_LhmJ8hB6hRgUWIfph-o6zzhIq5NRGogarjxS; PanIndiaStateName=Karnataka; PanIndiaStateCode=KA; PanIndiaStateID=16; PanIndiaCityName=Bangalore; PanIndiaCityID=20122; userLocation=Karnataka; isPanIndia=Y; UserLocationPincode=560102; pagerefresh=N; revisedCart=Y; CampId=88044NfYd3Bvh1XSgupY; searchTxt=; addressTypName=; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19241%7CMCMID%7C03547093981926272024322102480078472856%7CMCAAMLH-1663010343%7C12%7CMCAAMB-1663010343%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1662412743s%7CNONE%7CMCAID%7CNONE; SN=VI7F750F1184AD4050BFE2B9FF9E47DF3F.TOK345F9C5008D24E7BA8C2664FC3964F30.1662409859.LO; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Agreen-soul-zodiac-pro-high-back-ergonomic-chair-home-office-wfh-seat-slider-premium-mesh-office-adjustable-arm-chair%25253Ap%25253Aitm0dce3d575abc4%2526pidt%253D1%2526oid%253DfunctionEr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT; S=d1t19OU5JPz8GaD9QOj9hPz9eP7zYFo6UGWLj7ZyEZgq7i6Fuk/nOdJiJj9fID1AFisS3wBtLmmcTQ2JlvzHuX0LSWA==; Network-Type=4g; sspl_csrf=3a5321192e04b0b3262f9ee8f411daca; _gcl_au=1.1.760732449.1662657146; DeliveryDateVal=Earliest Delivery in 3 day(s); DeliveryDateCallTime=1662657145437; cisession_in_com=1979f7c688dd0012a2f71a896239c1b8; browserPopUpData=[null,"2022-09-08T17:12:35.785Z"]; PHPSESSID=bg1aaa2ln1d3rqpo3nq3gaas16; GuestUserID=bg1aaa2ln1d3rqpo3nq3gaas16; UIVAL=AgAAdV1bEwVrEBA%3D; WHId=1; WHIdCreationDate=1662657182547; IsLab=0; addressId=0; _ga_PXT3VW5F62=GS1.1.1662657159.25.1.1662657188.31.0.0', 'origin': 'ttps://healthplus.flipkart.com', 'referer': 'ttps://healthplus.flipkart.com/', 'sec-ch-ua': 'Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"', 'sec-ch-ua-mobile': '1', 'sec-ch-ua-platform': 'Android"', 'sec-fetch-dest': 'mpty', 'sec-fetch-mode': 'ors', 'sec-fetch-site': 'ame-origin', 'user-agent': 'ozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.3'},
                        data = {'app_type': '', 'csrf_test_name': 'a5321192e04b0b3262f9ee8f411daca', 'TimeStamp': '', 'fkh_deviceid': ''}
                        )
        elif var <= 79 + 15 + 45:
            self.client.post("https://catalog.sastasundar.com/home/getmasterhomewidgets", headers=header2,
                                                                                             data={
                                                                                                        "panindia":"1",
                                                                                                        "warehouseId":"10",
                                                                                                        "pincode":"560102",
                                                                                                        "app_type":"N",
                                                                                                        "app_version":"4.0.5",
                                                                                                        "page":"1",
                                                                                                        "IsLab":"0",
                                                                                                        "userId":"6579209"
                                                                                                    }
                            )
        elif var <= 79 + 15 + 45 + 47:
            self.client.get("https://healthplus.flipkart.com/index.php/webapi/product/customer_load_rating?ProductId=dpnven&warehouseId=10&PanIndia=1&Pincode=560102&fkh_deviceid=", headers=header2)
        elif var <= 79 + 15 + 45 + 47 + 76:
            self.client.post("https://healthplus.flipkart.com/index.php/webapi/product/getProductDetails", headers=header1, data = {"productId":"2an7zr",
                                                                                                                                "warehouseId":"10",
                                                                                                                                "apptype":"M",
                                                                                                                                "panindia":"1",
                                                                                                                                "pincode":"560102",
                                                                                                                                "csrf_test_name":"75ec21446ff5ca33168ed802cde2d5cf",
                                                                                                                                "fkh_deviceid":"",
                                                                                                                               }
                         )
        elif var <= 79 + 15 + 45 + 47 + 76 + 64:
            self.client.post("https://healthplus.flipkart.com/index.php/webapi/Product/getSellerNameFK", headers=header1, data={"productId":"100383",
                                                                                                                            "isFoodProduct":"0",
                                                                                                                            "csrf_test_name":"75ec21446ff5ca33168ed802cde2d5cf",
                                                                                                                            "fkh_deviceid":"",
                                                                                                                           }
                         )
        elif var <= 79 + 15 + 45 + 47 + 76 + 64 + 80:
            self.client.get("https://search.sastasundar.com/similar_products?product_id=100383&wh=10&panindia=1&format=2&pincode=560102", headers=header2)
        elif var <= 79 + 15 + 45 + 47 + 76 + 64 + 80 + 47:
            self.client.post("https://catalog.sastasundar.com/product/getRelatedProductList", headers=header2, data ={"productId":"3720",
                                                                                                                    "warehouseId":"10",
                                                                                                                    "panindia":"1",
                                                                                                                    "pincode":"560102",
                                                                                                                  }
                         )
        elif var <= 79 + 15 + 45 + 47 + 76 + 64 + 80 + 47 + 1:
            self.client.post("https://healthplus.flipkart.com/index.php/webapi/product/load_review_rating", headers=header1, data={"ProductId":"3720",
                                                                                                                                "csrf_test_name":"75ec21446ff5ca33168ed802cde2d5cf",
                                                                                                                                "fkh_deviceid":"",
                                                                                                                               }
                         )
        elif var <= 79 + 15 + 45 + 47 + 76 + 64 + 80 + 47 + 1 + 80:
            self.client.get("https://healthplus.flipkart.com/index.php/webapi/location/set_user_location", headers=header1, data={"AppType":"M",
                                                                                                                                "Pincode":"560102",
                                                                                                                                "csrf_test_name":"26025458c22a867b82ab0c7267318b7d",
                                                                                                                              }
                        )
        elif var <= 79 + 15 + 45 + 47 + 76 + 64 + 80 + 47 + 1 + 80 + 19:
            self.client.get("https://healthplus.flipkart.com/index.php/webapi/location/get_user_location?fkh_deviceid=", headers=header1)
        elif var <= 79 + 15 + 45 + 47 + 76 + 64 + 80 + 47 + 1 + 80 + 19 + 88:
            self.client.post("https://healthplus.flipkart.com/index.php/webapi/fkh_app_in_app/dochkLogging_app_in_app", headers=header_login, data={"csrf_test_name":"3a5321192e04b0b3262f9ee8f411daca"})
        elif var <= 79 + 15 + 45 + 47 + 76 + 64 + 80 + 47 + 1 + 80 + 19 + 88 + 5:
            self.client.get("https://healthplus.flipkart.com/index.php/webapi/order/myOrderList", headers=header_myorder, data = {"PageNo":"1",
                                                                                                                                    "RecordPerPage":"10",
                                                                                                                                    "csrf_test_name":"1a9254d989af450dd92b8e3bf2d79a73",
                                                                                                                                    "appinapp":"[object Object]",
                                                                                                                                    "fkh_deviceid":"",})



