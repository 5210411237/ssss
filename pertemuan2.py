Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
str='aku cinta indonesia'
print(str)
aku cinta indonesia
str=str[:10]+'tanah airku'+str[9:]
print(str)
aku cinta tanah airku indonesia
kelas='praktikum pemrograman berorientasi objek'
up=kelas.upper()
lo=kelas.lower()
print(kelas)
praktikum pemrograman berorientasi objek
print(Up)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(Up)
NameError: name 'Up' is not defined. Did you mean: 'up'?
print(up)
PRAKTIKUM PEMROGRAMAN BERORIENTASI OBJEK
print(lo)
praktikum pemrograman berorientasi objek

s='     python     "
SyntaxError: unterminated string literal (detected at line 1)
s='     python     '
s.strip()
'python'
s
'     python     '
print(kelas)
praktikum pemrograman berorientasi objek
s.strip()
'python'
s.strip()
'python'
s.rstrip()
'     python'
len(kelas)
40
jumlah=len(kelas)
print('panjang string adalah : ',jumlah)
panjang string adalah :  40
s1='python'
s2='pemrograman'
s1+s2
'pythonpemrograman'
kelas
'praktikum pemrograman berorientasi objek'
print(kelas.index('a'))
2
kelas2=kelas.replace('praktikum','praktik')
print(kelas2)
praktik pemrograman berorientasi objek
a='satu'
b='dua'
c='tiga'
print('saya membuat %s mangga'%(c))
saya membuat tiga mangga
kelas2
'praktik pemrograman berorientasi objek'
kelas2.split()
['praktik', 'pemrograman', 'berorientasi', 'objek']
input=('hari ini adalah : ')
hari ini adalah: rabu
SyntaxError: invalid syntax
kelas2
'praktik pemrograman berorientasi objek'
kelas2.split()
['praktik', 'pemrograman', 'berorientasi', 'objek']
input('hari ini adalah: ')
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    input('hari ini adalah: ')
TypeError: 'str' object is not callable
 input('hari ini adalah: ')
 
SyntaxError: unexpected indent

data1=input('angka 1: ')
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    data1=input('angka 1: ')
TypeError: 'str' object is not callable
data1=input('angka 2: ')
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    data1=input('angka 2: ')
TypeError: 'str' object is not callable
list=[0,1,2,3,4,5,6,7,8,9]

print(list)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list[4])
4
print(list[:4])
[0, 1, 2, 3]
len(list)
10
print(list[10-3:])
[7, 8, 9]
print(list[2:9])
[2, 3, 4, 5, 6, 7, 8]
print(list[-10])
0
list.append(10)
list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list.insert(1,11)
list
[0, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2=['halo']
list.extend(list2)
list
[0, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'halo']
list.extend('hai')
list
[0, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'halo', 'h', 'a', 'i']
del list[3]
list
[0, 11, 1, 3, 4, 5, 6, 7, 8, 9, 10, 'halo', 'h', 'a', 'i']
list.remove(10)
list
[0, 11, 1, 3, 4, 5, 6, 7, 8, 9, 'halo', 'h', 'a', 'i']
list.pop()
'i'
list
[0, 11, 1, 3, 4, 5, 6, 7, 8, 9, 'halo', 'h', 'a']
list.pop(2)
1
list
[0, 11, 3, 4, 5, 6, 7, 8, 9, 'halo', 'h', 'a']
a=[30,20,10,50,40,]
b=sorted(a)
b
[10, 20, 30, 40, 50]
a.sort()
a
[10, 20, 30, 40, 50]
a.sort(reverse=True)
a
[50, 40, 30, 20, 10]
min(a)
10
max(a)
50
d={1:100,2:200,3:300,4:400,5:500}
d
{1: 100, 2: 200, 3: 300, 4: 400, 5: 500}
d[2]
200
d.get(4)
400
d.keys()
dict_keys([1, 2, 3, 4, 5])
d.values()
dict_values([100, 200, 300, 400, 500])
del d[1]
d
{2: 200, 3: 300, 4: 400, 5: 500}
b=d.copy()
b
{2: 200, 3: 300, 4: 400, 5: 500}
d.clear()
d
{}
len(d)
0
t=100,200,300,400)
SyntaxError: unmatched ')'
t=(100,200,300,400)
t
(100, 200, 300, 400)
t[0]
100
t[3]
400
t.index(200)
1
t
(100, 200, 300, 400)
t2=(10,20,10,30,10,40)
t.count(10)
0
t2.count(20)
1
t2.count(10)
3
t.count(30)
0
t2.count(30)
