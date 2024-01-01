import os
from flask import Flask, send_file
import random

# 建立空字典
Image_Dict = {}
# 定义编号起始值
Image = 0
# 定义图片存放目录
File_dir = 'images/'

# 获取文件夹下所有文件名
file_list = os.listdir(File_dir)

# 遍历并进行编号
for x in file_list:
    Image += 1
    Image_Dict[Image] = x

# 实例化Flask
Web = Flask(__name__)


# 定义API路由
@Web.route('/API/images')
def images():
    random_num = random.randint(1, len(Image_Dict) - 1)  # 生成随机数
    file_name = file_list[random_num]  # 根据随机数读取文件名
    return send_file(File_dir + file_name, mimetype='image/png')  # 返回对应文件名的内容


if __name__ == "__main__":
    Web.run(host='0.0.0.0', port=5001)
