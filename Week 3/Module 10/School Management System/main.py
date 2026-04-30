from school import School
from person import Teacher, Student
from subject import Subject
from classroom import ClassRoom

school = School("ABC", "Dhaka")

# adding classroom

eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

rahim = Student("Rahim", eight)
kahim = Student("Kahim", nine)
fahim = Student("Fahim", ten)
hahim = Student("hahim", ten)
# rahim = Student("Rahim", eight)

school.student_admission(rahim)
school.student_admission(kahim)
school.student_admission(fahim)
school.student_admission(hahim)
# school.student_admission(rahim)


abul = Teacher("Abul khan")
babul = Teacher("Babul khan")
kabul = Teacher("Kabul khan")

# subject

bangla = Subject("Bangla", abul)
physics = Subject("Physics", babul)
chemistry = Subject("Chemistry", kabul)
biology = Subject("Biolody", kabul)


eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chemistry)
nine.add_subject(biology)
nine.add_subject(physics)
nine.add_subject(chemistry)
ten.add_subject(chemistry)
ten.add_subject(physics)
ten.add_subject(bangla)
ten.add_subject(biology)


eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

print(school)
