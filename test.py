import subprocess
import sys,os,time
subprocess.check_call([sys.executable, "-m", "pip", "install", "selenium"])
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
print("python : "+str(os.system("ls")))
chrome_options = Options()
chrome_options.add_argument("--headless")
#options.add_argument('--no-first-run --no-service-autorun --password-store=basic --no-sandbox')
driver = webdriver.Chrome("chromedriver",options=chrome_options)
driver.get("https://miner.eo.finance")
driver.add_cookie({'domain': '.eo.finance', 'expiry': 1967784870, 'httpOnly': False, 'name': 'userId', 'path': '/', 'secure': False, 'value': '922240272'})
driver.add_cookie({'domain': '.eo.finance', 'expiry': 1967784870, 'httpOnly': False, 'name': 'token', 'path': '/', 'secure': False, 'value': '0cb6cd98f8f46770c5002f06e39751a87dd85ca7545f1e0b263a572932b9b413e2ffe17896f508dd8e98362619a4e9d22f0406bba48d12c5f01ed727f15ef931'})
driver.refresh()
driver2 = webdriver.Chrome("chromedriver",options=chrome_options)
driver2.get("https://miner.eo.finance")
driver2.add_cookie({'domain': '.eo.finance', 'expiry': 1967784870, 'httpOnly': False, 'name': 'userId', 'path': '/', 'secure': False, 'value': '922240272'})
driver2.add_cookie({'domain': '.eo.finance', 'expiry': 1967784870, 'httpOnly': False, 'name': 'token', 'path': '/', 'secure': False, 'value': '0cb6cd98f8f46770c5002f06e39751a87dd85ca7545f1e0b263a572932b9b413e2ffe17896f508dd8e98362619a4e9d22f0406bba48d12c5f01ed727f15ef931'})
driver2.refresh()
print("succsess")
while True:
    time.sleep(10)
    print(f"\ndriver1 = {driver.find_element(By.ID,'hashes-per-second').text}\ndriver2: {driver2.find_element(By.ID,'hashes-per-second').text}")
