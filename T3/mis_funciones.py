#funcion NO GENERADORA/FUNCIONES AUXILIARES
# NO Usar for o while en una función no generadora (hace return en vez de yield)

def reduce_acum(diccionario, elemento):
    if elemento.especie not in diccionario: 
        diccionario[elemento.especie] = [1, [elemento.nombre]]
    else: 
        if elemento.nombre not in diccionario[elemento.especie][1]:
            diccionario[elemento.especie][0]+=1
            diccionario[elemento.especie][1].append(elemento.nombre)
    return diccionario #hace return es NO GENERADORA

def reduce_votos(diccionario, elemento):
    if elemento.id_candidato not in diccionario: 
        diccionario[elemento.id_candidato] = [1, [elemento.id_voto]]
    else: 
        diccionario[elemento.id_candidato][0]+=1
        diccionario[elemento.id_candidato][1].append(elemento.id_voto)
    return diccionario #hace return es NO GENERADORA


def reduce_edad(diccionario, elemento):
    if elemento.especie not in diccionario: 
        diccionario[elemento.especie] = [elemento.ponderador]
    return diccionario

def calculo_edad(diccionario, elemento): 
    edad_humana = float(diccionario[elemento.especie][0]) * int(elemento.edad)
    diccionario[elemento.especie].append((elemento.nombre, edad_humana)) 
    return diccionario

#diccionario de votos x especie
def votos_especie(diccionario, elemento):
    #print(elemento)
    if elemento.especie not in diccionario: 
        #id_candidato, su especie y la cantidad de votos que tiene
        diccionario[elemento.especie] = [[elemento.id_candidato], 0]
    else: 
        diccionario[elemento.especie][0].append(elemento.id_candidato)
    return diccionario 

def reduce_distritos(diccionario, elemento):
    if elemento.nombre not in diccionario: 
        diccionario[elemento.nombre] = [[elemento.id_comuna], 0]
    else: 
        diccionario[elemento.nombre][0].append(elemento.id_comuna)
    return diccionario

def dict_distrito(diccionario, elemento):
    informacion = [elemento.nombre, elemento.id_candidato, 0]
    if elemento.id_distrito_postulacion not in diccionario: 
        diccionario[elemento.id_distrito_postulacion] = [informacion]
    else: 
        diccionario[elemento.id_distrito_postulacion].append(informacion)
    return diccionario
#(['Don Pepe', 1, 2], ['Sr. Cortizona', 2, 1])
def obtener_max(elemento):
    #print(list(elemento))
    maximo = max(elemento, key= lambda x: x[2]) 
    if elemento[0][2] == maximo[2] and elemento[1][2] == maximo[2]: 
        return [elemento[0][0], elemento[1][0]]
    elif elemento[0][2] == maximo[2]: 
        return [elemento[0][0]]
    elif elemento[1][2] == maximo[2]: 
        return [elemento[1][0]]
    
def orden_dict(lista, elemento):
    key, info = elemento 
    lista.append((key, info[0], info[1]))
    return lista
#Animal(id=385, nombre="Gay", especie="Tortuga marina", id_comuna=190, peso_kg=288.0, edad=45, fecha_nacimiento="1979/12")
def fechas_nacimiento(lista, elemento): 
    fecha = elemento.fecha_nacimiento #"1979/12"
    fecha = fecha.split('/')
    lista.append([elemento.id,fecha])
    return lista

def filtro_fechas(lista, elemento, fecha_candidato):
    id_animal = elemento[0]
    year = elemento[1][0]
    mes = elemento[1][1]
    if fecha_candidato[0] == year and fecha_candidato[1] == mes: 
        lista.append(id_animal)
    elif fecha_candidato[0] == year: 
        lista.append(id_animal)
    elif fecha_candidato[1] == mes:
        lista.append(id_animal)
    return lista

def promedio_edades(lista_edades):
    suma_edades = sum(lista_edades)
    total_edades = len(lista_edades)
    return suma_edades / total_edades

def comparaciones(simbolo, edad, numero): 
#numero_edad = numero
    cumple= False
    if simbolo == '=': 
        if edad == numero: 
            cumple= True
    elif simbolo == '<': 
        if edad > numero: 
            cumple= True
    elif simbolo == '>':
        if edad < numero: 
            cumple= True
    return cumple 

#Animales = namedtuple('Animales', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])
def lista_inter_candidatos(lista, elemento):
    id_candidato = elemento.id_candidato
    especie = elemento.especie
    info = [id_candidato, especie]
    if info not in lista: 
        lista.append(info)
    return lista
#votos_validos, tiene id_candidato, id_votante
def lista_interespecie(lista, elemento): 
    id_candidato = elemento.id_candidato
    id_votante = elemento.id_animal_votante
    info = [id_votante, id_candidato]
    if info not in lista: 
        lista.append(info)
    return lista

def agregar_votantes(diccionario,elemento, dict_animales):
    #todos los que son de esa especie se guarda en el id del candidato 
    especie_votante = dict_animales.get(elemento.id_animal_votante)
    especie_id = elemento.id_animal_votante
    especie_voto_x = elemento.id_candidato
    if especie_voto_x in diccionario: 
        #revisar si son de la misma especie 
        if diccionario[especie_voto_x][0] == especie_votante: 
            diccionario[especie_voto_x][1].append(especie_id)
    return diccionario


def edades_validas(lista, elemento):
    if len(elemento) > 1: 
        elemento = elemento[1: ] 
        lista.append(elemento)
    return lista

def obtener_ponderado(dicc, especie):
    ponderado = dicc.get(especie)
    return ponderado