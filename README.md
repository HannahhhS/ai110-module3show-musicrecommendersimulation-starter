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

Loaded songs: 18

============================================
  TOP RECOMMENDATIONS
  for genre=pop, mood=happy, energy=0.8
============================================

1. Sunrise City - Neon Echo
   Score: 3.98
   Reasons:
     - genre match: pop (+2.0)
     - mood match: happy (+1.0)
     - energy 0.82 vs target 0.8 (+0.98)

2. Gym Hero - Max Pulse
   Score: 2.87
   Reasons:
     - genre match: pop (+2.0)
     - energy 0.93 vs target 0.8 (+0.87)

3. Rooftop Lights - Indigo Parade
   Score: 1.96
   Reasons:
     - mood match: happy (+1.0)
     - energy 0.76 vs target 0.8 (+0.96)

4. Concrete Kingdom - Blvck Ivory
   Score: 0.95
   Reasons:
     - energy 0.85 vs target 0.8 (+0.95)

5. Night Drive Loop - Neon Echo
   Score: 0.95
   Reasons:
     - energy 0.75 vs target 0.8 (+0.95)
```

```
additional testing:

==================================================
  PROFILE: High-Energy Pop
  prefs: {'genre': 'pop', 'mood': 'happy', 'energy': 0.9}
==================================================

1. Sunrise City - Neon Echo
   Score: 3.92
   Reasons:
     - genre match: pop (+2.0)
     - mood match: happy (+1.0)
     - energy 0.82 vs target 0.9 (+0.92)

2. Gym Hero - Max Pulse
   Score: 2.97
   Reasons:
     - genre match: pop (+2.0)
     - energy 0.93 vs target 0.9 (+0.97)

3. Rooftop Lights - Indigo Parade
   Score: 1.86
   Reasons:
     - mood match: happy (+1.0)
     - energy 0.76 vs target 0.9 (+0.86)

4. Storm Runner - Voltline
   Score: 0.99
   Reasons:
     - energy 0.91 vs target 0.9 (+0.99)

5. Pulse Reactor - Voltage Kids
   Score: 0.95
   Reasons:
     - energy 0.95 vs target 0.9 (+0.95)


==================================================
  PROFILE: Chill Lofi
  prefs: {'genre': 'lofi', 'mood': 'chill', 'energy': 0.3, 'likes_acoustic': True}
==================================================

1. Library Rain - Paper Lanterns
   Score: 4.45
   Reasons:
     - genre match: lofi (+2.0)
     - mood match: chill (+1.0)
     - energy 0.35 vs target 0.3 (+0.95)
     - acoustic preference match (+0.5)

2. Midnight Coding - LoRoom
   Score: 4.38
   Reasons:
     - genre match: lofi (+2.0)
     - mood match: chill (+1.0)
     - energy 0.42 vs target 0.3 (+0.88)
     - acoustic preference match (+0.5)

3. Focus Flow - LoRoom
   Score: 3.40
   Reasons:
     - genre match: lofi (+2.0)
     - energy 0.4 vs target 0.3 (+0.90)
     - acoustic preference match (+0.5)

4. Spacewalk Thoughts - Orbit Bloom
   Score: 2.48
   Reasons:
     - mood match: chill (+1.0)
     - energy 0.28 vs target 0.3 (+0.98)
     - acoustic preference match (+0.5)

5. Paper Boats - The Quiet Pines
   Score: 1.47
   Reasons:
     - energy 0.33 vs target 0.3 (+0.97)
     - acoustic preference match (+0.5)


==================================================
  PROFILE: Deep Intense Rock
  prefs: {'genre': 'rock', 'mood': 'intense', 'energy': 0.9}
==================================================

1. Storm Runner - Voltline
   Score: 3.99
   Reasons:
     - genre match: rock (+2.0)
     - mood match: intense (+1.0)
     - energy 0.91 vs target 0.9 (+0.99)

2. Gym Hero - Max Pulse
   Score: 1.97
   Reasons:
     - mood match: intense (+1.0)
     - energy 0.93 vs target 0.9 (+0.97)

3. Pulse Reactor - Voltage Kids
   Score: 0.95
   Reasons:
     - energy 0.95 vs target 0.9 (+0.95)

4. Concrete Kingdom - Blvck Ivory
   Score: 0.95
   Reasons:
     - energy 0.85 vs target 0.9 (+0.95)

5. Iron Verdict - Ashfall
   Score: 0.92
   Reasons:
     - energy 0.98 vs target 0.9 (+0.92)


==================================================
  PROFILE: Conflicting: Sad but Energetic
  prefs: {'genre': 'pop', 'mood': 'melancholy', 'energy': 0.95}
==================================================

1. Gym Hero - Max Pulse
   Score: 2.98
   Reasons:
     - genre match: pop (+2.0)
     - energy 0.93 vs target 0.95 (+0.98)

2. Sunrise City - Neon Echo
   Score: 2.87
   Reasons:
     - genre match: pop (+2.0)
     - energy 0.82 vs target 0.95 (+0.87)

3. Elegy in Grey - Camille Ferro
   Score: 1.30
   Reasons:
     - mood match: melancholy (+1.0)
     - energy 0.25 vs target 0.95 (+0.30)

4. Pulse Reactor - Voltage Kids
   Score: 1.00
   Reasons:
     - energy 0.95 vs target 0.95 (+1.00)

5. Iron Verdict - Ashfall
   Score: 0.97
   Reasons:
     - energy 0.98 vs target 0.95 (+0.97)


==================================================
  PROFILE: Empty Profile (no preferences)
  prefs: {}
==================================================

1. Sunrise City - Neon Echo
   Score: 0.00
   Reasons:
     - no strong matches

2. Midnight Coding - LoRoom
   Score: 0.00
   Reasons:
     - no strong matches

3. Storm Runner - Voltline
   Score: 0.00
   Reasons:
     - no strong matches

4. Library Rain - Paper Lanterns
   Score: 0.00
   Reasons:
     - no strong matches

5. Gym Hero - Max Pulse
   Score: 0.00
   Reasons:
     - no strong matches
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:
 I tested how sensitive the system was by changing to weights. The energy weight was doubled from 1-2, and the genre was halved, from 2-1. Typically, the first pick stayed the same but the middle ones shuffled. Sometimes songs that didnt match the genre welll, but the energy, starting shifting to the top. This means the system is sensitive to changes in energy since it uses the difference to make a score. This means energy should be weighted less than the genre. 


- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

The model doesnt favor mood much, hasnt been tested with larger datasets, cant work with sub genres. 

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



