from selenium import webdriver
import os
from fake_useragent import UserAgent
#Useragent stuff
ua = UserAgent()
#Might need to define a user agent for consistency. Example, user agent for Linux system if you are running on Linux
userAgent = ua.random


def lambda_handler(event=None, context=None):
    # For troubleshooting, will show if your files are where you expective them to be once the container uploaded to aws
    # print (os.getcwd())
    # print (os.listdir())
    # os.chdir(r"/tmp/")
    # print (os.getcwd())
    # print (os.listdir())
    # os.chdir(r"/opt")
    # print (os.getcwd())
    # print (os.listdir())
    # os.chdir(r"/opt/chrome/stable")
    # print (os.getcwd())
    # print (os.listdir())
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "/opt/chrome/stable/chrome"
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-tools")
    chrome_options.add_argument("--no-zygote")
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("window-size=1900x1200")
    chrome_options.add_argument("--user-data-dir=/tmp/chrome-user-data")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument("--user-data-dir=/tmp/chrome-user-data")
    driver = webdriver.Chrome("/opt/chromedriver/stable/chromedriver", options=chrome_options)
    driver.get("https://www.google.com")
    test = driver.find_element_by_xpath("/html/head/title")
    return test.get_attribute("innerHTML")