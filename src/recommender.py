import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

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
    Loads songs from a CSV file into a list of dictionaries.

    Uses Python's csv module. Numeric columns are converted from strings
    to int/float so they can be used in math later; the remaining columns
    stay as strings.

    Required by src/main.py
    """
    songs: List[Dict] = []

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": int(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.

    Implements the Algorithm Recipe from the README:
      - genre match:  +2.0 (genre is more unique, so it is rewarded most)
      - mood match:   +1.0
      - energy:       +1.0 * (1 - |song energy - target energy|)
                      (smaller gap => higher score)
      - acoustic:     +0.5 when the song's acoustic-ness agrees with the
                      user's acoustic preference (only if that pref is given)

    Returns (score, reasons) where reasons explains each points award so the
    user understands the recommendation.

    Required by recommend_songs() and src/main.py
    """
    # --- EXPERIMENT: Weight Shift (sensitivity test) ---
    # Original weights: genre=2.0, mood=1.0, energy=1.0, acoustic=0.5
    # This experiment DOUBLES energy (1.0 -> 2.0) and HALVES genre (2.0 -> 1.0)
    # to see how sensitive the rankings are to the numeric feature vs. the
    # categorical genre match. Restore these to 1.0 / 2.0 to undo.
    GENRE_WEIGHT = 2.0    # experiment used 1.0
    MOOD_WEIGHT = 1.0     # unchanged
    ENERGY_WEIGHT = 1.0   # experiment used 2.0
    ACOUSTIC_WEIGHT = 0.5  # unchanged
    # --- end experiment ---

    score = 0.0
    reasons: List[str] = []

    # Genre match: worth the most because genre is the most distinctive feature.
    if user_prefs.get("genre") is not None and song["genre"] == user_prefs["genre"]:
        score += GENRE_WEIGHT
        reasons.append(f"genre match: {song['genre']} (+{GENRE_WEIGHT})")

    # Mood match.
    if user_prefs.get("mood") is not None and song["mood"] == user_prefs["mood"]:
        score += MOOD_WEIGHT
        reasons.append(f"mood match: {song['mood']} (+{MOOD_WEIGHT})")

    # Energy closeness: reward songs whose energy is near the target energy.
    if user_prefs.get("energy") is not None:
        energy_points = ENERGY_WEIGHT * (1 - abs(song["energy"] - user_prefs["energy"]))
        score += energy_points
        reasons.append(
            f"energy {song['energy']} vs target {user_prefs['energy']} "
            f"({energy_points:+.2f})"
        )

    # Acoustic preference: +0.5 when the song agrees with the user's taste.
    # Only applied when the user actually stated an acoustic preference.
    if user_prefs.get("likes_acoustic") is not None:
        is_acoustic = song["acousticness"] >= 0.5
        if is_acoustic == user_prefs["likes_acoustic"]:
            score += ACOUSTIC_WEIGHT
            reasons.append(f"acoustic preference match (+{ACOUSTIC_WEIGHT})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Scores every song, ranks them from highest to lowest score, and returns
    the top ``k`` as (song_dict, score, explanation) tuples.

    Required by src/main.py
    """
    # Score every song once. A list comprehension is the Pythonic way to build
    # a new list by transforming each item in an existing one.
    scored = [
        (song, *score_song(user_prefs, song))  # (song, score, reasons)
        for song in songs
    ]

    # sorted() returns a NEW list rather than mutating `scored` in place.
    # key=lambda item: item[1] sorts by the score; reverse=True puts the
    # highest scores first.
    ranked = sorted(scored, key=lambda item: item[1], reverse=True)

    # Keep only the top k, turning each reasons list into a readable string.
    return [
        (song, score, "; ".join(reasons) if reasons else "no strong matches")
        for song, score, reasons in ranked[:k]
    ]
