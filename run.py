from selenium import webdriver
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.headless = True
def hit():
  try:
    browser = webdriver.Firefox(options=opts,'/home/ubuntu/geckodriver')
  except Exception as e:
    print(e)
