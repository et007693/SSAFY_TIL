# 원주율
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
# 반지름
r = 15

a = '원주율 : '
b = '반지름 : '
c = '원의 둘레 : '
d = '원의 넓이 : '

print(a, str(pi)[:17])
print(b, r)
print(c, r*2*pi)
print(d, r*r*pi)