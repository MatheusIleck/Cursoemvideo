import random
from quicksort import quicksort


any_numbers = random.sample(range(1, 1000), 42)
print(any_numbers)
quicksort(any_numbers)
print("\n Ordenado:")
print(any_numbers)
print("*******************************")