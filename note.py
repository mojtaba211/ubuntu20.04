import requests,time,random

headers = {
    'authority': 'clicker-api.joincommunity.xyz',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'auth': '5',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjM3MzgwMDYsImV4cGlyZSI6MTcwNTI4ODM5OTI1MywiaWF0IjoxNzA1MjY2Nzk5LCJleHAiOjE3MTMwNDI3OTl9.EbxaAsktPjCDiIQILexR4xkLBBCSBFhoOEWnuZRpsKo',
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
    'webAppData': 'query_id=AAFF2TITAAAAAEXZMhP3U_R9&user=%7B%22id%22%3A322099525%2C%22first_name%22%3A%22Mojtaba%22%2C%22last_name%22%3A%22%22%2C%22username%22%3A%22MojtabaIRI%22%2C%22language_code%22%3A%22fa%22%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=1705266654&hash=7fe865584a2d8ff84cdc547456414e84de100d97a4752913c0656dc1539aa967',
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
                json_data['count'] = random.randint(1,(800 if response.json()['data'][0]['availableCoins'] > 800 else response.json()['data'][0]['availableCoins']) )
                time.sleep(random.randint(20,40))
        else:
            print(response.text)
            m += 1
            if m == 10:
                break
    except:
      pass
