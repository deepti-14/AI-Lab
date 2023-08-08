import random

class SimpleVacuumEnvironment:
    def __init__(self):
        # Initialize rooms, room status, and agent location
        self.rooms = ['Room A', 'Room B']
        self.room_status = {room: 'Dirty' for room in self.rooms}
        self.agent_location = random.choice(self.rooms)

    def is_dirty(self, room):
        # Returns if the room is dirty or not
        return self.room_status[room] == 'Dirty'

    def clean(self, room):
        # Marks the room as clean
        self.room_status[room] = 'Not Dirty'

    def move_agent(self, room):
        # Moves the agent to the specified room
        self.agent_location = room

    def display(self):
        # Display the current state of rooms and agent location
        print("Current state:")
        for room in self.rooms:
            print(f"{room} is {self.room_status[room]}")
        print(f"Agent is in {self.agent_location}\n")


class ModelBasedReflexVacuumAgent:
    def __init__(self, environment):
        # Initialize agent with the environment and an internal model
        self.environment = environment
        self.model = {room: 'Dirty' for room in self.environment.rooms}

    def perceive(self):
        # Perceive and return the current room and dirt status
        current_room = self.environment.agent_location
        dirt_status = self.environment.is_dirty(current_room)
        return current_room, dirt_status

    def update_model(self, room):
        # Update the internal model when the agent cleans a room
        self.model[room] = 'Not Dirty'

    def decide_action(self, dirt_status):
        # Decide whether to clean or move based on perception and model
        current_room = self.environment.agent_location
        if dirt_status:
            return "Clean"
        elif self.model[current_room] == 'Dirty':
            return "Clean"
        else:
            return "Move"

    def act(self):
        # Perform the chosen action and update environment and model
        current_room, dirt_status = self.perceive()
        action = self.decide_action(dirt_status)
        
        if action == "Clean":
            print(f"Agent cleans {current_room}")
            self.environment.clean(current_room)
            self.update_model(current_room)
        elif action == "Move":
            other_room = [room for room in self.environment.rooms if room != current_room][0]
            print(f"Agent moves from {current_room} to {other_room}")
            self.environment.move_agent(other_room)


# Example usage
env = SimpleVacuumEnvironment()
env.display()
agent = ModelBasedReflexVacuumAgent(env)
for _ in range(3):
    agent.act()
    env.display()
