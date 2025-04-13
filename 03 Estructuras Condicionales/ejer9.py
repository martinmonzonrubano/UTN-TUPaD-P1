mag=int(input("Cual fue la magnitud del terremoto? "))
if mag<3:
    print=("Muy leve")
else:
    if mag<4:
        print("Leve")
    else:
        if mag<5:
            print("Moderado")
        else: 
            if mag<6:
                print("Fuerte")
            else:
                if mag<7:
                    print("Muy fuerte")
                else:
                    print("EXTREMO")

