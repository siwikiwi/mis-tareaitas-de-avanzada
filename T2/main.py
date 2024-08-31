from sys import exit, argv
from random import choice
import parametros
import funcionalidades
import entidades
import os
def main():
    ronda_actual = ejercito_dcc.ronda
    while True: 
        print('***Menu de inicio***\n')
        print(f'Dinero disponible: {ejercito_dcc.oro}')
        print(f'Ronda actual: {ronda_actual} \n') 
        print(f'¿Qué quieres hacer?')
        print(f'[1] Tienda\n[2] Ejercito\n[3] Combatir\n')
        print(f'[0] Salir del programa')
        opcion = input('Indique su opción: ' )

        if funcionalidades.validacion_menus(opcion, 'inicio') == False: 
            print('ERROR Indica una opcion correcta\n')
        elif int(opcion) == 0: 
            print('Seleccionaste: Salir del programa')
            exit(0)
        elif int(opcion) == 1: 
            menu_tienda()
            #abrir tienda
        elif int(opcion) == 2: 
            print(ejercito_dcc)
            #print a la clase ejercito para que se presente
        elif int(opcion) == 3: 
            resultado_combate = ejercito_dcc.combatir()
            if  resultado_combate == True: 
                #sumamos a la siguiente ronda
                ronda_actual+=1
                ejercito_dcc.oro+=parametros.ORO_GANADO
                if ronda_actual == 4: 
                    print('☺ ☺ ☺ ☺ ☺')
                    print('VICTORIAAA!!!!')
                    print('㏊㏊㏊㏊㏊')
                    exit(0)
            elif resultado_combate == None: 
                print('Compra ejercito antes :v')
            elif resultado_combate == False:
                exit(0)

        
        
def menu_tienda(): 
    while True: 
        print('***Tienda***\n')
        print(f'Dinero disponible: {ejercito_dcc.oro}\n')
        print(f'¿Qué quieres hacer?\n')
        elementos_tienda = [
            ['[1] Gato Mago', parametros.PRECIO_MAG], 
            ['[2] Gato Guerrero', parametros.PRECIO_GUE],
            ['[3] Gato Caballero', parametros.PRECIO_CAB],
            ['[4] Ítem Armadura', parametros.PRECIO_ARMADURA],
            ['[5] Ítem Pergamino', parametros.PRECIO_PERGAMINO],
            ['[6] Ítem Lanza', parametros.PRECIO_LANZA],
            ['[7] Curar Ejercito', parametros.PRECIO_CURA]
            ]
        etiquetas = ['Producto', 'Precio']
        print(f'{etiquetas[0]:20} {etiquetas[1]}')
        for elementos in elementos_tienda:
            print(f'{elementos[0]:20} - {elementos[1]}')
        print('[0] Volver al Menu de inicio\n')

        opcion = input('Indique su opción: ' )
        if funcionalidades.validacion_menus(opcion,'tienda') == False: 
            print('ERROR Indica una opcion correcta\n')
        elif int(opcion) == 0: 
            print('Seleccionaste: Volver al Menu de inicio')
            main()

        elif int(opcion) == 1: #comprar gato mago
            gatos_magos = gatos_tienda['MAG']
            precio_mago = parametros.PRECIO_MAG
            if len(gatos_magos) != 0: #si hay disponibles para comprar 
                #c compra
                if precio_mago <= ejercito_dcc.oro:
                    ejercito_dcc._oro-=(precio_mago) #actualiza la cantidad de oro
                    add_combatiente = choice(gatos_magos) #selecciona un gato al azar
                    ejercito_dcc.agregar_combatiente(add_combatiente) #lo agrega al ejercito
                    gatos_magos.remove(add_combatiente) #lo elimina de las opciones disponibles
                    print('Compra exitosa!')
                else: 
                    print('buuhh!!')
                    print('No tienes plata suficiente!!')
            else:
                print('ops..')
                print('No hay gatos magos disponibles')
        elif int(opcion) == 2: #comprar gato guerrero
            gatos_guerreros = gatos_tienda['GUE']
            precio_guerrero = parametros.PRECIO_GUE
            if len(gatos_guerreros) != 0: #si hay disponibles para comprar 
                #c compra
                if precio_guerrero <= ejercito_dcc.oro:
                    ejercito_dcc._oro-=(precio_guerrero) #actualiza la cantidad de oro
                    add_combatiente = choice(gatos_guerreros) #selecciona un gato al azar
                    ejercito_dcc.agregar_combatiente(add_combatiente) #lo agrega al ejercito
                    gatos_guerreros.remove(add_combatiente) #lo elimina de las opciones disponibles
                    print('Compra exitosa!')
                else: 
                    print('buuhh!!')
                    print('No tienes plata suficiente!!')
            else:
                print('ops..')
                print('No hay gatos guerreros disponibles')
            
        elif int(opcion) == 3: #comprar gato caballero
            gatos_caballeros = gatos_tienda['CAB']
            precio_caballero = parametros.PRECIO_CAB
            if len(gatos_caballeros) != 0: #si hay disponibles para comprar 
                #c compra
                if precio_caballero <= ejercito_dcc.oro:
                    ejercito_dcc._oro-=(precio_caballero) #actualiza la cantidad de oro
                    add_combatiente = choice(gatos_caballeros) #selecciona un gato al azar
                    ejercito_dcc.agregar_combatiente(add_combatiente) #lo agrega al ejercito
                    gatos_caballeros.remove(add_combatiente) #lo elimina de las opciones disponibles
                    print('Compra exitosa!')
                else: 
                    print('buuhh!!')
                    print('No tienes plata suficiente!!')
            else:
                print('ops..')
                print('No hay gatos caballeros disponibles')
        elif int(opcion) == 4: #comprar armadura
            informacion_gatos = funcionalidades.diccionario_items(ejercito_dcc.combatientes)
            gatos_armadura = informacion_gatos['MAG'] + informacion_gatos['GUE']
            if parametros.PRECIO_ARMADURA <= ejercito_dcc.oro:
                if len(gatos_armadura) == 0:
                    print('No hay gatos para evolucionar con armadura')
                else:
                    menu_seleccion_de_gato(gatos_armadura,'armadura', int(opcion))
            else:
                print('Oppps...')
                print('No tienes plata suficiente :v')
            
            #[['Mago', 0], ['Mago', 1], ['Guerrero', 2]]
        elif int(opcion) == 5: #comprar pergamino
            informacion_gatos = funcionalidades.diccionario_items(ejercito_dcc.combatientes)
            gatos_pergamino = informacion_gatos['GUE'] + informacion_gatos['CAB']
            if parametros.PRECIO_PERGAMINO <= ejercito_dcc.oro: 
                if len(gatos_pergamino) == 0: 
                    print('No hay gatos para evolucionar con pergamino')
                else:
                    menu_seleccion_de_gato(gatos_pergamino,'pergamino',int(opcion))
                    
            else: 
                print('Oppps...')
                print('No tienes plata suficiente :v')
        elif int(opcion) == 6: #comprar lanza
            informacion_gatos = funcionalidades.diccionario_items(ejercito_dcc.combatientes)
            gatos_lanza = informacion_gatos['MAG'] + informacion_gatos['CAB']
            if parametros.PRECIO_LANZA <= ejercito_dcc.oro: 
                if len(gatos_lanza) == 0: 
                    print('No hay gatos para evolucionar con lanza')
                else:
                    menu_seleccion_de_gato(gatos_lanza, 'lanza',int(opcion))
            else:
                print('Oppps...')
                print('No tienes plata suficiente :v')


        elif int(opcion) == 7: #curar ejercito
            print('Llegan los curitas gatito...')
            if ejercito_dcc.oro >= parametros.PRECIO_CURA: 
                #se actualiza el precio del oro
                ejercito_dcc.oro-=parametros.PRECIO_CURA
                print('wololooo')
                for combatientes in ejercito_dcc.combatientes:
                    combatientes.vida+= parametros.CURAR_VIDA
            else: 
                print("No hay plata")
                print("los curitas se retiran...")
                


def menu_seleccion_de_gato(informacion_gatos, item,opcion):
    print('*** Selecciona un gato ***')
    indice = funcionalidades.gatito_prime(informacion_gatos, item, ejercito_dcc)
    if opcion == 4: #eligio armadura 
        ejercito_dcc.oro-= parametros.PRECIO_ARMADURA
        item = entidades.Item(ejercito_dcc.combatientes, indice)
        nuevo_ejercito = item.armadura()
        ejercito_dcc.combatientes = nuevo_ejercito

    elif opcion == 5: #eligio pergamino 
        ejercito_dcc.oro-= parametros.PRECIO_PERGAMINO
        item = entidades.Item(ejercito_dcc.combatientes, indice)
        nuevo_ejercito = item.pergamino()
        ejercito_dcc.combatientes = nuevo_ejercito

    elif opcion == 6: #eligio lanza
        ejercito_dcc.oro-= parametros.PRECIO_LANZA
        item = entidades.Item(ejercito_dcc.combatientes, indice)
        nuevo_ejercito = item.lanza()
        ejercito_dcc.combatientes = nuevo_ejercito
    print('saliending..')



if __name__ == "__main__":
    dificultad = argv 
    if len(dificultad) == 2: 
        dificultad = dificultad[1]
        file = dificultad + '.txt'
        print('Bienvenido a DCCcombatientes')
        lista_enemigos = os.listdir("data")
        if file not in lista_enemigos:
            print('La dificultad no es válida')
        else: 
            print(f'Dificultad DCCcombatientes: {dificultad}')
            ruta_enemigos = os.path.join("data", file)
            with open (ruta_enemigos, "rt") as archivo:
                data = archivo.readlines()
            combatientes_enemigos = funcionalidades.validacion_archivo(data, 'enemigo')
            if combatientes_enemigos == False: 
                print('Los archivos cargados tienen errores')
            else: 
                print('archivos cargados correctamente')
                print('creando combatientes enemigos...\n')
                print("Preparando el entorno...")
                ejercito_dcc = entidades.Ejercito()
                ejercito_dcc.oro = parametros.ORO_INICIAL
                ###cargar unidades disponibles como diccionario
                ruta_unidades= os.path.join("data", 'unidades.txt')
                with open (ruta_unidades, "rt") as archivo:
                    data = archivo.readlines()
                gatos_tienda = funcionalidades.validacion_unidades(data)
                if gatos_tienda != False:
                    print('Cargando unidades disponibles...')
                    ejercito_dcc.enemigos = combatientes_enemigos
                    print('TODO LISTO!\n')
                    main()

    else: 
        print('Los parámetros entregados son incorrectos')

