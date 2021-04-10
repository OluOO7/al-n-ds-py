'''Function below converts an integer 
to a string any base from 2 to 16.'''

def to_string(n, base):
    base_sys = "0123456789ABCDEF"

    if (n < base):
        return base_sys[n]
    else:
        return to_string(n // base, base) + base_sys[n % base]
print(to_string(10, 2))