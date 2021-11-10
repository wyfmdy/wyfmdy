from 工商银行完整版 import bank_addUser
from unittest import  TestCase
from ddt import ddt
from ddt import data
from ddt import  unpack
import xlrd
import xlwt



wb = xlrd.open_workbook(filename=r"D:\pythonProject2day1111\111.xls",encoding_override=True)
df = wb.sheet_names()
wb_len = len(wb.sheets())
da_addUser = []
# da_saveMoney = []
# da_takeMoney = []
# da_transformMoney = []
# da_selectUser = []
# da_transformMoney = []
for i in range(wb_len):
  st = wb.sheet_by_index(i)
  rows = st.nrows
  for j in range(1,rows):
    data = st.row_values(j)
    if i == 0:
        da_addUser.append([data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]])

    # elif i == 1:
    #     da_saveMoney.append([data[0], data[1], data[2]])
    # elif i == 2:
    #     da_takeMoney.append([data[0], data[1], data[2], data[3]])
    # elif i == 3:
    #     da_transformMoney.append([data[0], data[1], data[2], data[3], data[4]])
    # elif i == 4:
    #     da_selectUser.append([data[0], data[1], data[2]])
        print(da_addUser)
        # print(da_saveMoney)
        # print (da_takeMoney)
        # print (da_transformMoney)
        # print(da_selectUser)
#username,password,country,province,street,door,money
#da = xlrd.open_workbook(filename=r"D:\pythonProject2day1111\111.xls",encoding_override=True)  # 程序自动去读取参数化数据

# @ddt
# class TestBank(TestCase):
#
#     @data(*da)
#     @unpack
# #     def testAddUser(self,a,b,c,d,e,f,g,h):
#         result = bank_addUser(a,b,c,d,e,f,g)
#
#         if result == h:  # 让程序自动将测试结果写到excel表里。
#             xlwt.Worksheet(1,8,"通过！")
#         else:
#             xlwt.Worksheet(1,8,"不通过")
#
#         # 断言
#         self.assertEqual(result,h)

























