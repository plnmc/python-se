import sys
import argparse
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", help="address to search", metavar="ADDRESS", default="Серафимовича, 14")
    args = parser.parse_args()
    address = args.a
    print("Search for address \"" + address + "\" on 2gis")

    browser = webdriver.Chrome()
    browser.get('https://2gis.ru/novosibirsk')
    time.sleep(10)
    elem = browser.find_element(By.CLASS_NAME, '_1gvu1zk')  # Find the search box
    elem.send_keys(address + Keys.RETURN)
    s=input('Press Enter to continue...') 
    
if __name__ == '__main__':
    main()
