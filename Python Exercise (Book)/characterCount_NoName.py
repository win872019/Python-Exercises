message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
c = {}

for i in message:
    c.setdefault(i, 0)
    c[i] = c[i] + 1

print(c)