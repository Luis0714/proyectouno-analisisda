import numpy as np


class Arrays:
    array_channels: np.ndarray
    EstadoCanalF: np.ndarray
    EstadoEstadoF: np.ndarray
    EstadoCanalP: np.ndarray
    EstadoEstadoP: np.ndarray
    combos: list
    elements: list

    def __init__(self):
        array_channels = []
        self.combos = []
        self.elements = []
        EstadoCanalF, EstadoEstadoF, EstadoCanalP, EstadoEstadoP = [], [], [], []

    def fill_array(self, *x: list) -> np.ndarray:
        lengths = [len(i) for i in x]
        equals_lengths = all([i == lengths[0] for i in lengths])

        if not equals_lengths:
            raise Exception("Las longitudes de los channels no son iguales")

        self.array_channels = np.array(x)
        self.elements = list(set(self.array_channels.flatten()))
        self.combos = self._generate_combos()
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
            
            if i + 1 >= len(self.array_channels[0]):  # last element
                continue
            
            next_system = self.array_channels[channel][i + 1]
            
            if next_system == element:
                ok_next_system += 1
        if len(index_equal_system) == 0:
            return 0
        
        return ok_next_system / len(index_equal_system)

    # for EstadoEstadoF
    def probability_next_system_by_system(self, system: list, next_system: list) -> float:
        if len(system) != len(self.array_channels) or len(next_system) != len(
            self.array_channels
        ):
            raise Exception("Uno de los systemas no están completo")

        # TODO: check if next_system an system is in self.array_channels

        index_equal_system = []
        for i in range(len(self.array_channels[0])):
            system_i = [channel[i] for channel in self.array_channels]
            if system == system_i:
                index_equal_system.append(i)

        ok_next_system = 0
        for i in index_equal_system:
            
            if i + 1 >= len(self.array_channels[0]):  # last element
                continue
            
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
        for i in range(len(self.array_channels[0])):
            if self.array_channels[origin_channel][i] == element:
                index_equal_system.append(i)

        ok_next_system = 0
        for i in index_equal_system:
            if i + 1 >= len(self.array_channels[0]):  # last element
                continue
            
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
        for i in range(num_inputs):
            if self.array_channels[origin_channel][i] == origin_element:
                index_equal_system.append(i)

        ok_next_system = 0
        for i in index_equal_system:
            if i + 1 >= len(self.array_channels[0]):  # last element
                continue
            
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
                new_combinations.append(combination + [e]) 

        return new_combinations
        
    def fill_EstadoCanalF(self):
        pass