'''
From CoderByte: "Using the Python language, have the function TimeConvert(num)
take the num parameter being passed and return the number of hours and minutes
the parameter converts to (ie. if num = 63 then the output should be 1:3).
Separate the number of hours and minutes with a colon. 
'''
#1-Divide the number of minutes and get the quotient and remainder.
#2-Get the quotient (total hours) and remainder (minutes)
#3-Convert those values to the appropriate string format with the colon
#Return - Return the properly formatted string


def time_convert(num):

    hour_time = 60

    divide_times = divmod(num, hour_time)

    return_string = "{0}:{1}".format(divide_times[0], divide_times[1])

    return return_string


print time_convert(63)


