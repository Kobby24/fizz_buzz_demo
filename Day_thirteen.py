####DEBUGING
# # Describe the problem
# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")
# my_function()

# #Reproduce the bug
# from random import randint
# dice_imgs = ["@", "@", "@", "@", "@", "@"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# #Play Computer
# year = int(input("What is your year of birth?"))
# if year > 1980 and year < 1994:
#     print("You are a millenial.")
# elif year >= 1994:
#     print("You are a Gen Z.")

# #Fix the Errors
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")

# #Print is your friend 
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# print(pages)
# word_per_page = int(input("NUmber of words per page: "))
# print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item *2
#         b_list.append(new_item)
#     print(b_list) 
# mutate([1, 2, 3, 5, 8, 13])

# # Ex 1
# number = int(input("Which number do you want to check"))

# if number % 2 == 0:
#     print("This ia an even number ")
# else:
#     print("This is an odd number.")
 
# year = int(input("Which year do you want to check "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap Year")
#         else:
#             print("Not Leap Year")
#     else:
#         print("Leap Year")
# else:
#     print("Not Leap Year")

for number in range(1, 101):
    if number % 3 ==0 and number % 5 == 0:
        print("FizzBuzz")
    if number % 3 ==0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    else:
        print([number])