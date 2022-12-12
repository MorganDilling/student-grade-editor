# imports
import menu
import pyChalk
import database
import generateCSV

# Constants
COLOURS = pyChalk.pyChalk()

# Database
db = database.Database("database.json")
db.create()
db.hook()

# Main
def main():
  d = db.read()
  if not "students" in d or len(d["students"]) == 0:
    d["students"] = []
    db.write(d)

    i = 0
    while True:
      i += 1
      print(COLOURS.underline("Student " + str(i)))
      print(COLOURS.green("Enter nothing to exit"))
      forename = menu.Prompt("Enter forename:")
      if forename == "":
        break

      surname = menu.Prompt("Enter surname:")
      if surname == "":
        break

      student = {
        "forename": forename,
        "surname": surname,
        "grades": {}
      }

      d["students"].append(student)
    db.write(d)

  while True:
    selection = menu.Menu("Choose an option", ["Enter Grade", "Show Summary", "Find Highest, Lowest and Average", "Generate CSV File", "Edit Students", "Exit"]).run()

    if selection == 0:
      print(COLOURS.underline("Enter Grade"))
      student = menu.Prompt("Enter student name:")
      subject = menu.Prompt("Enter subject:")
      grade = menu.NumberPrompt("Enter grade:", 0, 100)

      d = db.read()
      for i, s in enumerate(d["students"]):
        if s["forename"] + " " + s["surname"] == student:
          d["students"][i]["grades"][subject] = grade
          db.write(d)
          break
      else:
        print(COLOURS.fail("Student not found"))
    elif selection == 1:
      print(COLOURS.underline("Summary"))
      d = db.read()
      for student in d["students"]:
        print(COLOURS.bold(student["forename"] + " " + student["surname"]))
        if len(student["grades"]) == 0:
          print(" - No grades.")
        else:
          for subject, grade in student["grades"].items():
            print(f" - {subject}: {grade}")

    elif selection == 2:
      print(COLOURS.underline("Highest, Lowest and Average"))
      d = db.read()
      for student in d["students"]:
        print(COLOURS.bold(student["forename"] + " " + student["surname"]))
        if len(student["grades"]) == 0:
          print(" - No grades.")
        else:
          highest = 0
          lowest = 100
          total = 0
          for subject, grade in student["grades"].items():
            if grade > highest:
              highest = grade
            if grade < lowest:
              lowest = grade
            total += grade
          average = total / len(student["grades"])
          print(f" - Highest: {highest}")
          print(f" - Lowest: {lowest}")
          print(f" - Average: {average}")

      print(COLOURS.underline("Highest, Lowest and Average (All Students)"))
      subjects = {}
      for student in d["students"]:
        for subject, grade in student["grades"].items():
          if not subject in subjects:
            subjects[subject] = {
              "highest": 0,
              "lowest": 100,
              "total": 0,
              "count": 0
            }
          if grade > subjects[subject]["highest"]:
            subjects[subject]["highest"] = grade
          if grade < subjects[subject]["lowest"]:
            subjects[subject]["lowest"] = grade
          subjects[subject]["total"] += grade
          subjects[subject]["count"] += 1
      for subject, data in subjects.items():
        print(COLOURS.bold(subject))
        print(f" - Highest: {data['highest']}")
        print(f" - Lowest: {data['lowest']}")
        print(f" - Average: {data['total'] / data['count']}")

    elif selection == 3:
      print(COLOURS.underline("CSV File"))
      fileName = menu.Prompt("Enter file name:", True)
      response = generateCSV.generate(fileName, db.read())
      if response == True:
        print(COLOURS.green("File generated successfully."))
      else:
        print(COLOURS.fail("File generation failed."))

    elif selection == 4:
      choice = menu.Menu("Choose an option", ["Add Student", "Remove Student", "Back"]).run()
      if choice == 0:
        print(COLOURS.underline("Add Student"))
        print(COLOURS.green("Enter nothing to exit"))
        forename = menu.Prompt("Enter forename:")
        if forename == "":
          continue

        surname = menu.Prompt("Enter surname:")
        if surname == "":
          continue

        student = {
          "forename": forename,
          "surname": surname,
          "grades": {}
        }

        d = db.read()
        d["students"].append(student)
        db.write(d)
      elif choice == 1:
        print(COLOURS.underline("Remove Student"))
        print(COLOURS.green("Enter nothing to exit"))
        forename = menu.Prompt("Enter forename:")
        if forename == "":
          continue

        surname = menu.Prompt("Enter surname:")
        if surname == "":
          continue

        d = db.read()
        for i, s in enumerate(d["students"]):
          if s["forename"] + " " + s["surname"] == forename + " " + surname:
            del d["students"][i]
            db.write(d)
            break
        else:
          print(COLOURS.fail("Student not found"))
      elif choice == 2:
        continue

      

    elif selection == 5:
      print(COLOURS.underline("Exiting"))
      db.unhook()
      exit()

if __name__ == "__main__":
  main()