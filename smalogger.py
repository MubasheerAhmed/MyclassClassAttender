import schedule
import time


def class1():

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains 

    print("Your Class Is being started and joining Listening mode as default")
    
    driver = webdriver.Chrome()
    driver.get('https://myclass.lpu.in/')

    Regid = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]').send_keys('11804714')

    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]').send_keys('1aA#pass')

    loginButton = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button').click()

    Tab1 =  driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]').click()

    class45 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[1]/div/div[2]').click()
    
    print("Browser Opened")
    print("Entering Login Credentials")

    print("Entering Class... ")

    join = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a').click()

    time.sleep(8)

    act = ActionChains(driver)
    
    for i in range(3):
        act.send_keys(Keys.TAB).perform()
        time.sleep(1)   
        print("Joined Listen mode Successfully if You are Seeing Acknowledgement for 3 Times")

    act.send_keys(Keys.ENTER).perform()
    time.sleep(7200)
    print("Closing The Expired Class Tab")
    driver.close()


def class2():

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains

    print("Your Class Is being started and joining Listening mode as default")
    
    driver = webdriver.Chrome()
    driver.get('https://myclass.lpu.in/')

    Regid = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]').send_keys('11804714')

    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]').send_keys('1aA#pass')
 
    loginButton = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button').click()

    Tab1 =  driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]').click()

    class45 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[2]/div/div[2]').click()

    print("Browser Opened")
    print("Entering Login Credentials")

    print("Entering Class... ")

    join = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a').click()

    time.sleep(8)

    act = ActionChains(driver)

    for i in range(3):
        act.send_keys(Keys.TAB).perform()
        time.sleep(1)   
        print("Joined Listen mode Successfully if You are Seeing Acknowledgement for 3 Times")

    act.send_keys(Keys.ENTER).perform()

    time.sleep(7200)
    print("Closing The Expired Class Tab")
    driver.close()

def class3():

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains 

    print("Your Class Is being started and joining Listening mode as default")
    
    driver = webdriver.Chrome()
    driver.get('https://myclass.lpu.in/')

    Regid = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]').send_keys('11804714')

    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]').send_keys('1aA#pass')

    loginButton = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button').click()
    
    print("Browser Opened")
    print("Entering Login Credentials")

    Tab1 =  driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]').click()
    
    class45 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[3]/div/div[2]').click()
    
    print("Entering Class... ")

    join = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a').click()

    time.sleep(8)

    act = ActionChains(driver)
    for i in range(3):
        act.send_keys(Keys.TAB).perform()
        time.sleep(1)   
        print("Joined Listen mode Successfully if You are Seeing Acknowledgement for 3 Times")

    act.send_keys(Keys.ENTER).perform()

    time.sleep(7200)
    print("Closing The Expired Class Tab")
    driver.close()


def class4():

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains 
    
    print("Your Class Is being started and joining Listening mode as default")

    driver = webdriver.Chrome()
    driver.get('https://myclass.lpu.in/')

    print("Browser Opened")
    print("Entering Login Credentials")

    Regid = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]').send_keys('11804714')

    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]').send_keys('1aA#pass')
 
    loginButton = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button').click()
    
    print("Attempt to login was Successful")

    Tab1 =  driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]').click()
    
    class45 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[4]/div/div[2]').click()
    
    print("Entering Class... ")

    join = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a').click()

    time.sleep(8)

    act = ActionChains(driver)
    for i in range(3):
        act.send_keys(Keys.TAB).perform()
        time.sleep(1)   
        print("Joined Listen mode Successfully if You are Seeing Acknowledgement for 3 Times")

    act.send_keys(Keys.ENTER).perform()

    time.sleep(3600)
    print("Closing The Expired Class Tab")
    driver.close()


def class5():

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains 

    print("Your Class Is being started and joining Listening mode as default")
    
    driver = webdriver.Chrome()
    driver.get('https://myclass.lpu.in/')

    Regid = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
    Regid.send_keys('11804714')

    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]').send_keys('1aA#pass')

    loginButton = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button').click()

    print("Browser Opened")
    print("Entering Login Credentials")

    Tab1 =  driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]').click()

    class45 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[5]/div/div[2]').click()
    
    print("Entering Class... ")

    join = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a').click()

    time.sleep(8)

    act = ActionChains(driver)
    for i in range(3):
        act.send_keys(Keys.TAB).perform()
        time.sleep(1)
        print("Joined Listen mode Successfully if You are Seeing Acknowledgement for 3 Times")

    act.send_keys(Keys.ENTER).perform()

    time.sleep(3600)
    print("Closing The Expired Class Tab")
    driver.close()

def bye():
    quit()

def timer():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("The Time is : ", current_time)

schedule.every(60).seconds.do(timer)

schedule.every().monday.at("09:05").do(class1)
schedule.every().monday.at("12:03").do(class2)
schedule.every().monday.at("15:03").do(class3)
schedule.every().tuesday.at("11:03").do(class1)
schedule.every().tuesday.at("12:03").do(class2)
schedule.every().tuesday.at("14:03").do(class3)
schedule.every().tuesday.at("16:03").do(class4)
schedule.every().wednesday.at("09:05").do(class1)
schedule.every().wednesday.at("12:03").do(class2)
schedule.every().wednesday.at("14:03").do(class3)
schedule.every().wednesday.at("15:03").do(class4)
schedule.every().wednesday.at("16:03").do(class5)
schedule.every().thursday.at("09:05").do(class1)
schedule.every().thursday.at("14:03").do(class2)
schedule.every().friday.at("09:05").do(class1)
schedule.every().friday.at("10:03").do(class2)
schedule.every().friday.at("13:03").do(class3)
schedule.every().saturday.at("09:05").do(class1)
schedule.every().saturday.at("13:03").do(class2)
schedule.every().saturday.at("16:03").do(class3)

schedule.every().saturday.at("17:30").do(bye)

while True:
    schedule.run_pending()
    time.sleep(1)
