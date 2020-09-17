
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


def gender_to_numeric(x):
    """Funcion que cuenta las filas masculinas o femeninas de un dataframe cuando esto viene indicado 
    por las letras M y F"""
    if x == 'M':
        return 1
    if x == 'F':
        return 0


def fix_century(x):
    """ Funcion que corrige el año de una columna datatime en panda cuando el año de la fecha excede 
    100 años al que deberia ser. El formato de esa columna es año/mes/dia"""
  year = x.year - 100 if x.year > 1989 else x.year
  return datetime.date(year, x.month, x.day)


  le = LabelEncoder()
def encode_columna(columna, encoder):
    """ Función que codifica columnas de un dataframe con valores string y los pasa a integers.
        Se le pasa la columna y el LabelEncoder """
    variety_encoded = encoder.fit_transform(columna)
    variety_encoded = np.array(variety_encoded)
    return variety_encoded