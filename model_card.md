# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**

Model Name: Tune-a Match

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 
The recommender is a program that suggests songs to a listener that they might like. The user has to provide genre, mood, and energy. The system looks through all the songs and picks the top 5. It also has a short description on why a song was chosen. This would not be ready yet for real users, as there are alot of biases and limitations, and ai generated songs for testing. 
Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

A song gets a score based on the genre, energy, mood, and also if they like acoustic music. These are the user preferences that are considered. A song gets 2 points if it matches the genre, 1 point for matching the mood. The closer the user energy score is to a song energy score, the song gets a score that is closer to 1. If the user likes acoustic music and the song is acoustic, the song also gets 0.5 point for that. All the points are then added. The list of songs is ordered from highest to lowest, and the top k are chosen to display to user. 

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

The data set has 18 songs across a wide 15 genres to cover niche genres and test those. Each song has the title, artist, mood, energy, tempo, valence, danceability, and acousticness. It is a small and made up data set. Since it is small, there is not much variety a user can get. The original dataset had 10 songs, and we were told to add more to it. an additional 8 songs were added. 

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

The model seems to work pretty well for common types, like pop, rock, or lofi. When the genre and energy and mood are typical and match, there are better chances of getting a good song. The pick reason is also explained well to the user. 

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

I tested six user profiles whocj all had a diversity of user profiles. Three were general tastes, which included the following: High energy pop, chill lofi, and deep intense rock. The other three were edge cases meant to try to trick the scoring and it included sad but energetic, acoustic metalhead, and an emptry profile. For each profile,  I looked at whether the top songs actually matched what the user asked for, or whether the wrong songs were sneaking in.

For the sad but energetic " user, the sad song in the catalog did not even make the top two. Instead, two upbeat pop songs came out on top, and the sad song landed in 3rd. This is because the recommender gives the most points for matching the genre and a lot of points for having energy close to what the user asked for. This user wanted very high energy (0.95), but the sad song is very calm (0.25 energy), so it lost almost all of its energy points even though it matched the sad mood. This most likely happened becuase the model favors matching genre, and energy gets matched for everything is it isnt categorical. The mood doesnt have as much of a weight. With the modification of energy having more weight than the genre, this was even more emphasized. It still was suprising though to see the sad song not being weighed as much. 

pop vs chill lofi:
These profiles are quite different from eachother, as the pop profile like faster upbeat songs with high energy, while the chill lofi prefers softer acoustic/lower enerft songs.  

high energy pop vs intense rock:
Both of these profiles like high energy, so high energy songs appear in both, like gym hero and other high energy songs. The main difference is genre, the rock profile as storm runner at the top since it is rock and also high energy, while pop profile doesnt have that at all. 

chill lofi vs intense rock:
There is almost no overlap here, since one profile likes calm music and the other likes loud and faster music. a

high energy pop vs sad but energetic: same genre (pop) and similar high energy, so their lists look alik, and both feature gym hero and sunrise city near the top. The difference is the sad song, becuase the 2nd profile likes sad but energetic. Mood doesnt have as much weighting though, so the sad song (Elegy in grey) is only ranked third
  
intense rock vs acoistic metalhead: both want aggressive, high energy music, but the Metalhead also likes acoustic, which contrasts the metal request. Both of the preferences cant be satisfied so there is a mix of acoustic as well

normal vs empty profile: a normal profiles produce clearly ranked, explained songs, but the empty profile produces all-zero scores and just returns songs in file order,which means the system needs user input to be able to work

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  
For future iterations, I would make the dataset have more similar genres to see how that impacts the recommendations. I would also allow it to score similar genres like pop vs indie pop with partial credit. I would also handle the empty profile better than just returning the top 2 songs. 
Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  
The biggest learning moment was seeing how the songs are actually scored, and understanding how the logic works when scoring energy. I had seen lines of code like that before but never took the time to understand it. AI tools helped as it wrote the logic out pretty easily, as some of it was repitive. I had to double check AI tools at the beginning especially, when planning the algorithm. The AI initially suggested using alot of the numerical values, which included alot more math and normalization. It didnt take the genre/mood into account alot. This was a time where i inputted my own ideas as well. It was cool to see how the simple algorithms can be combined to crrate a recommendation system. In the future, I would love to add a different mix of songs to see how the dataset impacts the predictions. I would also play around with different scorings and weights. 
Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
