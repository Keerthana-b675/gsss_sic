capitals = ['panjim','bhubanewar','guwahati','aizwal','imphal','agartala','ganktok','kohima','itanagar','shilong']

print(capitals[1:7]) #default from begin to one before end
print(capitals[2:8:2]) #default from begin to end and default increment of 1
#print(capitals[10]) #index error
print(capitals[1:17]) #there is no indexerror in slicing
print(capitals[3:2]) #empty list
print(capitals[3:3]) 
print(capitals[3:2:-1])
print(capitals[::3]) #strt from begin and end at last but increment of 3 at each
print(capitals[-11]) #indexerror becoxz there is no 11 elements 
print(capitals[-10]) #panjim which is the 1st element in the list with 10 elements
print(capitals[::-1])


