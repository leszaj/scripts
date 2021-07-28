

def rozpakowywanie(pierwszy, drugi, trzeci):
    print(pierwszy)
    print(drugi)
    print(trzeci) 


lista_argumentow = [1,3,5] 
rozpakowywanie(*lista_argumentow) 


"""

    # same as:
    rozpakowywanie(lista_argumentow[0], lista_argumentow[1], lista_argumentow[2])
    
"""
