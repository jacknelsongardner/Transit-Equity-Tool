import numpy as np
from stats import log_normalize


def calculate_equity():
    pass




# YOUR SCORES
salary = 50000
people = 3
cars = 2

salary_weight = 5
people_weight = 4
car_weight = 3

total_weight = salary_weight + people_weight + car_weight

salary_weight = salary_weight/total_weight
people_weight = people_weight/total_weight
car_weight = car_weight/total_weight


# PEOPLES SCORES 
salaryList = [10000,20000,30000,40000,60000,80000,100000]
peoplelist = [0,1,2,3,4,8,12]
carsList = [12,3,2,1,0]

salaryFunc = log_normalize(salaryList)
peopleFunc = log_normalize(peoplelist)
carsFunc = log_normalize(carsList)

salaryScore = salaryFunc(salary)
peopleScore = peopleFunc(people)
carScore = carsFunc(cars)

print(salaryScore)
print(peopleScore)
print(carScore)

