from flask import Flask, request, render_template, send_file, flash, redirect, url_for
import os
from moviepy.editor import AudioFileClip
from yt_dlp import YoutubeDL
import tempfile

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a random secret key

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        link = request.form.get('youtube_link')
        if not link:
            flash('Please provide a YouTube link.')
            return redirect(url_for('index'))

        try:
            # Create a temporary directory for downloads
            with tempfile.TemporaryDirectory() as temp_dir:
                # Step 1: Download audio (best quality)
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': os.path.join(temp_dir, '%(title)s.%(ext)s'),
                    'quiet': False,
                    'noplaylist': True,  # Download only single video, not playlists
                }

                with YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(link, download=True)
                    filename = ydl.prepare_filename(info)

                # Step 2: Convert to MP3
                print("\nConverting to MP3...")
                clip = AudioFileClip(filename)
                # Create a temporary file for the MP3 that persists
                mp3_temp = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
                mp3_temp.close()  # Close the file handle so moviepy can write
                mp3_file = mp3_temp.name
                clip.write_audiofile(mp3_file)
                clip.close()

                # Optional: remove original file
                if os.path.exists(filename):
                    os.remove(filename)

                # Load the MP3 into memory to avoid file locking issues
                with open(mp3_file, 'rb') as f:
                    mp3_data = f.read()

                # Clean up the temporary file immediately
                if os.path.exists(mp3_file):
                    os.remove(mp3_file)

                # Serve the MP3 data from memory
                from io import BytesIO
                return send_file(BytesIO(mp3_data), as_attachment=True, download_name=os.path.basename(mp3_file))

        except Exception as e:
            flash(f'An error occurred: {str(e)}')
            return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
