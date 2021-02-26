from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()
driver.get('https://myclass.lpu.in/')

Regid = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
Regid.send_keys('11804714')

Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]')
Password.send_keys('1aA#pass')


loginButton = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button')
loginButton.click()

Tab1 =  driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]')
Tab1.click()

#class23 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[3]/div/div[2]')
#class23.click()

class45 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[1]/div/div[2]')
class45.click()

join = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a').click()




print( driver.current_window_handle) #CDwindow-39519BA48D0EDD579A61BAE8543ADB72
print(driver.current_url)            #https://lovelyprofessionaluniversity.codetantra.com/secure/tla/jnr.jsp?m=d7b5f95d-2216-391a-ab7c-38216c83d3a4




time.sleep(10)

act = ActionChains(driver)
act.send_keys(Keys.TAB).perform()

time.sleep(2)


act.send_keys(Keys.TAB).perform()

time.sleep(2)


act.send_keys(Keys.TAB).perform()

time.sleep(2)

act.send_keys(Keys.ENTER).perform()

# driver.switch_to_window('Join audio modal')


# driver.switch_to.__class__("ReactModal__Content ReactModal__Content--after-open modal--1DxJyC modal--lmEc2")
# join = driver.find_element_by_class_name("jumbo--Z12Rgj4 buttonWrapper--x8uow audioBtn--1H6rCK")
# join.click()

# /html/body/div[2]/div/div
# Mub = WebDriverWait(driver, 10)
#element = Mub.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Listen only')))
# element.click()

# driver.quit()

# mag = driver.find_element_by_xpath('//*[@id="tippy-23"]/span[1]')
# mag.click()
time.sleep(8)
driver.quit()



