Grade_list = ["F", "D", "C", "B", "A"]

eie_323_grade = input("Enter your grade for EIE 323: ").upper()
while eie_323_grade not in Grade_list:
    print("Invalid grade, please enter a valid grade")
    eie_323_grade = input("Enter your grade for EIE 323: ").upper()
eie_323_score = Grade_list.index(eie_323_grade)

eie_327_grade = input("Enter your grade for EIE 327: ").upper()
while eie_327_grade not in Grade_list:
    print("Invalid grade, please enter a valid grade")
    eie_327_grade = input("Enter your grade for EIE 327: ").upper()
eie_327_score = Grade_list.index(eie_327_grade)

eie_326_grade = input("Enter your grade for EIE 326: ").upper()
while eie_326_grade not in Grade_list:
    print("Invalid grade, please enter a valid grade")
    eie_326_grade = input("Enter your grade for EIE 326: ").upper()
eie_326_score = Grade_list.index(eie_326_grade)

eie_328_grade = input("Enter your grade for EIE 328: ").upper()
while eie_328_grade not in Grade_list:
    print("Invalid grade, please enter a valid grade")
    eie_328_grade = input("Enter your grade for EIE 328: ").upper()
eie_328_score = Grade_list.index(eie_328_grade)

gec_320_grade = input("Enter your grade for GEC 320: ").upper()
while gec_320_grade not in Grade_list:
    print("Invalid grade, please enter a valid grade")
    gec_320_grade = input("Enter your grade for GEC 320: ").upper()
gec_320_score = Grade_list.index(gec_320_grade)

gec_324_grade = input("Enter your grade for GEC 324: ").upper()
while gec_324_grade not in Grade_list:
    print("Invalid grade, please enter a valid grade")
    gec_324_grade = input("Enter your grade for GEC 324: ").upper()
gec_324_score = Grade_list.index(gec_324_grade)

courses_score_addition = eie_323_score + eie_327_score + eie_326_score + eie_328_score + gec_320_score + gec_324_score
gpa_calculation = float(round(courses_score_addition / 6, 2))
print(f" your GPA is {gpa_calculation}")