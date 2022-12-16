# password genrator
import secrets
caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small = 'abcdefghijklmnopqrstuvwxyz'
special = """!@#$%^&*()_+"':;.,<>/?\|"""
nume = '1234567890'
final = caps+small+special+nume
pwd = 10
password = ''
for i in range(pwd):
    password = password + ''.join(secrets.choice(final))
print(password)