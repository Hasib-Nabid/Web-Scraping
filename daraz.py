from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.daraz.com.bd/mens-sunglasses//?q=sunglass')

driver.maximize_window()

name_list=[]
image_list=[]
link_list=[]

for i in range (1,6):
    j=str(i)

    name=driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+j+']/div/div/div[2]/div[2]/a').text
    name_list.append(name)

    link=driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+j+']/div/div/div[2]/div[2]/a').get_attribute('href')
    link_list.append(link)

    image=driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+j+']/div/div/div[1]/div/a/div/img').get_attribute('src')
    image_list.append(image)

print(name_list)
print(link_list)
print(image_list)

time.sleep(60)
driver.quit()
