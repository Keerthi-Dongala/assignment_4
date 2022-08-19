Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello world")
Hello world
>>> a=9
>>> b=7.2
>>> c="Keerthi"
>>> type(a)
<class 'int'>
>>> print(type(b))
<class 'float'>
>>> print(type(c))
<class 'str'>
>>> d="s"
>>> print(type(d))
<class 'str'>
>>> l=[1,2,3,4]
>>> t=(1,2,3)
>>> s=()
>>> s1={1,2,3,4,5}
>>> type(l)
<class 'list'>
>>> type(s)
<class 'tuple'>
>>> type(s1)
<class 'set'>
>>> type(t)
<class 'tuple'>
>>> e={1:"one",2:"two",3:"three"}
>>> print(type(e))
<class 'dict'>
>>> a=10
>>> b=15
>>> c=20
>>> a+b
25
>>> b_a
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    b_a
NameError: name 'b_a' is not defined
>>> b-a
5
>>> b*c
300
>>> d/a
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    d/a
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> c/a
2.0
>>> a%b
10
>>> c%a
0
>>> c%b
5
>>> d=2
>>> a**d
100
>>> a>b
False
>>> a==b
False
>>> c>=a
True
>>> a<b
True
>>> b<=c
True
>>> a>b and a<b
False
>>> a>b or a<c
True
>>>  a not b
 
SyntaxError: unexpected indent
>>> a not b
SyntaxError: invalid syntax
>>> not a
False
>>> f=-2
>>> notf
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    notf
NameError: name 'notf' is not defined
>>> not f
False
>>> not 0
True
>>> not 1
False
>>> not true
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    not true
NameError: name 'true' is not defined
>>> x=12
>>> y=12.0
>>> a+int(b)
25
>>> x+int(y)
24
>>> x+y
24.0
>>> 
