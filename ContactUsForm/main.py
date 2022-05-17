from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")
driver.maximize_window()

try:
    #Click on 'Contact Us' button
    contactUsButton = driver.find_element(By.CSS_SELECTOR, "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(7) > a")
    contactUsButton.click()
    
    def fillForm():
        #Verify 'GET IN TOUCH' is visible
        getInTouchMessage = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#contact-page > div > div:nth-child(2) > div.col-sm-8 > div > h2")))
        if getInTouchMessage.is_displayed() == True:
            print("The messaage is visible!")
        else:
            print("it is not visible!")
            driver.close()
        
        inputName = driver.find_element(By.CSS_SELECTOR, "#contact-us-form > div:nth-child(2) > input")
        inputName.send_keys("Luana Sousa")
        
        inputEmail = driver.find_element(By.CSS_SELECTOR, "#contact-us-form > div:nth-child(3) > input")
        inputEmail.send_keys("vitrr.gal@gmail.com")
        
        inputSubject = driver.find_element(By.CSS_SELECTOR, "#contact-us-form > div:nth-child(4) > input")
        inputSubject.send_keys("Lorem Lorem")
        
        inputMessage = driver.find_element(By.ID, "message")
        inputMessage.send_keys("Lorem Ipsun, bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla")

        #Arrumar esta merdaaaaaaaaaaa
        inputFile = driver.find_element(By.CSS_SELECTOR, "#contact-us-form > div:nth-child(6) > input")
        inputFile.click()
        inputFile.send_keys("gato.jpeg")
        
        inputEmail.submit()
        
    fillForm()      
finally:
    print()