import pandas as pd
from selenium import webdriver
import time

urlpage = 'https://he.wikipedia.org/wiki/%D7%9E%D7%99%D7%95%D7%97%D7%93:%D7%A2%D7%A5_%D7%A7%D7%98%D7%92%D7%95%D7%A8%D7%99%D7%95%D7%AA?target=%D7%A7%D7%98%D7%92%D7%95%D7%A8%D7%99%D7%94%3A%D7%97%D7%91%D7%A8%D7%99+%D7%94%D7%9B%D7%A0%D7%A1%D7%AA+%D7%94%D7%A2%D7%A9%D7%A8%D7%99%D7%9D+%D7%95%D7%90%D7%97%D7%AA&mode=all&namespaces=&title=%D7%9E%D7%99%D7%95%D7%97%D7%93%3A%D7%A2%D7%A5_%D7%A7%D7%98%D7%92%D7%95%D7%A8%D7%99%D7%95%D7%AA'
print(urlpage)
# run firefox webdriver from executable path of your choice
driver = webdriver.Firefox(service_log_path="C:\\Users\\mord2\\AppData\\Local\\Temp\\geckodriver.log")
# run firefox webdriver from executable path of your choice
# get web page
driver.get(urlpage)
# execute script to scroll down the page
time.sleep(10)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 30s

#driver2 = webdriver.Firefox(service_log_path="C:\\Users\\mord2\\AppData\\Local\\Temp\\geckodriver.log")
#driver2.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 10s
#time.sleep(5)
#button = WebDriverWait(driver2, 10).until(EC.presence_of_element_located((By.XPATH, "yourXPATH")))
names = driver.find_elements_by_class_name("CategoryTreeChildren")
data=names[0].text
data=data.split("\n ")
ans=[]
for name in data:
    ans=ans+[{"name":name}]
print(ans)
df = pd.DataFrame(data)
print(df)
df.to_csv("C:\\Users\\mord2\\AppData\\Local\\Temp\\test3.csv")
driver.quit()
