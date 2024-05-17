# -*- coding: utf-8 -*-
"""
Created on Wed May 15 14:20:34 2024

@author: Matthew
"""

import pandas as pd
import seaborn as sns
import time
import yfinance as yf
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import matplotlib.pyplot as plt

options = Options()
options.add_argument("window-size=1400,1200")

driver = webdriver.Chrome(options = options)

esg_proj = pd.read_csv("https://bcdanl.github.io/data/esg_proj.csv")

company_list = esg_proj['Symbol'].to_list()

companies = yf.Tickers(company_list)

historical_data = companies.history(start='2023-01-01', end='2024-03-31')
income_stmt = pd.DataFrame([])
for ticker in company_list:
    comp = yf.Ticker(ticker)
    element = comp.quarterly_income_stmt.T
    element['company']=ticker
    income_stmt = pd.concat([income_stmt, element])
balance_sheet = pd.DataFrame([])
for ticker in company_list:
    comp = yf.Ticker(ticker)
    element = comp.quarterly_balance_sheet.T
    element['company']=ticker
    balance_sheet = pd.concat([balance_sheet, element])
    
df = pd.DataFrame([])
for company in company_list:
    url = 'https://finance.yahoo.com/quote/'+str(company)+'/sustainability'
    driver.get(url)
    time.sleep(8)
    
    symbol = pd.DataFrame([company])
    xpath_new = '//*[@id="nimbus-app"]/section/section/section/article/section[2]/section[1]/div/section[1]/div/div/h4'
    xpath_old = '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[1]/div/div[1]/div/div[2]/div[1]'
    try:
         total = driver.find_element(By.XPATH, xpath_new).text
    except:
        try: 
            total = driver.find_element(By.XPATH, xpath_old).text
        except:
            total = ''
        
    total = pd.DataFrame([total])

    xpath_new = '/html/body/div[1]/main/section/section/section/article/section[2]/section[1]/div/section[2]/div/div/h4'
    xpath_old = '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[1]/div/div[2]/div/div[2]/div[1]'
    try:
        environment = driver.find_element(By.XPATH, xpath_new).text
    except:
        try: 
            environment = driver.find_element(By.XPATH, xpath_old).text
        except:
            environment = ''
        
    environment = pd.DataFrame([environment])
    
    xpath_new = '/html/body/div[1]/main/section/section/section/article/section[2]/section[1]/div/section[3]/div/div/h4'
    xpath_old = '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[1]/div/div[3]/div/div[2]/div[1]'
    try:
        social = driver.find_element(By.XPATH, xpath_new).text
    except:
        try: 
            social = driver.find_element(By.XPATH, xpath_old).text
        except:
            social = ''
        
    social = pd.DataFrame([social])
    
    xpath_new = '/html/body/div[1]/main/section/section/section/article/section[2]/section[1]/div/section[4]/div/div/h4'
    xpath_old = '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[1]/div/div[4]/div/div[2]/div[1]'
    try:
        government = driver.find_element(By.XPATH, xpath_new).text
    except:
        try: 
            government = driver.find_element(By.XPATH, xpath_old).text
        except:
            government = ''
        
    government = pd.DataFrame([government])
    
    xpath_new = '/html/body/div[1]/main/section/section/section/article/section[3]/section[1]/div/div[2]/span[1]'
    xpath_old = '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[2]/div[2]/div/div/div/div[1]/div'
    try:
        controversy = driver.find_element(By.XPATH, xpath_new).text
    except:
        try: 
            controversy = driver.find_element(By.XPATH, xpath_old).text
        except:
            controversy = ''
        
    controversy = pd.DataFrame([controversy])
    
    obs = pd.concat([symbol, total, environment, social, government, controversy], axis = 1)
    df = pd.concat([df, obs])
    