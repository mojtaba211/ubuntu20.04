import requests,time,random

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjMyMjA5OTUyNSwiaWF0IjoxNzEyMzE2OTUwLCJleHAiOjE3MTIzMjA1NTB9.0H2ki1l2lg2tlQr7sOzv-YY7zKjoW43im18vEqx6CpY',
    'Connection': 'keep-alive',
    'Content-Id': '322070279',
    'Content-Type': 'application/json',
    'Origin': 'https://app.tapswap.ai',
    'Referer': 'https://app.tapswap.ai/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'x-cv': '342',
}

json_data = {
    'taps': 1,
    'time': 1712317237798,
}

balance = None
tap = 1
while True:
    try:
        json_data['taps'] = random.randint(1,tap)
        json_data['time'] = int(time.time()*1000)
        response = requests.post('https://api.tapswap.ai/api/player/submit_taps', headers=headers, json=json_data)
        
        if response.status_code == 201:
            balanace_2 = response.json()['player']['shares']
            if balanace_2 == balance:
                print("ERR Balance")
                time.sleep(60)
                continue
            else:
                tap = (response.json()['player']['energy']//response.json()['player']['tap_level'])
            time.sleep(random.randint(10,30))
        else:
            print(response.status_code)
            print(response.text)
            time.sleep(60)
    except:
      pass
