# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**

Model

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

The main weakness i found is that energy takes over for people who like a less common genre. FOr example, there are around 15 different genres in my dataset after adding the newer songs. This was done to have diversity in genres so now genre is over preferalixed. However, this means an exact genre match is required, and only energy can be used to score on every song. Therefore fans of rarer genres dont get as accurate preditctions becuase energy starts to be used



Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

I tested six user profiles whocj all had a diversity of user profiles. Three were general tastes, which included the following: **High-Energy Pop**
(pop / happy / 0.9), **Chill Lofi** (lofi / chill / 0.3, likes acoustic), and, **Deep Intense Rock** (rock / intense / 0.9). The other three were edge cases meant to try to trick the scoring: **Sad but Energetic**,  **Acoustic Metalhead**, **Empty Profile** with no preferences at all. For each profile,  I looked at whether the top songs actually matched what the user asked for, or whether the wrong songs were sneaking in.

**What surprised me:** for the "Sad but Energetic" user, the one truly sad song
in the catalog ("Elegy in Grey") did not even make the top two. Instead, two
upbeat pop songs came out on top, and the sad song landed in 3rd. Here is why in
plain terms: the recommender gives the most points for matching the genre and a
lot of points for having energy close to what the user asked for. This user
wanted very high energy (0.95), but the sad song is very calm (0.25 energy), so
it lost almost all of its energy points even though it perfectly matched the sad
mood. Matching the mood is only worth a little on its own, so it was not enough
to make up for the huge energy gap. It surprised me that asking for a "sad" song
could still return happy pop at the top, and it showed me that my energy score
quietly overpowers the mood the user actually asked for.

**Comparing the profiles (what changed and why it makes sense):**

- **High-Energy Pop vs. Chill Lofi:** these are near opposites. Pop pulls fast,
  upbeat songs like "Sunrise City" and "Gym Hero" (energy ~0.8-0.9), while Lofi
  shifts all the way down to quiet, acoustic tracks like "Library Rain" (energy
  ~0.3). This makes sense because the energy target flips from high to low.
- **High-Energy Pop vs. Deep Intense Rock:** both want high energy, so they
  actually share songs ("Gym Hero" and high-energy tracks appear in both). The
  difference is the genre and mood: Rock puts "Storm Runner" (rock + intense)
  at #1, which never shows up for the Pop user. Same energy, different genre =
  overlapping but re-ordered lists.
- **Chill Lofi vs. Deep Intense Rock:** almost no overlap at all, which is the
  cleanest result. One wants calm acoustic music and the other wants loud fast
  music, so the energy gap alone is enough to keep their lists totally separate.
- **High-Energy Pop vs. Sad but Energetic:** same genre (pop) and similar high
  energy, so their lists look alike ("Gym Hero," "Sunrise City" near the top).
  The only real difference is the actual sad song, "Elegy in Grey," creeps into
  3rd for the sad user because of the mood match, even though it has very low
  energy. It shows the mood point is too weak to overcome a big energy gap.
- **Deep Intense Rock vs. Acoustic Metalhead:** both want aggressive, high-energy
  music, but the Metalhead also likes acoustic, which fights the metal request.
  The metal song "Iron Verdict" still wins, but the rest of the list fills up
  with quiet acoustic songs that are the opposite of metal. The two preferences
  can't both be satisfied, so the list looks split and confused.
- **Any normal profile vs. Empty Profile:** the normal profiles produce clearly
  ranked, explained songs, but the Empty Profile produces all-zero scores and
  just returns songs in file order, showing the system needs at least some
  input to behave meaningfully.

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
