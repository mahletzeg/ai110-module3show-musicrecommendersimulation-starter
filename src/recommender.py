from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """

    songs: List[Dict] = []
    # Read rows as dictionaries keyed by the CSV headers.
    with open(csv_path, "r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                # Convert numeric fields for scoring.
                row["energy"] = float(row["energy"])
                row["valence"] = float(row["valence"])
                row["danceability"] = float(row["danceability"])
                row["acousticness"] = float(row["acousticness"])
                row["tempo_bpm"] = int(row["tempo_bpm"])
            except (KeyError, TypeError, ValueError):
                # Skip rows with missing or malformed values.
                continue
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song using the scoring sheet logic.
    Returns (score, explanation).
    """
    favorite_genres = set(user_prefs.get("favorite_genres", []))
    favorite_moods = set(user_prefs.get("favorite_moods", []))
    avoid_genres = set(user_prefs.get("avoid_genres", []))

    weights = user_prefs.get(
        "weights",
        {
            "genre": 0.30,
            "mood": 0.20,
            "energy": 0.15,
            "tempo_bpm": 0.10,
            "valence": 0.10,
            "danceability": 0.10,
            "acousticness": 0.05,
        },
    )

    targets = user_prefs.get("targets", {})
    tolerances = user_prefs.get("tolerances", {})

    genre = song.get("genre", "")
    mood = song.get("mood", "")

    genre_score = 0.0
    if genre in favorite_genres:
        genre_score = 2.0
    if genre in avoid_genres:
        genre_score = -3.0

    mood_score = 1.0 if mood in favorite_moods else 0.0

    def similarity(feature: str) -> float:
        value = song.get(feature)
        target = targets.get(feature)
        tolerance = tolerances.get(feature)
        if value is None or target is None or not tolerance:
            return 0.0
        distance = abs(value - target)
        return max(0.0, 1.0 - (distance / tolerance))

    energy_sim = similarity("energy")
    tempo_sim = similarity("tempo_bpm")
    valence_sim = similarity("valence")
    dance_sim = similarity("danceability")
    acoustic_sim = similarity("acousticness")

    base = (
        genre_score * weights.get("genre", 0.0)
        + mood_score * weights.get("mood", 0.0)
        + energy_sim * weights.get("energy", 0.0)
        + tempo_sim * weights.get("tempo_bpm", 0.0)
        + valence_sim * weights.get("valence", 0.0)
        + dance_sim * weights.get("danceability", 0.0)
        + acoustic_sim * weights.get("acousticness", 0.0)
    )

    avoid_penalty = 0.40 if genre in avoid_genres else 0.0

    novelty_bonus = 0.0
    if genre not in favorite_genres and genre not in avoid_genres:
        novelty_bonus = float(user_prefs.get("novelty_bias", 0.0))

    diversity_bonus = 0.0
    seen_genres = set(user_prefs.get("seen_genres", []))
    seen_moods = set(user_prefs.get("seen_moods", []))
    if genre and mood and (genre not in seen_genres or mood not in seen_moods):
        diversity_bonus = float(user_prefs.get("diversity", 0.0)) * 0.05

    score = base - avoid_penalty + novelty_bonus + diversity_bonus

    explanation_parts: List[str] = []
    if genre in favorite_genres:
        explanation_parts.append("genre match (+2.0)")
    if mood in favorite_moods:
        explanation_parts.append("mood match (+1.0)")
    if genre in avoid_genres:
        explanation_parts.append("avoid genre penalty (-3.0)")
    if energy_sim > 0:
        explanation_parts.append(f"energy similarity ({energy_sim:.2f})")
    if tempo_sim > 0:
        explanation_parts.append(f"tempo similarity ({tempo_sim:.2f})")
    if valence_sim > 0:
        explanation_parts.append(f"valence similarity ({valence_sim:.2f})")
    if dance_sim > 0:
        explanation_parts.append(f"danceability similarity ({dance_sim:.2f})")
    if acoustic_sim > 0:
        explanation_parts.append(f"acousticness similarity ({acoustic_sim:.2f})")
    if energy_sim > 0 or tempo_sim > 0 or valence_sim > 0 or dance_sim > 0 or acoustic_sim > 0:
        pass
    if not explanation_parts:
        explanation_parts.append("no strong matches")
    return score, explanation_parts

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    top_k = sorted(
        ((song, *score_song(user_prefs, song)) for song in songs),
        key=lambda item: item[1],
        reverse=True
    )[:k]
    return top_k
