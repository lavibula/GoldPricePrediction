from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
from datetime import datetime, timedelta
import os 
def get_currencies(myurl, start, end, export_csv=False):
    data=[]
    
        # Opening the connection and grabbing the page
    os.environ['PATH']+=r"C:/Users/Laptop K1/Downloads/bai 3 selenium/chromedriver.exe"
    driver = webdriver.Chrome()
    driver.get(myurl)
    driver.maximize_window()
    # Clicking on the date button
    # Sending the start date
    close_button=WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/footer/div[2]/div/div/button")))
    close_button.click()
    start_bar = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, 
                "/html/body/div[3]/div[6]/div/mw-downloaddata/form/div/div[2]/div[1]/input")))
    start_bar.clear()
    start_bar.send_keys(start)
    # Sending the end date
    end_bar = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, 
                "/html/body/div[3]/div[6]/div/mw-downloaddata/form/div/div[2]/div[2]/input")))
    end_bar.clear()
    end_bar.send_keys(end)
    # Clicking on the apply button
    apply = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[6]/div/mw-downloaddata/form/div/button")))
    apply.click()
    sleep(5)
    data=[]
    # Getting the tables on the page and quiting
    date = driver.find_elements(By.XPATH,"/html/body/div[3]/div[6]/div/div/mw-tabs/div[2]/div[1]/mw-downloaddata/div/div[1]/table/tbody/tr/td[1]")
    close_price=driver.find_elements(By.XPATH,"/html/body/div[3]/div[6]/div/div/mw-tabs/div[2]/div[1]/mw-downloaddata/div/div[1]/table/tbody/tr/td[5]")
    for i in range(min(len(date),len(close_price))):
        tem_data={'Date':date[i].text,'Price':close_price[i].text}
        data.append(tem_data)      
    return data
i=1
for url in ['https://www.marketwatch.com/investing/future/si00/download-data?mod=mw_quote_tab',
            'https://www.marketwatch.com/investing/future/pl00/download-data?mod=mw_quote_tab',
            'https://www.marketwatch.com/investing/future/hg00/download-data?mod=mw_quote_tab']:
    current_date = datetime.strptime('4/1/2010', "%m/%d/%Y")
    end_date = datetime.strptime('11/4/2023', "%m/%d/%Y")
    interval=25
    all_data=[]
    while current_date < end_date:
        next_date = min(current_date + timedelta(days=interval), end_date)
        data=get_currencies(url, 
                        current_date.strftime("%m/%d/%Y"),next_date.strftime("%m/%d/%Y")
                            , export_csv=True)
        all_data=data+all_data
        current_date=next_date+timedelta(days=1)
        df=pd.DataFrame(all_data)
        df['Price'] = df['Price'].str.replace('$', '')
        if i==1:
            df.to_csv(r"C:/Users/Laptop K1/Downloads/bai 3 selenium/silver.csv", index=False)
        elif i==2:
            df.to_csv(r"C:/Users/Laptop K1/Downloads/bai 3 selenium/platinum.csv", index=False)
        else :df.to_csv(r"C:/Users/Laptop K1/Downloads/bai 3 selenium/copper.csv", index=False)
    i+=1

