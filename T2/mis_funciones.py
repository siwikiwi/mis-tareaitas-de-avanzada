import entidades
def duelo(combatiente1, combatiente2):
    while True: 
        ataque_combatiente1 = combatiente1.atacar(combatiente2)
        ataque_combatiente2 = combatiente2.atacar(combatiente1)
        print(f"Atacan a {combatiente1.nombre} con {ataque_combatiente2}")
        print(f"Atacan a {combatiente2.nombre} con {ataque_combatiente1}")
        combatiente1.vida-=ataque_combatiente2
        combatiente2.vida-=ataque_combatiente1
        texto1 = f'Vida de {combatiente1.nombre}: {combatiente1.vida}'
        texto2 = f'Vida de {combatiente2.nombre}: {combatiente2.vida}'
        print(f'{texto1} - {texto2}')
        if combatiente2.vida == 0 or combatiente1.vida == 0: 
            break

def pelea_recursiva(mis_combatientes, enemigos): 
    nombres_combatientes = [i.nombre for i in mis_combatientes]
    nombres_enemigos = [i.nombre for i in enemigos]
    print(f'{nombres_combatientes} V/S {nombres_enemigos}')
    if len(mis_combatientes) == 0 and len(enemigos) == 0:
        return 'empate'
    elif len(mis_combatientes) == 0: 
        return 'Gana el enemigo'
    elif len(enemigos) == 0:
        return 'Somos victoriosos!' 
    else: 
        print("Seleccionando a los duelistas")
        duelista1 = mis_combatientes[-1]
        duelista2 = enemigos[0]
        print(f'{duelista1.tipo}       {duelista2.tipo}')
        print(f'{duelista1.nombre}  *V/S* {duelista2.nombre}')
        duelo(duelista1, duelista2)
        if duelista1.vida == duelista2.vida: #es un empate de duelo
            print("Duelo empatado! :o")
            mis_combatientes.pop(-1)
            enemigos.pop(0)
        elif duelista1.vida == 0: 
            print(f'Ganador: {duelista2.nombre}!')
            mis_combatientes.pop(-1)
        elif duelista2.vida == 0: 
            print(f'Ganador: {duelista1.nombre}!')
            enemigos.pop(0)
        return pelea_recursiva(mis_combatientes,enemigos)
 




