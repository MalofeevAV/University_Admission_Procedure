def take_data():
    total_number_of_applicants = int(input())
    number_of_accepted = int(input())

    applicants = []

    for _ in range(total_number_of_applicants):
        name, surname, gpa = input().split()
        applicants.append([" ".join([name, surname]), float(gpa)])

    return applicants, number_of_accepted


def sort_applicants(applicants):
    return sorted(applicants, key=lambda x: (-x[1], x[0]))


def avg_score():
    score_of_exams = [int(input()) for i in range(3)]
    return sum(score_of_exams)/len(score_of_exams)


if __name__ == '__main__':
    applicants, number_of_accepted = take_data()

    sorted_applicants = sort_applicants(applicants)
    print("Successful applicants:")
    for i in range(number_of_accepted):
        print(sorted_applicants[i][0])