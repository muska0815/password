print('你只有三次機會, 請輸入密碼')
i = 3
while True:
	password = input('請輸入密碼: ')
	if password == 'a123456':
		print('登入成功!!')
		break
	else:
		i = i - 1
		print('密碼錯誤, 還有', i,' 次機會')
		if i == 0:
			break