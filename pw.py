password = 'a123456'
pw_num = 3
while pw_num > 0:
	pw_num = pw_num - 1 
	pw = input('Enter your password: ')
	if pw == password:
		print('Login Successfully')
		break
	else:
		if pw_num == 0:
			print('Password Incorrect')
			print('Program Shut Down')
		else:
			print('Wrong Password, ')
			print('You have ', pw_num, 'time(s) left')
		
			
