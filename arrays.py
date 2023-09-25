import numpy as np
class Arrays:
    def fill_array(*x: list):
        lengths = [len(i) for i in x]
        equals_lengths = all([i == lengths[0] for i in lengths])

        if not equals_lengths:
            raise Exception("Las longitudes de los channels no son iguales")

        return np.array(x)


    def probability_next_element_in_channel_by_system(
        data: np.ndarray, system: list, channel: int, element):
        if len(system) != len(data):
            raise Exception("El system no tiene está completo")

        if not element in data.flatten():
            raise Exception("element no válido")

        if not channel in range(len(data)):
            raise Exception("channel no válido")

        index_equal_system = []
        for i in range(len(data[0]) - 1):
            system_i = [channel[i] for channel in data]
            if system == system_i:
                index_equal_system.append(i)
        ok_next_element = 0
        for i in index_equal_system:
            next_element_channel = data[channel][i + 1]
            if i + 1 >= len(data[0]):  # last element
                continue

            if next_element_channel == element:
                ok_next_element += 1

        return ok_next_element / len(index_equal_system)

    def generate_binary_combinations(n:int):
        # Comprobamos si n es menor que 1
        if n < 1:
            return [[]]

        # Caso base: si n es 1, hay dos combinaciones posibles: [0] y [1]
        if n == 1:
            return [[0], [1]]

        # Generamos las combinaciones recursivamente
        smaller_combinations = Arrays.generate_binary_combinations(n - 1)
        
        # Para cada combinación anterior, agregamos 0 y 1 para obtener las nuevas combinaciones
        new_combinations = []
        for combination in smaller_combinations:
            new_combinations.append(combination + [0])
            new_combinations.append(combination + [1])

        return new_combinations