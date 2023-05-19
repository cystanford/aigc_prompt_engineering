import requests
from bs4 import BeautifulSoup
import csv
import urllib.parse

# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# 目标链接
url = 'https://leetcode-cn.com/problemset/all/'

# 发送请求，获取HTML源码
response = requests.get(url, headers=headers)

# 解析HTML源码
soup = BeautifulSoup(response.text, 'html.parser')

# 获取包含所有题目信息的列表
question_list = soup.find_all('div', class_='question-list-table')

# 创建一个CSV文件，保存题目信息
with open('Leetcode-problems.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # 写入表头
    writer.writerow(['序号', '标题', '难度', '通过率', '链接'])

    # 遍历所有题目信息
    for question in question_list:
        # 获取序号、题目名称、难度等级、通过率和题目链接
        number = question.find('div', class_='col-xs-1').text.strip()
        title = question.find('div', class_='col-xs-7').a.text.strip()
        difficulty = question.find('div', class_='col-xs-1').find('span')['class'][1].replace('diff-', '')
        acceptance = question.find_all('div', class_='col-xs-1')[1].text.strip()
        link = urllib.parse.urljoin(url, question.a['href'])

        # 将题目信息写入到CSV文件中
        writer.writerow([number, title, difficulty, acceptance, link])

print('题目信息采集完成！')
