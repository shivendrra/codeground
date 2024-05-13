rng = int(input("enter the range"))
list = []

for x in range(0,rng):
    inpNo = int(input("enter the no"))
    list.append(inpNo)
for ele in range(len(list)):
    currNo = list[ele]
    rev = 0
    while currNo > 0:
        remain = currNo/10
        rev = (rev*10) + remain
        currNo = currNo//10
        print("\n reverse no are = %d" %rev)