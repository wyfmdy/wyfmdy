'''
分支判断：
单分支：if
双分支：if    else
多分支：if    elif      elif
'''
score =  input("请输入您的分数:")
score = int(score)
if score >= 90 and score <= 100:
    print("优秀!excellent!")
elif score >= 80 and score <90:
    print("好! Good!")
elif score >= 70 and score <80:
    print("一般般!just so so")
elif score >= 60 and score <70:
    print("小伙子.你很危险!")
elif score >= 0 and score <60:
    print("不及格！恭喜，您的试卷在路上！")
else:
    print("输入非法!")