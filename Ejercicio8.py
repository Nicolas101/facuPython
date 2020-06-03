print('Ingresa una palabra')
word = (input().lower()) 
c_word = set(word)
primos = []

for letra in c_word :
    cant = 0
    for i in word :
        if letra == i :
            cant += 1  

    print('La letra '+letra.upper()+' aparece '+str(cant)+' veces')

    if cant < 2 :
        es_primo = False
    for j in range(2, cant) :
        if cant % j == 0 :
            es_primo = False
        es_primo = True

    if es_primo :
        primos.append((letra, cant))


print('Primos =',primos)