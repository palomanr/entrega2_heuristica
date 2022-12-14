# Example of input -> {"3XX": 11, "1CX": 12, "6XX": 15, "5XX": 16} -> Position 0 is front of the line
# Function calculates the cost with current distribution
from random import randint


def distribution_cost(distribution: dict):
    distribution_keys = list(distribution.keys())
    len_distribution = len(distribution)
    cost_dict = {}
    same_dict = {}

    # We create dictionary with all the initial costs
    for current in distribution_keys:
        if current[-2:] == "XX":
            cost_dict[current] = 1
            same_dict[current] = 0
        elif current[-2:] == "XR":
            cost_dict[current] = 3
            same_dict[current] = 0
        elif current[-2:] == "CX":
            cost_dict[current] = 1
            same_dict[current] = 0
        elif current[-2:] == "CR":
            cost_dict[current] = 3
            same_dict[current] = 0

    print("INITIAL COST DICTIONARY: ", cost_dict)

    for index in range(0, len_distribution):

        # Get current student key
        current = distribution_keys[index]

        # If current student is non-problematic and has reduced mobility
        if current[-2:] == "XR":

            # Get student behind, he has to exist because current has reduced mobility
            student_behind = distribution_keys[index+1]

            # Link both student costs with random number
            random_num = randint(0, 1000)
            same_dict[current] = random_num
            same_dict[student_behind] = random_num

        elif current[-2:] == "CX":

            # Checking if indexes in range
            front_exist = (index-1) in range(0, len_distribution)
            behind_exist = (index + 1) in range(0, len_distribution)

            if front_exist:
                # Getting student in front
                student_front = distribution_keys[index - 1]
                cost_dict[student_front] = cost_dict[student_front] * 2  # Student front cost multiplied by two

            if behind_exist:
                # Getting student behind
                student_behind = distribution_keys[index + 1]
                cost_dict[student_behind] = cost_dict[student_behind] * 2  # Student front cost multiplied by two

        elif current[-2:] == "CR":
            # Checking if indexes in range, student being has to exist
            front_exist = (index - 1) in range(0, len_distribution)

            if front_exist:
                # Getting student in front
                student_front = distribution_keys[index - 1]
                cost_dict[student_front] = cost_dict[student_front] * 2  # Student front cost multiplied by two

            # Multiplied student behind cost by two
            student_behind = distribution_keys[index + 1]
            cost_dict[student_behind] = cost_dict[student_behind] * 2  # Student front cost multiplied by two

            # Link both student costs with random number
            random_num = randint(0, 1000)
            same_dict[current] = random_num
            same_dict[student_behind] = random_num

        if current[-2] == "C":
            # Duplicating costs for every student behind current with a seat number higher than current
            # We skip two
            if index + 2 <= len_distribution:
                for aux in range(index + 2, len_distribution):
                    new_current_key = distribution_keys[aux]

                    # Checking if there is a student behind
                    two_behind_exist = (index + 1) in range(0, len_distribution)

                    # If student behind exists and his seat has a higher number multiply cost by two
                    if two_behind_exist and distribution[new_current_key] > distribution[current]:
                        cost_dict[new_current_key] = cost_dict[new_current_key] * 2

    print("SAME VALUES DICTIONARY: ", same_dict)

    read = []
    same_dict_list = list(same_dict.keys())

    # Making linked values the same, highest value
    for index in range(0, len(same_dict_list)):
        current_key = same_dict_list[index]
        current_key_cost = cost_dict[current_key]
        current_key_same = same_dict[current_key]

        if current_key_same != 0 and (current_key_same not in read):
            for new_index in range(index, len(same_dict_list)):
                new_current_key = same_dict_list[new_index]
                new_current_key_same = same_dict[new_current_key]
                if new_current_key_same == current_key_same:
                    new_current_key_cost = cost_dict[new_current_key]
                    read.append(current_key_same)

            max_value = max(current_key_cost, new_current_key_cost)
            cost_dict[current_key] = max_value
            cost_dict[new_current_key] = max_value
            del cost_dict[current_key]

    cost_list = list(cost_dict.values())
    total_cost = 0

    # Adding up all costs
    for current in cost_list:
        total_cost += current

    print("FINAL COST DICTIONARY: ", cost_dict)

    return total_cost


print(distribution_cost({"3XX": 11, "1CX": 12, "6XX": 15, "5XX": 7, "6XR": 17, "7XX": 18}))













