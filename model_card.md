# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

My model is called VibeFinder 1.0.

---

## 2. Intended Use

- What kind of recommendations does it generate: A few top songs from a small catalog.
- What assumptions does it make about the user: The user has clear genre and mood preferences plus numeric targets.
- Is this for real users or classroom exploration: Classroom exploration only.

---

## 3. How the Model Works

- What features of each song are used: Genre, mood, energy, tempo, valence, danceability, acousticness.
- What user preferences are considered: Favorite genres and moods plus target values and tolerances.
- How does the model turn those into a score: It adds weighted points for matches and closeness.
- What changes did you make from the starter logic: I added weights and tolerance-based similarity.

---

## 4. Data

- How many songs are in the catalog: 18 songs.
- What genres or moods are represented: Pop, lofi, rock, jazz, ambient, r&b, and more.
- Did you add or remove data: I added new rows to expand genres and moods.
- Are there parts of musical taste missing in the dataset: Yes, many styles of music and languages are missing.

---

## 5. Strengths

- User types for which it gives reasonable results: Clear genre and mood profiles.
- Any patterns you think your scoring captures correctly: It separates chill vs. high energy.
- Cases where the recommendations matched your intuition: Pop and lofi profiles ranked as expected.

---

## 6. Limitations and Bias

- Features it does not consider: lyrics, language, artist loyalty, or context like time of day.
- Genres or moods that are underrepresented: the catalog is small, so many styles are missing or rare.
- Cases where the system overfits to one preference: genre matches can dominate, so the same songs repeat.
- Ways the scoring might unintentionally favor some users: strict tolerances can penalize users with broader tastes and reduce variety.

---

## 7. Evaluation

- Which user profiles you tested: Happy Pop, Chill Lofi, and Workout.
- What you looked for in the recommendations: Mood and energy alignment at the top.
- What surprised you: Gym Hero showed up for Happy Pop users.
- Any simple tests or comparisons you ran: I compared top results across the profiles.

---

## 8. Future Work

- Additional features or preferences: Artist likes and dislikes.
- Better ways to explain recommendations: Short, human-readable reasons per song.
- Improving diversity among the top results: Add a stronger diversity boost.
- Handling more complex user tastes: Support multiple moods per profile.

---

## 9. Personal Reflection

- What you learned about recommender systems: Small weight changes can shift rankings.
- Something unexpected or interesting you discovered: The same songs repeated often.
- How this changed the way you think about music recommendation apps: I notice the tradeoff between relevance and discovery.
