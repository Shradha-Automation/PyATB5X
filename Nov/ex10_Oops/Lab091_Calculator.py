class Calc:
    def __init__(self):
        print('DC')

        def sum(self,a,b):
            return a+b
        def sub(self,a,b):
            return a-b
        def mul(self,a,b):
            return a*b
        def dev(self,a,b):
            return a/b
object_ref=Calc()
a=float(input("Enter the value of a\n"))
b=float(input("Enter the value of b\n"))
object_sum=object_ref.sum(a,b)
object_sub=object_ref.sub(a,b)
object_mul=object_ref.mul(a,b)
object_div=object_ref.div(a,b)
print(object_sum,object_sub,object_mul,object_div)


