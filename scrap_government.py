import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def knest_number(lines):
    data=[]

    for line in lines:
        data.append({"position":line.find_element_by_class_name("historyField historyFieldPositionName").get_attribute("innerText")})
    print(data)
    return data


# specify the url
urlpage = 'https://main.knesset.gov.il/mk/government/pages/governments.aspx?govId=1'
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

data = []
i = 2
while i < 37:
    govermment_number = driver.find_element_by_xpath("//*[@id=\"KnessetGovermentsContainerDiv\"]/div[2]/div/ul[2]/li["+str(i)+"]")
    govermment_number.click()
    time.sleep(10)
   # driver.refresh()
    govermment_number.click()
    time.sleep(15)
    lines = driver.find_elements_by_class_name("govermentLine2ListHistory")
    t=2
    for line in lines:
        temp=t
        try:
             position=line.find_element_by_xpath("//*[@id=\"govermentLine2\"]/div[2]/div/div["+str(t)+"]/div[2]").get_attribute("innerText")
             if position == "":
                t=t+1
        except:
            t=t+1
            continue
        if temp != t:
            continue
        try: name=line.find_element_by_xpath("//*[@id=\"govermentLine2\"]/div[2]/div/div["+str(t)+"]/div[3]").get_attribute("innerText")
        except: name=""
        try: party=line.find_element_by_xpath("//*[@id=\"govermentLine2\"]/div[2]/div/div["+str(t)+"]/div[7]").get_attribute("innerText")
        except: party=""
        gov= line.find_element_by_xpath("//*[@id=\"govermentLine2\"]/div[2]/div/div["+str(t)+"]/div[4]").get_attribute("innerText")
        data.append({"name":name,"position":position,"govermmrnt number":i-1,"gov":gov,"party":party})
        t=t+1
    i=i+1
  #  for _l in _list:
   #     data.append(_l)
 #   i = i + 1
# close drivers
#driver2.quit()
time.sleep(4)

driver.quit()
# save to pandas dataframe
df = pd.DataFrame(data)
print(df)
df.to_csv("C:\\Users\\mord2\\AppData\\Local\\Temp\\test2.csv")
