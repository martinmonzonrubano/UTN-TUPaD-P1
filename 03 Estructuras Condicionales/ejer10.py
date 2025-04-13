hem=input("En que hemisferio se encuentra, Norte o Sur: ")
mes=int(input("Que numero de mes es? "))
dia=int(input("Que numero de dia es? "))
hem=hem.lower()
if hem == "norte":
    if (mes == 12 and dia > 20) or mes==1 or mes==2 or (mes == 3 and dia < 21):
        print("Se encuentra en invierno")
    else:
        if (mes==3 and dia>=21) or mes==4 or mes==5 or (mes==6 and dia<21):
            print("Se encuentra en primavera")
        else:
            if (mes==6 and dia>=21) or mes==7 or mes==8 or (mes==9 and dia<21):
                print("Se encuentra en verano")
            else:
                print("Se encuentra en otoño")


    
elif hem == "sur":
    if (mes == 12 and dia > 20) or mes==1 or mes==2 or (mes == 3 and dia < 21):
        print("Se encuentra en verano")
    else:
        if (mes==3 and dia>=21) or mes==4 or mes==5 or (mes==6 and dia<21):
            print("Se encuentra en otoño")
        else:
            if (mes==6 and dia>=21) or mes==7 or mes==8 or (mes==9 and dia<21):
                print("Se encuentra en invierno")
            else:
                print("Se encuentra en primavera")
    
    


