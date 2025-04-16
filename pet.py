# Defines the Pet class to represent a virtual pet with attributes and behaviors
class Pet:
    # Constructor to initialize a new Pet object
    # Parameters: name (string), pet_type (string, defaults to "Dog")
    def __init__(self, name, pet_type="Dog"):
        self.name = name  # Stores the pet's name
        self.pet_type = pet_type  # Stores the pet's type (e.g., Dog, Dragon)
        self.hunger = 5  # Initial hunger level (0 = full, 10 = very hungry)
        self.energy = 5  # Initial energy level (0 = tired, 10 = fully rested)
        self.happiness = 5  # Initial happiness level (0 = sad, 10 = very happy)
        self.tricks = []  # List to store learned tricks

    # Method to simulate the pet eating
    def eat(self):
        # Reduce hunger by 3, but not below 0
        self.hunger = max(0, self.hunger - 3)
        # Increase happiness by 1, but not above 10
        self.happiness = min(10, self.happiness + 1)
        # Print action with emojis for visual appeal
        print(f"🍽️ {self.name} the {self.pet_type} ate some food! Hunger decreased, happiness increased. 😊")

    # Method to simulate the pet sleeping
    def sleep(self):
        # Increase energy by 5, but not above 10
        self.energy = min(10, self.energy + 5)
        # Print action with sleep-related emojis
        print(f"😴 {self.name} the {self.pet_type} took a nap! Energy increased. 💤")

    # Method to simulate the pet playing
    def play(self):
        # Check if pet has enough energy (at least 2) to play
        if self.energy >= 2:
            self.energy -= 2  # Decrease energy by 2
            # Increase happiness by 2, but not above 10
            self.happiness = min(10, self.happiness + 2)
            # Increase hunger by 1, but not above 10
            self.hunger = min(10, self.hunger + 1)
            # Print action with playful emojis
            print(f"🎉 {self.name} the {self.pet_type} had fun playing! Happiness increased, but got hungrier and more tired. 🏃")
        else:
            # Print message if pet is too tired
            print(f"😓 {self.name} the {self.pet_type} is too tired to play!")

    # Custom method to simulate cuddling with the pet (bonus creativity)
    def cuddle(self):
        # Increase happiness by 2, but not above 10
        self.happiness = min(10, self.happiness + 2)
        # Decrease energy by 1, but not below 0
        self.energy = max(0, self.energy - 1)
        # Print action with affectionate emojis
        print(f"🤗 {self.name} the {self.pet_type} loved the cuddles! Happiness increased, slightly tired. 💖")

    # Method to teach the pet a new trick
    # Parameter: trick (string, the trick to learn)
    def train(self, trick):
        # Check if the trick is not already known
        if trick not in self.tricks:
            self.tricks.append(trick)  # Add trick to the list
            # Increase happiness by 1, but not above 10
            self.happiness = min(10, self.happiness + 1)
            # Print success message with training emojis
            print(f"🎓 {self.name} the {self.pet_type} learned a new trick: {trick}! 🐾")
        else:
            # Print message if trick is already known
            print(f"🤔 {self.name} the {self.pet_type} already knows {trick}!")

    # Method to display all learned tricks
    def show_tricks(self):
        # Check if the pet knows any tricks
        if self.tricks:
            # Print tricks as a comma-separated list with celebratory emojis
            print(f"🌟 {self.name} the {self.pet_type}'s tricks: {', '.join(self.tricks)}")
        else:
            # Print message if no tricks are known
            print(f"😕 {self.name} the {self.pet_type} doesn't know any tricks yet!")

    # Method to display the pet's current status
    def get_status(self):
        # Print header with status emoji
        print(f"\n📊 {self.name} the {self.pet_type}'s Status:")
        # Print hunger with food emoji
        print(f"🍖 Hunger: {self.hunger}/10")
        # Print energy with lightning emoji
        print(f"⚡ Energy: {self.energy}/10")
        # Print happiness with smiley emoji
        print(f"😄 Happiness: {self.happiness}/10")