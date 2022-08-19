Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x="I love DSP"
>>> len(x)
10
>>> max(x)
'v'
>>> min(x)
' '
>>> y="sailu"
>>> x+y
'I love DSPsailu'
>>> y*2
'sailusailu'
>>> capitalize(y)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    capitalize(y)
NameError: name 'capitalize' is not defined
>>> y.capitalize()
'Sailu'
>>> upper(x)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    upper(x)
NameError: name 'upper' is not defined
>>> x.upper()
'I LOVE DSP'
>>> z="KEERTHI"
>>> z.lower()
'keerthi'
>>> x.swapcase()
'i LOVE dsp'
>>> x.slice[1:4]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x.slice[1:4]
AttributeError: 'str' object has no attribute 'slice'
>>> x[1:4]
' lo'
>>> 
