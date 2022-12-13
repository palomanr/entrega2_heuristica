# Example of input -> {’3XX’: 11, ’1CX’: 12, ’6XX’: 15, ’5XX’: 16} -> Position 0 is front of the line
# Function calculates the cost with current distribution
def distribution_cost(distribution: dict):
    cost = 0
    distribution_keys = list(distribution.keys())
    len_distribution = len(distribution)
    cost_dict = {}
    same_dict = {}

    # We create dictionary with all the initial costs
    for current in distribution_keys:
        if current[1:] == "XX":
            cost_dict[current] = 1
            same_dict[current] = 0
        elif current[1:] == "XR":
            cost_dict[current] = 3
            same_dict[current] = 0
        elif current[1:] == "CX":
            cost_dict[current] = 1
            same_dict[current] = 0
        elif current[1:] == "CR":
            cost_dict[current] = 3
            same_dict[current] = 0

    for index in range(0, len_distribution):

        # Get current student key
        current = distribution_keys[index]

        # If current student is non-problematic and has reduced mobility
        if current[1:] == "XR":

            # Get student behind, he has to exist because current has reduced mobility
            student_behind = distribution_keys[index+1]

            if student_behind == "CX":
                cost_dict[current] = cost_dict[current] * 2  # Current student cost multiplied by two
                cost_dict[student_behind] = cost_dict[student_behind]  # Student behind has to have same cost as current

                # Linking both students time
                same_dict[current] = 1
                same_dict[student_behind] = 1

            else:
                cost_dict[distribution_keys[index+1]] = cost_dict[distribution_keys[index]]  # Student behind has the same cost as current

        elif current[1:] == "CX":

            # Checking if indexes in range
            front_exist = (index-1) in range(0, len_distribution)
            behind_exist = (index + 1) in range(0, len_distribution)

            if front_exist:
                # Getting student in front
                student_front = distribution_keys[index - 1]
                cost_dict[student_front] = cost_dict[student_front] * 2 # Student front cost multiplied by two

            if behind_exist:
                # Getting student behind
                student_behind = distribution_keys[index + 1]
                cost_dict[student_behind] = cost_dict[student_behind] * 2 # Student front cost multiplied by two

            elif current[1:] == "CR":
                # Checking if indexes in range, student being has to exist
                front_exist = (index - 1) in range(0, len_distribution)

                if front_exist:
                    # Getting student in front
                    student_front = distribution_keys[index - 1]
                    cost_dict[student_front] = cost_dict[student_front] * 2  # Student front cost multiplied by two

                # Multiplied student behind cost by two
                student_behind = distribution_keys[index + 1]
                cost_dict[student_behind] = cost_dict[student_behind] * 2  # Student front cost multiplied by two

                # Linking all three students
                same_dict[current] = 1
                same_dict[student_behind] = 1
                same_dict[student_front] = 1



        return



