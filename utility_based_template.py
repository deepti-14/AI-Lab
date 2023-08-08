import random

class SimpleVacuumEnvironment:
    def __init__(self):
        self.room_status = {
            'A': random.choice(['Clean', 'Dirty']),
            'B': random.choice(['Clean', 'Dirty'])
        }
        self.agent_location = random.choice(['A', 'B'])

    def is_dirty(self, room):
        return self.room_status[room] == 'Dirty'

    def clean(self, room):
        self.room_status[room] = 'Clean'

    def move_agent(self, room):
        self.agent_location = room

    def display(self):
        print("Room A:", self.room_status['A'])
        print("Room B:", self.room_status['B'])
        print("Agent Location:", self.agent_location)
        print()

class UtilityBasedVacuumAgent:
    def __init__(self, environment):
        self.environment = environment
        self.utilities = {'A': 0, 'B': 0}

    def calculate_utilities(self):
        for room in self.utilities:
            if self.environment.is_dirty(room):
                self.utilities[room] = -1  # Negative utility for dirty rooms
            else:
                self.utilities[room] = 1   # Positive utility for clean rooms

    def decide_action(self):
        current_room = self.environment.agent_location
        other_room = 'B' if current_room == 'A' else 'A'
        
        if self.utilities[current_room] < self.utilities[other_room]:
            return "Clean" if self.environment.is_dirty(current_room) else "Move"
        else:
            return "Move"

    def act(self):
        current_room, dirt_status = self.environment.agent_location, self.environment.is_dirty(self.environment.agent_location)
        action = self.decide_action()

        if action == "Clean":
            self.environment.clean(current_room)
            print("Agent cleans", current_room)
        elif action == "Move":
            target_room = 'B' if current_room == 'A' else 'A'
            self.environment.move_agent(target_room)
            print("Agent moves to", target_room)

        self.environment.display()

# Example usage
env = SimpleVacuumEnvironment()
agent = UtilityBasedVacuumAgent(env)

for _ in range(5):
    agent.calculate_utilities()
    print(f"Utility Values: {agent.utilities}")
    agent.act()
    print()