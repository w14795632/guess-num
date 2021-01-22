import random


start = input('請輸入開始數字值')
end = input('請輸入結束數字值')
start = int(start)
end = int(end)


r = random.randint(start, end)
count = 0
while  True :
	count = count + 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('你猜中了!')
		print('這是你猜的第', count, '次')
		break
	elif num > r :
		print('再往下猜一點喔!!太大了')
	elif num < r :
		print('往上猜，不夠大!')
	print('這是你猜的第', count, '次')