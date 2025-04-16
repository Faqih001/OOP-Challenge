from pet import Pet

def main():
    # Create a new pet with a pet type
    my_pet = Pet("Buddy", pet_type="Dragon")
    
    # Test the pet's functionality
    print("🐉 Welcome to your virtual pet!")
    my_pet.get_status()
    
    # Test eating
    my_pet.eat()
    my_pet.get_status()
    
    # Test playing
    my_pet.play()
    my_pet.get_status()
    
    # Test sleeping
    my_pet.sleep()
    my_pet.get_status()
    
    # Test cuddling (new action)
    my_pet.cuddle()
    my_pet.get_status()
    
    # Test training
    my_pet.train("sit")
    my_pet.train("roll over")
    my_pet.train("sit")  # Try teaching same trick again
    my_pet.show_tricks()
    
    # Test playing when tired
    my_pet.energy = 1  # Force low energy
    my_pet.play()
    my_pet.get_status()

if __name__ == "__main__":
    main()