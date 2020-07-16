from functools import wraps

def prepost(key_url):
    def inner(function):
        @wraps(function)
        def wrapper(*a, **k): 
            # antes
            if key_url:
                df = pd.read_csv('http://winterolympicsmedals.com/medals.csv')
            retval = function(*a, **k)  
            # después
            df.hist()
            return retval
        return wrapper
    return inner

@prepost(key_url='http://winterolympicsmedals.com/medals.csv')
def _f_protected():
    l1 = [elem for elem in range(0,16)]
    c = list(filter(lambda x: True if x > 5 else False, l1))
    return c
_f_protected()
