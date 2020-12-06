import urllib3
import pyautogui
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
pyautogui.FAILSAFE = False

# pyautogui.moveTo(0, 1080, duration=0.25)
# file = 'latlon.csv'
#
# f = open('latlon.csv','w',encoding='utf-8')
# csv = csv.writer(f)
# csv.writerow(["row", "col", "lat", "lon"])

# try:
#     while True:
#         x, y = pyautogui.position()
#         print(x,y)
# except KeyboardInterrupt:
#     print('\nExit.')
driver = webdriver.Chrome()
url = 'https://www.ecmwf.int/en/forecasts/charts/catalogue/medium-2t-wind?facets=undefined&time=2020120512,0,2020120512&layer_name=2t&projection=classical_eastern_asia'
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)
pyautogui.scroll(-300)
pyautogui.sleep(3)
x = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[3]/div[1]/div[3]/div[1]/img')
# x.click()
a, b = pyautogui.position()
print(a)
print(b)
pyautogui.moveTo(171, 445)
pyautogui.sleep(1)
lat = driver.find_elements_by_xpath('//*[@id="chart-browser"]/div[3]/div[1]/div[3]/div[2]/span[1]')
lon = driver.find_elements_by_xpath('//*[@id="chart-browser"]/div[3]/div[1]/div[3]/div[2]/span[2]')
print(lat[0].text)
print(lon[0].text)
