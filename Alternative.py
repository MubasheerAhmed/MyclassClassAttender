



import schedule
import time



def m0911():

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains 
    
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

    class45 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[1]/div/div[2]')
    class45.click()

    join = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a').click()

    time.sleep(8)

    act = ActionChains(driver)
    
    for i in range(3):
        act.send_keys(Keys.TAB).perform()
        time.sleep(1)   

    act.send_keys(Keys.ENTER).perform()

def m1201():

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    
    driver = webdriver.Chrome()
    driver.get('https://myclass.lpu.in/')

    Regid = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
    Regid.send_keys('11806518')

    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]')
    Password.send_keys('Roshan@3')

    loginButton = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button')
    loginButton.click()

    Tab1 =  driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]')
    Tab1.click()

    class45 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[3]/div/div[2]')
    class45.click()

    join = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a').click()

    time.sleep(8)

    act = ActionChains(driver)

    for i in range(3):
        act.send_keys(Keys.TAB).perform()
        time.sleep(1)   

    act.send_keys(Keys.ENTER).perform()

def m0304():

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains 
    
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

    class45 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[3]/div/div[2]')
    class45.click()

    join = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a').click()

    time.sleep(8)

    act = ActionChains(driver)
    for i in range(3):
        act.send_keys(Keys.TAB).perform()
        time.sleep(1)   

    act.send_keys(Keys.ENTER).perform()


    time.sleep(3600)
    driver.close()

def t0405():

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains 
    
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

    class45 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[4]/div/div[2]')
    class45.click()

    join = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a').click()

    time.sleep(8)

    act = ActionChains(driver)
    for i in range(3):
        act.send_keys(Keys.TAB).perform()
        time.sleep(1)   

    act.send_keys(Keys.ENTER).perform()

    


def w0405():

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains 
    
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

    class45 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[5]/div/div[2]')
    class45.click()

    join = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a').click()

    time.sleep(8)

    act = ActionChains(driver)
    for i in range(3):
        act.send_keys(Keys.TAB).perform()
        time.sleep(1)   

    act.send_keys(Keys.ENTER).perform()


def rosen():

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains 
    
    driver = webdriver.Chrome()
    driver.get('https://myclass.lpu.in/')

    Regid = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
    Regid.send_keys('11806518')

    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]')
    Password.send_keys('Roshan@3')

    loginButton = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button')
    loginButton.click()

    Tab1 =  driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]')
    Tab1.click()

    class45 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[2]/div/div[2]')
    class45.click()

    join = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a').click()

    time.sleep(8)

    act = ActionChains(driver)
    for i in range(3):
        act.send_keys(Keys.TAB).perform()
        time.sleep(1)   

    act.send_keys(Keys.ENTER).perform()

    

# //*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[2]/div/div[2]

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
schedule.every().thursday.at("09:05").do(m0911)
schedule.every().thursday.at("14:05").do(m0304)
schedule.every().friday.at("09:05").do(m0911)
schedule.every().friday.at("10:05").do(m1201)
schedule.every().friday.at("13:05").do(m0304)
schedule.every().saturday.at("09:05").do(m0911)
schedule.every().saturday.at("13:05").do(m0304)
schedule.every().saturday.at("16:05").do(w0405)

schedule.every().thursday.at("11:52").do(rosen)
schedule.every().thursday.at("12:23").do(m1201)

schedule.every().saturday.at("17:30").do(bye)


while True:
    schedule.run_pending()
    time.sleep(1)
    
