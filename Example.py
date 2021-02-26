from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as act
import schedule
import time
from lib2to3.pgen2 import driver



from selenium.common.exceptions import NoSuchElementException  


def mainone():
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

    

def mainsec():

    join = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a').click()

    time.sleep(10)
    for i in range(3):
        act.send_keys(Keys.TAB).perform()
        time.sleep(1)   

    act.send_keys(Keys.ENTER).perform()

def m0911():
    mainone()
    lass1201 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[1]/div/div[2]').click()
    mainsec()
    # driver.close()

def m1201():
    mainone()
    Class1201 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[2]/div/div[2]').click()
    mainsec()
    driver.close()
 
def m0304():
    mainone()
    Class0304 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[3]/div/div[2]').click()
    mainsec()
    driver.close()

# def t1112():         #m0911
#     mainone()
#     Class1112 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[1]/div/div[2]').click()
#     mainsec()
#     driver.close()

# def t1201():                #m1201
#     mainone()
#     Class1201 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[2]/div/div[2]').click() 
#     mainsec()
#     driver.close()

# def t0203():               #m0304
#     mainone()
#     Class0203 =  driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[3]/div/div[2]').click()
#     mainsec()
#     driver.close()

def t0405():
    mainone()
    Class0405 =  driver.find_element_by_class_name('INT243-Lecture').click()
    mainsec()
    driver.close()

# def w0911():            #m0911
#     mainone()
#     Class0910 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[1]/div/div[2]').click()
#     mainsec()
#     driver.close()

# def w1201():            #m1201
#     mainone()
#     Class1201 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[2]/div/div[2]').click()
#     mainsec()
#     driver.close()

# def w0203():             #m0304
#     mainone()
#     Class0203 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[3]/div/div[2]').click()
#     mainsec()
#     driver.close()

# def w0304():             #t0405
#     mainone()
#     Class0304 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[4]/div/div[2]').click()
#     mainsec()
#     driver.close()

def w0405():
    mainone()
    Class0405 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[5]/div/div[2]').click()
    mainsec()
    driver.close()

# def th0911():              #m0911
#     mainone()
#     Class0910 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[1]/div/div[2]').click()
#     mainsec()
#     driver.close()

# def th0203():             #m0304
#     mainone()
#     Class0203 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[3]/div/div[2]').click()
#     mainsec()
#     driver.close()

# def f0910():             #m0911
#     mainone()
#     Class0910 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[1]/div/div[2]').click()
#     mainsec()
#     driver.close()

# def f1011():             #m1201
#     mainone()
#     Class1011 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[2]/div/div[2]').click()
#     mainsec()
#     driver.close()

# def f0103():              #m0304
#     mainone()
#     Class0103 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[3]/div/div[2]').click()
#     mainsec()
#     driver.close()

# def s0911():           #m0911
#     mainone()
#     Class0910 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[1]/div/div[2]').click()
#     mainsec()
#     driver.close()

# def s0103():           #m0304
#     mainone()
#     Class0103 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[3]/div/div[2]').click()
#     mainsec()
#     driver.close()

# def s0405():            #w0405
#     mainone()
#     blanks = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[5]/div/div[2]').click()
#     mainsec()
#     driver.close()

def bye():
    quit()

def timer():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("The Time is : ", current_time)


schedule.every(60).seconds.do(timer)




schedule.every().monday.at("09:05").do(m0911)
schedule.every().monday.at("12:05").do(m1201)
schedule.every().monday.at("15:05").do(m0304)
schedule.every().tuesday.at("11:05").do(m0911)
schedule.every().tuesday.at("12:05").do(m1201)
schedule.every().tuesday.at("14:05").do(m0304)
schedule.every().tuesday.at("16:05").do(t0405)
schedule.every().wednesday.at("09:05").do(m0911)
schedule.every().wednesday.at("12:05").do(m1201)
schedule.every().wednesday.at("14:05").do(m0304)
schedule.every().wednesday.at("15:05").do(t0405)
schedule.every().wednesday.at("16:05").do(w0405)
schedule.every().thursday.at("10:38").do(m0911)
schedule.every().thursday.at("14:05").do(m0304)
schedule.every().friday.at("09:05").do(m0911)
schedule.every().friday.at("10:05").do(m1201)
schedule.every().friday.at("13:05").do(m0304)
schedule.every().saturday.at("09:05").do(m0911)
schedule.every().saturday.at("13:05").do(m0304)
schedule.every().saturday.at("16:05").do(w0405)

schedule.every().saturday.at("17:30").do(bye)




while True:
    schedule.run_pending()
    time.sleep(1)
    
