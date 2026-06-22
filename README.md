# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [The game allows players to guess a secret number while receiving hints and tracking their score. ] Describe the game's purpose.

- [Show Hints toggle hid essential feedback.
   Higher/Lower hint messages were reversed.
   Attempt counting was incorrect] Detail which bugs you found.

- [Made feedback display regardless of the hint toggle.
   Corrected the Higher/Lower messages.
   Fixed attempt counting and validated guesses before incrementing attempts.] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. <!-- The game starts and displays the number of attempts remaining. -->
2. <!-- The player enters a guess below the secret number and receives "Go HIGHER!". -->
3. <!-- The player enters a guess above the secret number and receives "Go LOWER!". -->
4. <!-- The score updates after each valid guess. -->
5. <!-- The game ends after the final attempt or when the player guesses the correct number. -->

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
