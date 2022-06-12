#!/usr/bin/env python
# coding: utf-8

# # Non Graded Challenge 2 - Function
# 
# - Buatlah sebuah function yang dapat mengkonversi suhu dari kelvin ke celcius, dan celcius ke kelvin.
# - Buatlah sebuah function yang dapat mengkonversi suhu ke fahrenheit. Tambahkan parameter untuk memastikan bahwa argumen yang dimasukan adalah celcius atau kelvin. Panggil function yang pertama jika diperlukan.
# - Buatlah sebuah function yang dapat mengkonversi suhu dari fahrenheit. Berikan argumen untuk memastikan bahwa outputnya dalah celcius atau kelvin.
# - Berikan dokumentasi pada setiap baris kode yang kalian tulis.

# ### **Function** yang dapat mengkonversi suhu dari *kelvin* ke *celcius*

# In[ ]:


kelv = int(input("Enter a kelvin degree between 273° and 373°:"))            #entering kelvin degree

def kelvtocels_converter(kelv):                                              #converter function
    if 273 <= kelv <= 373:                                                   #conditioning kelv temp must be in range:
        celsius = kelv - 273                                                 #kelv to cels formula
        print(f'{kelv}° Kelvin = {celsius}° Celsius')                        #print the result
        
    else:                                                                    #else statement if the degrees out of ranges
        print('out of degrees range :\nKelvin scale is marked from 273° to 373° \nwhere 273° K shows the freezing point of water \nand 373° K shows the boiling point of water')

kelvtocels_converter(kelv)                                                   #calling the converter function       


# ### **Function** yang dapat mengkonversi suhu dari *celcius* ke *kelvin*

# In[ ]:


cels = int(input("Enter a celsius degree between 0° and 100°:"))             #entering celsius degree

def celstokelv_converter(cels):                                             #converter function
    if 0 <= cels <= 100:                                                    #conditioning cels temp must be in range:
        kelvin = cels + 273                                                 #cels to kelv formula
        print(f'{cels}° Celsius = {kelvin}° Kelvin')                        #print the result
        
    else:                                                                   #else statement if the degrees out of ranges
        print('out of degrees range :\nCelsius scale is marked from 0° to 100° \nwhere 0° C shows the freezing point of water \nand 100° C shows the boiling point of water')

celstokelv_converter(cels)                                                  #calling the converter function      


# ### **Function** yang dapat mengkonversi suhu ke *Fahrenheit*

# In[ ]:


kelv = int(input("Enter a kelvin degree between 273° and 373°:"))           #entering kelvin degree
cels = int(input("Enter a celsius degree between 0° and 100°:"))            #entering celsius degree

def fahr_converter(kelv,cels):                                              #converter function
    if 273 <= kelv <= 373 and 0 <= cels <= 100:                             #conditioning kelv and cels must be in range
        fahrkelv = ((9/5)*(kelv-273))+32                                    #kelv to fahr formula
        fahrcels = ((9/5)*cels)+32                                          #cels to fahr formula
        print(f'{kelv}° Kelvin = {fahrkelv}° Fahrenheit\n{cels}° Celsius = {fahrcels}° Fahrenheit')     #print the result
        
    else:                                                                   #else statement if the degrees out of ranges
        print('out of degrees range :\nKelvin and Celsius scale is marked from 273° to 373° and 0° to 100° \nwhere 273° K, 0° C shows the freezing point of water \nand 373° K, 100° C shows the boiling point of water')
        
fahr_converter(kelv,cels)                                                   #calling the converter function


# ### **Function** yang dapat mengkonversi suhu dari *Fahrenheit*

# In[ ]:


fahrx = int(input("Enter a fahrenheit degree between 32° and 212°:"))       #entering a fahrenheit degree

def tofahr_converter(fahrx):                                                #converter function
    if 32 <= fahrx <= 212:                                                  #conditioning the degree must be in range
        kelvfahr = ((5/9)*(fahrx-32))+273                                   #fahr to kelv formula
        celsfahr = ((5/9)*(fahrx-32))                                       #fahr to cels formula
        print(f'{fahrx}° Fahrenheit = {kelvfahr}° Kelvin\n{fahrx}° Fahrenheit = {celsfahr}° Celsius')     #print the result
    
    else:                                                                   #else statement if the degrees out of ranges
        print('out of degrees range :\nthe Fahrenheit scale is marked from 32° to 212° where 32° F shows the freezing point of water and 212° F shows the boiling point of water')
        
tofahr_converter(fahrx)                                                     #calling the converter function

