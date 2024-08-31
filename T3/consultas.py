from typing import Generator
import utilidades #para hacer las namedtuples
from functools import reduce #usar reduce
from os.path import join #crear rutas
import mis_funciones
from itertools import combinations, tee
from collections import Counter
def cargar_datos(tipo_generator: str, tamano: str):
    ruta = join('data', tamano, tipo_generator + '.csv')
    with open(ruta, 'r', encoding='latin-1') as file:
        next(file)
        data = file.readlines()
        if tipo_generator == 'animales':
            for info in data: 
                info = info.strip('\n').split(',')
                id, nombre, especie, id_comuna, peso_kg, edad, nacimiento = (int(info[0]), 
                    info[1], info[2], int(info[3]), float(info[4]), int(info[5]), info[6]
                    )
                yield(utilidades.Animales(id,
                                          nombre,
                                          especie,
                                          id_comuna,
                                          peso_kg,
                                          edad,
                                          nacimiento)
                                          )
        elif tipo_generator == 'candidatos':
            for info in data: 
                info = info.strip('\n').split(',')
                id, nombre, id_postulacion, especie = (int(info[0]), info[1], 
                                                       int(info[2]), info[3]
                                                       )
                yield(utilidades.Candidatos(id, nombre, 
                                            id_postulacion, especie)
                                            )
        elif tipo_generator == 'distritos':
            for info in data: 
                info = info.strip('\n').split(',')
                id, nombre, id_comuna, provincia, region = (
                    int(info[0]), info[1], int(info[2]), info[3], info[4]
                    )
                yield(utilidades.Distritos(id,
                                            nombre, 
                                            id_comuna,
                                            provincia,
                                            region)
                                            )
        elif tipo_generator == 'locales':
            for info in data: 
                info = info.strip('\n').split('[')
                info_1 = info[0].split(',')
                info_list = info[1].strip(']').split(',')
                info_list = [int(i) if i!='' else '' for i in info_list]
                id, nombre_local, id_comuna, id_votantes = (int(info_1[0]), info_1[1], 
                                                            int(info_1[2]), info_list
                                                            )
                yield(utilidades.Locales(id, nombre_local, 
                                         id_comuna, id_votantes)
                                         )
        elif tipo_generator == 'ponderadores':
            for info in data: 
                info = info.strip('\n').split(',')
                especie, ponderador = (info[0], float(info[1]))
                yield(utilidades.Ponderador(especie, ponderador))
        elif tipo_generator == 'votos':
            for info in data: 
                info= info.strip('\n').split(',')
                id_voto, id_animal, id_local, id_candidato = (int(info[0]), int(info[1]), 
                                                              int(info[2]), int(info[3])
                                                              )
                yield(utilidades.Votos(id_voto, id_animal,
                                       id_local, id_candidato)
                                        )
def animales_segun_edad(generador_animales: Generator,
    comparador: str, edad: int) -> Generator:

    if comparador == '>': 
        edad_filtrado = filter(lambda x: x if x.edad > edad else None, generador_animales)
    elif comparador == '<':
        edad_filtrado = filter(lambda x: x if x.edad < edad else None, generador_animales)
    elif comparador == '=':
        edad_filtrado = filter(lambda x: x if x.edad == edad else None, generador_animales)
    for animal in edad_filtrado:
        yield animal.nombre
def animales_que_votaron_por(generador_votos: Generator,
    id_candidato: int) -> Generator:    

    votos_filtrado = filter(lambda x: x if x.id_candidato == id_candidato else None, 
                            generador_votos
                            )
    for animal in votos_filtrado: 
        yield animal.id_animal_votante
def cantidad_votos_candidato(generador_votos: Generator,
    id_candidato: int) -> int:

    resultado_votantes = filter(lambda x: x.id_candidato == id_candidato, generador_votos)
    resultado = sum(1 for i in resultado_votantes)
    return resultado

def ciudades_distritos(generador_distritos: Generator) -> Generator:
    ciudades= map(lambda x: x.provincia, generador_distritos)
    provincias= reduce(lambda x, y: x if y in x else x + [y], ciudades, [])
    for nombre in provincias:
        yield nombre

def especies_postulantes(generador_candidatos: Generator,
    postulantes: int) ->Generator:

    info_especies= reduce(mis_funciones.reduce_acum, generador_candidatos, {})
    for especie, indice in info_especies.items(): 
        if indice[0] >= postulantes: 
            yield especie 

def pares_candidatos(generador_candidatos: Generator) -> Generator:

    selec_nombres = [x.nombre for x in generador_candidatos] 
    selec_nombres = (combinations(selec_nombres, 2))
    for i in selec_nombres:
        yield i
     
def votos_alcalde_en_local(generador_votos: Generator, candidato: int,
    local: int) -> Generator:
    votos_alcalde = filter(lambda x: x if x.id_local == local and x.id_candidato == candidato
                          else None, generador_votos)
    for voto in votos_alcalde: 
        yield voto
def locales_mas_votos_comuna (generador_locales: Generator,
    cantidad_minima_votantes: int, id_comuna: int) -> Generator:

    filtro_id = filter(lambda x: x.id_comuna == id_comuna, generador_locales)
    resultado = filter(lambda x:  x if len(x.id_votantes) >= cantidad_minima_votantes 
                       else None, filtro_id)
    select_id = [x.id_local for x in resultado]
    for id in select_id: 
        yield id

def votos_candidato_mas_votado(generador_votos: Generator) -> Generator:

    info_votos = reduce(mis_funciones.reduce_votos, generador_votos, {})
    resultado = reduce(mis_funciones.orden_dict, info_votos.items(),[])
    maximo = max(resultado, key= lambda x: (x[1],x[0])) 
    for id in maximo[2]: 
        yield id

def animales_segun_edad_humana(generador_animales: Generator,
    generador_ponderadores: Generator, comparador: str,
    edad: int) -> Generator:

    ponderadores = reduce(mis_funciones.reduce_edad, generador_ponderadores, {})
    edades_ordenadas = reduce(mis_funciones.calculo_edad, generador_animales, ponderadores)
    for key, contenido in edades_ordenadas.items(): 
        contenido = contenido[1: ]
        for elemento in contenido:
            edad_humana = elemento[1]
            check = mis_funciones.comparaciones(comparador, edad, edad_humana) 
            if check == True: 
                yield elemento[0] #nombre

def animal_mas_viejo_edad_humana(generador_animales: Generator,
    generador_ponderadores: Generator) -> Generator:

    ponderadores = reduce(mis_funciones.reduce_edad, generador_ponderadores, {})
    edades_ordenadas = reduce(mis_funciones.calculo_edad, generador_animales, ponderadores) 
    edades = edades_ordenadas.values()
    edades = reduce(lambda x, y: x + y, edades, [])
    edades = [x for x in edades if isinstance(x, tuple)]
    edades.sort(key=lambda x: x[1], reverse=True)
    maximo_edades = edades[0][1]
    mas_viejos = [x[0] for x in edades if maximo_edades == x[1]]
    for i in mas_viejos: 
        yield i

def votos_por_especie(generador_candidatos: Generator,
    generador_votos: Generator) -> Generator:

    votos = [i.id_candidato for i in generador_votos]
    info_candidatos = reduce(mis_funciones.votos_especie, generador_candidatos, {})
    for key_cand, info in info_candidatos.items(): 
        id_candidatos = info[0]
        total_votos = sum(voto in id_candidatos for voto in votos)
        info[1] = total_votos
        yield (key_cand, info[1])

def hallar_region(generador_distritos: Generator,
    generador_locales: Generator, id_animal: int) -> str:
    instancia_local = filter(lambda x: x if id_animal in x.id_votantes else None, 
                             generador_locales
                             )
    local = next(instancia_local)
    comuna = local.id_comuna
    instancia_distrito = filter(lambda x: x if x.id_comuna == comuna else None, 
                                generador_distritos
                                )
    distrito = next(instancia_distrito)
    region = distrito.region 
    return region

def max_locales_distrito(generador_distritos: Generator,
    generador_locales: Generator) -> Generator:

    info_distritos = reduce(mis_funciones.reduce_distritos, generador_distritos, {})
    id_comunas = [x.id_comuna for x in generador_locales]
    for key_cand, info in info_distritos.items(): 
        id_locales= info[0]
        total_locales = sum(id in id_locales for id in id_comunas)
        info_distritos[key_cand][1] = total_locales
    info_distritos = info_distritos.items()
    maximo = max(info_distritos, key= lambda x: x[1][1]) 
    empatados = [elemento[0] for elemento in info_distritos if maximo[1][1] == elemento[1][1]]
    for animales in empatados: 
        yield animales

def votaron_por_si_mismos(generador_candidatos: Generator,
    generador_votos: Generator) -> Generator:
    votos_iguales = filter(lambda x: x if x.id_animal_votante == x.id_candidato 
                           else None, generador_votos)
    votos_iguales = [x.id_animal_votante for x in votos_iguales]
    generador_candidatos = (candidato.nombre for candidato in generador_candidatos 
                            if candidato.id_candidato in votos_iguales
                            )
    for candidatos in generador_candidatos: 
        yield candidatos

def ganadores_por_distrito(generador_candidatos: Generator,
    generador_votos: Generator) -> Generator:

    info_distritos = reduce(mis_funciones.dict_distrito, generador_candidatos, {})
    votos = [x.id_candidato for x in generador_votos]
    for key_distrito, info in info_distritos.items(): 
        for i in range(len(info)): 
            id_candidato = info[i][1]
            total_votos = votos.count(id_candidato)
            info[i][2] = total_votos 
        info_distritos[key_distrito] = reduce(
            lambda x: x.sort(key=lambda y: y[2], reverse= True), 
            [()]
            )
        combinaciones = combinations(info, 2)
        info_distritos[key_distrito] = combinaciones
        for comb in info_distritos[key_distrito]: 
            resultado_comb = mis_funciones.obtener_max(comb)
            for candidatos in resultado_comb:
                yield candidatos

def mismo_mes_candidato(generador_animales: Generator,
    generador_candidatos: Generator, generador_votos: Generator,
    id_candidato: str) -> Generator:

    id_candidatos = [x.id_candidato for x in generador_candidatos]
    votaron_por_candidato = filter(lambda x: x if x.id_candidato == id_candidato 
                            and x.id_candidato in id_candidatos else None, generador_votos)
    id_votantes = [x.id_animal_votante for x in votaron_por_candidato]
    dato_animales = [x for x in generador_animales if x.id in id_votantes or x.id == id_candidato]   
    solo_votantes = [x for x in dato_animales if x.id in id_votantes]
    fecha_id_animales = reduce(mis_funciones.fechas_nacimiento, solo_votantes, [])
    dato_candidato = (x for x in dato_animales if x.id == id_candidato)
    dato_candidato = reduce(mis_funciones.fechas_nacimiento, dato_candidato, [])
    if len(dato_candidato) == 0: 
        for i in dato_candidato: 
            yield i
    else: 
        fecha = dato_candidato[0][1]
        fechas_seleccionadas = reduce(lambda lista, elemento: 
                            mis_funciones.filtro_fechas(lista, elemento, fecha), 
                            fecha_id_animales, []
                            )
        for ides in fechas_seleccionadas: 
            yield ides
        
def edad_promedio_humana_voto_comuna(generador_animales: Generator,
    generador_ponderadores: Generator, generador_votos: Generator,
    id_candidato: int, id_comuna:int ) -> float:

    votos_filtrados = filter(lambda x: x if x.id_candidato == id_candidato else None, 
                             generador_votos
                             )
    copia_generador_votos = tee(votos_filtrados, 2)
    copia_votos = copia_generador_votos[0]
    copia_verificadora = copia_generador_votos[1]
    iterador = iter(copia_verificadora)
    primer_elemento = next(iterador, None)
    if primer_elemento is None: 
        return float(0)
    animales_votantes = [animales.id_animal_votante for animales in copia_votos]
    animales_comuna = filter(lambda x: x if x.id in animales_votantes and x.id_comuna == id_comuna
                              else None, generador_animales)
    copia_generador_comunas = tee(animales_comuna, 3)
    copia_comuna = copia_generador_comunas[0]
    copia_verificadora = copia_generador_comunas[1]
    copia_para_ponderar = copia_generador_comunas[2]
    iterador = iter(copia_verificadora)
    primer_elemento = next(iterador, None)
    if primer_elemento is None: 
        return float(0)
    especies = [animales.especie for animales in copia_para_ponderar]
    generador_ponderadores = filter(lambda x: x if x.especie in especies else None, 
                                generador_ponderadores
                                )
    ponderadores = reduce(mis_funciones.reduce_edad, generador_ponderadores, {})
    edades_ordenadas = reduce(mis_funciones.calculo_edad, copia_comuna, ponderadores)
    edades_ordenadas = edades_ordenadas.items()
    edades_ordenadas = [edad[1][1][1] for edad in edades_ordenadas]
    return mis_funciones.promedio_edades(edades_ordenadas)

def votos_interespecie(generador_animales: Generator,
    generador_votos: Generator, generador_candidatos: Generator,
    misma_especie: bool = False,) -> Generator:
    #sufri con esta D:
    id_candidatos = [x.id_candidato for x in generador_candidatos]
    id_votante_candidato = map(lambda x: [x.id_animal_votante, x.id_candidato] if x.id_candidato 
                               in id_candidatos else [x.id_animal_votante, ''], generador_votos)
    dict_animales = {animal.id: animal for animal in generador_animales}
    for info in id_votante_candidato: 
        votante = dict_animales.get(info[0])
        candidato = dict_animales.get(info[1])
        if votante.especie == candidato.especie and misma_especie == True:
            yield votante
        elif votante.especie != candidato.especie and misma_especie == False: 
            yield votante

def porcentaje_apoyo_especie(generador_animales: Generator,
    generador_candidatos: Generator, generador_votos: Generator) -> Generator:
    copia_generador_votos = tee(generador_votos, 2)
    copia_votos = copia_generador_votos[0]
    copia_especies_voto = copia_generador_votos[1]
    dict_animales = {animal.id: animal.especie for animal in generador_animales}
    dict_especies_totales = [dict_animales.get(x.id_animal_votante) for x in copia_especies_voto]
    dict_especies_totales = Counter(dict_especies_totales)
    dict_candidatos = {animal.id_candidato: [animal.especie, []] for animal in generador_candidatos}
    dict_candidatos = reduce(lambda lista, elemento: mis_funciones.agregar_votantes
                             (lista, elemento, dict_animales), copia_votos, dict_candidatos
                             )
    for id_candidato, info in dict_candidatos.items():
        total = dict_especies_totales.get(info[0])
        votos = len(info[1])
        if votos == 0: 
            yield (id_candidato, 0)
        else: 
            porcentaje = (votos / total) * 100
            yield (id_candidato, round(porcentaje))

    dict_animales = {animal.id: animal.especie for animal in generador_animales}
def votos_validos(generador_animales: Generator,
    generador_votos: Generator, generador_ponderadores) -> int:

    dict_ponderador = {animal.especie: animal.ponderador for animal in generador_ponderadores} 
    id_votantes = {x.id_animal_votante: '' for x in generador_votos}
    edades = (x.edad * mis_funciones.obtener_ponderado(dict_ponderador, x.especie) 
              for x in generador_animales if x.id in id_votantes
              )
    edades = filter(lambda x: x if x >= 18 else None, edades)
    suma = sum(1 for x in edades)
    return suma

def cantidad_votos_especie_entre_edades(generador_animales: Generator,
    generador_votos: Generator, generador_ponderador: Generator,
    especie: str, edad_minima: int, edad_maxima: int) -> str:

    ponderador = [x.ponderador for x in generador_ponderador if x.especie == especie]
    if len(ponderador) == 0: 
        texto1 = f'Hubo {0} votos emitidos por animales entre {edad_minima}'
        texto2 = f"y {edad_maxima} años de la especie {especie}."
        return f'{texto1} {texto2}'
    ponderador = ponderador[0]
    dict_animales = {animal.id: (animal.edad * ponderador) for animal in 
                     generador_animales if animal.especie == especie}
    votos_emitidos = filter(lambda x: (x if x.id_animal_votante in dict_animales and
                                    edad_minima < dict_animales[x.id_animal_votante] < edad_maxima 
                                    else None), generador_votos
                                    )
    total = sum(1 for x in votos_emitidos)
    texto1 = f'Hubo {total} votos emitidos por animales entre {edad_minima}'
    texto2 = f"y {edad_maxima} años de la especie {especie}."
    return f'{texto1} {texto2}'

def distrito_mas_votos_especie_bisiesto(generador_animales: Generator,
    generador_votos: Generator, generador_distritos: Generator,
    especie: str) -> str:
    pass

def votos_validos_local(generador_animales: Generator,
    generador_votos: Generator, generador_ponderadores: Generator,
    id_local: int) -> Generator:

    dict_ponderadores = {animal.especie: animal.ponderador for animal in generador_ponderadores}
    filtrar_locales = {x.id_animal_votante: x.id_voto for x in generador_votos 
                       if x.id_local == id_local}
    filter_gen_anim = filter((lambda x: x if x.id in filtrar_locales and 
                              (x.edad * dict_ponderadores[x.especie]) >= 18 else None), 
                              generador_animales
                            )
    for animales in filter_gen_anim:
        voto = filtrar_locales.get(animales.id)
        yield voto

def votantes_validos_por_distritos(generador_animales: Generator,
    generador_distritos: Generator, generador_locales: Generator,
    generador_votos: Generator, generador_ponderadores: Generator) -> Generator:
    # COMPLETAR
    pass































