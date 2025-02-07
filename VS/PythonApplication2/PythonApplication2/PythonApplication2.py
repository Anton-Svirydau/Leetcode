import random
import itertools


some_list = [1,2,3,4,5]
some_choice = random.choice(some_list)

#print(some_choice)


accumulate_sum = list(itertools.accumulate(some_list))

print(accumulate_sum)
