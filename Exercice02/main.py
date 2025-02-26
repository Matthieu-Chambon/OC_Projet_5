students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
     'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}

student = input("Entrez le nom de l’étudiant : ")

if student in students:
     print(f"Notes de {student} : ")
     moyenne = 0

     for matiere, note in students[student].items():
          print(f"{matiere} : {str(note)}")
          moyenne += note

     moyenne = moyenne/len(students[student].items())
     print(f"Moyenne de {student} : {moyenne}")

else:
     print(f"L'étudiant {student} n'existe pas dans la liste.")