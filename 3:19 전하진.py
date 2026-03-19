Number = int(input("입력값 진수 설정(16/10/8/2)"))
Input = input("값 입력:")
if Number == 16:
    Input = int(Input,16)
    
if Number == 10:
    Input = int(Input)
    
if Number == 8:
    Input = int(Input,8)
  
if Number == 2:
    Input = int(Input,2)
    

    

print("16진수 ==>",hex(Input),
      "10진수 ==>",int(Input),
      "8진수 ==>",oct(Input),
      "2진수 ==>",bin(Input))