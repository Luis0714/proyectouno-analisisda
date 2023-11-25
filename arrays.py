import numpy as np
import copy


class Arrays:
    array_channels: np.ndarray
    EstadoCanalF: np.ndarray
    EstadoEstadoF: np.ndarray
    EstadoCanalP: np.ndarray
    EstadoEstadoP: np.ndarray
    combos: list
    elements: list
    element: any

    def __init__(self):
        array_channels = []
        self.combos = []
        self.elements = []
        self.EstadoCanalF, self.EstadoEstadoF, self.EstadoCanalP, self.EstadoEstadoP, self.initial_table_for_taller3 = [], [], [], [], []

    def fill_array(self, element, *x: list) -> np.ndarray:
        lengths = [len(i) for i in x]
        equals_lengths = all([i == lengths[0] for i in lengths])

        if not equals_lengths:
            raise Exception("Las longitudes de los channels no son iguales")

        self.array_channels = np.array(x)
        self.elements = list(set(self.array_channels.flatten()))
        self.combos = self._generate_combos()
        self.element = element
        # self.fill_EstadoCanalF()
        # self.fill_EstadoEstadoF()
        # self.fill_EstadoCanalP()
        # self.fill_EstadoEstadoP()
        self.fill_initial_table_for_taller3()
        return self.array_channels

    # for EstadoCanalF 
    def probability_next_element_in_channel_by_system(self, system: list, channel: int, element) -> float:
        
        if len(system) != len(self.array_channels):
            raise Exception("El system no tiene está completo")

        if not element in self.array_channels.flatten():
            raise Exception("element no válido")

        if not channel in range(len(self.array_channels)):
            raise Exception("channel no válido")
        
        index_equal_system = []
        for i in range(len(self.array_channels[0]) - 1):
            system_i = [channel[i] for channel in self.array_channels]
            if system == system_i:
                index_equal_system.append(i)
        ok_next_system = 0
        for i in index_equal_system:
            next_system = self.array_channels[channel][i + 1]
            
            if next_system == element:
                ok_next_system += 1
        if len(index_equal_system) == 0:
            return 0
        
        return ok_next_system / len(index_equal_system) 
    
    # for EstadoEstadoF
    #! for taller 3
    def probability_next_system_by_system(self, system: list, next_system: list) -> float:
        if len(system) != len(self.array_channels) or len(next_system) != len(
            self.array_channels
        ):
            raise Exception("Uno de los systemas no están completo")

        # TODO: check if next_system an system is in self.array_channels

        index_equal_system = []
        for i in range(len(self.array_channels[0]) - 1):
            system_i = [channel[i] for channel in self.array_channels]
            if system == system_i:
                index_equal_system.append(i)

        ok_next_system = 0
        for i in index_equal_system:
            real_next_system = [channel[i + 1] for channel in self.array_channels]
            
            if real_next_system == next_system:
                ok_next_system += 1
        if len(index_equal_system) == 0:
            return 0
        
        return ok_next_system / len(index_equal_system)

    # for EstadoCanalP 
    def probability_next_system_by_elemetn_channel(self, origin_channel: int, element: int, next_system: list) -> float:
        if len(next_system) != len(self.array_channels):
            raise Exception("sistema no completo")

        # TODO: check if next_system and system is in self.array_channels

        index_equal_system = []
        for i in range(len(self.array_channels[0]) - 1):
            if self.array_channels[origin_channel][i] == element:
                index_equal_system.append(i)

        ok_next_system = 0
        for i in index_equal_system:
            real_next_system = [channel[i + 1] for channel in self.array_channels]
            
            if real_next_system == next_system:
                ok_next_system += 1

        if len(index_equal_system) == 0:
            return 0
        
        return ok_next_system / len(index_equal_system)
    
    # for EstadoEstadoP
    def probability_next_element_in_channel_by_element_channel(self, origin_channel:int, origin_element, next_channel:int, next_element) -> float: 
        if not origin_element in self.array_channels.flatten() or not next_element in self.array_channels.flatten():
            raise Exception("element no válido")

        index_equal_system = []
        num_inputs = len(self.array_channels[0])
        for i in range(num_inputs - 1):
            if self.array_channels[origin_channel][i] == origin_element:
                index_equal_system.append(i)

        ok_next_system = 0
        for i in index_equal_system:
            real_next_element = self.array_channels[next_channel][i + 1]
            
            if real_next_element == next_element:
                ok_next_system += 1
        if len(index_equal_system) == 0:
            return 0
        
        return ok_next_system / len(index_equal_system)

    def _generate_combos(self, n: int = None) -> list[str]:
        n = len(self.array_channels) if n is None else n
        if n < 1:
            return [[]]
        # Caso base: si n(tamaño palabra) == 1 las palabras seran los elementos base
        if n == 1:
            return [ [i] for i in self.elements]    

        # Generamos las combinaciones con tamaño de palabra n-1
        smaller_combinations = self._generate_combos(n - 1)

        # Para cada combinación anterior, agregamos los elemnentos base
        new_combinations = []
        for combination in smaller_combinations:
            for e in self.elements:
                new_combinations.append([e] + combination) 

        return new_combinations
        
    def obtener_letra_por_numero(self,numero):
            if 1 <= numero <= 26:
                # Asumiendo que el número 1 corresponde a 'A', el número 2 a 'B' y así sucesivamente.
                letra = chr(ord('A') + numero - 1)
                return letra
            else:
                return "Número fuera de rango"
    
    def fill_EstadoCanalF(self):
        count_channels = len(self.array_channels)
        channels_string = ['Canal '+self.obtener_letra_por_numero(i+1)+"\n"+str(self.element) for i in range(count_channels)]
        systemString = [self.obtener_letra_por_numero(i+1) for i in range(count_channels)]
        headers = systemString + channels_string
        systems = self.combos
        channels = [i for i in range(count_channels)]
        response = []
        lista = []
        # lista.append(headers)
        for system in systems:
            
            # probability_list = [i for i in system]
            probability_list = []
            system_list = [i for i in system]
            for channel in channels:
                probability = self.probability_next_element_in_channel_by_system(
                    system=system_list, channel=channel, element=self.element
                )
                porcentage = probability
                probability_list.append(porcentage)
            lista.append(probability_list)
            probability_list = []
        self.EstadoCanalF = lista

    def fill_EstadoEstadoF(self):
        count_channels = len(self.array_channels)
        channels_string = [''.join(map(str, i)) for i in self.combos]
        combo_string = [self.obtener_letra_por_numero(i+1) for i in range(count_channels)]
        headers = combo_string + channels_string
        combos = self.combos
        channels = [i for i in range(count_channels)]
        lista = []
        lista.append(headers)
        for combo in combos:
            probability_list = copy.copy(combo)
            for next_state in combos:
                probability = self.probability_next_system_by_system(system=combo, next_system=next_state)
                porcentage = str(round((probability * 100), 2)) + "%"
                probability_list.append(porcentage)
            lista.append(probability_list)
            probability_list = []
        self.EstadoEstadoF = lista

    def fill_EstadoCanalP(self):
        count_channels = len(self.array_channels)
        channels_string = [''.join(map(str, i)) for i in self.combos]
        headers = ["-"] + channels_string
        combos = self.combos
        channels = [i for i in range(count_channels)]
        lista = []
        lista.append(headers)
        for i in range(count_channels):
            probability_list = ['Canal '+self.obtener_letra_por_numero(i+1)+" ("+str(self.element)+")"]
            for next_state in combos:
                probability = self.probability_next_system_by_elemetn_channel(origin_channel = i, element = self.element, next_system=next_state)
                porcentage = str(round((probability * 100), 2)) + "%"
                probability_list.append(porcentage)
            lista.append(probability_list)
            probability_list = []
        self.EstadoCanalP = lista

    def fill_EstadoEstadoP(self): 
        count_channels = len(self.array_channels)
        channels_string = ['Canal '+self.obtener_letra_por_numero(i+1)+"\n"+str(self.element) for i in range(count_channels)]
        headers = ["-"] + channels_string
        combos = self.combos
        channels = [i for i in range(count_channels)]
        lista = []
        lista.append(headers)
        for i in range(count_channels):
            probability_list = ['Canal '+self.obtener_letra_por_numero(i+1)+" ("+str(self.element)+")"]
            for j in range(count_channels):
                probability = self.probability_next_element_in_channel_by_element_channel(origin_channel=i, origin_element=self.element, next_channel=j, next_element=self.element)
                porcentage = str(round((probability * 100), 2)) + "%"
                probability_list.append(porcentage)
            lista.append(probability_list)
            probability_list = []
        self.EstadoEstadoP = lista
        
    #! for taller 3
    def fill_initial_table_for_taller3(self):
        result = []
        for combo in self.combos:
            probability_row = []
            for next_state in self.combos:
                probability = self.probability_next_system_by_system(system=combo, next_system=next_state)
                probability_row.append(probability)
            result.append(probability_row)
            probability_row = []
        self.initial_table_for_taller3 = np.array(result)
        
    def marginalize_next_systems(self, initial_state:tuple[int], next_state:tuple[int]):
        table = self.initial_table_for_taller3.copy()
        quit_channels_col = [i for i in range(len(next_state)) if next_state[i] is None]

        # next_state obtenemos los combos resultantes de quitar los canales
        new_combos_col = []
        for combo in self.combos:
            new_combo = []
            for i in range(len(combo)):
                if i not in quit_channels_col:
                    new_combo.append(combo[i])
            new_combos_col.append(new_combo)                

        # next_state obtenemos los índices de los combos repetidos        
        indice_elemento = {}
        for indice, elemento in enumerate(new_combos_col):
            if str(elemento) in indice_elemento:
                indice_elemento[str(elemento)].append(indice)
            else:
                indice_elemento[str(elemento)] = [indice]
        
        # next_state sumamos las probabilidades de los combos repetidos
        new_table = None
        for key in indice_elemento:
            acc = np.zeros(len(table[:,0]))
            for indice in indice_elemento[key]:
                acc = acc + table[:,indice]
                
            if new_table is None:
                new_table = acc
            else:
                new_table = np.c_[new_table, acc]        
                    
        #! curret_state
        quit_channels_row = [i for i in range(len(initial_state)) if initial_state[i] is None]
        
        # next_state obtenemos los combos resultantes de quitar los canales
        new_combos_row = []
        for combo in self.combos:
            new_combo = []
            for i in range(len(combo)):
                if i not in quit_channels_row:
                    new_combo.append(combo[i])
            new_combos_row.append(new_combo) 
            
        # next_state obtenemos los índices de los combos repetidos 
        indice_elemento_row = {}
        for indice, elemento in enumerate(new_combos_row):
            if str(elemento) in indice_elemento_row:
                indice_elemento_row[str(elemento)].append(indice)
            else:
                indice_elemento_row[str(elemento)] = [indice]
        
        # next_state sumamos las probabilidades de los combos repetidos y dividimos entre 2
        # ! use la fórmula (depronto recusrión)
        result_table = None
        for key in indice_elemento_row:
            acc = np.zeros(len(new_table[0]))
            for indice in indice_elemento_row[key]:
                acc = (acc + new_table[indice, :]) /2
                
            if result_table is None:
                result_table = acc   
            else:
                result_table = np.vstack((result_table, acc))            
                
        return new_table, result_table