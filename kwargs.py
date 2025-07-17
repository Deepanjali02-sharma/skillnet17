def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")
        student_info(name="John", age=23, roll_number=107)