"""
OK, so the course calls for you to learn to read code by reading code.

I'm not doing that strictly. I've been using this file to step through code and to
learn about how I expect code to run vs how it does.

Also, you know, time. The chances of my death increase each day.

"""

def normalize(numbers):
    max_number = max(numbers)
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
    return numbers  

try:
      normalize([0, 0, 0])
except ZeroDivisionError:
      print('Invalid maximum element')