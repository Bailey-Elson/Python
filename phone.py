#!/usr/bin/env python3.8
test_list = [0,1,2,3,4,5,6,7,8,9]
output_phone_number = []
output_phone_number.append("(")
for i in range(0,3):
    output_phone_number.append(str(test_list[i]))
output_phone_number.append(") ")
for i in range(3,6):
    output_phone_number.append(str(test_list[i]))
output_phone_number.append("-")
for i in range(6,10):
    output_phone_number.append(str(test_list[i]))
print(*output_phone_number, sep="")