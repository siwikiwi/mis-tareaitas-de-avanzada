from abc import ABC, abstractmethod
from random import random, randint
import parametros
from mis_funciones import pelea_recursiva
class Ejercito: 
    ronda = 1 #dice en que ronda vamos 
    #tambien ayuda para abrir el diccionario de enemigos
    #porque estan guardadas en las key
    def __init__(self) -> None:
        self.combatientes = [] #todos los combatientes que posee el ejercito 
        self._oro = 0 #oro disponible para usar en la tienda 
        self.enemigos = []
    @property
    def oro(self):
        return self._oro
    @oro.setter
    def oro (self, cantidad_oro): #MODIFICAR ORO CUANDO SE COMPRE, VERIFICAR QUE ME ALCANZA 
        if cantidad_oro < 0: 
            self._oro = 0
        else:
            self._oro = cantidad_oro
    def agregar_combatiente(self, nuevo_combatiente):
        self.combatientes.append(nuevo_combatiente)
#{'ronda 1': [<entidades.Caballero object at 0x000001D6A76E5BD0>,
    def combatir(self): 
        if len(self.combatientes) == 0: 
            return None
        else: 
            #manejar los enfrentamientos entre combatientes 
            print(f'\nInicio de la ronda: {self.ronda}')
            print(f'Formacion de Batalla!')
            enemigos = self.enemigos[f'ronda {self.ronda}'] #DATOS RONDA 1 ENEMIGOS
            resutado = pelea_recursiva(self.combatientes, enemigos)
            if resutado == 'Somos victoriosos!':
                print('Somos victoriosos!' )
                print(':v')
                self.ronda+=1
                return True 
            elif resutado == 'Gana el enemigo': 
                print('Victoria enemiga chicos')
                print(':ccccc')
                return False 
            elif resutado == 'empate':
                print('Derrotamos a gatochico')
                print('Pero morimos en el intento')
                print('mirada de las mil yardas:\n')
                print('(⊙ _ ⊙ )')
                return False

    def __str__(self) -> str:
        print(f'\n*** Este es tu Ejército Actual ***\n')
        if len(self.combatientes) != 0: 
            presentarse = ''
            for combatientes in self.combatientes:
                presentarse+= str(combatientes) + '\n'
            return presentarse
        else:
            return('Ejercito vacio >:c')

#CLASE ABSTRACTA COMBATIENTE 

class Combatiente(ABC): 
    crear_instancia = True
    def __init__(self, nombre, tipo, vida_maxima, defensa, poder, agilidad, resistencia) -> None:
        self.nombre = nombre 
        self._tipo = tipo
        self._vida_maxima = vida_maxima
        self._vida = vida_maxima #vida actual
        self._defensa = defensa
        self._poder = poder
        self._agilidad = agilidad
        self._resistencia = resistencia
    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self, nuevo_tipo):
        self._tipo = nuevo_tipo
    #  VIDA MAXIMA
    @property 
    def vida_maxima(self):
        return self._vida_maxima 
    @vida_maxima.setter
    def vida_maxima(self, valor_max_vida):
        if  0 <= valor_max_vida <= 100:
            self._vida_maxima = valor_max_vida
        else:
            self.crear_instancia = False

    #VIDA
    @property
    def vida(self):
        return self._vida
    @vida.setter
    def vida(self,valor_vida):
        if  0 <= valor_vida <= self._vida_maxima: 
            self._vida = valor_vida
        if valor_vida < 0:
            self._vida = 0
    @property
    def poder(self):
        return int(self._poder)
    @poder.setter
    def poder(self, valor_poder):
        if  1 <= valor_poder <= 10:
            self._poder = valor_poder
        else:

            self.crear_instancia = False
            
    #DEFENSA
    @property
    def defensa(self):
        return int(self._defensa)
    @defensa.setter
    def defensa(self,valor_defensa):
        if  1 <= valor_defensa <= 20:
            self._defensa = valor_defensa
        else:

            self.crear_instancia = False
            
    #AGILIDAD
    @property
    def agilidad(self):
        return int(self._agilidad)
    @agilidad.setter
    def agilidad(self, valor_agilidad):
        if  1 <= valor_agilidad <= 10:
            self._agilidad = valor_agilidad
        else:

            self.crear_instancia = False
            
    #RESISTENCIA
    @property
    def resistencia(self):
        return int(self._resistencia)
    @resistencia.setter
    def resistencia(self, valor_resistencia):
        if  1<= valor_resistencia <= 10:
            self._resistencia = valor_resistencia
        else:

            self.crear_instancia = False
            
    #ATAQUE
    @property
    def ataque(self): #el dmg que puede producir el combatiente
        primer_valor = (self._poder + self._agilidad + self._resistencia)
        segundo_valor = ((2*self._vida)/self._vida_maxima)
        return round(primer_valor * segundo_valor ) 
    @abstractmethod
    def atacar(self, enemigo): # DEPENDE DEL ATAQUE Y DEFENSA DEL ENEMIGO
        pass
    def curarse(self, valor): 
        self.vida = self._vida + valor
    def evolucionar(self):
        pass 
    def __str__(self) -> str:
        return f'¡Hola! Soy {self.nombre}, un Gato {self.tipo} con {self._vida} / {self._vida_maxima} de vida, {self.ataque} de ataque y {self._defensa} de defensa.'




class Item: 
    def __init__(self,ejercito,indice):
        self.ejercito = ejercito
        self.indice = indice
    def pergamino(self):
        combatiente = self.ejercito[self.indice]
        if combatiente.tipo == 'Guerrero' or combatiente.tipo == 'Caballero': 
            nuevo_combatiente = combatiente.evolucionar('pergamino')
            self.ejercito[self.indice] = nuevo_combatiente
        return self.ejercito
    def lanza(self):
        combatiente = self.ejercito[self.indice]
        if combatiente.tipo == 'Mago' or combatiente.tipo == 'Caballero': 
            nuevo_combatiente = combatiente.evolucionar('lanza')
            self.ejercito[self.indice] = nuevo_combatiente
        return self.ejercito
    def armadura(self):
        combatiente = self.ejercito[self.indice]
        if combatiente.tipo == 'Mago' or combatiente.tipo == 'Guerrero': 
            nuevo_combatiente = combatiente.evolucionar('armadura')
            self.ejercito[self.indice] = nuevo_combatiente
        return self.ejercito
#TIPOS DE COMBATIENTES 

#CLASE GUERRERO 
class Guerrero(Combatiente):
    def __init__(self, nombre, tipo, vida_maxima, defensa, poder, agilidad, resistencia) -> None:
        super().__init__(nombre, tipo, vida_maxima, defensa, poder, agilidad, resistencia)

    def atacar(self, enemigo):
        ataque_default = self.ataque
        dmg = round(ataque_default - enemigo.defensa)
        self.agilidad = self.agilidad - ((parametros.CANSANCIO/100) * self.agilidad)
        if dmg < 1: 
            return 1
        else:
            return int(dmg)
    def evolucionar(self, item):
        print('Evolucionado... miaumiauuu')
        if item == 'pergamino':
            self.tipo = 'Mago De Batalla'
            return MagoDeBatalla(
                self.nombre,
                self.tipo,
                self.vida_maxima,
                self.defensa,
                self.poder,
                self.agilidad,
                self.resistencia)
        elif item == 'armadura':
            self.tipo = 'Paladin'
            return Paladin(
                self.nombre,
                self.tipo,
                self.vida_maxima,
                self.defensa,
                self.poder,
                self.agilidad,
                self.resistencia)


#CLASE CABALLERO 
class Caballero(Combatiente):
    def __init__(self, nombre, tipo, vida_maxima, defensa, poder, agilidad, resistencia) -> None:
        super().__init__(nombre, tipo, vida_maxima, defensa, poder, agilidad, resistencia)
    def atacar(self, enemigo):
        dmg = 1
        ataque_default = self.ataque
        if random() < (parametros.PROB_CABALLERO/100):
            #reduce el poder en red_cab 
            enemigo.poder = enemigo.poder - ((parametros.RED_CAB/100) * enemigo.poder)
            #ataca con la formula de da;o caballero
            dmg = (ataque_default * (parametros.ATQ_CAB/100) - enemigo.defensa)
        else:
            #su dmg se calcula como la del guerrero
            dmg = (ataque_default - enemigo.defensa) 
        #disminucion de resistencia: 
        self.resistencia = self.resistencia - (self.resistencia * (parametros.CANSANCIO/100))
        if dmg < 1: 
            return 1
        else:
            return int(dmg)
    def evolucionar(self, item):
        print('Evolucionado... miaumiauuu')
        if item == 'pergamino':
            self.tipo = 'Caballero Arcano'
            return CaballeroArcano(
                self.nombre,
                self.tipo,
                self.vida_maxima,
                self.defensa,
                self.poder,
                self.agilidad,
                self.resistencia)
        elif item == 'lanza': 
            self.tipo = 'Paladin'
            return Paladin(
                self.nombre,
                self.tipo,
                self.vida_maxima,
                self.defensa,
                self.poder,
                self.agilidad,
                self.resistencia)
        

#CLASE MAGO 
class Mago(Combatiente):
    def __init__(self, nombre, tipo, vida_maxima, defensa, poder, agilidad, resistencia) -> None:
        super().__init__(nombre, tipo, vida_maxima, defensa, poder, agilidad, resistencia)
    def atacar(self, enemigo):
        dmg = 1
        ataque_default = self.ataque
        if random() < (parametros.PROB_MAG/100):
            #ignora un % de la defensa del enemigo
            defensa = enemigo.defensa - (enemigo.defensa * (parametros.RED_MAG/100))
            valor = ((100 - parametros.RED_MAG)/100)
            dmg = round(ataque_default - (parametros.ATQ_MAG/100) - defensa * valor)
            
        else: 
            #su da;o se calcula como el de un guerrero 
            dmg = round(ataque_default - enemigo.defensa) 
        self.resistencia = self.resistencia - (self.resistencia * (parametros.CANSANCIO/100))
        self.agilidad = self.agilidad - (self.agilidad * (parametros.CANSANCIO/100))
        if dmg < 1: 
            return 1
        else:
            return int(dmg)
    def evolucionar(self, item):
        print('Evolucionado... miaumiauuu')
        if item == 'lanza':
            self.tipo = 'Mago de Batalla'
            return MagoDeBatalla(
                self.nombre,
                self.tipo,
                self.vida_maxima,
                self.defensa,
                self.poder,
                self.agilidad,
                self.resistencia)
        elif item == 'armadura': 
            self.tipo = 'Caballero Arcano'
            return CaballeroArcano(
                self.nombre,
                self.tipo,
                self.vida_maxima,
                self.defensa,
                self.poder,
                self.agilidad,
                self.resistencia)

#CLASE PALADIN 
class Paladin(Caballero,Guerrero): 
    def __init__(self, nombre, tipo, vida_maxima, defensa, poder, agilidad, resistencia) -> None:
        super().__init__(nombre, tipo, vida_maxima, defensa, poder, agilidad, resistencia)
        super().__init__(nombre, tipo, vida_maxima, defensa, poder, agilidad, resistencia)
    def atacar(self, enemigo):
        dmg = 1
        if random() < parametros.PROB_PAL:
            dmg = Caballero.atacar(self,enemigo)
        else: 
            dmg = Guerrero.atacar(self,enemigo)
        self.resistencia= self.resistencia + ((parametros.AUM_PAL/100) * self.resistencia)

        if dmg < 1: 
            return 1
        else:
            return int(dmg)


#CLASE MAGO DE BATALLA 
class MagoDeBatalla(Mago,Guerrero):
    def __init__(self, nombre, tipo, vida_maxima, defensa, poder, agilidad, resistencia) -> None:
        super().__init__(nombre, tipo, vida_maxima, defensa, poder, agilidad, resistencia)
        super().__init__(nombre, tipo, vida_maxima, defensa, poder, agilidad, resistencia)
    def atacar(self, enemigo):
        dmg = 1
        if random() < (parametros.PROB_MDB/100):
            dmg = Mago.atacar(self,enemigo)
        else: 
            dmg = Guerrero.atacar(self,enemigo)
        self.agilidad = self.agilidad - ((parametros.CANSANCIO/100) * self.agilidad)
        self.defensa = self.defensa + ((parametros.DEF_MDB/100) * self.defensa)
        if dmg < 1: 
            return 1
        else:
            return int(dmg)

#CLASE CABALLERO ARCANO 
class CaballeroArcano(Caballero,Mago,Guerrero):
    def __init__(self, nombre, tipo, vida_maxima, defensa, poder, agilidad, resistencia):
        super().__init__(nombre, tipo, vida_maxima, defensa, poder, agilidad, resistencia)
        super().__init__(nombre, tipo, vida_maxima, defensa, poder, agilidad, resistencia)

    def atacar(self, enemigo):
        dmg = 1
        if random() < (parametros.PROB_CAR/100): #prob de atacar como caballero 
            dmg = Caballero.atacar(self, enemigo)
        elif random() < (parametros.PROB_ATK_MAG/100): #atacar por hechizos como mago 
            dmg = Mago.atacar(self, enemigo)
        else: 
            dmg = Guerrero.atacar(self, enemigo)
        self.agilidad = self.agilidad + ((parametros.AUM_CAR/100) * self.agilidad)
        self.poder = self.poder + ((parametros.AUM_CAR/100) * self.poder)
        self.resistencia = self.resistencia - ((parametros.CANSANCIO/100) * self.resistencia)
        if dmg < 1: 
            return 1
        else:
            return int(dmg)







