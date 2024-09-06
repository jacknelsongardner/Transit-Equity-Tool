import numpy as np
from score import calculate_score
from geo import *



def calculate_equity(salary, cost_of_living, people, cars):

    salary_col_ratio = salary / cost_of_living
    people_car_ratio = cars / people

    salary_weight = 5
    people_weight = 4

    total_weight = salary_weight + people_weight

    salary_weight = salary_weight/total_weight
    people_weight = people_weight/total_weight


    # PEOPLES SCORES 
    salaryList = [0, .5, 1, 2]
    peoplelist = [0, .25, .5, 1]

    output = calculate_score(vals=[salary_col_ratio, people_car_ratio], 
                    weights=[salary_weight, people_weight], 
                    trainSets=[salaryList, peoplelist],
                    names=['salaryCostRatio', 'carPeopleRatio'])

    return output

def equity_by_address(address):
    coordinates = get_coordinates(address=address)
    geo = get_geoCode(coordinates=coordinates)
    print(geo)
    salary, num_cars, num_people = get_demographic_info(geo, 2022)
    cost_of_living = 50000
    return calculate_equity(salary, cost_of_living, num_people, num_cars)

if __name__ == "__main__":

    print(calculate_equity(50000, 70000, 2, 2))

