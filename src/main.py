"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from .recommender import load_songs, recommend_songs
except ImportError:
    from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Starter example profile (matches scoring keys)
    user_prefs = {
        "favorite_genres": ["pop"],
        "favorite_moods": ["happy"],
        "targets": {"energy": 0.8},
        "tolerances": {"energy": 0.2},
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for index, rec in enumerate(recommendations, start=1):
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        if isinstance(explanation, list):
            reasons = "; ".join(explanation)
        else:
            reasons = str(explanation)
        print(f"{index}. {song['title']} - Score: {score:.2f}")
        print(f"   Reasons: {reasons}")
        print()


if __name__ == "__main__":
    main()
