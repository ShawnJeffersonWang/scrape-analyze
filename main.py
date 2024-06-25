import csv

from bs4 import BeautifulSoup
import os
import time
import requests


def get_data():
    base_url = 'https://college.gaokao.com/schlist/p{}'
    num_pages = 107

    for i in range(1, num_pages + 1):
        print(f"正在下载第{i}页数据")
        url = base_url.format(i)
        res = requests.get(url)

        if res.status_code != 200:
            print(f"第{i}页数据下载失败，状态码：{res.status_code}")
            continue

        content = BeautifulSoup(res.text, "html.parser")
        college_list = content.find('div', class_='scores_List').find_all('dl')
        items = [parse_item(item) for item in college_list]

        save_to_csv(items)

        # time.sleep(1)


def parse_item(item):
    try:
        college_name = item.find('strong')['title']
        college_attr = item.find_all('li')
        college_site = college_attr[0].text.split('：', 1)[1]
        college_title = college_attr[1].text.split('：', 1)[1]
        college_type = college_attr[2].text.split('：', 1)[1]
        college_belong = college_attr[3].text.split('：', 1)[1]
        college_nature = college_attr[4].text.split('：', 1)[1]
        college_website = college_attr[5].text.split('：', 1)[1]

        result = {
            'college_name': college_name,
            'college_site': college_site,
            'college_title': college_title,
            'college_type': college_type,
            'college_belong': college_belong,
            'college_nature': college_nature,
            'college_website': college_website
        }

        return result
    except Exception as e:
        print(f"解析项目时出错: {e}")
        return None


def save_to_csv(data):
    file_exists = os.path.exists('college_data.csv')

    with open('college_data.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['college_name', 'college_site', 'college_title', 'college_type',
                                               'college_belong', 'college_nature', 'college_website'])

        if not file_exists:
            writer.writeheader()

        for item in data:
            if item:
                writer.writerow(item)


if __name__ == '__main__':
    get_data()
