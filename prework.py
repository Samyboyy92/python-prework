# Question 1:
def hello_name(user_name):
    print("Hello" + user_name + "!")

hello_name('user_name')


# Question 2:
def odd_numbers2():
    for i in range(1,101):
        print(i)
        
        
# Question 3:
def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num

print(max_num_in_list([3,7,9,11,13]))


# Question 4:
def is_leap(a_year):
    if a_year % 4 == 0 and (a_year % 400 == 0 or a_year % 100 != 0):
        print(True)
    else:
        print(False)

is_leap_year(2024)


# Question 5:
def is_consecutive(a_list):
    a_list.sort()
    status = True
    while i < len(a_list) - 1:
       if a_list[i] + 1 == a_list[i + 1]:
           i += 1
       else:
            status = False
            
    print(status)


