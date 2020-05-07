a  = 10
print(id(a))
def something():
                  # Or global a      #if you want local variable use in global variable
    a = 9
    x = globals()['a']
    print(id(x))
    print("Inside Function:",a) #we can use global veriable in inside function and result is inside function = 10

    globals()['a'] = 15      #when you want to use local in global


something()
print("Outside Function:",a)
