def lyrics_generator(lista):
    lista_aux = ""
    cont = 0 
    for beat in lista:
        if beat == 0:
            lista_aux = lista_aux + "Boom "
        else:
            cont += 1
            lista_aux = lista_aux + "Drop the bass "
            if cont == 3:
                lista_aux = lista_aux + "!!!Break the bass!!! "
    return lista_aux

# Your code above, nothing to change after this line
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))



