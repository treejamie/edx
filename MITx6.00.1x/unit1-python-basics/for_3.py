end = 25


x = 0
for i in range(1, end + 1):
	x += i
print(x)



num = 10
for num in range(5):
    print(num)
print(num)


divisor = 2
for num in range(0, 10, 2):
    print(num/divisor)

print("-----------")


for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!')

print("---------")
count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)