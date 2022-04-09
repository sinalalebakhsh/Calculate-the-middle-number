import os
os.system('cls')

list_of_nums = [1,2]

len_list = len(list_of_nums)


if len_list ==0:
    print('\nmy friend!!! list can not Empty! \n')
elif len_list % 2 ==1:
    my_index = int((len_list-1)/2)
    print("\n",list_of_nums[my_index],"\n")
elif len_list % 2 ==0:
    my_index = int(len_list/2)
    middle_avg = (my_index + (my_index-1))/2
    print("\n",middle_avg,"\n")


