import os

print("请确保您已将下列内容置于当前目录下：")
print("<测试数据 或 数据生成程序> <解答程序>")
os.system("pause")
print("不建议您在程序中写入文件操作")

# read _ begin

os.system("dir > list.txt")

file_list_txt = ""
file_list_lst = []

with open("list.txt") as fp:
	file_list_txt = fp.read()

os.system("del list.txt")

# read _ end

# get list _ begin

tot_data = 0
tot_exe = 0
final_list = []
solution = []

file_list_lst = []
mid_lst = file_list_txt.split('\n')

sted = False

for i in mid_lst:
	if sted:
		if i.find(" <DIR> ") != -1:
			continue
		if i.find(":") == -1:
			break
		file_list_lst.append(i.split(' ')[-1])
	else:
		if i.find(" <DIR> ") != -1:
			sted = True
		else:
			pass


for i in file_list_lst:
	if len(i) <= 0:
		continue
	if i[0] == '.':
		continue
	else:
		whl_name = i.split('.')
		if whl_name[-1] == "exe":
			solution.append(i)
			tot_exe += 1
			continue
		if whl_name[-1] == 'in':
			final_list.append(i)
			tot_data += 1
			continue
		if i.find("input") != -1:
			final_list.append(i)
			tot_data += 1
			continue
		if whl_name[-1] != 'py' and i != "list.txt":
			print("Unkonwn file: " + i)
			continue

if tot_data > 0:
	print("以下为已确认的测试数据列表，请在确认无误后继续。")
	for i in final_list:
		print(i)
	print("共" + str(tot_data) + "个测试点")
	os.system("pause")

# get list _ end

# Correction _ begin

work_type = -1

sol_exe = ""
make_exe = ""

if tot_exe > 1:
	if tot_data > 0:
		print("发现有多个可执行文件")
		id = -1
		for i in solution:
			id += 1
			print("No." + str(id) + " " + i)
		print("请输入编号，指定一个<解答程序>")
		sol_exe = solution[int(input().split(' ')[0])]
		make_exe = "NONE"
	else:
		print("当前无可用测试数据，")
		print("但是存在下列可执行文件：")
		id = -1
		for i in solution:
			id += 1
			print("No." + str(id) + " " + i)
		print("请输入编号，指定<数据生成器>")
		make_exe = solution[int(input().split(' ')[0])]
		print("请输入编号，指定<解答程序>")
		sol_exe = solution[int(input().split(' ')[0])]

else:
	if tot_data <= 0:
		print("要素不足，程序将自行退出")
		os.system("pause")
		exit()
	else:
		sol_exe = solution[0]
		make_exe = "NONE"

# Correction _ end

os.system("cls")
print("准备工作已经完成，接下来你将看到数据生成进度")

# MAIN

if make_exe != "NONE":
	tot = int(input("请输入要生成的测试点数目:").split(' ')[0])
	all_qwq = tot
	while tot > 0:
		os.system(make_exe + " > " + "data" + str(tot) + ".in")
		os.system(sol_exe +" < data" + str(tot) + ".in" + " > data" + str(tot) + ".out")
		tot -= 1
		print("已完成" + str(all_qwq - tot) + r"/" + str(all_qwq))
else:
	tot = len(final_list)
	num = 0
	for inputfile in final_list:
		if inputfile.split('.')[-1] == 'in':
			os.system(sol_exe +" < " + inputfile + " > " + inputfile.replace(".in", ".out"))
		else:
			os.system(sol_exe +" < " + inputfile + " > " + inputfile.replace("input", "output"))
		num += 1
		print("已完成" + str(num) + r"/" + str(tot))

print("数据已全部生成完毕.")

os.system("pause")

# END
