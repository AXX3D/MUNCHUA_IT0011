namef = input('Enter your First Name: ')
namel = input('Enter your Last Name: ')
age = input('Enter your Age: ')
print('')
print('Full Name: ' + namef + ' ' + namel)
sliced = namef[:3]
print ('Sliced Name: ' + sliced)
print('Greeting Message: Hello, ' + sliced + '! Welcome. You are ' + age + ' years old.')