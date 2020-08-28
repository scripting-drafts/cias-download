from selenium import webdriver
from tqdm import tqdm
import subprocess

url = 'https://archive.org/download/nintendo-dsiware-cias'

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get(url)

cias = driver.find_elements_by_partial_link_text('.cia.7z')

for raw_cia in tqdm(cias):
    cia_link = raw_cia.get_attribute('href')
    driver.get(cia_link + '/')
    cia = driver.find_element_by_partial_link_text('.cia')
    subprocess.Popen('wget ' + cia.get_attribute('href'), stdin=None, stderr=None, shell=True, universal_newlines=False).communicate()
    driver.back()

url = 'https://archive.org/download/dsiware-cias-2'
driver.get(url)

cias = driver.find_elements_by_partial_link_text('.cia.7z')

for raw_cia in tqdm(cias):
    cia_link = raw_cia.get_attribute('href')
    driver.get(cia_link + '/')
    cia = driver.find_element_by_partial_link_text('.cia')
    subprocess.Popen('wget ' + cia.get_attribute('href'), stdin=None, stderr=None, shell=True, universal_newlines=False).communicate()
    driver.back()

driver.quit()
