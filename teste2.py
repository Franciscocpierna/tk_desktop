'''
#for n in range(0, 7):
    globals()['strg%s' % n] = 'Hello'
# strg0 = 'Hello', strg1 = 'Hello' ... strg6 = 'Hello'

for x in range(0, 7):
    globals()[f"variable1{x}"] = f"Hello the variable number {x}!"


print(variable15)
'''


name = 'Elon'
exec("%s = %s" % (name,"100"))
Elon = "maria"
print(type(name))
print(Elon)