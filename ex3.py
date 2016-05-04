scores = [60, 73, 81, 95, 34]
n = 0
total = 0
a=0
total2=0
total3=0
for x in scores:
    n += 1
    total += x

avg = total / n

for x in scores:
    a=x**2
    total2 += a
    n += 1

squares=total2

for x in scores:
    b=(x-avg)**2
    total3 += b
    n += 1

squares1=total3

print('total ' + str(total))
print('average ' + str(avg))
print('squares ' + str(squares))
print('sum of squares ' + str(squares1))
