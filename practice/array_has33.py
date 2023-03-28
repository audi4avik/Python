# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere

def listhas33(input_list):
    print(len(input_list))
    s1 = ''.join(str(i) for i in input_list)

    if '33' in s1:
        print('True')
    else:
        print('False')
    # for i in range(0, len(input_list) - 1):
    #     if input_list[i] == 3 and input_list[i + 1] == 3:
    #         print("True")
    #     else:
    #         print("False")


nums = [1, 3, 1, 3, 1]
listhas33(nums)