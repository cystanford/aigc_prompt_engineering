from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置Chrome浏览器的配置项
chrome_options = Options()
#chrome_options.add_argument('--headless')  # 无界面模式
#chrome_options.add_argument('--start-maximized')  # 窗口最大化模式

# 创建一个ChromeDriver实例
driver = webdriver.Chrome(options=chrome_options)

# 目标链接
url = 'https://leetcode-cn.com/problemset/all/'

# 访问目标链接
driver.get(url)

# 隐式等待页面加载完成
driver.implicitly_wait(3)

# 等待弹窗出现并点击关闭按钮
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'redesign-notice-close-btn'))).click()

# 获取包含所有题目信息的列表
question_list = driver.find_elements(By.XPATH, '//div[@class="question-list-table"]/table/tbody/tr')

# 遍历所有题目信息
for question in question_list:
    # 获取序号、标题、难度等级、通过率和题目链接
    number = question.find_element(By.XPATH, './/td[1]').text.strip()
    title = question.find_element(By.XPATH, './/td[3]//a').text.strip()
    difficulty = question.find_element(By.XPATH, './/td[6]//span').get_attribute('innerHTML')
    acceptance = question.find_element(By.XPATH, './/td[7]//text()[1]').replace(' ', '').replace('\n', '')[:-1]
    link = question.find_element(By.XPATH, './/td[3]//a').get_attribute('href')

    # 打印题目信息
    print('序号：{}\n标题：{}\n难度等级：{}\n通过率：{}\n链接：{}\n'.format(number, title, difficulty, acceptance, link))

# 关闭浏览器窗口
driver.quit()
