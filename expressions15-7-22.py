Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #EXPRESSIONS IN PYTHON
>>> #ARITHMETIC EXPRESSIONS
>>> a=10
>>> b=20
>>> a+b
30
>>> print(a-b)
-10
>>> print(+a)
10
>>> print(-b)
-20
>>> a+b
30
>>> a-b
-10
>>> a*b
200
>>> a/b
0.5
>>> a%b
10
>>> a**b
100000000000000000000
>>> a//b
0
>>> -2//3
-1
>>> -2//-1
2
>>> #RELATIONAL
>>> a=5
>>> b=3
>>> a==b
False
>>> a!=b
True
>>> a>b
True
>>> a<b
False
>>> a>=b
True
>>> a<=b
False
>>> x=1+2
>>> x==3
True
>>> x=1.1
>>> x=1.2+1.0
>>> x==2.2
True
>>> x=1.1+2.2
>>> x==3
False
>>> x==3.3
False
>>> type(a+b)
<class 'int'>
>>> type(a==b)
<class 'bool'>
>>> #LOGICAL
>>> x=10
>>> y=20
>>> not x=5
SyntaxError: can't assign to operator
>>> not x
False
>>> not x = 5
SyntaxError: can't assign to operator
>>> x<20
True
>>> callable(x)
False
>>> x==5 and x==4
False
>>> x==5 or x==4
False
>>> x==10 or x==4
True
>>> x==10 and x==20
False
>>> #BITWISE OPERATORS
>>> x=100
>>> y=101
>>> x=x+1
>>> print(x)
101
>>> print(x.y)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print(x.y)
AttributeError: 'int' object has no attribute 'y'
>>> print(x,y)
101 101
>>> x==y
True
>>> x ix y
SyntaxError: invalid syntax
>>> x is y
True
>>> id(x)
1852271344
>>> id(y)
1852271344
>>> x is not y
False
>>> a&b
1
>>> a|b
7
>>> a^b
6
>>> a>>b
0
>>> a<<b
40
>>> 
