while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password?')
    password = input()
    while password != 'swordfish':
        print('Hello, Joe. What is the password?')
        password = input()
    break
print('Access granted.')