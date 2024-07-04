from flask import Flask, render_template, url_for
import random

app = Flask(__name__)

verses = [
    "This is the verse of the song, where the story begins.",
    "As we move through the verse, we see where it leads.",
    "In the second verse, the plot starts to thicken.",
    "Here's another verse, continuing the tale."
]

choruses = [
    "Chorus part one, everyone sing along!",
    "Chorus number two, this one's for you!",
    "Sing the chorus thrice, make it sound nice!",
    "Here comes the chorus again, bring it to an end."
]

verse_audio_files = ['verse1.mp3', 'verse2.mp3', 'verse3.mp3', 'verse4.mp3']
chorus_audio_files = ['chorus1.mp3', 'chorus2.mp3', 'chorus3.mp3', 'chorus4.mp3']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_song', methods=['POST'])
def get_song():
    verse1 = random.choice(verses)
    verse2 = random.choice(verses)
    chorus = random.choice(choruses)
    verse1_audio = random.choice(verse_audio_files)
    verse2_audio = random.choice(verse_audio_files)
    chorus_audio = random.choice(chorus_audio_files)
    return render_template('song.html', verse1=verse1, verse2=verse2, chorus=chorus, verse1_audio=verse1_audio, verse2_audio=verse2_audio, chorus_audio=chorus_audio)

if __name__ == '__main__':
    app.run(debug=True)
