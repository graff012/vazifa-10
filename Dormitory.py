class Student:
    def __init__(self, name, age, year):
        self.name = name
        self.age = age
        self.year = year
        self.students_room = {}

    def student_room(self, name, room_number):
        self.students_room[name] = room_number
        print(f"{name} is in {room_number}th room")


class Room:
    def __init__(self, number_of_room, capacity):
        self.number_of_room = number_of_room
        self.capacity = capacity
        self.students_in_room = []

    def has_space(self):
        return len(self.students_in_room) < self.capacity

    def add_student(self, student_name):
        if self.has_space():
            self.students_in_room.append(student_name)
            print(f"{student_name} added to room {self.number_of_room}")
        else:
            print(f"Room {self.number_of_room} is full.")


class Dormitory:
    def __init__(self):
        self.all_rooms = {}

    def add_room(self, room_number, capacity):
        if room_number not in self.all_rooms:
            self.all_rooms[room_number] = Room(room_number, capacity)
            print(f"Room {room_number} added with a capacity of {capacity}.")
        else:
            print(f"Room {room_number} already exists.")

    def assign_student(self, student_name):
        for room in self.all_rooms.values():
            if room.has_space():
                room.add_student(student_name)
                return
        print(f"No available rooms for {student_name}. All rooms are full.")

    def calculate_total_rooms(self):
        return len(self.all_rooms)

    def show_room_status(self):
        for room_number, room in self.all_rooms.items():
            print(f"Room {room_number}: {len(room.students_in_room)}/{room.capacity} students")
            print(f"Students: {room.students_in_room}")


dorm = Dormitory()
dorm.add_room(101, 2)
dorm.add_room(102, 3)

dorm.assign_student("Alice")
dorm.assign_student("Bob")
dorm.assign_student("Charlie")
dorm.assign_student("David")
dorm.assign_student("Eve")

dorm.show_room_status()
print(f"Total rooms in the dormitory: {dorm.calculate_total_rooms()}")
