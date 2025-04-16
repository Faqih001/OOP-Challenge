class Pet:
    def __init__(self, name, pet_type="Dog"):
        self.name = name
        self.pet_type = pet_type
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"🍽️ {self.name} the {self.pet_type} ate some food! Hunger decreased, happiness increased. 😊")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"😴 {self.name} the {self.pet_type} took a nap! Energy increased. 💤")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"🎉 {self.name} the {self.pet_type} had fun playing! Happiness increased, but got hungrier and more tired. 🏃")
        else:
            print(f"😓 {self.name} the {self.pet_type} is too tired to play!")

    def cuddle(self):
        self.happiness = min(10, self.happiness + 2)
        self.energy = max(0, self.energy - 1)
        print(f"🤗 {self.name} the {self.pet_type} loved the cuddles! Happiness increased, slightly tired. 💖")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1)
            print(f"🎓 {self.name} the {self.pet_type} learned a new trick: {trick}! 🐾")
        else:
            print(f"🤔 {self.name} the {self.pet_type} already knows {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"🌟 {self.name} the {self.pet_type}'s tricks: {', '.join(self.tricks)}")
        else:
            print(f"😕 {self.name} the {self.pet_type} doesn't know any tricks yet!")

    def get_status(self):
        print(f"\n📊 {self.name} the {self.pet_type}'s Status:")
        print(f"🍖 Hunger: {self.hunger}/10")
        print(f"⚡ Energy: {self.energy}/10")
        print(f"😄 Happiness: {self.happiness}/10")