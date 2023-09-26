from channels import A, B, C
from arrays import Arrays

data = Arrays.fill_array(A, B, C)

print(Arrays.probability_next_system_by_system(data, [1, 1, 1], [1, 1, 0]))
