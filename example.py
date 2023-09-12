# import json
# from urllib.request import urlopen

# class Setting(object):
#     def __init__(self, url):
#         with urlopen(url) as content:
#             self.config = json.load(content)
#             print("in init")    
    
#     def __call__(self, value):
#         print(value)
#         return self.config[value]

    
# settings = Setting("https://bit.ly/3ippyXa")
# db = settings("db")

# list = ['a','b','c']
dict = {'number':'1',
        'greek':'alpha',
        "alphabeth":["cn","jp"]
}

def listing (dict,**kwargs):
    alphabeth = dict.get('alphabeth')
    l = {}
    fn = lambda kwargs: lis(alphabeth, kwargs)
    # if alphabeth is not None:
    #     l = kwargs
    #     # for alpha in alphabeth:
    #     #     l[alpha] = kwargs[alpha]
    
    return fn(kwargs)

def lis(alphabeth,arg):
    l = {}
    if alphabeth is not None:
        # l = arg
        for alpha in alphabeth:
            l[alpha] = arg[alpha]
    print(l)

l = listing(dict,cn = "4",jp = "ri")




# define two methods
 
# second method that will be returned
# by first method
# def B(st2):
#     print("Good " + st2 + ".")
     
# # first method that return second method
# def A(st1):
#     print(st1 + " and ")
     
#     # return second method
#     return B
 
# # call first method that do two work:
# # 1. execute the body of first method, and
# # 2. execute the body of second method as
# #    first method return the second method
# A("Hello")('morning')

# fn = lambda x: x*2

# a = fn(2)
# print(a)
# from typing import Dict

# callback: Dict[str, function] = {}

# fn = lambda x : x*2

# callback["name"] = fn

# print(callback)