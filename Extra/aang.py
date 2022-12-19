f_aang = int(input())
f_enemies = int(input())
agl_aang = str(input())
agl_enemies = str(input())
acc_aang = float(input())
acc_enemies = float(input())


venceu = "Aang venceu o combate!"
perdeu = "Aang perdeu o combate e agora esta preso na fortaleza da nacao do fogo."

if (f_aang > f_enemies and f_aang != f_enemies): 
    print(venceu)
elif (f_aang < f_enemies):
    print(perdeu)
else:  
    if agl_aang == "Rapido" and agl_aang != agl_enemies:
        print(venceu)
    elif agl_enemies == "Rapido" and agl_enemies != agl_aang:
        print(perdeu)
    else:
        if acc_aang > acc_enemies:
            print (venceu)
        elif acc_aang < acc_enemies:
            print(perdeu)
        else: print(venceu)



    
      
      
      
       

   
