# this code is written by Masih Heidari
# date : 10/2/2023
# importing packages
import numpy as np
import random

# these are the factors
age = np.random.randint(1, 10)
humanity = np.random.randint(1, 10)
skin_color = np.random.randint(1, 10)
IQ = np.random.randint(1, 10)
bliefe = np.random.randint(1, 10)
# as far as we dont have more than one generation for now its our only generation
first_generation = []
# the first test of DNA changing is gonna be done on them
new_generation = []


# we prpduce our generation with this function randomly
def best_person():
    best_age = np.random.choice(age)

    best_hum = np.random.choice(humanity)
    best_skc = np.random.choice(skin_color)
    best_IQ = np.random.choice(IQ)
    best_blf = np.random.choice(bliefe)
    best = [best_age, best_hum, best_skc, best_IQ, best_blf]
    first_generation.append(best)


''' as far as we use function 
the first generation list would be full of "None" valiues
so this part of the code is about to delete them from list
'''
# its a number we se in algorithem
num = 1

for i in range(100):
    first_generation.append(best_person())
for q in range(100):
    first_generation.pop(num)
    num = num + 1

# random peopleto do the experiment

for m in range(10):
    num = random.choice(first_generation)
    new_generation.append(num)

# defineing their indexes as numbers
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

new_generation = [index0, index1, index2, index3, index4]


# finding the best person
def check_person():
    v = 0
    for e in range(len(first_generation)):
        ex = first_generation[v]
        if ex[0] == 10:
            print(ex)
            break
        else:
            # counter
            v = v + 1


# starting the second sergery
second_sergury_people = []
# finding valentueres
for i in range(20):
    choosed_people = random.choice(first_generation)
    second_sergury_people.append(choosed_people)
    choosed_people = []
# changing their DNA
counter = 0
list1 = []
while counter <= len(second_sergury_people):
    for i in range(10):
        surgery = second_sergury_people[counter]
        surgery2 = second_sergury_people[counter + 1]
        surgery = surgery[:2]
        surgery2 = surgery2[2:]
        new_person = list([surgery + surgery2])
        list1.append(new_person)
        new_person = []
        counter = counter + 1
    else:
        break
print(list1)
