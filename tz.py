import pytz
print('country_names =')
di={}
d2={}
for key, val in pytz.country_names.items():
    print(key, '=', val, end=',')
    di[key]=val
    d2[val]=key
print('\n')
print('IN full name =', pytz.country_names['IN'])
print (d2)