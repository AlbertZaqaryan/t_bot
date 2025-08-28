from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get(url='https://smartcode.am/hy/')
    driver.maximize_window()
    time.sleep(3)

except Exception as ex:
    print(f'❌❌❌ ERROR ❌❌❌❌\n{ex.__class__.__name__}')
finally:
    driver.close()
    driver.quit()