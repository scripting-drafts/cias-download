from selenium import webdriver
from tqdm import tqdm
import subprocess

url = 'https://archive.org/download/nesencia/'


driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get(url)

cias = driver.find_elements_by_partial_link_text('.cia')

for raw_cia in tqdm(cias):
    cia = raw_cia.get_attribute('href')
    subprocess.Popen('wget ' + cia, stdin=None, stderr=None, shell=True, universal_newlines=False).communicate()

driver.quit()
