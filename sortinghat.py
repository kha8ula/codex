gryffindor = int(0)
ravenclaw = int(0)
hufflepuff = int(0)
slytherin = int(0)
print('              ===================================')
print('              --- ¿Qué casa de Hogwarts eres? ---')
print('              ===================================')
print('    --- ¡Responde a las siguientes preguntas y AVERÍGUALO! ---')
p1= int(input('1º ¿Qué prefieres, el amanecer o el atardecer?\n 1) Amanecer\n 2) Atardecer\n : '))
if p1 ==1:
    gryffindor += 1
    hufflepuff += 1
elif p1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print('¡Error!')

p2= int(input('2º Cuando muera, quiero que me recuerden como alguien: \n 1) Bueno.\n 2) Grande.\n 3) Mediocre\n 4) Malo\n : '))
if p2== 1:
    hufflepuff += 1
elif p2== 2:
    slytherin += 1
elif p2==3:
    ravenclaw +=1
elif p2== 4:
    gryffindor += 1
else:
    print('¡Error!')

p3 = int(input('3º¿Qué instrumento prefieres?\n 1) El violín.\n 2) La trompeta.\n 3) El piano.\n 4) El tambor.\n :'))
if p3== 1:
    slytherin += 1
elif p3== 2:
    hufflepuff +=1
elif p3== 3:
    ravenclaw+= 1
elif p3==4:
    gryffindor+= 1
else:
    print('¡Error!')
print('¡Enhorabuena tu casa es:')
if gryffindor> hufflepuff and gryffindor>slytherin and gryffindor>ravenclaw:
    print('🦁 Gryffindor!')
elif hufflepuff>gryffindor and hufflepuff>ravenclaw and hufflepuff> slytherin:
    print('🦡 Hufflepuff!')
elif ravenclaw> gryffindor and ravenclaw>hufflepuff and ravenclaw>slytherin:
    print('🦅 Ravenclaw!')
elif slytherin>gryffindor and slytherin>hufflepuff and slytherin>ravenclaw:
    print('🐍 Slytherin!')
else:
    print('Hay un empate, elige tu casa entre: ')
    print('🦁 Gryffindor: ',gryffindor)
    print('🦡 Hufflepuff: ', hufflepuff)
    print('🦅 Ravenclaw: ', ravenclaw)
    print('🐍 Slytherin: ', slytherin)