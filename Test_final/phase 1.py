c1 = int(input("cạnh đầu tiên dài là: "))
c2 = int(input("cạnh thứ hai dài là: "))
c3 = int(input("cạnh thứ ba dài là: "))

if(c1 == c2 == c3):
    print("Đây là tam giác đều")
elif(c1 == c2 or c1 == c3 or c2 == c3):
    print("Đây là tam giác cân")
elif(c1*c1) + (c2*c2) == (c3*c3):
    print("Đây là tam giác vuông")
elif(c1 + c2 < c3 or c1 + c3 < c2 or c2 + c3 < c1):
    print("Đây không phải là tam giác")
else:
    print("Đây là tam giác thường")