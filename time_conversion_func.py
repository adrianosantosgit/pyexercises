#!/bin/python3

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING user_input as parameter.
# The function just handles two (00) digit hours input.
#

def timeConversion(user_input):
    # Write your code here
    # Define the last two chars as marker AM or PM
    marker = user_input[-2:]
    
    if marker == "PM" and user_input[:2] != '12':
        user_input = str(12 + int(user_input[:2])) + user_input[2:]
    if marker == "AM" and user_input[:2] == '12':
        user_input = '00' + user_input[2:]
    return user_input[:-2]
    
user_input = input("Please insert a time in hour AM/PM format:\nLike 06:00:00AM or 06:00:00PM\n")
print("In military (24-hour) time: ", timeConversion(user_input))
