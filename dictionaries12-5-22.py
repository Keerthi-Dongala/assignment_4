Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d={}
>>> type(d)
<class 'dict'>
>>> d={"name":"kittu","rno":32}
>>> len(d)
2
>>> type(d)
<class 'dict'>
>>> d["rno"]=1
>>> print(d)
{'name': 'kittu', 'rno': 1}
>>> d["contact"]=123456789
>>> print(d)
{'name': 'kittu', 'rno': 1, 'contact': 123456789}
>>> len(d)
3
>>> del (d["rno"])
>>> print(d)
{'name': 'kittu', 'contact': 123456789}
>>> d.pop("name")
'kittu'
>>> print(d)
{'contact': 123456789}
>>> d["id"]=S180532
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d["id"]=S180532
NameError: name 'S180532' is not defined
>>> d["id"]="S180532"
>>> d["branch"]="CSE"
>>> d["prend"]="neeru"
>>> d["frnd"]="hasee"
>>> print(d)
{'contact': 123456789, 'id': 'S180532', 'branch': 'CSE', 'prend': 'neeru', 'frnd': 'hasee'}
>>> d.popitem()
('frnd', 'hasee')
>>> d.keys()
dict_keys(['contact', 'id', 'branch', 'prend'])
>>> d.values()
dict_values([123456789, 'S180532', 'CSE', 'neeru'])
>>> d.items()
dict_items([('contact', 123456789), ('id', 'S180532'), ('branch', 'CSE'), ('prend', 'neeru')])
>>> d.get(d["prend"])
>>> d.get("prend")
'neeru'
>>> del(d["contact"])
>>> print(d)
{'id': 'S180532', 'branch': 'CSE', 'prend': 'neeru'}
>>> d["id"]
'S180532'
>>> 
