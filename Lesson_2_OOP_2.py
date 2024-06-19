# Task 2: Event Management System Enhancement

# Problem Statement: Use the existing Event class by adding an instance attribute to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.

# Code Example: Basic Event class without participant tracking.

class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date
            self.num_participants = 0

        def add_participant(self):
              participants = input(f"Please enter the number of participants for the {self.name} on {self.date}: \n")
              self.num_participants += int(participants)
              print(f'\n {participants} participant(s) has been added to {self.name} \n')

        def get_participant_count(self):
              print(f'Total number of participants for the {self.name} on {self.date}: {self.num_participants} \n')


event1 = Event('Tech Conference', '6-18-24')

event1.get_participant_count()

event1.add_participant()

event1.get_participant_count()

event1.add_participant()

event1.get_participant_count()