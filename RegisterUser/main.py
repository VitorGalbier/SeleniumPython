from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")
driver.maximize_window()
try:
    signUpLoginButton = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(4) > a"))).click()
    
    #Check if the element is visible
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
    
    #Check if the form is visible
    formSignUp = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#form > div > div > div > div > form")))
    if formSignUp.is_displayed() == True:
        print("Element is visible!")
    else:
        print("Element is not visible!")
        driver.quit()
    
    #Select "Mr."
    titleCheckBox = driver.find_element(By.ID, "id_gender1").click()
    
    #Select password
    passwordInput = driver.find_element(By.ID, "password").send_keys("Senha123!")
    
    #Select day 9
    calendarDays = driver.find_element(By.ID, "days").click()
    dayNine = driver.find_element(By.CSS_SELECTOR, "#days > option:nth-child(10)").click()
    
    #Select September
    calendarMonth = driver.find_element(By.ID, "months").click()
    monthSeptember = driver.find_element(By.CSS_SELECTOR, "#months > option:nth-child(10)").click()
    
    #Select 1994
    calendarYear = driver.find_element(By.ID, "years").click()
    selectYear = driver.find_element(By.CSS_SELECTOR, "#years > option:nth-child(29)").click()
    
    #Select checkbox for news
    newsCheckBox = driver.find_element(By.ID, "newsletter").click()
    
    #Select checkbox for offers
    offersCheckBox = driver.find_element(By.ID, "optin").click()
    
    #Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    firstNameInput = driver.find_element(By.ID, "first_name").send_keys("Vitor")
    lastNameInput = driver.find_element(By.ID, "last_name").send_keys("Galbier")
    companyInput = driver.find_element(By.ID, "company").send_keys("Globant")
    firstAdressInput = driver.find_element(By.ID, "address1").send_keys("Rua dos Auetes")
    secondAdressInput = driver.find_element(By.ID, "address2").send_keys("Vila Costa e Silva")
    countryInput = driver.find_element(By.ID, "country").click()
    canadaOption = driver.find_element(By.CSS_SELECTOR, "#country > option:nth-child(3)").click()
    stateInput = driver.find_element(By.ID, "state").send_keys("Rio de Janeiro")
    cityInput = driver.find_element(By.ID, "city").send_keys("Paraty")
    zipCodeInput = driver.find_element(By.ID, "zipcode").send_keys(13980123)
    mobileInput = driver.find_element(By.ID, "mobile_number").send_keys("+55 (19) 99781-7052")
    createAccountButton = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div > div > form > button").click()
    
    # Verify that 'ACCOUNT CREATED!' is visible
    accountCreatedDiv = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#form > div > div > div")))
    if accountCreatedDiv.is_displayed() == True:
        print("Account Created!")
    else:
        print("Element is not visible!")
        driver.quit()

    #Click 'Continue' button
    continueButton = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div > div > a").click()
    
    # Verify that 'Logged in as username' is visible
    loggedUsername = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(9) > a")))
    if loggedUsername.is_displayed() == True:
        print("Account username visible")
    else:
        print("Element is not visibile!")
        driver.close()
    
    #Click 'Delete Account' button
    deleteButton = driver.find_element(By.CSS_SELECTOR, "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(5) > a").click()
    #Delete button does not work!    
finally:
    print("Test ended")
    driver.close()


