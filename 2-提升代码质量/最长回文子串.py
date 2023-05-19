# 最长回文子串
def longestPalindrome(s):
    # 内部函数，用于判断给定字符串是否是回文串
    def check(s):
        return s == s[::-1]
    
    # 以最长长度 start_len 开始枚举所有可能的回文子串
    start_len = len(s)
    while start_len > 0:
        for i in range(len(s) - start_len+1):
            # 检查以 i 为起始位置、长度为 start_len 的子串是否为回文串
            if check(s[i:i+start_len]):
                return s[i:i+start_len]
        # 如果当前长度值 start_len 对应的所有子串都不是回文串，则将长度减一，继续枚举
        start_len -= 1
    # 如果整个循环结束后还没有找到回文串，则返回空串
    return ""


#print(longestPalindrome('babad'))
s = 'babad'
print(s[::-1])