import re
ip_count = 0
ip_data = {}
data = open(file="baidu_x_system.log", mode="r+", encoding="utf-8")

for i in data.readlines():
    da = re.split(' ', i)
    if da[0] not in ip_data:
        ip_data[da[0]] = 1
    elif da[0] in ip_data:
        ip_data[da[0]] = ip_data[da[0]]+1

print(ip_data)