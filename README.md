# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

Real world recommendations, like spotify and youtube, work by using both collaboritive filtering and content based filtering. Collaborative filtering finds other similar users that have a similar taste, and suggests what they like. Content based looks at the attributes of the songs you already like. My version will mainly use content based recommendations. 

Each song will use features like genre, mood, energy, and acousticeness. The user profile will also store the users favorite genre, mood, energy, and acoustic preference as a boolean. The score is computed for each song by looking at each feature. When the genre or mood matches, the score increases by either 2 or 1 respectively. For energy, the closeness is calculated by finding the difference between the user preference and the song itself, and subtracting 1 to get a score. There is also a acoustic scoring as well. Finally, the top songs are chosen after ranking all the songs from highest to lowest.  

Visualization of Process:
Input & obtain user pref -> loop through each song in csv -> calculate score for each song, based on each feature. -> score starts at 0, keep updating based on ahy matches -> rank all songs from highest to lowest -> choose top k songs

Algorithm for scoring:
score = 0
--here we reward genre matches with a higher score, as it is more unique--
if song.genre == user.favorite_genre:  score += 2.0 

--mood matches have a score of +1--
if song.mood  == user.favorite_mood:   score += 1.0

--match the energy, find the gap between the user pref and the song. Then negate the value, so lowest gaps are a higher score--
score += 1.0 * (1 - abs(song.energy - user.target_energy))

--look at the acoustic value, and compare to user pref--
if (song.acousticness >= 0.5) == user.likes_acoustic:  score += 0.5

possible biases - could favor more popular genre/types because it is more well represented. Weight would also have a bias, as it gets a higher score than mood



- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



