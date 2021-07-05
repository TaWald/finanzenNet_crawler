import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver

from typing import List

def get_exchange_and_table_data(soup) -> dict:
    """ Uses the side column to gather the exchange volume and other data.

    :param soup: Soup of the current page
    :return:
    """
    side_col = soup.find_all("div", class_="box table-quotes")[0]
    exchange_element = side_col.find_all("li", class_="active")[0]
    current_exchange_name = exchange_element.text
    current_exchange_data = dict(exchange_name=current_exchange_name)
    table_content = side_col.contents[3]
    values = table_content.find_all("td", class_="font-bold")
    for value in values:
        table_row = {str(value.text): value.next_sibling.text}
        current_exchange_data.update(table_row)
    return current_exchange_data

def get_all_page_links(url, soup) -> List[str]:
    exchange_name_link_dict = {}
    side_col = soup.find_all("div", class_="box table-quotes")[0]  # Side box table
    menu_down = side_col.find_all("div", class_="menuDown")[0]
    driver_path = "/usr/bin/chromedriver"
    driver = webdriver.Chrome(driver_path)
    page = driver.get(url)
    driver.find_elements_by_class_name()
    return


def main(name):
    url = "https://www.finanzen.net/aktien/gamestop-aktie"
    page = requests.get(url)
    soup = bs(page.content, features="html.parser")

    page_links = get_all_page_links(url, soup)

    return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
