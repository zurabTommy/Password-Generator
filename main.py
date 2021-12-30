import random
final = ''
password = []
diggits = '1234567890'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
punctuation = '!#$%&*+-=?@^_'
pwd_length = int(input('Enter password length: '))
pwd_digits = input('Include numbers (yes = y, no = n): ')
if pwd_digits == 'y':
    password.extend(list(diggits))
pwd_uppercase = input('Include uppercase letters (yes = y, no = n): ')
if pwd_uppercase == 'y':
    password.extend(list(uppercase))
pwd_lowercase = input('Include lowercase letters (yes = y, no = n): ')
if pwd_lowercase == 'y':
    password.extend(list(lowercase))
pwd_punctuation = input('Include symbols "!#$%&*+-=?@^_"? (yes = y, no = n): ')
if pwd_punctuation == 'y':
    password.extend(list(punctuation))
for i in range(pwd_length):
    final = final + random.choice(password)
print(final)


