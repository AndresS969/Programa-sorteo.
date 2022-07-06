# Programa-sorteo.
programa básico de un sorteo . 
import random
 
 
cantidad = int(input("introduzca cantidad total de su compra: "))
print()

if cantidad<100:
    print("USTED NO TIENE DESCUENTO, NO PUEDE PARTICIPAR")
    print()
    print(f"SU PRECIO A PAGAR ES: {cantidad}")
    pass
        
    
if cantidad>=100:
    print("USTED TIENE DESCUENTO, PUEDE PARTICPAR EN EN LA RIFA!")
    
    
    print()
    print("SU GASTO IGUALA O SUPER LOS $100.00 Y POR LO TANTO PARTICIPA EN LA PROMOCION!")
    print()
    print("\t\tCOLOR")  
    print("\t\tBOLA BLANCA")
    print("\t\tBOLA ROJA")
    print("\t\tBOLA AZUL")
    print("\t\tBOLA VERDE")
    print("\t\tBOLA AMARILLA")
    print()
    print("\t\tDESCUENTO")
    print("\t\tBOLA BLANCA = NO TIENE DESCUENTO") 
    print("\t\tBOLA ROJA TIENE UN DESCUENTO DE 10%")
    print("\t\tBOLA AZUL TIENE UN DESCUENTO DE 20%")
    print("\t\tBOLA VERDE TIENE UN DESCUENTO DE 25%")
    print("\t\tBOLA AMARILLA TIENE UN DESCUENTO DE 50%")
    print()



    rifa = random.randint(1,5)
if rifa==1:
    print("ALEATORIAMENTE USTED OBTUVO LA BOLA BLANCA, NO SE APPLICA DESCUENTO, GRACIAS POR JUGAR")
    
elif rifa==2:
    print("ALEATORIAMENTE USTED OBTUVO LA BOLA ROJA,TIENE UN DESCUENTO DE 10%")
    descuento = cantidad * 0.10
    print()
    print("USTED DEBERA PAGAR:", cantidad - descuento)

elif rifa==3:
    print("ALEATORIAMENTE USTED OBTUVO LA BOLA AZUL,TIENE UN DESCUENTO DE 20%")
    descuento = cantidad * 0.20
    print()
    print("USTED DEBERA PAGAR:", cantidad - descuento)
    

elif rifa==4:
    print("ALEATORIAMENTE USTED OBTUVO LA BOLA VERDE,TIENE UN DESCUENTO DE 25%")
    descuento = cantidad * 0.25
    print()
    print("USTED DEBERA PAGAR:", cantidad - descuento)
    
elif rifa==5:
    print("ALEATORIAMENTE USTED OBTUVO LA BOLA AMARILLA,TIENE UN DESCUENTO DE 50%")
    descuento = cantidad * 0.50
    print()
    print("USTED DEBERA PAGAR: ", cantidad - descuento)
