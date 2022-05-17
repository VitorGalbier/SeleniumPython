from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")
driver.maximize_window()

try:
    
    def registerWithSameEmail():
        #4. Click on 'Signup / Login' button
        signUpLoginButton = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(4) > a"))).click()
    
        newUserSignUpDiv = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "col-sm-4")))
    
        if newUserSignUpDiv.is_displayed() == True:
            print("Element is visible!")
        else:
            print("Element is not visible!")
            driver.quit()
         
            #Create a new account
        nameInput = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div:nth-child(3) > div > form > input[type=text]:nth-child(2)")
        emailInput = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div:nth-child(3) > div > form > input[type=email]:nth-child(3)")
        
        nameInput.send_keys("Luana Sousa")
        emailInput.send_keys("vitrr.gal@gmail.com") 
        signUp = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div:nth-child(3) > div > form > button").click()
    
    registerWithSameEmail()
    
    def messageVisible():
        userMessage = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#form > div > div > div:nth-child(3) > div > form > p")))
        if userMessage.is_displayed() == True:
            print("The message appeared!")
        else:
            print("It didn`t show!")    
            
    messageVisible()
    
finally:
    driver.close()
    print("Test Ended!")