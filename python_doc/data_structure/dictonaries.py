tel = {'jack': 4055, 'sape': 8784}
print(tel)
tel['gudo'] = 2555
print(tel)
print(tel['jack'])

del tel['sape']
print(tel)

tel['irv'] = 4222
print(tel)

print(list(tel.keys()))
print(sorted(tel.keys()))

print('gudo' in tel)
print('jack' in tel)

print(dict([('sape', 568999), ('gudo', 1111), ('jack', 88888)]))

print({x: x**2 for x in {2, 4, 6}})

print(dict(sape=222, gudio=593, jjac=999))
