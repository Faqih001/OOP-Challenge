# Import the Pet class from pet.py
from pet import Pet

# Main function to demonstrate the Pet class functionality
def main():
    # Create a new pet named "Buddy" with type "Dragon" (bonus creativity)
    my_pet = Pet("Buddy", pet_type="Dragon")
    
    # Print welcome message with dragon emoji
    print("🐉 Welcome to your virtual pet!")
    # Display initial status
    my_pet.get_status()
    
    # Test eating functionality
    my_pet.eat()
    my_pet.get_status()
    
    # Test playing functionality
    my_pet.play()
    my_pet.get_status()
    
    # Test sleeping functionality
    my_pet.sleep()
    my_pet.get_status()
    
    # Test cuddling functionality (custom action)
    my_pet.cuddle()
    my_pet.get_status()
    
    # Test training functionality
    my_pet.train("sit")  # Teach "sit" trick
    my_pet.train("roll over")  # Teach "roll over" trick
    my_pet.train("sit")  # Try teaching "sit" again (should show already known)
    my_pet.show_tricks()  # Display all tricks
    
    # Test playing when energy is low
    my_pet.energy = 1  # Manually set energy to 1 to simulate tiredness
    my_pet.play()  # Should indicate pet is too tired
    my_pet.get_status()  # Show final status

# Ensure main() runs only when the script is executed directly
if __name__ == "__main__":
    main()