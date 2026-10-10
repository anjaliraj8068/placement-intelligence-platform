def display_welcome():
 print("\n" + "=" * 45)
 print("   PLACEMENT INTELLIGENCE PLATFORM")
 print("=" * 45)
 print("Your personal placement preparation assistant!")

def create_student_profile():
 print("\n--- Create Your Student Profile ---")

 name = input("Enter your name: ").strip()
 college = input("Enter your college name: ").strip()
 degree = input("Enter your degree: ").strip()
 graduation_year = input("Enter your graduation year: ").strip()

 student = {
    "name": name,
    "college": college,
    "degree": degree,
    "graduation_year": graduation_year
 }

 return student


def display_student_profile(student):
 print("\n" + "=" * 45)
 print("           STUDENT PROFILE")
 print("=" * 45)


 print(f"Name: {student['name']}")
 print(f"College: {student['college']}")
 print(f"Degree: {student['degree']}")
 print(f"Graduation Year: {student['graduation_year']}")

print("=" * 45)

def main():
 display_welcome()


student = create_student_profile()

display_student_profile(student)


if __name__ == "__main__": 
 main()
