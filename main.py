class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self):
        pass
        Name = "Boakai Dorbor Kamara"
        Age = 15
        Tracks = [General,FullStack]
        Score = 9.524


Name: A string, should be initialized when creating an instance of Student
 Age: An integer, should be initialized when creating an instance of Student
Tracks: A list of strings, should be initialized when creating an instance of Student. Feel free to pick any values as tracks.
 Score: A float, should be initialized when creating an instance of Student.  


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
