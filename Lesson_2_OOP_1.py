# 1. City Infrastructure Management System
# Objective: The aim of this assignment is to apply the concepts of Object-Oriented Programming in Python to build a simulated City Infrastructure Management System. This system will incorporate classes, objects, methods, and data structures to manage different aspects of a city, such as buildings, traffic, and events.

# Task 1: Vehicle Registration System

# Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.

# Code Example: Provide a basic structure for the Vehicle class without methods.
class Vehicle:
    def __init__(self, reg_num, vehicle_type, owner):
        self.registration_number = reg_num
        self.type = vehicle_type
        self.owner = owner


    def update_owner (self):
        new_owner = input(f"Please enter the name of the new vehicle owner for the {self.type}: \n")
        self.owner = new_owner
        print(f"The owner of the vehicle has been updated to {new_owner}")

ford = Vehicle(234324, 'Mustang', 'Matt')
honda = Vehicle(345353, 'Civic', 'Alice')
cheverolet = Vehicle(9988998, 'Spark', 'Jeremy')


# # Expected Outcome: Completion of the Vehicle class with the update_owner method and a demonstration script showing the creation of Vehicle objects and updating their owners.


print("Original owner's list:")
print(ford.owner + ' - ' + ford.type)
print(honda.owner + ' - ' + honda.type)
print(cheverolet.owner + ' - ' + cheverolet.type)

ford.update_owner()
honda.update_owner()
cheverolet.update_owner()

print("Updated owner's list:")
print(ford.owner + ' - ' + ford.type)
print(honda.owner + ' - ' + honda.type)
print(cheverolet.owner + ' - ' + cheverolet.type)







