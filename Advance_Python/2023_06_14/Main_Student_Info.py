from Class_Student_Info import*


if __name__ == "__main__":

    Inf=[["Cárine Gonçalves", 7, 12], ["José Cruz", 15, 16], ["Paulo Sousa", 19, 20], ["Gilberto Moreira", 17, 16], ["Tiago Reis", 19, 20]]

    Pauta = {}
    for i in Inf:
        students = StudentInfo(i[0], i[1], i[2])
        Pauta[students.name] = str(students.finalgrade()), students.finalClassification()
    print(Pauta)

    # student = StudentInfo("", 0, 0)
    # student.data_input()
    # student.presentation()
