import pandas as pd
import selenium
from selenium import webdriver
import pandas


driver = webdriver.Chrome()
ApplicationURL = "https://venetablinds.com.au/"
driver.get(ApplicationURL)
driver.maximize_window()

data = pd.read_csv("C:/Users/ls217/OneDrive/Desktop/SQl cheat sheet.csv")