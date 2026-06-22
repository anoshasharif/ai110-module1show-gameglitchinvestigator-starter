# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
Hints were backwards; "Go Lower" actually meant the number was too low, and "Go Higher" meant it was too high.
The difficulty setting (Easy/Medium/Hard) did not change the number range as expected.
The hint toggle ("Show Hints") caused the game to stop working when unchecked.
The attempt counter was off by one, when it said "Out of attempts," one guess was still available.
Pressing "New Game" displayed "Game over. Start a new game to try again" instead of resetting properly.
The higher/lower scale displayed on screen was inaccurate.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Guess Lower than secret number|"Go Higher" Hint shown|"Go Lower" hint shown instead|none| 
|Unchecked "Show Hints" toggle|Game continues without hints|Game stops working entirely|none|
|Last attempt used|Game ends with no guesses left|One guess still remains|none| 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
    I used Claude and Copilot

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
    One correct AI suggestion was identifying that the bug caused by turning off the "Show Hints" toggle was located in app.py. The AI explained that the "Too High" and "Too Low" feedback messages were incorrectly tied to the show_hint flag. I verified this by inspecting the code and confirming that st.warning(message) was only executed when show_hint was True. After removing the if show_hint: condition and always displaying the feedback message, I tested the game and confirmed that it continued to work properly even when hints were turned off.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
    One AI suggestion that was misleading was when it first said the attempts bug was only caused by st.session_state.attempts starting at 1 instead of 0. That was partly correct, but incomplete. I verified this by testing the game again and noticing the attempts display still felt off. After asking AI again, it found another issue: attempts were being counted before the guess was validated.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
    I decided a bug was fixed by running the game again in Streamlit and repeating the same actions that originally caused the bug. If the game behaved the way I expected, I considered the fix successful.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
    One manual test I ran was turning off the “Show Hints” toggle and submitting a guess. Before the fix, the game gave no feedback. After the fix, it still showed “Go Higher” or “Go Lower,” which showed that the bug was fixed.

- Did AI help you design or understand any tests? How?
    AI helped me understand what to test by explaining the logic behind each bug and pointing out which user actions would confirm whether the fix worked.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
    I would explain Streamlit reruns by saying that every time the user interacts with the app, Streamlit runs the whole script again from top to bottom. Session state is like memory that lets the app remember values such as the secret number, score, and number of attempts between reruns.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
      One habit I want to reuse is asking AI to explain the logic behind a bug instead of immediately asking for a fix. This helped me understand the code better and verify the solutions myself.
    
- What is one thing you would do differently next time you work with AI on a coding task?
      Next time, I would test the AI's suggestions more carefully because some explanations were incomplete and required additional investigation

- In one or two sentences, describe how this project changed the way you think about AI generated code.
      This project taught me that AI-generated code can contain subtle bugs and that AI suggestions should be treated as a starting point rather than blindly trusted. I learned that understanding and testing the code is just as important as generating it.