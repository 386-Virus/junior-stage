#this is luhn formular trying to varify bank account number
Acc_number = input("enter the account number:\t")
if len(Acc_number) == 16:
    reverse_num = Acc_number[: : -1]
   # print(reverse_num)
    # we have to change the values to list to access the second digit
    reverse_num_list = list(reverse_num)
    reverse_num_list[1] = str(int(reverse_num_list[1])*2)
    reverse_num_list[1] = str(int(reverse_num_list[1]) - 9)
    #print(reverse_num_list)
    #here now we are looking for the sum of elements of list
    sum_of_lista = sum(int(i) for i in reverse_num_list)
#5161480031419730
    #print(sum_of_lista)
    if sum_of_lista% sum_of_lista==  0 or sum_of_lista%1== 0:
            print("Valid credit number")
    else:
            print("not valid")

else:
    print('not valid')