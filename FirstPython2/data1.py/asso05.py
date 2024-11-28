##연관관계 다중성(1:1관계)
class Student:
    def __init__(self, name):
        self.name = name    
        self.professor = None   #초기에는 교수 정보 없음
        
class Professor:
    def __init__(self, name):
        self.name = name    
        self.student = None    #초기에는 학생 정보 없음

    def assign_student(self, student):
        self.student =student      #교수에게 학생을 할당
        student.professor = self   #학생에게 교수 정보를 설정

#일대일 관계: 한 교수와 한 학생이 연결됨
professor = Professor("Dr. Smith")
student = Student("Alice")

professor.assign_student(student)

print(f"{student.name}'s professor is {student.professor.name}.")  # Dr. Smith
print(f"{professor.name}'s student is {professor.student.name}.")  # Alice


##다중성 (1:n 관계 )
class Professor:
    def __init__(self, name):
        self.name = name    
        self.students = []

    def add_student(self, student):
        self.students.append(student)  
        student.professor = self   #학생에게 교수 정보를 저장

class Student:
    def __init__(self, name):
        self.name = name  
        self.professor = None     #학생은 처음에 소속 교수 없음

#일대다 관계: 한명의 교수와 여러명의 학생
professor = Professor("Dr. Smith")
student1 = Student("Alice")
student2 = Student("Bob")

professor.add_student(student1)
professor.add_student(student2)

#교수의 학생목록 출력
print(f"Students taught by {professor.name}:")
for student in professor.students:
    print(student.name)


