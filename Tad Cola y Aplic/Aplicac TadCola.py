import TadCola

from TadCola import *

c=crearCola()
caux=crearCola()

print ("Carga datos en la cola")
for i in range (1,5):
    elem=input()
    encolar(c,elem)

#Imprime la Cola original   
print ("Imprime los datos de la cola")
for i in range (0, tamanio(c)):
    elem=desencolar(c)
    encolar(caux,elem)
    print (elem)
    
#Ojo!! para imprimir la cola hay que ir recuperando los datos pero para probar
#Prueba no hacer, muestra que quedo la cola original vacia y la auxiliar con datos
print ("cola original y auxiliar")
print (c)
print (caux)

#pasamos los datos de la cola auxiliar a la original
copiarCola(c,caux)
print ("cola original y auxiliar despues del copiarcola")
#Prueba no hacer, muestra que quedo la cola original tiene los datos y la auxiliar esta vacia
print (c)
print (caux)
