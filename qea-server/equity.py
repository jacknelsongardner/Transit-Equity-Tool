import numpy as np
from score import calculate_score

def calculate_equity(salary, cost_of_living, people, cars):

    salary_col_ratio = salary / cost_of_living
    people_car_ratio = cars / people

    salary_weight = 5
    people_weight = 4

    total_weight = salary_weight + people_weight

    salary_weight = salary_weight/total_weight
    people_weight = people_weight/total_weight


    # PEOPLES SCORES 
    salaryList = [2, 1, .5, 0]
    peoplelist = [1,.5,.25,0]

    output = calculate_score(vals=[salary_col_ratio, people_car_ratio], 
                    weights=[salary_weight, people_weight], 
                    trainSets=[salaryList, peoplelist],
                    names=['salaryCostRatio', 'carPeopleRatio'])

    return output



if __name__ == "__main__":

    print(calculate_equity(50000, 70000, 2, 2))

