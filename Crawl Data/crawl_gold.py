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
    os.environ['PATH']+=r"C:/Users/Laptop K1/Downloads/bai 3 selenium/chromedriver.exe"
    driver = webdriver.Chrome()
    driver.get(myurl)
    # Clicking on the date button
    # Sending the start date
    close_button=WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/footer/div[2]/div/div/button")))
    close_button.click()
    start_bar = WebDriverWait(driver,20).until(
                EC.element_to_be_clickable((By.XPATH, 
                "/html/body/div[3]/div[6]/div/mw-downloaddata/form/div/div[2]/div[1]/input")))
    start_bar.clear()
    start_bar.send_keys(start)
    # Sending the end date
    end_bar = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, 
                "/html/body/div[3]/div[6]/div/mw-downloaddata/form/div/div[2]/div[2]/input")))
    end_bar.clear()
    end_bar.send_keys(end)
    # Clicking on the apply button
    apply = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[6]/div/mw-downloaddata/form/div/button")))
    apply.click()
    sleep(5)
    data=[]
    # Getting the tables on the page and quiting
    date = driver.find_elements(By.XPATH,"/html/body/div[3]/div[6]/div/div/mw-tabs/div[2]/div[1]/mw-downloaddata/div/div[1]/table/tbody/tr/td[1]")
    close_price=driver.find_elements(By.XPATH,"/html/body/div[3]/div[6]/div/div/mw-tabs/div[2]/div[1]/mw-downloaddata/div/div[1]/table/tbody/tr/td[5]")
    open_price=driver.find_elements(By.XPATH,"/html/body/div[3]/div[6]/div/div/mw-tabs/div[2]/div[1]/mw-downloaddata/div/div[1]/table/tbody/tr/td[2]")
    high_price=driver.find_elements(By.XPATH,"/html/body/div[3]/div[6]/div/div/mw-tabs/div[2]/div[1]/mw-downloaddata/div/div[1]/table/tbody/tr/td[3]")
    low_price=driver.find_elements(By.XPATH,"/html/body/div[3]/div[6]/div/div/mw-tabs/div[2]/div[1]/mw-downloaddata/div/div[1]/table/tbody/tr/td[4]")
    
    
    for i in range(min(len(date),len(close_price))):
        tem_data={'Date':date[i].text,'Open':open_price[i].text,
                  'High':high_price[i].text,'Low':low_price[i].text
                  ,'Close':close_price[i].text}
        data.append(tem_data)      
    driver.quit()
    return data
url='https://www.marketwatch.com/investing/future/gc00/download-data?mod=mw_quote_tab'
current_date = datetime.strptime('4/1/2010', "%m/%d/%Y")
end_date = datetime.strptime('11/4/2023', "%m/%d/%Y")
interval=25
i=0
while current_date < end_date:
    next_date = min(current_date + timedelta(days=interval), end_date)
    data = get_currencies(url, 
                          current_date.strftime("%m/%d/%Y"),
                          next_date.strftime("%m/%d/%Y"),
                          export_csv=True)
    current_date = next_date + timedelta(days=1)
    df = pd.DataFrame(data)
    df['Open'] = df['Open'].str.replace('$', '')
    df['High'] = df['High'].str.replace('$', '')
    df['Low'] = df['Low'].str.replace('$', '')
    df['Close'] = df['Close'].str.replace('$', '')
    # Define the file path
    file_path = r"C:/Users/Laptop K1/Downloads/bai 3 selenium/gold.csv"
    
    # Check if the file exists and append the DataFrame content
    if os.path.getsize(file_path) > 0:
        existing_data = pd.read_csv(file_path)
        df = pd.concat([df,existing_data], ignore_index=True)
    # Write the DataFrame to CSV
    df.to_csv(file_path, index=False)

    i += 1
    if i == 10:
        sleep(10)
        i = 0