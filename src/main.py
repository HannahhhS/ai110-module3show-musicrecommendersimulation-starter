"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs

# Three distinct, "normal" user profiles.
NORMAL_PROFILES = [
    ("High-Energy Pop", {"genre": "pop", "mood": "happy", "energy": 0.9}),
    (
        "Chill Lofi",
        {"genre": "lofi", "mood": "chill", "energy": 0.3, "likes_acoustic": True},
    ),
    ("Deep Intense Rock", {"genre": "rock", "mood": "intense", "energy": 0.9}),
]

# Adversarial / edge-case profiles: built to try to "trick" the scoring logic
# and surface unexpected results.
EDGE_CASE_PROFILES = [
    # Conflicting signals: "melancholy" mood usually implies LOW energy, but
    # this user also demands very HIGH energy. Which signal wins?
    (
        "Conflicting: Sad but Energetic",
        {"genre": "pop", "mood": "melancholy", "energy": 0.95},
    ),
    # Conflicting signals: wants aggressive, high-energy metal but ALSO prefers
    # acoustic music -- metal is almost never acoustic, so genre and the
    # acoustic preference pull in opposite directions.
    (
        "Conflicting: Acoustic Metalhead",
        {"genre": "metal", "mood": "aggressive", "energy": 0.9, "likes_acoustic": True},
    ),
    # Empty profile: no preferences at all -> every song should tie at 0.0,
    # exposing whatever the tie-breaking / default order happens to be.
    ("Empty Profile (no preferences)", {}),
]

# Everything to run, in order.
PROFILES = NORMAL_PROFILES + EDGE_CASE_PROFILES


def print_recommendations(name: str, user_prefs: dict, songs: list, k: int = 5) -> None:
    """Run the recommender for one profile and print its top-k results."""
    recommendations = recommend_songs(user_prefs, songs, k=k)

    # Header describing the profile we recommended for.
    print("\n" + "=" * 50)
    print(f"  PROFILE: {name}")
    print(f"  prefs: {user_prefs}")
    print("=" * 50 + "\n")

    if not recommendations:
        print("  (no recommendations)\n")
        return

    for rank, rec in enumerate(recommendations, start=1):
        # Each item is (song, score, explanation).
        song, score, explanation = rec

        print(f"{rank}. {song['title']} - {song['artist']}")
        print(f"   Score: {score:.2f}")
        print("   Reasons:")
        # The explanation is a "; "-joined string of reasons from score_song;
        # show each reason on its own line for readability.
        for reason in explanation.split("; "):
            print(f"     - {reason}")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Run the recommender for every profile so we can compare the results.
    for name, user_prefs in PROFILES:
        print_recommendations(name, user_prefs, songs, k=5)


if __name__ == "__main__":
    main()
