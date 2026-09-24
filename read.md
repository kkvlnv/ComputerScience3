LMAOO 😭 that actually tells me a lot about the SA.

If they were allowed to open anything and still just stared at the code, it’s probably testing application/design, not “do you remember the syntax?”

You should prepare for something like:

“Here is a scenario. Create the appropriate classes and demonstrate inheritance, composition, and aggregation.”

And the hard part is recognizing the relationship.

The cheat sheet I’d literally keep beside you

If the problem says…

Think…

Example

“is a” / “is a type of”
Inheritance
Dog is an Animal

“has a” + cannot meaningfully exist without it
Composition
House has Rooms

“has a” + can exist independently
Aggregation
Team has Players

Object contains another object
Association / has-a
Teacher has Students

Parent → child
Inheritance
Person → Student

Inheritance
class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade
        

Composition 
class House:
    def __init__(self):
        self.room = Room()

Aggregation
class Team:
    def __init__(self, players):
        self.players = players

Create a University system. A university has departments. Each department has professors. Professors are people. Students are also people. Students may enroll in courses. A course can exist independently of a student.

Person
├── Student       ← inheritance
└── Professor     ← inheritance

University
└── Department    ← composition/aggregation depending on specification

Department
└── Professor     ← aggregation

Course
└── Student       ← aggregation
