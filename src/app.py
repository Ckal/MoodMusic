import gradio as gr
from deepface import DeepFace
import random

# Sample playlists for different moods
playlists = {
    "happy": ["Happy - Pharrell Williams", "Can't Stop the Feeling - Justin Timberlake", "Good Vibrations - The Beach Boys"],
    "sad": ["Someone Like You - Adele", "Fix You - Coldplay", "Stay With Me - Sam Smith"],
    "angry": ["Break Stuff - Limp Bizkit", "Killing In The Name - Rage Against The Machine", "Duality - Slipknot"],
    "surprise": ["Surprise Yourself - Jack Garratt", "Suddenly I See - KT Tunstall", "Unexpected - Anna Clendening"],
    "fear": ["Fear of the Dark - Iron Maiden", "Disturbia - Rihanna", "Creep - Radiohead"],
    "disgust": ["Dirty Laundry - Don Henley", "Toxic - Britney Spears", "Bad Blood - Taylor Swift"],
    "neutral": ["Let It Be - The Beatles", "Imagine - John Lennon", "Bohemian Rhapsody - Queen"]
}

def analyze_mood(image):
    try:
        analysis = DeepFace.analyze(image, actions=['emotion'], enforce_detection=False)
        dominant_emotion = analysis[0]['dominant_emotion']
        recommended_playlist = playlists.get(dominant_emotion, playlists["neutral"])
        return f"Detected Mood: {dominant_emotion.capitalize()}\n\nRecommended Playlist:\n- " + "\n- ".join(random.sample(recommended_playlist, 3))
    except Exception as e:
        return f"An error occurred: {str(e)}"

iface = gr.Interface(
    fn=analyze_mood,
    inputs=gr.Image(type="filepath", label="Upload Your Selfie"),
    outputs="text",
    title="MoodMuse 🎵",
    description="Upload a selfie, and MoodMuse will analyze your facial expression to recommend a playlist that matches your mood."
)

iface.launch()
