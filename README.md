# 🐶 Python OOP Challenge: Build Your Own Digital Pet

Welcome to this week's Python challenge! 🎉

In this challenge, you’ll be creating a virtual pet using Object-Oriented Programming concepts in Python. This fun project will help you practice how to use classes, attributes, methods, and constructors.

---

## 🧠 Objective

Create a class called `Pet` with the following:

### Attributes

- `name`: the name of your pet
- `hunger`: an integer representing hunger level (0 = full, 10 = very hungry)
- `energy`: an integer representing energy level (0 = tired, 10 = fully rested)
- `happiness`: an integer (0–10)

### Methods

- `eat()`: reduces hunger by 3 points (but not below 0), and increases happiness by 1.
- `sleep()`: increases energy by 5 points (but not above 10).
- `play()`: decreases energy by 2, increases happiness by 2, and increases hunger by 1.
- `get_status()`: prints the current state of the pet.

### Bonus 🎯

- Add a method `train(trick)` that teaches your pet a new trick and stores it in a list.
- Add a method `show_tricks()` that prints all learned tricks.

---

## 📝 How to Complete

1. Fork or clone this repo: <https://github.com/Faqih001/OOP-Challenge>
2. Write your `Pet` class in `pet.py`.
3. In `main.py`, create a pet object and call its methods to test functionality.
4. Submit a GitHub repo or a zipped folder with your code and a screenshot of the output.

---

## 🚀 How to Run the Challenge

To execute your Digital Pet program, follow these steps:

1. **Install Python**:
   - Ensure Python 3 is installed. Check by running `python3 --version` or `python --version` in a terminal.
   - If not installed, download Python 3 from [python.org](https://www.python.org/downloads/) and install it, selecting "Add Python to PATH" during setup.

2. **Set Up Files**:
   - Save `pet.py` (containing your `Pet` class) and `main.py` (containing test code) in the same directory (e.g., `OOP-Challenge`).

3. **Open a Terminal**:
   - Windows: Press `Win + R`, type `cmd`, and press Enter.
   - macOS/Linux: Open the Terminal app.

4. **Navigate to the Directory**:
   - Use the `cd` command to enter the directory with your files:

     ```bash
     cd path/to/digital_pet
     ```

5. **Run the Program**:
   - Execute `main.py` with:

     ```bash
     python3 main.py
     ```

     or

     ```bash
     python main.py
     ```

   - This runs the program, displaying your pet's interactions and status.

6. **Verify Output**:
   - Check that the output matches the expected format (see Sample Output below).
   - If errors occur, ensure both files are in the same directory and named correctly (`pet.py`, `main.py`).

---

## ✅ Sample Output

```bash
🐉 Welcome to your virtual pet!

📊 Buddy the Dragon's Status:
🍖 Hunger: 5/10
⚡ Energy: 5/10
😄 Happiness: 5/10
🍽️ Buddy the Dragon ate some food! Hunger decreased, happiness increased. 😊

📊 Buddy the Dragon's Status:
🍖 Hunger: 2/10
⚡ Energy: 5/10
😄 Happiness: 6/10
🎉 Buddy the Dragon had fun playing! Happiness increased, but got hungrier and more tired. 🏃

📊 Buddy the Dragon's Status:
🍖 Hunger: 3/10
⚡ Energy: 3/10
😄 Happiness: 8/10
😴 Buddy the Dragon took a nap! Energy increased. 💤

📊 Buddy the Dragon's Status:
🍖 Hunger: 3/10
⚡ Energy: 8/10
😄 Happiness: 8/10
🤗 Buddy the Dragon loved the cuddles! Happiness increased, slightly tired. 💖

📊 Buddy the Dragon's Status:
🍖 Hunger: 3/10
⚡ Energy: 7/10
😄 Happiness: 10/10
🎓 Buddy the Dragon learned a new trick: sit! 🐾
🎓 Buddy the Dragon learned a new trick: roll over! 🐾
🤔 Buddy the Dragon already knows sit!
🌟 Buddy the Dragon's tricks: sit, roll over
😓 Buddy the Dragon is too tired to play!

📊 Buddy the Dragon's Status:
🍖 Hunger: 3/10
⚡ Energy: 1/10
😄 Happiness: 10/10
```

---

## 🏁 Submission

**Deadline**: April 16th, 2025

**Submission format**: Clone or fork this repo: <https://github.com/Faqih001/OOP-Challenge>

**Bonus points**: Add creativity with custom actions (e.g., cuddling), emojis, or unique pet types (e.g., Dragon, Unicorn).
