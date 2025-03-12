

class Human(object):

    def __init__(self, *args, **kwargs):
        print("human")


class Student(Human):

    def __init__(self, *args, **kwargs):
        print("student")
        super(Student, self).__init__(*args, **kwargs)



s = Student()


print(s)