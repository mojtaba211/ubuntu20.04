import requests,time,random

headers = {
    'authority': 'clicker-api.joincommunity.xyz',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'auth': '5',
   'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjExMzI2NDAzLCJleHBpcmUiOjE3MDUyOTI2NDY0MDUsImlhdCI6MTcwNTI3MTA0NiwiZXhwIjoxNzEzMDQ3MDQ2fQ.GdHKMVMSwv_H4g43lvaYH1j6bH_gahIKrrav3vleMyE',
    'content-type': 'application/json',
    'origin': 'https://clicker.joincommunity.xyz',
    'referer': 'https://clicker.joincommunity.xyz/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
}

json_data = {
    'count': 1,
     'webAppData': 'query_id=AAHnHX8IAwAAAOcdfwjnT6d9&user=%7B%22id%22%3A6584999399%2C%22first_name%22%3A%22Majid%22%2C%22last_name%22%3A%22%22%2C%22username%22%3A%22majid_sozoki1%22%2C%22language_code%22%3A%22fa%22%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=1705270954&hash=9e5f42038bb26cc579abfecf647be7320355c2530202691044ce569bfdb2f2b0',
}
m = 0
while True:
    try:
        response = requests.post('https://clicker-api.joincommunity.xyz/clicker/core/click', headers=headers, json=json_data,timeout=5)
        if response.json()['ok'] == True:
            if response.json()['data'][0] == 0:
                time.sleep(random.randint(1,5))
                continue  
            else:
                json_data['count'] = random.randint(1,(400 if response.json()['data'][0]['availableCoins'] > 400 else response.json()['data'][0]['availableCoins']) )
                time.sleep(random.randint(20,40))
        else:
            print(response.text)
            time.sleep(random.randint(1,7))
            json_data['count'] = 1
    except:
      pass
