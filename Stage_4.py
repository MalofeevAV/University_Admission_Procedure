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
    return sorted(list_of_applicants, key=lambda x: (-float(x[2]), x[3], x[0]))


def create_dict_with_applicants(list_of_applicants, max_num_of_students):
    """Create dict with department as a key and inner dict(applicant : GPA) as a value"""
    dict_with_applicants = dict()
    enrolled_applicants = []

    # range equals amount of departments
    for i in range(len(list_of_applicants[0][3:])):
        for applicant in list_of_applicants:
            department = applicant[3+i]
            if applicant not in enrolled_applicants:
                if department not in dict_with_applicants:
                    dict_with_applicants[department] = [[" ".join(applicant[:2]), float(applicant[2])]]
                    enrolled_applicants.append(applicant)
                else:
                    # For each department, choose the N best candidates
                    if len(dict_with_applicants[department]) < max_num_of_students:
                        dict_with_applicants[department].append([" ".join(applicant[:2]), float(applicant[2])])
                        enrolled_applicants.append(applicant)

    return dict_with_applicants


def print_result(dict_with_applicants):
    """Print result(applicant, gpa) sorted by alphabetical order"""
    for department in sorted(dict_with_applicants):
        print(department)
        for name, gpa in sorted(dict_with_applicants[department], key=lambda x: (-x[1], x[0])):
            print(name, gpa)
        print()


if __name__ == "__main__":
    max_num_of_students = int(input())
    list_of_applicants = read_from_file("Test_files/applicants.txt")
    # list_of_applicants = read_from_file("Test_files/test1.txt")
    dict_with_applicants = create_dict_with_applicants(sorted_list_of_applicants(list_of_applicants), max_num_of_students)
    print_result(dict_with_applicants)
