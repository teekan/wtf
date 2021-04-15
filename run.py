import subprocess
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.headless = True
def hit():
  try:
    browser = webdriver.Firefox(options=opts,executable_path='/home/ubuntu/wtf/geckodriver')
    try:
      browser.get("http://www.slutbags.tk")
      try:
        browser.find_elements_by_tag_name('body')[0].click()
        try:
          browser.switch_to.window(browser.window_handles[1])
          for x in range(len(browser.find_elements_by_tag_name('iframe'))):
            browser.find_elements_by_tag_name('iframe')[x].click()
            browser.switch_to.window(browser.window_handles[1])
            try:
              for x in browser.window_handles:
                browser.switch_to.window(x)
                browser.close()
              try:
                subprocess.run(['ps','-aux'], capture_output=True)
              except Expection as e:
                print("Failed closing resources")
            except Expection as e:
              print(e)
              print("Failed to close tabs and browser")
        except Exception as e:
          print(e)
          print("Failed clicking ads")
      except Exception as e:
        print(e)
        print("Failed clicking popunder")
    except Expection as e:
      print(e)
      print("Failed getting page")
  except Exception as e:
    print(e)
    print("Failed loading browser")
hit()
