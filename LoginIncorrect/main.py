from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")
driver.maximize_window()

try:
    #4. Click on 'Signup / Login' button
    loginButton = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(4) > a"))).click()
    #Verify 'Login to your account' is visible
    divLogin = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#form > div > div > div.col-sm-4.col-sm-offset-1 > div")))
    if divLogin.is_displayed() == True:
        print("The login div is visible.")
    else:
        print("The login div is not visible.")
        
    #6. Enter incorrect email address and password
    loginInput = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > input[type=email]:nth-child(2)").send_keys("vitor.galbier@gmcom")
    passwordInput = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > input[type=password]:nth-child(3)").send_keys("Senha124!")
    
    #7. Click 'login' button
    enterButton = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > button").click()
    
    userMessage = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > p")))
    
    if userMessage.is_displayed == True:
        print("The message has appeared.")
    else:
        print("Message is not visible")
    
            
finally:
    print("Test ended")
    driver.close()