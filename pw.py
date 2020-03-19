password = 'a123456'
pw_num = 3
while True:
	pw = input('Enter your password: ')
	if pw == password:
		print('Login Successfully')
		break
	else:
		pw_num = pw_num - 1
		print('Wrong Password, ', 'You have ', pw_num ,'time(s) left' )
		if pw_num == 0:
			print('Password Incorrect')
			print('Program Shut Down')
			break
