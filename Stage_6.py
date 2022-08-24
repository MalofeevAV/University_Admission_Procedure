def read_from_file(filename):
    """Read data from file and return sotred list of applicants"""
    with open(filename, "r") as file:
        return create_list_of_applicants(file)


def write_to_file(path, department, applicants):
    """Write data to file - for each department creates their own file <department>.txt"""
    with open(f"{path}/{department}.txt", "w") as file:
        for applicant in sorted(applicants, key=lambda x: (-float(x[2]), x[0])):
            file.write(" ".join(applicant) + "\n")


def create_files(dict_with_applicants):
    """Create files with results - for each department creates their own file <department>.txt"""
    for department in dict_with_applicants:
        write_to_file(".", department, dict_with_applicants[department])


def create_list_of_applicants(file):
    """Split data from file and return list of applicants"""
    return [applicant.split() for applicant in file]


def sorted_list_of_applicants(list_of_applicants):
    """Sort applicants in ascending order by scores for particular exams: physics, chemistry, math, computer science.
    If two applicants have the same score, it will be sorted by their full names in alphabetical order"""
    return sorted(list_of_applicants, key=lambda x: (-float(x[2]), -float(x[3]), -float(x[4]), -float(x[5]), x[0] + " " + x[1]))


def mean_score(applicant, index):
    """Return mean score of student"""
    return sum((float(applicant[i]) for i in index))/len(index)


def sorted_applicants_by_department(list_of_applicants, index):
    """Sort applicants in ascending order by department and their full names"""
    return sorted(list_of_applicants, key=lambda x: (-float(x[index]), x[0], x[1]))


def create_list_of_applicants_with_mean_score(list_of_applicants):
    """Create list of applicants with mean score and priorities"""
    return [applicant[:2] + [mean_score(applicant, departments[department]) for department in departments] + applicant[-amount_of_priorities:] for applicant in list_of_applicants]


def create_dict_with_applicants(list_of_applicants):
    """Create dict with department as a key and list of applicants as a value"""
    for i in range(amount_of_priorities):
        department_index = -len(departments) - amount_of_priorities
        for department in departments:
            for applicant in sorted(list_of_applicants, key=lambda x: (-x[department_index], x[:2])):
                if applicant[-amount_of_priorities+i] == department and applicant not in enrolled_applicants and len(dict_with_applicants[department]) < max_num_of_students:
                    dict_with_applicants[department].append(applicant[:2] + [str(applicant[department_index])])
                    enrolled_applicants.append(applicant)
            department_index += 1

    return dict_with_applicants


def print_result(dict_with_applicants):
    """Print result(applicant, gpa) sorted by alphabetical order"""
    for department in sorted(dict_with_applicants):
        print(department)
        for app in sorted(dict_with_applicants[department], key=lambda x: (-x[2], x[0])):
            print(*app)
        print()


if __name__ == "__main__":
    enrolled_applicants = []
    departments = {"Physics": [2, 4], "Chemistry": [3], "Biotech": [2, 3], "Mathematics": [4], "Engineering": [4, 5]}
    dict_with_applicants = {dep: [] for dep in departments}
    amount_of_priorities = 3

    max_num_of_students = int(input())

    list_of_applicants = read_from_file("Test_files/applicants3.txt")
    # list_of_applicants = read_from_file("Test_files/test1")

    dict_with_applicants = create_dict_with_applicants(create_list_of_applicants_with_mean_score(list_of_applicants))
    create_files(dict_with_applicants)