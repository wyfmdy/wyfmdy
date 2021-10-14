

data=[5,2,4,7,9,1,3,5,4,0,6,1,3]
for j in range(len(data)+1):
    for i in range(len(data)-1):
     if data[i] > data[i+1]:
        tmp = data[i+1]
        data[i+1] = data[i]
        data[i]=tmp
        print(data)
