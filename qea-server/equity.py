import numpy as np
from stats import log_normalize


def calculate_equity(salary, cost_of_living, people, cars):

    salary_col_ratio = salary / cost_of_living

    salary_weight = 5
    people_weight = 4
    car_weight = 3

    total_weight = salary_weight + people_weight + car_weight

    salary_weight = salary_weight/total_weight
    people_weight = people_weight/total_weight
    car_weight = car_weight/total_weight


    # PEOPLES SCORES 
    salaryList = [2, 1, .5, 0]
    peoplelist = [1,2,3,4,8]
    carsList = [3,2,1,0]

    salaryFunc = log_normalize(salaryList)
    peopleFunc = log_normalize(peoplelist)
    carsFunc = log_normalize(carsList)

    salaryScore = salaryFunc(salary_col_ratio)
    peopleScore = peopleFunc(people)
    carScore = carsFunc(cars)

    print("raw scores")
    print(salaryScore)
    print(peopleScore)
    print(carScore)

    adjustedSalaryScore = salary_weight * salaryScore
    adjustedPeopleScore = people_weight * peopleScore
    adjustedCarsScore = car_weight * carScore

    adjustedTotal = adjustedCarsScore + adjustedPeopleScore + adjustedCarsScore

    print("adjusted scores")
    print(adjustedSalaryScore)
    print(adjustedPeopleScore)
    print(adjustedCarsScore)
    print(adjustedTotal)

    output = {
        'salary' : {
            'score' : salaryScore,
            'weight' : salary_weight
        },
        'people' : {
            'score' : peopleScore,
            'weight' : people_weight
        },
        'cars' : {
            'score' : carScore,
            'weight' : car_weight
        },
        'total' : adjustedTotal,
    }

    return output



if __name__ == "__main__":

    print(calculate_equity(50000, 70000, 2, 2))

