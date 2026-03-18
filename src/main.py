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
    user_profiles = {
        "High Energy Pop": {
            "favorite_genres": ["pop"],
            "favorite_moods": ["happy"],
            "targets": {"energy": 0.8},
            "tolerances": {"energy": 0.2},
        },
        "Chill R&B": {
            "favorite_genres": ["r&b"],
            "favorite_moods": ["calm"],
            "targets": {"energy": 0.3},
            "tolerances": {"energy": 0.2},
        },
        "Rap": {
            "favorite_genres": ["rap"],
            "favorite_moods": ["upbeat"],
            "targets": {"energy": 0.8},
            "tolerances": {"energy": 0.2},
        },
        "cold_start_minimal": {
            "favorite_genres": [],
            "favorite_moods": [],
            "targets": {},
            "tolerances": {},
        },
        "conflicting_signals": {
            "favorite_genres": ["lofi"],
            "favorite_moods": ["intense"],
            "targets": {"energy": 0.90, "tempo_bpm": 150},
            "tolerances": {"energy": 0.05, "tempo_bpm": 5},
        },
        "avoid_everything": {
            "favorite_genres": ["pop"],
            "favorite_moods": ["happy"],
            "avoid_genres": ["pop", "lofi", "rock", "jazz", "ambient", "synthwave", "indie pop"],
            "targets": {"energy": 0.50},
            "tolerances": {"energy": 0.10},
        }
    }

    for profile_name, user_prefs in user_profiles.items():
        print(f"\n=== Top recommendations for {profile_name} ===\n")

        recommendations = recommend_songs(user_prefs, songs, k=5)

        for index, rec in enumerate(recommendations, start=1):
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
