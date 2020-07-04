from bs4 import BeautifulSoup
import pickle
import requests
from selenium import webdriver
import time
import pickle
import json
import os
import re
import random


file = open('data.json',"w+") 

driver = webdriver.Safari()

for i in range(0,1734):
	driver.get("https://docs.google.com/forms/d/e/1FAIpQLScYoPvvVViiAJjaoHdM1hCPJgEfht2CGVaUTsO5te8WhH3VLA/viewform")
	soup = BeautifulSoup(driver.page_source , "html.parser")
	
	nbr_product = random.randint(0, 10)

	product_index = []

	while len(product_index) < 10 :
		x = random.randint(0, 39)
		if x not in product_index :
			product_index.append(x)

	div = soup.find(role="list")

	file.write(div)
	break 