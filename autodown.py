from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request

import time

# What you enter here will be searched for in
# Google Images
query = "cầu thủ Nguyễn Tuấn Anh"

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

# Function for scrolling to the bottom of Google
# Images results
def scroll_to_bottom():

	last_height = driver.execute_script('\
	return document.body.scrollHeight')

	while True:
		driver.execute_script('\
		window.scrollTo(0,document.body.scrollHeight)')

		# waiting for the results to load
		# Increase the sleep time if your internet is slow
		time.sleep(2)

		new_height = driver.execute_script('\
		return document.body.scrollHeight')

		# click on "Show more results" (if exists)
		try:
			driver.find_element("xpath", '//*[@id="islmp"]/div/div/div/div/div[1]/div[2]/div[2]/input').click()

			# waiting for the results to load
			# Increase the sleep time if your internet is slow
			time.sleep(2)

		except:
			pass

		# checking if we have reached the bottom of the page
		if new_height == last_height:
			break

		last_height = new_height


# Calling the function

# NOTE: If you only want to capture a few images,
# there is no need to use the scroll_to_bottom() function.
scroll_to_bottom()
count = 1

	


# Loop to capture and save each image
for i in range(1, 100):

	# range(1, 50) will capture images 1 to 49 of the search results
	# You can change the range as per your need.
	try:

		# XPath of each image
		img = driver.find_element('xpath',
			'//*[@id="islrg"]/div[1]/div[' +
		str(i) + ']/a[1]/div[1]/img')

		# Enter the location of folder in which
		# the images will be saved
		src = img.get_attribute("src");
		# img.screenshot('image/' +
		# 			query + ' (' + str(i) + ').png')
		urllib.request.urlretrieve(src, 'image/' +query + ' (' + str(count) + ').png')
		# Each new screenshot will automatically
		# have its name updated
		count = count+1
		# Just to avoid unwanted errors

	except:
		
		# if we can't find the XPath of an image,
		# we skip to the next image
		check = 1
		for o in range(1, 200):
			try:
				img1 = driver.find_element('xpath',
					'//*[@id="islrg"]/div[1]/div[' +
				str(i) + ']/div[' +
				str(o) + ']/a[1]/div[1]/img')

				# Enter the location of folder in which
				# the images will be saved
				src1 = img1.get_attribute("src");
				# img.screenshot('image/' +
				# 			query + ' (' + str(i) + ').png')
				urllib.request.urlretrieve(src1, 'image/' +query + ' (' + str(count) + ').png')
				count = count +1
			except:
				check = check + 1
				if check > 15:
					break
				continue
		print(i)
		continue

# Finally, we close the driver
driver.close()
