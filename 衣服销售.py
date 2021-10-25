import xlrd

# 打开工作簿
wb = xlrd.open_workbook(filename=r"C:\Users\Administrator\Desktop\刚学的python\day07\任务\111.xls",encoding_override=True)

# 整体存储数据库
store = {}
'''
    存储结构：
        风衣：{
            "sum_money":xxxx,  # 总销售额
            "sum_count":xxx,   # 总销售量
        },
        "羽绒服":{
            "sum_money":xxx,
            "sum_count":xxxxx,
        }
'''
# 获取所有工作簿选项卡个数
nsheet = wb.nsheets

# 现在要获取所有工作簿的表格数据
for i in range(nsheet):  # 遍历每个选项卡
    # 获取第n个选项卡
    st = wb.sheet_by_index(i)
    # 获取有多少行
    nrow = st.nrows
    for j in range(1, nrow):  # 遍历选项卡每一行
        cell = st.row_values(j)  # 获取第j行数据
        if cell[1] in store:  # 判断在存储库是否存在
            store[cell[1]] = {  # 若存在，则累加数据
                "sum_money": round(store[cell[1]]["sum_money"] + cell[2] * cell[4], 2),
                "sum_count": int(store[cell[1]]["sum_count"] + cell[4])
            }
        else:  # 若不存在，这是以第一次统计数据
            store[cell[1]] = {
                "sum_money": round(cell[2] * cell[4], 2),
                "sum_count": int(cell[4])
            }
# 全年统计总和
all_sum = sum(store[item]["sum_money"] for item in store)  # 全部总销售额
all_count = sum(store[item]["sum_count"] for item in store)  # 全部总销售量
print("全年的统计总销售额：￥", round(all_sum, 2))
print("全年的统计总销售量：", round(all_count, 2), "件！")
for name in store:
    print("------------------------------------------")
    print(name, "的销售额占比为：", round(store[name]["sum_money"] / all_sum * 100, 2), "%")
    print(name, "的销售量占比为：", round(store[name]["sum_count"] / all_count * 100, 2), "%")

'''
{
"羽绒服":{price:253.6,count:500,销售量:150},
"牛仔裤"：{price:86.3,count:600,销售量：60}
}
12月份销售额：49791￥(将所有每种衣服单价 * 销售总量加在一起)
平均单日销售件数：58(总销售量 / 30)
    风衣本月销售比：46%
    皮草本月销售比：23%
    T血本月销售比：63%
    羽绒服本月销售比：24%
    牛仔裤本月销售比：35%
    衬衫本月销售比：38%
'''
# 1. 将excel表数据形成一个字典
import xlrd
import xlwt
from xlutils.copy import copy

work = xlrd.open_workbook(filename=r"C:\Users\Administrator\Desktop\刚学的python\day07\任务\111.xls")
sheet = work.sheet_by_index(0)  # 打开第一个选项卡

rows = sheet.nrows  # 所有行
cols = sheet.ncols  # 所有列
name_index = 1  # 服装名称所在的列角标
price_index = 2  # 价格列角标
count_index = 3  # 库存量的列角标
sale_index = 4  # 日销售量的列角标
store = {}  # 存储数据的空字典
for i in range(1, rows):
    name = sheet.cell_value(i, name_index)  # 获取当前服装的名称
    price = sheet.cell_value(i, price_index)  # 获取当前行的单价
    count = sheet.cell_value(i, count_index)  # 获取当前行的库存量
    sale = sheet.cell_value(i, sale_index)  # 获取当前行的日销售量
    if name in store:  # 已经在字典中存在的情况
        store[name]["销售量"] = store[name]["销售量"] + sale  # 将当前销售量累加进去
    else:
        store[name] = {"price": price, "count": count, "销售量": sale}  # 将销售量存进去

# 2.计算各项数据
'''
    总销售额：
    平均每日销售量：
    每个商品销售占比：
'''
sum = 0
avg = 0
s = 0  # 总的销售量
sales = {}  # "羽绒服":35%
for key in store.keys():
    sum = sum + (store[key]["price"] * store[key]["销售量"])  # 统计总额
    s = s + store[key]["销售量"]  # 所有商品销售总量
    if key in sales:  # 如果统计过，则跳过
        continue
    else:
        sales[key] = str(round(store[key]["销售量"] / store[key]["count"], 3) * 100) + "%"
avg = s // 30  # 平均每日销售量
print("总的销售额：", round(sum, 1), ",平均每日销售量：", avg, ",每个商品的销售占比：")
for key in sales.keys():
    print(key, "=", sales[key])

# 3.继续写到excel表里
workbook = xlwt.Workbook(encoding="utf-8")  # 使用xlwt写入excel表格数据
copywb = copy(work)  # 把原来的工作簿拷贝一份
target = copywb.get_sheet(0)  # 获取第一个选项卡
target.write(rows + 1, 0, "总销售额：" + str(round(sum, 1)))  # 写入总额
target.write(rows + 1, count_index, "平均日销售量：" + str(avg))  # 写入平局销售量
# 循环写入占比
for key in sales.keys():
    rows = rows + 1
    precent = sales[key]  # 获取占比
    target.write(rows, sale_index, key + "本月销售占比:" + precent)
copywb.save("总数据.xls")  # 保存数据
