
def mean_visualization():
    """ Draw the mean in a plot """
    return None

def get_inputs():
    """ Insert things, test if is insede de range. In the case the word or number were out of the range, 
    the funtion is going to ask again til we will do correctly"""
    word = input("Elige una palabra:")
    n_max = len(word)
    number = int(input("Elige un numero entre 1 y " + str(n_max) + ":"))
    if number > n_max:
        print("El número elegido debe ser menor o igual a la cantidad de letras que forman la palabra elegida")
        word, number, n_max = get_inputs()
        return word, number, n_max
    else:
        return word, number, n_max
    
    x, y, z = get_inputs()


def eliminate_duplicates(lista):
    """Elimina elementos duplicados de una lista """
    set_no_duplicates = set(lista)
    lista_no_duplicates = list(set_no_duplicates)
    return lista_no_duplicates

z = eliminate_duplicates(lista=lista_ejer)
print(z)

