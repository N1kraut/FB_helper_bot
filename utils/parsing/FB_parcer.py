from bs4 import BeautifulSoup
from selenium import webdriver



from webdriver_manager.chrome import ChromeDriverManager


HOST = 'https://ficbook.net/'
URL = 'https://ficbook.net/popular/'


url_es =['all', 'gen', 'het']

#временная
import sys
sys.path.append('..')
from db_api.sql_top_worker import SQLwork

dbt = SQLwork('../../data/database.db')

def main():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(URL+url_es[2])

    items = driver.find_elements_by_class_name('visit-link')

    for item in items:
        if not dbt.names_exists(item.text):
            print(item.text)

    dbt.close()
    driver.quit()

if __name__ == '__main__':
    main()
