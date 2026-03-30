question = int(input("1.입력한 수식 계산 2.두 수 사이의 합계"))

if question == 1:
    term1 = str(input("수식을 입력하세요"))
    answer = eval(term1)
    result = print("%s의 결과는 %d입니다"%(term1,answer))


if question == 2:
    n1 = int(input("첫 번째 숫자를 입력하세요"))
    n2 = int(input("두 번째 숫자를 입력하세요"))
    result = 0
    if n2>n1:
        for i in range(n1,n2+1):
            result += i
        print("%d+.....+%d는 %d입니다"%(n1,n2,result))
    if n1>n2:
        for i in range(n2,n1+1):
            result += i
        print("%d+.....+%d는 %d입니다"%(n2,n1,result))

else:
    print("1 또는 2만 입력해주세요")
