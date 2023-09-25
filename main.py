import numpy as np
from channels import A, B, C

# entradas m channels con n data
# m00, m01, .... m0k-1 serán instantes de tiempo
# m00, m10, m20, ... mk0-1 seran un system

# matriz n x m con np


def fill_array(*x: list):
    lengths = [len(i) for i in x]
    equals_lengths = all([i == lengths[0] for i in lengths])

    if not equals_lengths:
        raise Exception("Las longitudes de los channels no son iguales")

    return np.array(x)


def probability_next_element_in_channel_by_system(
    data: np.ndarray, system: list, channel: int, element
):
    if len(system) != len(data):
        raise Exception("El system no tiene está completo")

    if not element in data.flatten():
        raise Exception("element no válido")

    if not channel in range(len(data)):
        raise Exception("channel no válido")

    index_equal_system = []
    for i in range(len(data[0]) - 1):
        system_i = [j[i] for j in data]
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


data: np.ndarray = fill_array(A, B, C)

prob = probability_next_element_in_channel_by_system(
    data=data, system=["⓪", "⓪", "⓪"], channel=2, element="❶"
)

print(prob)
