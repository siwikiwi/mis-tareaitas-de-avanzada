import parametros
import entidades

def validacion_menus(valor, tipo): #validacion menu
    if valor.isdigit() == False: 
        return False
    elif tipo == 'inicio':
        if int(valor) not in [1, 2, 3, 0]: 
            return False 
    elif tipo == 'tienda': 
        if int(valor) not in [1, 2, 3, 4, 5, 6, 7, 0]: 
            return False
    elif tipo =='seleccion de gato': 
        if int(valor) not in [1, 2, 3]: 
            return False
        
def verificar_formato(lista, tipo_ejercito): 
    #revisa que el formato sea el correcto
    formato = True
    if len(lista) != 7: 
        print('numero de atributos incorrecto')
        print('Formato incorrecto')
        formato = False
        return formato 
    if not(isinstance(lista[0], str)) and not(isinstance(lista[1], not str)): 
        print('no entrega string en los primeros dos atributos')
        print('Formato incorrecto')
        formato = False
        return formato 
    if tipo_ejercito == 'enemigo':
        if lista[1] not in ['GUE', 'CAB', 'MAG', 'PAL', 'CAR', 'MDB']: 
            print('clase de gato que no existe')
            print('Formato incorrecto')
            formato = False
            return formato 
    if tipo_ejercito == 'dcc_combatientes':
        if lista[1] not in ['GUE', 'CAB', 'MAG']: 
            print('clase de gato que no existe')
            print('Formato incorrecto')
            formato = False
            return formato 
    for i in lista[2:]: #reviso que los atributos despues del tipo sean valores enteros
        if i.isdigit() == False:
            print('numero no entero')
            return False


    #revisa que los valores cumplan el rango
    #se revisa en clase caballero, porque da igual en cual revise, simplemente quiero checkear que los valores esten en los rangos
    #indicados, y esto es una caracteristica compartida por todas las clases...
    combatiente= entidades.Caballero(
        str(lista[0]),
        str(lista[1]),
        int(lista[2]),
        int(lista[3]),
        int(lista[4]),
        int(lista[5]),
        int(lista[6]))
    
    combatiente.vida_maxima = int(lista[2])
    combatiente.defensa = int(lista[3])
    combatiente.poder = int(lista[4])
    combatiente.agilidad = int(lista[5])
    combatiente.resistencia = int(lista[6])
    

    if combatiente.crear_instancia == True: 
        return True, [lista[0],
                      lista[1],
                      int(lista[2]),
                      int(lista[3]),
                      int(lista[4]),
                      int(lista[5]),
                      int(lista[6])]
    else: 
        print('los parametros entregados son incorrectos')
        return False

def crear_instancia(datos): 
    tipo = datos[1]
    if tipo == 'GUE': 
        datos[1] = 'Guerrero'
        combatiente = entidades.Guerrero(*datos)
        return combatiente
        #crea instancia guerrero
    elif tipo == 'CAB':
        datos[1] = 'Caballero'
        combatiente = entidades.Caballero(*datos)
        return combatiente
        #crea instancia caballero 
    elif tipo == 'MAG':
        #crea instancia mago 
        datos[1] = 'Mago'
        combatiente = entidades.Mago(*datos)
        return combatiente
    elif tipo == 'PAL': 
        datos[1] = 'Paladin'
        #crea instancia paladin
        combatiente = entidades.Paladin(*datos)
        return combatiente
    elif tipo == 'CAR':
        datos[1] = 'Caballero Arcano'
        combatiente = entidades.CaballeroArcano(*datos)
        return combatiente
    elif tipo == 'MDB': 
        datos[1] = 'Mago de Batalla'
        combatiente = entidades.MagoDeBatalla(*datos)
        return combatiente

    
def validacion_archivo(info_gatos, tipo_ejercito): #validar el archivo cargado 
    rondas_diccionario = {'ronda 1':[], 'ronda 2':[], 'ronda 3': []}
    info_gatos =  [i.split(';') for i in info_gatos]

    if len(info_gatos) != 3: 
        print('No cumple con la cantidad de rondas')
        return False
    else:
        for i in range(3): 
            #esto ordena la informacion, para poder verificar si estan bien los datos
            info_gatos[i] = [j.strip('\n').split(',') for j in info_gatos[i]]
            for j in range(len(info_gatos[i])):
                verificar_combatiente = verificar_formato(info_gatos[i][j], tipo_ejercito)
                if verificar_combatiente == False:
                    return False
                else:
                    rondas_diccionario[f'ronda {i+1}'].extend([verificar_combatiente[1]])

    rondas_diccionario['ronda 1'] = [crear_instancia(i) for i in rondas_diccionario['ronda 1']]
    rondas_diccionario['ronda 2'] = [crear_instancia(i) for i in rondas_diccionario['ronda 2']]
    rondas_diccionario['ronda 3'] = [crear_instancia(i) for i in rondas_diccionario['ronda 3']]
    return(rondas_diccionario)


def validacion_unidades(info_unidades): #validar unidades.txt
    gatos_disponibles = {'MAG':[], 'GUE':[], 'CAB':[]}
    for i in range(len(info_unidades)):
        info_unidades[i] = info_unidades[i].strip('\n').split(',')
        verificando_unidad = verificar_formato(info_unidades[i],'dcc_combatientes')
        if verificando_unidad == False:
            print('error al cargar unidades de dcc_combatientes')
            return False
        else: 
            info_unidades[i] = verificando_unidad[1]
    for unidades in info_unidades:
        if unidades[1] == 'MAG':
            gatos_disponibles['MAG'].extend([unidades])
        elif unidades[1] == 'GUE':
            gatos_disponibles['GUE'].extend([unidades])
        elif unidades[1] == 'CAB':
            gatos_disponibles['CAB'].extend([unidades])
    gatos_disponibles['GUE'] = [ crear_instancia(i)for i in gatos_disponibles['GUE']]
    gatos_disponibles['MAG'] = [ crear_instancia(i)for i in gatos_disponibles['MAG']]
    gatos_disponibles['CAB'] = [ crear_instancia(i)for i in gatos_disponibles['CAB']]
    return(gatos_disponibles)

def diccionario_items(ejercito):
    indice = 0
    diccionario = {'GUE':[], 'MAG':[], 'CAB':[]}
    for combatiente in ejercito:
        if isinstance(combatiente, entidades.Guerrero):
            diccionario['GUE'].extend([['Guerrero', indice]])
        elif isinstance(combatiente, entidades.Mago):
            diccionario['MAG'].extend([['Mago', indice]])
        elif isinstance(combatiente, entidades.Caballero):
            diccionario['CAB'].extend([['Caballero', indice]])
        indice+=1
    return diccionario

#ayuda al menu seleccion gato, resulta mas eficiente, para que indique el indice del combatiente a evolucionar 
def gatito_prime(informacion_gatos, item, ejercito_dcc): 
    opciones = []
    etiquetas = ['Tipo', 'Nombre']
    print(f'{etiquetas[0]:23} {etiquetas[1]}')
    for indice, elementos in enumerate(informacion_gatos):
        combatiente = ejercito_dcc.combatientes[elementos[1]]
        opciones.append((indice+1,elementos[1]))
        print(f'{[indice+1]} {elementos[0]:20} - {combatiente.nombre}')

    opcion = input('Indique su opción: ' )
    total_opciones = [i+1 for i in range(len(opciones))] #[0, 1, 2, 3]
    if opcion.isdigit() == False: 
        print('Ingresa una opcion valida')
        return False
    if opcion.isdigit() == True:   
        if int(opcion) not in total_opciones:
            print('Ingresa una opcion valida')
            return False
        else: 
            #[(0, 0), (1, 2), (2, 1), (3, 3)]
            for tupla_info in opciones: 
                if tupla_info[0] == int(opcion): 
                    combatiente = ejercito_dcc.combatientes[tupla_info[1]]
                    print(f"Evolucionar a {combatiente.nombre}, con {item}")
                    return (tupla_info[1]) #retorna el indice del combatiente en la lista del ejercito y la opcion de item



