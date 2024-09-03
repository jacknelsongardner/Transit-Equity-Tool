import numpy as np
from stats import log_normalize



def calculate_equity(salary, cost_of_living, people, cars):

    salary_col_ratio = salary / cost_of_living

    salary_weight = 5
    people_weight = 4

    total_weight = salary_weight + people_weight

    salary_weight = salary_weight/total_weight
    people_weight = people_weight/total_weight


    # PEOPLES SCORES 
    salaryList = [2, 1, .5, 0]
    peoplelist = [1,.5,.25,0]

    salaryFunc = log_normalize(salaryList)
    peopleFunc = log_normalize(peoplelist)

    salaryScore = salaryFunc(salary_col_ratio)
    peopleScore = peopleFunc(people)

    adjustedSalaryScore = salary_weight * salaryScore
    adjustedPeopleScore = people_weight * peopleScore

    adjustedTotal = adjustedPeopleScore + adjustedSalaryScore

    output = {
        'salary' : {
            'score' : salaryScore,
            'weight' : salary_weight
        },
        'people2cars' : {
            'score' : peopleScore,
            'weight' : people_weight
        },
        'total' : adjustedTotal,
    }

    return output



if __name__ == "__main__":

    print(calculate_equity(50000, 70000, 2, 2))

