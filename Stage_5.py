def read_from_file(filename):
    """Read data from file and return sotred list of applicants"""
    with open(filename, "r") as file:
        return create_list_of_applicants(file)


def create_list_of_applicants(file):
    """Split data from file and return list of applicants"""
    return [applicant.split() for applicant in file]


def sorted_list_of_applicants(list_of_applicants):
    """Sort applicants in ascending order by GPA and priorities.
    If two applicants to the same department have the same GPA, it will be sorted by their full names in alphabetical order"""
    return sorted(list_of_applicants, key=lambda x: (-float(x[2]), -float(x[3]), -float(x[4]), -float(x[5]), x[0] + " " + x[1]))


def sorted_applicants_by_department(list_of_applicants, index):
    return sorted(list_of_applicants, key=lambda x: (-float(x[index]), x[0], x[1]))


def create_dict_with_applicants(list_of_applicants, max_num_of_students):
    """Create dict with department as a key and inner dict(applicant : GPA) as a value"""
    enrolled_applicants = []
    department_index = {"Physics": 2, "Chemistry": 3, "Biotech": 3, "Mathematics": 4, "Engineering": 5}
    dict_with_applicants = {dep: [] for dep in department_index}

    for i in range(3):
        for department in department_index:
            for applicant in sorted_applicants_by_department(list_of_applicants, department_index[department]):
                if applicant[-3+i] == department and applicant not in enrolled_applicants and len(dict_with_applicants[department]) < max_num_of_students:
                    dict_with_applicants[department].append(applicant[:2] + [float(applicant[department_index[department]])])
                    enrolled_applicants.append(applicant)

    return dict_with_applicants


def print_result(dict_with_applicants):
    """Print result(applicant, gpa) sorted by alphabetical order"""
    for department in sorted(dict_with_applicants):
        print(department)
        for app in sorted(dict_with_applicants[department], key=lambda x: (-x[2], x[0])):
            print(*app)
        print()


if __name__ == "__main__":
    max_num_of_students = int(input())
    # list_of_applicants = read_from_file("Test_files/applicants2.txt")
    list_of_applicants = read_from_file("Test_files/test1")
    dict_with_applicants = create_dict_with_applicants(sorted_list_of_applicants(list_of_applicants), max_num_of_students)
    print_result(dict_with_applicants)
