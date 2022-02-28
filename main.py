import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.google.co.in/')
driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('wikipedia')
driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]').click()
driver.find_element(By.XPATH,'/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/a/h3').click()
driver.find_element(By.XPATH,'/html/body/div[3]/form/fieldset/div/input').send_keys('what is the size of sun')
driver.find_element(By.XPATH,'/html/body/div[3]/form/fieldset/button/i').click()
driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[4]/div[3]/ul/li[1]/div[1]/a').click()
wiki_text = driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div[5]/div[1]/p[2]').text
print(wiki_text)
#sudo apt install espeak
import pyttsx3
engine = pyttsx3.init()
engine.say(wiki_text)
engine.runAndWait()