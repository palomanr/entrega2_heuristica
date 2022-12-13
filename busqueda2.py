# Example of input -> {’3XX’: 11, ’1CX’: 12, ’6XX’: 15, ’5XX’: 16} -> Position 0 is front of the line
# Function calculates the cost with current distribution

# Class returns the cost of the distribution
class Cost:
    def __init__(self, distribution: dict):
        self.cost = 0
        self.distribution_keys = list(distribution.keys())
        self.distribution = distribution
        self.length = len(self.distribution)

        for self.index in range(0, self.length):

            # Getting current key and value of key
            current_key = self.distribution_keys[self.index]
            current_seat = self.distribution[current_key]

            # If current student is non-problematic and does not have reduced mobility
            if current_key[1:] == "XX":
                self.current_student_xx()

            # if current student is non-problematic and has reduced mobility
            # There has to be a student behind because the current student has reduced mobility
            elif current_key[1:] == "XR":
                self.current_student_xr()

    def current_student_xx(self):
        self.cost += 1

    def current_student_xr(self):
        student_behind_key = self.distribution_keys[self.index + 1]  # Student behind current student

        # If student behind does not have reduced mobility and is not problematic
        if student_behind_key[1:] == "XX":
            self.cost += 3  # Cost for current student
            self.cost += 3  # Cost for student behind
            self.index += 1  # Skip student behind

        elif student_behind_key[1:] == "CX":
            self.cost += 6  # Cost for current student is duplicated because of problematic student
            self.cost += 3  # Cost for problematic student

            if (self.index + 2) in range(0, self.length):
                self.index += 2  # Skip next two students
                self.cost












