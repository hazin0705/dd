import random

def lotto_num():
    return random.randrange(0,46)

lotto = []
num = 0

while True:
    num = lotto_num()
    
    if lotto.count(num) == 0:
        lotto.append(num)
    
    if len(lotto) == 6:
        break


print("** 로또 추첨을 시작합니다 **")
print('추첨된 로또 번호 ======>',end= " ")
lotto.sort()
for i in lotto :
    print(i,end=" ")