


ages = [23, 45, 32, 19, 21, 38,42, 18]

# for in

for i in ages:
    print(i)

print("----------------------------------")


for i in range(len(ages)):
    if ages[i] > 30:
     print(ages[i])

## Usando comprension de listas 


ages2 = [i for i in ages  if i > 30]

print(ages2)