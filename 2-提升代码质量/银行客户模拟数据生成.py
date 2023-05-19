import random

# 客户基本属性
names = ["李刚", "张萍", "王亮", "刘丽", "周华", "陈文", "林伟", "黄建华", "吕丹"]
genders = ["男", "女"]
marriages = ["已婚", "未婚"]
ages = [21, 27, 28, 32, 34, 37, 39, 45, 53]

# 不同职业所对应的平均月收入和家庭资产
occupations = {
    "学生": (3000, "低等"),
    "工人": (6000, "中等"),
    "销售": (8000, "中等"),
    "教师": (10000, "中等"),
    "医生": (18000, "高等"),
    "IT工程师": (20000, "高等"),
    "会计师": (22000, "高等"),
    "律师": (25000, "高等"),
    "企业家": (50000, "非常高等")
}

# 客户的存款历史
balance_history = [1000, 2000, 5000, 6000, 8000, 10000, 12000, 18000, 20000, 25000, 30000]

# 客户账户信息
account_types = ["个人活期账户", "个人定期账户", "个人储蓄账户", "对公活期账户", "对公定期账户"]
card_levels = ["普通级别", "金级别", "白金级别", "钻石级别"]
net_banking = ["是", "否"]
mobile_banking = ["是", "否"]
e_payment = ["是", "否"]
credit_limits = [0, 50000, 100000, 200000, 300000, 500000, 1000000]
signed_digital_certificates = ["是", "否"]
transaction_count = [0, 1, 2, 3, 5, 8, 10, 15, 20, 50]

# 生成10条数据
for i in range(10):
    name = random.choice(names)
    gender = random.choice(genders)
    marriage = random.choice(marriages)
    age = random.choice(ages)
    occupation = random.choice(list(occupations.keys()))
    print('occupation=', occupation)
    income, home_asset = occupations[occupation]
    balance = random.choice(balance_history)
    account_type = random.choice(account_types)
    card_level = random.choice(card_levels)
    net_bank = random.choice(net_banking)
    mobile_bank = random.choice(mobile_banking)
    e_pay = random.choice(e_payment)
    credit_limit = random.choice(credit_limits)
    signed_cert = random.choice(signed_digital_certificates)
    trans_count = random.choice(transaction_count)
    print(name, gender, marriage, occupation, age, income, home_asset, balance, account_type, card_level, net_bank, mobile_bank, e_pay, credit_limit, trans_count, signed_cert)
    print("客户名称：{}，性别：{}，婚姻：{}，职业：{}，年龄：{}；月收入：{}元，家庭资产：{}；历史存款日均余额：{}元；账户类型：{}，开卡等级：{}，签约直销银行：{}，网上银行：{}，手机银行：{}，电子支付：{}，授信额度：{}元，开卡数量：{}张，是否签约数字证书：{}，近一年动账次数：{}次。".format(
        name, gender, marriage, occupation, age, income, home_asset, balance, account_type, card_level, net_bank, mobile_bank, e_pay, credit_limit, trans_count, signed_cert))
