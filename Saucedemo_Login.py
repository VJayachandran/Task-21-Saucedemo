#Saucedemo Login

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from time import sleep

# Set options for not prompting DevTools information
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

print("Login Started")

driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")
sleep(3)

# Display cookies before login
cookies_before_login = driver.get_cookies()
print("Cookies before login:")
for cookie in cookies_before_login:
    print(cookie)


# Find element using element's id attribute
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
sleep(5)

text = driver.find_element(By.CLASS_NAME, "title").text

# Check if login was successful
assert "products" in text.lower()

# Display cookies after login
cookies_after_login = driver.get_cookies()
print("Cookies after login:")
for cookie in cookies_after_login:
    print(cookie)

print("TEST PASSED: LOGIN SUCCESSFUL")

# Verify cookies generated during login process
login_cookies = ({set(cookies_after_login), set(cookies_before_login)})
if login_cookies:
    print("Cookies generated during login:")
    for cookie in login_cookies:
        print(cookie)
else:
    print("No new cookies generated during login.")

    print("Logged out successfully.")

# Close the driver
driver.quit()




