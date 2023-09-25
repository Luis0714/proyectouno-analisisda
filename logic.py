from copy import copy
from arrays import Arrays
import numpy as np

class Logic:
    def probability_system_and_channels(data: np.ndarray):
        systems = Arrays.generate_binary_combinations(len(data))
        channels = [i for i in range(len(data))]
        elements = [0,1]
        response= []

        for element in elements:
            lista = []
            for system in systems:
                probability_list = copy(system)
                for channel in channels:
                    probability = Arrays.probability_next_element_in_channel_by_system(data=data, system=system, channel=channel, element=element)
                    porcentage = str(round((probability * 100),2)) + '%'
                    probability_list.append(porcentage)
                lista.append(probability_list)
                probability_list = []
            response.append(lista);
        return response
    

# from channels import A, B, C
# from arrays import Arrays
# data: np.ndarray  = Arrays.fill_array(A, B, C)
# response  = Logic.probability_system_and_channels(data)
# print(response)