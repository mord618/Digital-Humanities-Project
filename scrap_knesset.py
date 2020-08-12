import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_more_info():
    c=0;
    try:
        army=driver2.find_element_by_id("ctl00_ctl56_g_4e85a275_d641_41ab_8bc5_98c140927f3d_armyHistoryDiv")
    except:
        try:
           army = driver2.find_element_by_id("ctl00_ctl56_g_4e85a275_d641_41ab_8bc5_98c140927f3d_armyHistoryDiv2")
        except:
            try:
                army = driver2.find_element_by_id("ctl00_ctl56_g_4e85a275_d641_41ab_8bc5_98c140927f3d_armyHistoryDiv3")
            except:
                try:
                    army = driver2.find_element_by_id("ctl00_ctl56_g_4e85a275_d641_41ab_8bc5_98c140927f3d_ArmyDiv3")
                except:
                    try:
                        army = driver2.find_element_by_id("ctl00_ctl56_g_4e85a275_d641_41ab_8bc5_98c140927f3d_ArmyDiv2")
                    except:
                        try:
                            army = driver2.find_element_by_id("ctl00_ctl56_g_4e85a275_d641_41ab_8bc5_98c140927f3d_ArmyDiv")
                        except:
                            army=""

    try:
        birth_date=driver2.find_element_by_id("ctl00_ctl56_g_4e85a275_d641_41ab_8bc5_98c140927f3d_BirthDateSpn")
    except:
        try:
            birth_date = driver2.find_element_by_id("ctl00_ctl56_g_4e85a275_d641_41ab_8bc5_98c140927f3d_BirthDateSpn2")
        except:
            try:
                birth_date = driver2.find_element_by_id("ctl00_ctl56_g_4e85a275_d641_41ab_8bc5_98c140927f3d_BirthDateSpn3")
            except:
                birth_date=""
    try:
      kneset=driver2.find_element_by_id("ctl00_PlaceHolderMain_dcpDesktop_ctl00_mkKnessetList")
    except:
      try:
          time.sleep(2)
          kneset = driver2.find_element_by_xpath("//*[@id=\"s4-bodyContainer\"]/div[1]/div[4]/div/div[2]/h1")
      except:
          kneset=""
    educations = driver2.find_elements_by_id("ctl00_ctl56_g_4e85a275_d641_41ab_8bc5_98c140927f3d_EducationDiv3")
    if educations == []:
            educations = driver2.find_elements_by_id("ctl00_ctl56_g_4e85a275_d641_41ab_8bc5_98c140927f3d_EducationDiv2")
            if educations == []:
                  educations = driver2.find_elements_by_id("ctl00_ctl56_g_4e85a275_d641_41ab_8bc5_98c140927f3d_EducationDiv")

    profs=driver2.find_elements_by_id("ctl00_ctl56_g_4e85a275_d641_41ab_8bc5_98c140927f3d_ProfessionsDiv3")
    if profs == []:
            profs=driver2.find_elements_by_id("ctl00_ctl56_g_4e85a275_d641_41ab_8bc5_98c140927f3d_ProfessionsDiv2")
            if profs == []:
                 profs = driver2.find_elements_by_id("ctl00_ctl56_g_4e85a275_d641_41ab_8bc5_98c140927f3d_ProfessionsDiv")
                 if profs == []:
                     profs =driver2.find_elements_by_id("ctl00_ctl56_g_4e85a275_d641_41ab_8bc5_98c140927f3d_ProfessionsDetailsDiv")

    try:
        language=driver2.find_element_by_id("ctl00_ctl56_g_4e85a275_d641_41ab_8bc5_98c140927f3d_LangDiv33")
    except:
        try:
            language=driver2.find_element_by_id("ctl00_ctl56_g_4e85a275_d641_41ab_8bc5_98c140927f3d_LangDiv2")
        except:
            language=""
    try:
        born_place = driver2.find_element_by_id("ctl00_ctl56_g_4e85a275_d641_41ab_8bc5_98c140927f3d_countrySpn3")
    except:
        try:
            born_place = driver2.find_element_by_id("ctl00_ctl56_g_4e85a275_d641_41ab_8bc5_98c140927f3d_countrySpn")
        except:
            try:
                born_place = driver2.find_element_by_xpath(
                    "//*[@id=\"ctl00_ctl56_g_4e85a275_d641_41ab_8bc5_98c140927f3d_countrySpn2\"]")
            except:
                born_place = ""
    p=[]
    ed=[]
    for x in educations:
        ed.append(x.get_attribute("innerText"))
    for x in profs:
       p.append(x.get_attribute("innerText"))
    if born_place != "":
        born_place=born_place.get_attribute("innerText")
    if language != "":
        language=language.text
    if birth_date != "":
        birth_date=birth_date.text
    if kneset != "":
        kneset=kneset.get_attribute("innerText")
    if army != "":
        army=army.get_attribute("innerText")

    ans={"born_place":born_place,"birth_date":birth_date,"kneset":kneset,"education":ed,"professional":p,"army_service":army,"language":language}
    print(ans)
    return ans

def page_letter(names):
    data=[]
    links=[]
    for name in names:
        link=name.find_element_by_tag_name("a").get_attribute("href")
        driver2.get(link)
        more_info = get_more_info()
        data.append({"name":name.text,"birth_date":more_info["birth_date"],"link":link,
                 "born_place":more_info["born_place"],"kneset":more_info["kneset"], "education":more_info["education"],"professional":more_info["professional"],
                 "army_service":more_info["army_service"],"language":more_info["language"]})
    print(data)
    print(links)
    return data


# specify the url
urlpage = 'https://main.knesset.gov.il/mk/Pages/previous.aspx?pg=mkpnames'
print(urlpage)
# run firefox webdriver from executable path of your choice
driver = webdriver.Firefox(service_log_path="C:\\Users\\mord2\\AppData\\Local\\Temp\\geckodriver.log")
# run firefox webdriver from executable path of your choice
# get web page
driver.get(urlpage)
# execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 30s
time.sleep(3)

driver2 = webdriver.Firefox(service_log_path="C:\\Users\\mord2\\AppData\\Local\\Temp\\geckodriver.log")
driver2.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 10s
time.sleep(5)
#button = WebDriverWait(driver2, 10).until(EC.presence_of_element_located((By.XPATH, "yourXPATH")))


data = []
i = 1;
#was 23
while i < 23:
    letter = driver.find_element_by_xpath("//*[@id=\"ctl00_ctl56_g_55d83661_73b1_4404_9562_b18e46be34e8_pnlControlsLoader\"]/div/div[1]/div[2]/ul/li[" +str(i)+"]")
    letter.click()
    names = driver.find_elements_by_class_name("MKLobbyMKNameDiv")
    _list = page_letter(names)
    for _l in _list:
        data.append(_l)
    i = i + 1
# close drivers
driver2.quit()
driver.quit()
# save to pandas dataframe
df = pd.DataFrame(data)
print(df)
df.to_csv("C:\\Users\\mord2\\AppData\\Local\\Temp\\test.csv")
