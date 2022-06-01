# 產出一個隨機整數1~100(不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對印出"恭喜猜對了！"
# 猜錯要告訴使用者比答案大/小

import random
start = input('請決定範圍最小值： ')
end = input('請決定範圍最大值： ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0 #為了計算猜幾次
while True:
	count += 1  # count = count + 1 
	s = input('請猜數字: ' )
	s = int(s)
	if s == r:
		print('恭喜猜對了！')
		print('總共猜了', count,'次')
		break
	elif s > r:
		print('比答案大')
	else:
		print('比答案小')
	print('這是你猜的第', count,'次')
