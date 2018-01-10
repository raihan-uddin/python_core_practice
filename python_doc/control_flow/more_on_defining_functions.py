def hyphen():
    print()
    for i in range(2):
        print("-" * 40)
    print()


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('Invalid user response')
        print(reminder)


# ask_ok('Do you really want to quite?')
# ask_ok('OK to overwrite the file?', 2)
# ask_ok('Ok to overwrite the file?', 2, 'Come on only yes or no')

i = 5


def f(arg=i):
    print(arg)


i = 6
f()


def f(a, l=[]):
    l.append(a)
    return l


print(f(1))
print(f(2))
print(f(3))
#  -----------------------
'''
def f(a, l=None):
    if l is None:
        l = []
    l.append(a)
    return l
print(f(1))
print(f(2))
print(f(3))
'''


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("If you put", voltage, "volts through it.")
    print('-- Lovely plumage, the', type)
    print("-- It's", state)


parrot(1000)  # 1 positional argument
parrot(voltage=1000)  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')  # 2 keyword argument
parrot(action='VOOOOOM', voltage=10000000000)  # 2 keyword argument
parrot('a million', 'bereft of life', 'jump')  # 3 positional argument
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword argument

# invalid call
# parrot() # required argument missing
# parrot(voltage=5.0, 'dead') # no-keyword argument after a keyword argument
# parrot(110, voltage=220) # duplicate value for the same argument
# parrot(actor='noe') # unknown keyword argument

hyphen()


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, '?')
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client='Joe',
           sketch='Cheese shop sketch')

hyphen()


def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


def concat(*args, sep='/'):
    return sep.join(args)


print(concat("earth", "marsh", "venues"))
print(concat("earth", "marsh", "venues", sep='.'))

hyphen()

print(list(range(3, 6)))
args = [3, 6]
print(list(range(*args)))

hyphen()


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print('if you put', voltage, 'volts through it.', end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
