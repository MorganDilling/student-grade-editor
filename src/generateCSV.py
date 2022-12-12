def generate(fileName:str, data:dict):
    # Format:
    #
    # Student Name,Subject 1, Subject 2, etc...
    # Student 1,Grade 1,Grade 2,etc...

    lines = []

    subjects = []
    for student in data["students"]:
        for subject in student["grades"]:
            if subject not in subjects:
                subjects.append(subject)

    lineOneSubjects = []
    for subject in subjects:
        lineOneSubjects.append('"' + subject + '"')

    lines.append("Student Name," + ",".join(lineOneSubjects))

    for student in data["students"]:
        line = '"' + student["forename"] + " " + student["surname"] + '"'
        for subject in subjects:
            if subject in student["grades"]:
                line += "," + str(student["grades"][subject])
            else:
                line += ",N/A"
        lines.append(line)

    writeString = ""
    for line in lines:
        writeString += line
        if line != lines[-1]:
            writeString += "\n"

    with open(fileName + ".csv", "w") as f:
        f.write(writeString)

    return True