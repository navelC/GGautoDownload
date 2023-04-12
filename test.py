from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request

import time

# What you enter here will be searched for in
# Google Images
query = "dogs"

# Creating a webdriver instance
driver = webdriver.Chrome(r'D:\Auto\chromedriver')

# Maximize the screen
driver.maximize_window()

# Open Google Images in the browser
driver.get('https://images.google.com/')
# Finding the search box
box = driver.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

# Type the search query in the search box
box.send_keys(query)

# Pressing enter
box.send_keys(Keys.ENTER)

# Loop to capture and save each image

		# XPath of each image
img = driver.find_element('xpath',
	'//*[@id="islrg"]/div[1]/div[34]/a[1]/div[1]/img')
# Enter the location of folder in which
# the images will be saved
src = img.get_attribute("src");
print(src)
time.sleep(40)

# img.screenshot('image/' +
# 			query + ' (' + str(i) + ').png')
urllib.request.urlretrieve(src, 'image/' +query + ' (34).png')
# Each new screenshot will automatically
# have its name updated

# Just to avoid unwanted errors


# Finally, we close the driver
driver.close()
