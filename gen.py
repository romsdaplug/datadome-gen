import requests, random, json

domain = "tickets.rolandgarros.com" # DOMAIN HERE 

def cookiegen(domain):
    headers = {
        'Content-type': 'application/x-www-form-urlencoded',
        'Host': 'api-js.datadome.co',
        'Origin': "https://"+domain.partition("https://")[2],
        'Referer':"https://"+domain.partition("https://")[2],
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko)'
    }
    payload = {
        'ddv': '4.6.0',
        'eventCounters': [],
        'jsType': 'ch',
        'ddk': 'A55FBF4311ED6F1BF9911EB71931D5',
        'events': [],
        'request': '%2F',
        'responsePage': 'origin',
        'cid': "null",
        'dddomain': "https://"+domain.partition("https://")[2],
        'Referer': '',
        'jsData':{
            "ttst": f'{random.randint(10, 99)}.{random.randint(1000000000000, 9000000000000)}',
            "ifov": False,
            "tagpu": f'{random.randint(10, 99)}.{random.randint(1000000000000, 9000000000000)}',
            "glvd": "Google Inc. (NVIDIA)",
            "glrd": "ANGLE (NVIDIA, NVIDIA GeForce GTX 1660 SUPER Direct3D11 vs_5_0 ps_5_0, D3D11)",
            "hc": 16,
            "br_oh": 1040,
            "br_ow": 1920,
            "ua": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko)",
            "wbd": False,
            "wdif": False,
            "wdifrm": False,
            "npmtm": False,
            "br_h": 969,
            "br_w": 963,
            "nddc": 1,
            "rs_h": 1080,
            "rs_w": 1920,
            "rs_cd": 24,
            "phe": False,
            "nm": False,
            "jsf": False,
            "lg": "en-US",
            "pr": 1,
            "ars_h": 1040,
            "ars_w": 1920,
            "tz": 480,
            "str_ss": True,
            "str_ls": True,
            "str_idb": True,
            "str_odb": True,
            "plgod": False,
            "plg": random.randint(5, 14),
            "plgne": True,
            "plgre": True,
            "plgof": False,
            "plggt": False,
            "pltod": False,
            "hcovdr": False,
            "hcovdr2": False,
            "plovdr": False,
            "plovdr2": False,
            "ftsovdr": False,
            "ftsovdr2": False,
            "lb": False,
            "eva": 33,
            "lo": False,
            "ts_mtp": 0,
            "ts_tec": False,
            "ts_tsa": False,
            "vnd": "Google Inc.",
            "bid": "NA",
            "mmt": "application/pdf,text/pdf",
            "plu": "PDF Viewer,Chrome PDF View"
        }
    }

    response = requests.post("https://api-js.datadome.co/js/", headers=headers, data=payload)
    data = json.loads(response.text)
    if "cookie" in response.text:
        print('Successfully genned cookie')
        print(data['cookie'])
    else:
        print('Error while genning cookie')
        print(data)

cookiegen(domain)