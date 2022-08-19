Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a= "Hello, welcome to my world."
>>> a.endswith("my world.")
True
>>> txt = "H\te\tl\tl\to"
>>> txt.expandtabs(2)
'H e l l o'
>>> a="H\ti\t \tf\tr\ti\te\tn\td\ts"
>>> a.expandtabs(5)
'H    i         f    r    i    e    n    d    s'
>>> print(a.expandtabs())
H       i               f       r       i       e       n       d       s
>>> print(a.expandtabs(3))
H  i     f  r  i  e  n  d  s
>>> print(a.expandtabs(30))
H                             i                                                           f                             r                             i                             e                             n                             d                             s
>>> print(a.expandtabs(1))
H i   f r i e n d s
>>> a= "Hello, welcome to my world."
>>> a.find("welcome")
7
>>> a.find("H")
0
>>> a.find("o")
4
>>> a="srikakulam123"
>>> a.isalnum()
True
>>> a="iiit srikakulam"
>>> a.isalpha
<built-in method isalpha of str object at 0x033EDD68>
>>> print(a)
iiit srikakulam
>>> a="srikakulam"
>>> a.isalpha
<built-in method isalpha of str object at 0x033EDD40>
>>> a="50800"
>>> a.isdigit()
True
>>> b="hi"
>>> 
KeyboardInterrupt
>>> a.isdigit()
True
>>> b.isdigit
<built-in method isdigit of str object at 0x02B546E0>
>>> b.isdigit()
False
>>> b.isalpha()
True
>>> a="my demo"
>>> b="my document"
>>> c="2python"
>>> a.isidentifier()
False
>>> d.isidentifier()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    d.isidentifier()
NameError: name 'd' is not defined
>>> b.isidentifier()
False
>>> c.isidentifier()
False
>>> d="demo"
>>> d.isidentifier()
True
>>> a="hello world!"
>>> a.islower()
True
>>> a="12345"
>>> a.isnumeric()
True
>>> x="Hello! Are you #1?"
>>> a.printable()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a.printable()
AttributeError: 'str' object has no attribute 'printable'
>>> a.isprintable()
True
>>> "hello/hghfg122334"
'hello/hghfg122334'
>>> y="     "
>>> y.isspace()
True
>>> z="123"
>>> z.isspace()
False
>>> a="Hello, And Welcome To My World!"
>>> a.istitle()
True
>>> b="hello"
>>> a.istitle()
True
>>> c="HELLO, AND WELCOME TO MY WORLD"
>>> b.istitle()
False
>>> c.istitle()
False
>>> a=("hai","how","are","you")
>>> "#".join(a)
'hai#how#are#you'
>>> " ".join(a)
'hai how are you'
>>> "-".join(a)
'hai-how-are-you'
>>> x="hello rguktians how are you"
>>> x.partion(how)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    x.partion(how)
AttributeError: 'str' object has no attribute 'partion'
>>> x.partion("how")
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    x.partion("how")
AttributeError: 'str' object has no attribute 'partion'
>>> x.partition("how")
('hello rguktians ', 'how', ' are you')
>>> a="we all love our IT sir"
>>> a.split()
['we', 'all', 'love', 'our', 'IT', 'sir']
>>> b="we all love our IT sir"
>>> b.splitlines()
['we all love our IT sir']
>>> x="hello\nhow are you"
>>> x.splitlines()
['hello', 'how are you']
>>> a="DonT LoOk at tHe sTaRs,lEt Be oNe"
>>> a.swapcase()
'dONt lOoK AT ThE StArS,LeT bE OnE'
>>> x="dont be afraid to be yourself"
>>> x.title()
'Dont Be Afraid To Be Yourself'
>>> a="50"
>>> a.zfill(10)
'0000000050'
>>> a.zfill(3)
'050'
>>> x="hello world how are you"
>>> x.zfill(10)
'hello world how are you'
>>> x="hello"
>>> x.zfill(10)
'00000hello'
>>> 
