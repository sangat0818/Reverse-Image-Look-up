from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.chrome.options import Options
from basic import upload_files
from imagecropper import getImage
def searchname():
    filename = "E:/Python/Selenium/ImagetobeSearched/image.jpg"
    url = upload_files(filename)
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome('E:/chromedriver' )
    driver.get('https://www.google.com/searchbyimage?image_url=' + url)
    input = driver.find_element_by_name("q")
    text = input.get_attribute('value')
    os.remove(filename)
    print(text)
    return text

