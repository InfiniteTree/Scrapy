# encoding:utf-8
import re # 使用正则 匹配想要的图片
import requests #使用requests得到网页源码
num = 1
# 定义mzt函数
def mzt():
    for i in range(1, 3):  # 循环100次 （可以用三元运算）
        yuan = requests.get('http://www.mzitu.com/zipai/comment-page-' + str(i)+'/#comments').content.decode('utf-8')  
        demo = re.compile('<img src="(.*?)" .*?>', re.S)  # 找到图片正则
        list1 = demo.findall(yuan) # 去源码中找匹配到的这个链接
        write_os(list1)
def write_os(list1):
    global num
    for j in list1: # 遍历你得到的图片
        num += 1 # 循环一次加一
        try:
            yuan = requests.get(j).content # 得到你图片的内容
        except requests.exceptions.ConnectionError:
            print("Saving Failed")
            continue
        with open('C://Users//AlexChen//Desktop//Sp//photos//' + str(num) + '.jpg', 'wb') as f:
            f.write(yuan) # 写进去
            f.close() # 关闭文件

 
if __name__ == '__main__': # 代码测试片段
    mzt() # 调用你的函数
