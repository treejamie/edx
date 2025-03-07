class Foo(object):

    def bar(self, msg):
        print(msg)


x = Foo()

# neat, you can manually feed "selfs". 
# I did not know that.
Foo.bar(x, "hello")
