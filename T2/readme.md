# Tarea 2: DCCombatientes 🐈⚔️

### Cosas implementadas y no implementadas :white_check_mark: :x:

**QUÉ SE REALIZO DETALLADAMENTE EN CADA ITEM:**

#### Programación Orientada a Objetos: 12 pts (10%)
##### ✅ Definición de clases, herencia y *properties*
    - Todas las clases están contenidas en el módulo entidades 
    - Clase Ejercito: 

        **Atributos**
        - Se encarga de contabilizar las rondas 
        - Se encarga de mantener la cantidad de oro adecuada mediante property
        - Contiene al ejército combatiente
        - Contiene el ejército enemigo 

        **Métodos**
        - Capacidad de agregar combatientes
        - Simular el combate
        -Imprimir información del ejército

    - Clase Combatiente (abstracta): 

        **Atributos**
        - Los descritos en la tarea y en el mismo modulo entidades
        - Se manejan los atributos mediante propertys para mantener los valores adecuados

        **Métodos**
        - atacar (abstractmethod, pues depende del ataque y defensa del enemigo)
        - curarse
        -evolucionar 
        -capacidad de imprimir su información

    - Clase Item: 

        **Atributos**
        - ejercito actual
        - indice del gato a evolucionar en el ejercito

        **Métodos**
        - uno por cada item, todos hacen lo mismo: 
            - Verifica si el gato tiene la capacidad de adquirir el item
            - gatilla el metodo evolucionar, de la clase evolucionar
            - elimina el combatiente, para agregar su versión actualizada al ejercito 
            - retorna una lista con el ejercito actualizado, segun la modificación requerida 

    - Clases especializadas: 
        - Clase Guerrero
        - Clase Caballero
        - Mago
        - Paladin
        - Mago de Batalla
        - Caballero arcano


#### Preparación del programa: 10 pts (8%)
##### ✅ Inicio de la partida
- Argumento desde la consola: Primero, se utiliza argv para recibir el nombre de la dificultad a ejecutar. 
- Se verifica que el largo sea el adecuado
- Se genera una lista con los nombres de los archivos en la carpeta data, para verificar si lo ingresado existe 
- Se abre el archivo ingresado, aquí ocupo la funcion validacion_archivo() del modulo funcionalidades: 
- Se crea la instancia ejercito_dcc y se cargan los enemigos extraidos 
    - Mencionar que, cuando se carga el ejercito, estos quedan ordenados en un diccionario, que se describe como {ronda_1: [contenido], ronda2: [contenido], ronda3: [contenido]}
- Si se cargan correctamente, se carga el ejercito propio desde unidades (descrito como gatos_tienda, porque en este punto aun no existe un ejercito, pues no se ha comprado nada), ocupandose también la funcion validacion_archivo(). 
    - Mencionar que gatos tienda, es un diccionario donde estan los gatos ordenados por categoria {MAG: [contenido], GUE: [contenido], CAB: [contenido]
- Si todo carga correctamente abre main()

#### Entidades: 56 pts (47%)
##### ✅ Ejército
##### ✅ Combatientes
##### ✅ Ítems


#### Flujo del programa: 30 pts (25%)

##### ✅ Menú de Inicio - main()

- Se agregan las opciones pedidas por el enunciado
- Se ocupa validacion_menus del funcionalidades, aqui se tienen las opciones correctas y si no se colocan bien, vuelve a preguntar la opcion
- Se agregan todas las opciones correspondientes, se sale del menu de inicio, cuando se marca la opcion 0 y además cuando el resultado del combate es negativo (consideré negativo que quedaran en empate, pues si quedan empate es porque ambos ejercitos quedan vacíos)

##### ✅ Menú Tienda - menu_tienda()
- Se agregan las opciones pedidas por el enunciado
- Se vuelve a opcupar validacion_menus del funcionalidades, pues tiene lo descrito anteriormente. 
- Descripcion de cuando se compran gatos: 
    - Primero, se selecciona la categoria del gato a comprar en gatos_tienda: Se revisa si existe un gato de la categoria y además si es que alcanza el dinero. 
    - Si no anterior no falla, se descuenta el dinero, y se agrega un gato al azar al ejercito usando choice() de random, luego el gato seleccionado se remueve de los gatos disponibles en la tienda 
- Descripcion de comprar items: 
    - Se ocupa la funcion creada diccionario_items del modulo funcionalidades, este crea un diccionario con los gatos existentes en el ejercito, para luego seleccionar aquellos que pueden adquirir el item definido en el formato gato_'el item que se desea' (ejemplo gatos_armadura), si se tiene el oro suficiente, se verifica que existan gatos para adquirir el item. 
    - Si hay gatos disponibles, se abre el menu_seleccion_gato()
##### ✅ Selección de gato - menu_seleccion_gato() 
- Mencionar que recibe los argumentos, ya ordenados de los gatos que reciben el item seleccionado, esto viene dado desde el menu_tienda, en la parte de comprar items. 
- Se genera con la funcion gatito_prime de funcionalidades, como ya están ordenados los gatos, es fácil ordenar, pues: 
    - Primero se genera un total de opciones del estilo [(posible opcion seleccionada, su posicion en la lista), (1, 2), (2, 1), (3, 3)]
    - Posterior, seleccionada una opcion, se busca en la lista generada anteriormente, y se retorna el indice del gato
    - Seleccionado el gato, el menu tienda, trae como argumento opcion, que viene desde el menu tienda, entonces se sabe según este valor, qué item se equipa el gato. 
    - Seleccionado el item y al gato que se quiere evolucionar, se descuenta el dinero, y se crea la instancia Item desde el modulo entidades.
    - Descripcion de Item (en la parte de entidades)
    - Se selecciona item.'item correspondiente'(ejemplo: item.armadura ()) que entrega un ejercito actualizado, y se actualiza el ejercito_dcc.combatientes (la lista de los combatientes en la clase ejercito)
##### ✅ Fin del Juego
    - El juego termina, si quedan empates
    - Si el enemigo gana alguna ronda
##### ✅ Robustez

#### Archivos: 12 pts (10%)
##### ✅ Archivos .txt
    - Todos los archivos, son abiertos desde main()
    - Limpiados con las funciones en funcionalidades(), que se encargan de: 
        - Verificar el formato correcto
        - Verificar que no excedan los parametros 
        - Generar diccionarios con la información a utilizar
##### ✅ parametros.py
    - Se describen los valores de las probabilidades en enteros, pues luego son divididos entre 100, en cada una de las fórmulas
    - Las constantes, se describen según la tarea. 

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se deben cargar:
1. ```entidades.py``` en ```carpeta T2```
2. ```funcionalidades.py``` en ```T2```
3. ```parametros.py``` en ```carpeta T2```
4. ```mis_funciones.py``` en ```T2```
5. ```entidades.py``` en ```carpeta T2```
2. ```archivos mencionados en la tares (dificultades y unidades)``` en ```Carpeta Data```

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```sys```: ```función() / exit, argv```
2. ```random```: ```función() / choice, randint``` 
3. ```os```: ```función() / path.join```
4. ```abc```: ```función() / ABC, abstractmethod``` 


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:
1. ```main.py```: Es el modulo principal para ejecutar la tarea
2. ```entidades.py```: Contiene a ```Clases:  Ejercito, Combatiente, Item, y Tipos de combatientes```
3. ```funcionalidades.py```: Hecha para <Validacion de menus, genera diccionarios para poder cargar los archivos enemigos desde archivos''-dificultad-.txt'' y mis unidades desde ''unidades.txt''>
4. ```parametros.py```: Hecha para <los valores de probabilidades, precios, etc (lo especificado en la tarea 2 )>

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <El empate no es victoria 1, pues ninguno queda con ejercito/a> 
