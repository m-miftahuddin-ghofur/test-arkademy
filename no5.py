def buyNoodle(tgl,uang) :

    mie = 2500
    dapat = uang / mie
    bojil = dapat // 3
    bonap = dapat // 4 

    if tgl % 5 == 0 and bojil % 2 == 0 :
        total = dapat + bojil*10
        print(total)
    elif tgl % 5 == 0 and bojil % 2 == 1 :
        total = dapat + bojil*5
        print(total)
    elif tgl%2 ==1 :
        total = dapat + bojil
        print(total)
    elif tgl%2 ==0 :
        total = dapat + bonap
        print(total)
    elif tgl % 5 == 0 and bojil % 2 ==0 :
        total = dapat + bojil*10
        print(total)
        
buyNoodle(25,50000)
