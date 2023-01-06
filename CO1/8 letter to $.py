a=input('enter a string with o:')
print(str(a))
o='$'
res=a.replace(a[0],o).replace(o, a[0],1)
print(str(res))


