# this code is written by Masih Heidari
# date : 10/2/2023
# importing packages
import numpy as np
import random

age = np.random.randint(1, 10)
humanity = np.random.randint(1, 10)
skin_color = np.random.randint(1, 10)
IQ = np.random.randint(1, 10)
bliefe = np.random.randint(1, 10)
first_generation = []
new_generation = []
tested_ones = []
after_surgery = []
def best_person():
    best_age = np.random.choice(age)

    best_hum = np.random.choice(humanity)
    best_skc = np.random.choice(skin_color)
    best_IQ = np.random.choice(IQ)
    best_blf = np.random.choice(bliefe)
    best = [best_age, best_hum, best_skc, best_IQ, best_blf]
    first_generation.append(best)
    # first_generation.remove("None")


num = 1

second_generation = []
for i in range(100):
    first_generation.append(best_person())
for q in range(100):
    first_generation.pop(num)
    num = num + 1

for m in range(10):
    num = random.choice(first_generation)
    new_generation.append(num)


a = 0
index0 = new_generation[0]
index1 = new_generation[1]
index2 = new_generation[2]
index3 = new_generation[3]
index4 = new_generation[4]

new_generation.clear()
index0[0] = 10
index1[0] = 10
index2[0] = 10
index3[0] = 10
index4[0] = 10

new_generation = [index0,index1,index2,index3,index4]
print(first_generation)
a = 0

def check_person():
    a = 0
    b = 0
    c = 0
    d = 0
    v = 0
    for e in range(len(first_generation)):
     ex = first_generation[v]
     if ex[0] == 10:
        print(ex)
        break
     else:
        v = v + 1
