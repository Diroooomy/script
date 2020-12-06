from selenium import webdriver
import pyautogui
import csv

# pyautogui.PAUSE = 0.01
pyautogui.FAILSAFE = False
file = 'latlon1.csv'

f = open('latlon1.csv', 'w', encoding = 'utf-8', newline='')
csv = csv.writer(f)

driver = webdriver.Chrome()
url = 'https://www.ecmwf.int/en/forecasts/charts/catalogue/medium-2t-wind?facets=undefined&time=2020120512,0,2020120512&layer_name=2t&projection=classical_eastern_asia'
driver.get(url)
driver.maximize_window()
# driver.implicitly_wait(5)
pyautogui.scroll(-300)
pyautogui.sleep(2)
for row in range(171, 1025, 7):
    for col in range(445, 1725, 5):
        pyautogui.moveTo(col, row)
        lat = driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div[2]/div[3]/div[1]/div[3]/div[2]/span[1]')
        lon = driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div[2]/div[3]/div[1]/div[3]/div[2]/span[2]')
        csv.writerow([row, col, lat[0].text, lon[0].text])
f.close()