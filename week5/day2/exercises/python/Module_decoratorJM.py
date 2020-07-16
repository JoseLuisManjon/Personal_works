import pandas as pd
from functools import wraps

def prepost(*args, **kwargs):
    def inner(function):
        @wraps(function)
        def wrapper(*a, **k): 
            # antes
            if 'key_url' in kwargs.keys():
                df = pd.read_csv(kwargs['key_url'])
            retval = function(*a, **k)  
            # después
            df.hist()
            print("done")
            return retval
        return wrapper
    return inner

@prepost(key_url='http://winterolympicsmedals.com/medals.csv')
def _f_protected():
    l1 = [elem for elem in range(0,16)]
    c = list(filter(lambda x: True if x > 5 else False, l1))
    return c

_f_protected()

