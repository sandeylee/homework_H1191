Python 3.7.0a2 (v3.7.0a2:f7ac4fe52a, Oct 16 2017, 21:11:18) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
#3.1
>>> years_list = [1972,1973,1974,1975,1976]
>>> years_list
[1972, 1973, 1974, 1975, 1976]
>>> #3.2
>>> years_list[3]
1975
>>> #3.3
>>> years_list[-1]
1976
>>> 
#3.4
>>> things = ['mozzarella','cin derella','salmonella']
>>> things
['mozzarella', 'cin derella', 'salmonella']
>>> 
>>> #3.5
>>> a=things[1]
>>> b=a[0].upper()
>>> b += a[1:]
>>> b
'Cin derella'
>>> things[1] = b
>>> things
['mozzarella', 'Cin derella', 'salmonella']
>>> #3.6
>>> a=things[0]
>>> a
'mozzarella'
>>> a=a.upper()
>>> a
'MOZZARELLA'
>>> things[0] = a
>>> things
['MOZZARELLA', 'Cin derella', 'salmonella']
>>> #3.7
>>> del things[-1]
>>> things
['MOZZARELLA', 'Cin derella']
>>> things.insert(2,'Nobel Prize')
>>> things
['MOZZARELLA', 'Cin derella', 'Nobel Prize']
>>> #3.8
>>> surprise=['Groucho','Chico','Harpo']
>>> surprise
['Groucho', 'Chico', 'Harpo']
>>> #3.9
>>> a=surprise[-1]
>>> a=a.lower()
>>> a=a[::-1]
>>> a
'oprah'
>>> b=a[0].upper()
>>> b += a[1:]
>>> b
'Oprah'
>>> surprise[-1] = b
>>> surprise
['Groucho', 'Chico', 'Oprah']
>>> #3.10
>>> e2f = {'dog':'chien','cat':'chat','walrus':'morse'}
>>> e2f
{'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
>>> #3.11
>>> e2f['walrus']
'morse'
>>> #3.12
>>> a,b,c = e2f.keys()
>>> A,B,C = e2f.values()
>>> f2e = {A:a, B:b, C:c}
>>> f2e
{'chien': 'dog', 'chat': 'cat', 'morse': 'walrus'}
>>> #3.13
>>> f2e['chien']
'dog'
>>> #3.14
>>> set(e2f.keys())
{'dog', 'walrus', 'cat'}
>>> #3.15
>>> life={'animals':{'cat':{'Henri','Grumpy','Lucy'},'octopi':{},'emus':{}},'plants':{},'other':{}}
>>> life
{'animals': {'cat': {'Henri', 'Grumpy', 'Lucy'}, 'octopi': {}, 'emus': {}}, 'plants': {}, 'other': {}}
>>> #3.16
>>> life.keys()
dict_keys(['animals', 'plants', 'other'])
>>> #3.17
>>> life['animals'].keys()
dict_keys(['cat', 'octopi', 'emus'])
>>> #3.18
>>> life['animals']['cat']
{'Henri', 'Grumpy', 'Lucy'}
>>> 
