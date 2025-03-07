"""
OK, so the course calls for you to learn to read code by reading code.

I'm not doing that strictly. I've been using this file to step through code and to
learn about how I expect code to run vs how it does.

Also, you know, time. The chances of my death increase each day.

"""

def normalize(numbers):
    max_number = max(numbers)
    assert(max_number != 0), "Cannot divide by 0"
    for i in range(len(numbers)):
        numbers[i]  /= float(max_number)
        assert(0.0 <= numbers[i] <= 1.0), "output not between 0 and 1"
    return numbers        
        