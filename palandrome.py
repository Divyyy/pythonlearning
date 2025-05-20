n = int(input( " enter the number"))
rev = 0
og = n
while n > 0:
    digit = n % 10
    rev = rev *10 + digit
    n //=10


if og == rev:
        print("palandrome")
else:
        print(" not a pallondrome")