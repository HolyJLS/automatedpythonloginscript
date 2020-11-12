from selenium import webdriver
import time, os
#from webdriver_manager.chrome import ChromeDriverManager
repo_name = "test"
# save chromedriver and website
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://github.com/login")
def create():

    # login
    find_button = driver.find_element_by_id("login_field")
    find_button.send_keys('USERNAME')
    find_button = driver.find_element_by_id("password")
    find_button.send_keys('PASSWORD')
    find_button = driver.find_element_by_xpath("//*[@id='login']/form/div[4]/input[12]").click()

    # make repo
    find_button = driver.find_element_by_xpath("//*[@id='repos-container']/h2/a").click()
    find_button = driver.find_element_by_xpath("//*[@id='repository_name']")
    find_button.send_keys(repo_name)
    find_button = driver.find_element_by_xpath("//*[@id='new_repository']/div[4]/button")
    time.sleep(1)
    find_button.click()

if __name__ == "__main__":
    create()
