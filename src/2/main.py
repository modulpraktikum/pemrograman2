#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 06:07:42 2019

@author: awangga
"""
#import ngitung


a=100
b=50
# In[]: ini contoh variabel list
c=['anu','crot','gede','kecil','5an']

print(c[0]+c[2])

c.append('ngos ngosan')

baru=c.pop()
c.insert(2,'banget')

# In[]: dictionary

a={
	 'nama' : 'jajang',
	 'kelas': 'C'
	 }

namamu=a['nama']

# In[]: input 

nama=input()
print(nama)

# In[]: perulangan

NPM = '113040087'

for c in NPM:
	print(c)
	

# In[]: kondisi

NPM = '113040087'
isinya = NPM[3:5]
if NPM[3:5] == '04':
	print('angkatan 2004')
else:
	print('bukan angkatan 2004')
	

# In[]: try except
	
NPM = 113040087

try:
	anu = NPM+' INI NPM'
except:
	anu = str(NPM)+' INI NPM'




