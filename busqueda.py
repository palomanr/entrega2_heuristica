
# Example of input -> {’3XX’: 11, ’1CX’: 12, ’6XX’: 15, ’5XX’: 16} -> Position 0 is front of the line
# Function calculates the cost with current distribution
def distribution_cost(distribution: dict):
    cost = 0
    distribution_keys = list(distribution.keys())
    for index in range(0, len(distribution)):

        # Nonconflictive student with reduced mobility
        if distribution_keys[index][1] == "X" and distribution_keys[index][2] == "R":
            cost += 3  # Cost for the reduced mobility
            cost += 3  # Cost for student behind him
            index += check_if_range_index(index, distribution)  # Saltando el alumno siguiente

        # Nonconflictive student without reduced mobility
        elif distribution_keys[index][1] == "X" and distribution_keys[index][2] == "X":
            cost += 1

        # Conflictive student without reduced mobility
        elif distribution_keys[index][1] == "C" and distribution_keys[index][2] == "X":
            cost += 1  # Cost for conflictive student
            student_front = distribution_keys[check_if_range_front(index, distribution)]
            student_back = distribution_keys[check_if_range_back(index, distribution)]

            # If student behind has reduced mobility
            if student_front[2] == "R" and student_front != "ERROR":
                cost += 3  # Duplicates the cost of student_behind
                cost += 3  # Also duplicates the cost of person helping student_behind

            # If student behind doesn't have reduced mobility
            else:
                cost += 2

            # If student in front has reduced mobility
            if student_back[2] == "R" and student_back != "ERROR":
                cost += 6  # Duplicates the cost of student in front
                cost += 5  # Conflictive student needs to have same cost
                index += check_if_range_index(index, distribution)  # Skip next student

            # If student in front doesn't have reduced mobility
            else:
                cost += 2  # Duplicates cost of student
                index += check_if_range_index(index, distribution) # Skip next student

    return cost

def check_if_range_index(index, distribution):
    length = len(distribution)
    if index+1 <= length:
        return 1
    return 0

def check_if_range_back(index, distribution):
    length = len(distribution)
    if index + 1 <= length:
        return index + 1
    return "ERROR"

def check_if_range_front(index, distribution):
    length = len(distribution)
    if index - 1 >= 0:
        return index - 1
    return "ERROR"









print(distribution_cost({"3XX": 11, "1CX": 12, "6XX": 15, "5XX": 16}))

#print(distribution_cost({"6XX":15, "3XX":11, "1CX":12, "7CX":32}))