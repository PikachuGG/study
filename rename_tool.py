import os                         # 导入 os 模块，提供操作系统相关功能（如重命名）
folder = input("文件夹路径：")      # 让用户输入要处理的文件夹
prefix = input("前缀：")           # 让用户输入要加的前缀，如 "照片_"
for f in os.listdir(folder):      # os.listdir 列出文件夹下所有文件名，逐个取出
    old = folder + "/" + f        # 旧完整路径
    new = folder + "/" + prefix + f  # 新完整路径（加了前缀）
    os.rename(old, new)           # 执行重命名
print("完成") 
