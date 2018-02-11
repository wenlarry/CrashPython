# Class_Python Standard Library

# We can use any function or class in the std lib
#   by including a simple import stat on top of the
#   file

#  Dict allow for connections of pieces of info, but
#     they don't keep track of the order in which 
#     key-value pairs are added
#  We can use the OrderedDict class from the collections
#     module

from collections import OrderedDict

fav_lang = OrderedDict() 

fav_lang['je'] = 'python'
fav_lang['sa'] = 'c'
fav_lang['ed'] = 'ruby'
fav_lang['ph'] = 'python'

for name, lang in fav_lang.items():
    print(name.title() + " 's fav lang is " + lang.title() + ".")


