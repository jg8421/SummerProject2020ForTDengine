import os
#本程序可以解压指定目录下的所有压缩文件（逐层进入）然后将各个压缩文件转化成文件夹形式
#需要调整的参数有三个：好压程序调用目录 未解压目录 解压导出目录
# 解压并创建相应的文件夹
def main(dir_file,dir_unzip):
	for file_dir in os.listdir(dir_file):
		if file_dir != "DTDS": # 根据自己的文件来的，可以不加
			unzip_dir = dir_unzip + file_dir # 定义解压缩的目录
			if not os.path.exists(unzip_dir):
				os.makedirs(unzip_dir)  # 创建目录，可以完善
			else:
				print("already exists")
				break
			os.chdir(dir_file + file_dir) # 改变工作目录
			for file in os.listdir(dir_file+ file_dir): # 解压缩
				if file[-4:] ==".ZIP":
					# 检验工作文件
					# print(file)
					# 检验目录
					# print(os.getcwd())
					rar_com = "D:\BaiduNetdiskDownload\HaoZip\HaoZipC.exe x %s -o%s" %(file, unzip_dir)
					#上面填入HaoZipC.exe这个可执行文件的目录（环境变量） HaoZip是好压软件的总文件夹
					# print (rar_com)
					os.system(rar_com)

if __name__ =="__main__":
	main(dir_file="D:\\BaiduNetdiskDownload\\patents_data\\I20200317\\"###此处填写等待解压的文件目录 系统会自动遍历并解压
	     , dir_unzip="D:\\BaiduNetdiskDownload\\patents_data\\4233\\")###此处填写输出文件的目录 可以在文件夹内任意命名新的文件夹 然后系统会自动新建文件夹 并将文件导入其中




