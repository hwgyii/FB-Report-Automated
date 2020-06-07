from selenium import webdriver
import random,time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import csv
import time

#TO BLOCK NOTIFICATION FROM THE BROWSER
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)


user_email = 'dhudotyukit018@gmail.com' #change with ur fb's email
user_pass = 'jhyyqtw8109692'			#change with ur fb's password
waitTime = 10


class FbReportUserProfile:

	def __init__(self, driver,url,email,password):
		self.driver = driver
		self.url = url
		self.email = email
		self.password = password

	def navigate(self,url):
		self.driver.get(url)

	def change_url(self,url):
		self.url = url

	def login(self,email,password,driver):
		try:
			emailelement = self.driver.find_element_by_name('email')
			passwordelement = self.driver.find_element_by_name('pass')
			emailelement.send_keys(self.email)
			passwordelement.send_keys(self.password)

			#logging in to the facebook using Selenium
			emailelement.send_keys(Keys.RETURN)

		except Exception as inst:
			print(type(inst))     # the exception instance
			print(inst.args)      # arguments stored in .args
			print(inst) 
			print("Please check your credential again.")

urls = open("listOfURLs.txt", "r")

indiv_url = urls.readlines()
count = 1
for x in indiv_url:
	url = x
	
	fbReportUserProfile = FbReportUserProfile(driver,url,user_email,user_pass)
	fbReportUserProfile.navigate(url)

	if count == 1:
		fbReportUserProfile.login(user_email,user_pass,driver)
		print("\t\tLOGGED IN")

	start = time.time()
	print(str(count)+". "+url)
	time.sleep(3)
	try:
		try:
			driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[3]/div/div[2]/div[2]/div/div/div/div/button").click()
		except NoSuchElementException:
			driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[3]/div/div[2]/div[2]/div/div/div[2]/button/i").click()
		driver.find_element(By.XPATH, "//span[contains(text(), 'Find Support or Report Profile')]").click()
		time.sleep(2)
	except NoSuchElementException:
		print("\tAccount Not Available")
		count += 1
		continue
	print("\tClicked Report")
	while True:
		try:
			driver.find_element(By.XPATH, "//span[contains(text(), 'Fake Account')]").click()
			driver.find_element(By.XPATH, "//div[contains(text(), 'Next')]").click()
		except NoSuchElementException:
			continue
		break
	print("\tClicked Next")
	while True:
		try:
			driver.find_element(By.XPATH, "//span[contains(text(), 'Report profile')]").click()
			time.sleep(1)
			print("\tClicked Report Profile")
		except NoSuchElementException:
			try:
				driver.find_element(By.XPATH, "//span[contains(text(), 'Done')]").click()
			except NoSuchElementException:
				continue
		driver.find_element(By.XPATH, "//div[contains(text(), 'Continue Anyway')]").click()
		print("\tClicked Continue Anyway")
		break
	time.sleep(2)
	index = 21
	while True:
		xpath = "/html/body/div["+str(index)+"]/div[2]/div/div/div/div/div[2]/div[3]/div/div[2]/input"
		try:
			driver.find_element_by_xpath(xpath).click()
		except NoSuchElementException:
			index += 1
			continue
		break			
	print("\tReported in Facebook Community")

	driver.find_element(By.XPATH, "//div[contains(text(), 'Report')]").click()

	end = time.time()
	print("\tDone in "+str(end-start)+"seconds.")
	count += 1
