

# argv + arg
def parametr_args(argument, *args):
    print("zawartość args: {}".format(args))
    print("argument nazwany: {}".format(argument))
    for arg in args:
        print("argument z *args: {}".format(arg))

        
# kwargs + arg
def parametr_kwargs(argument, **kwargs): 
    print("argument: {}".format(argument))
    print("zawartość kwargs: {}".format(kwargs))  # zawartość kwargs: {'dodatkowy': 48, 'nastepny': 111}
    
parametr_args('python', 'spam', 'eggs', 'test')
parametr_kwargs(dodatkowy=48, nastepny=111, argument=12) # argument: 12 


# argv
def myFun(*argv):
    for arg in argv:
        print (arg)
   
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


# argv + arg
def myFun(arg1, *argv):
    print ("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)
 
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

 
# kwargs
def myFun(**kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))

myFun(first ='Geeks', mid ='for', last='Geeks')   


# kwargs + arg
def myFun(arg1, **kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))
 
myFun("Hi", first ='Geeks', mid ='for', last='Geeks')   


# Now we can use *args or **kwargs to
# pass arguments to this function :
def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
     
args = ("Geeks", "for", "Geeks")
myFun(*args)
kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"}
myFun(**kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
def myFun(*args,**kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)

myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks")

