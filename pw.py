password = 'a123456'
pw_num = 1
while pw_num >= 1 and pw_num <= 3:
	pw = input('Enter your password: ')
	if pw == password:
		print('Login Successfully')
		break
	else:
		print('Wrong Password, ', 'You have tried ', pw_num ,'time(s)' )
		pw_num = pw_num + 1
		if pw_num == 4:
			print('Password Incorrect')
			print('Program Shut Down')
			break
