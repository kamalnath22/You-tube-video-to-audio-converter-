import os
from moviepy.editor import AudioFileClip
from yt_dlp import YoutubeDL

# Step 1: Get YouTube link
link = input("Enter YouTube video link: ")

# Step 2: Download audio (best quality)
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'quiet': False,
}

with YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(link, download=True)
    filename = ydl.prepare_filename(info)

# Step 3: Convert to MP3
base, ext = os.path.splitext(filename)
mp3_file = base + ".mp3"

# Convert using moviepy
print("\nConverting to MP3...")
clip = AudioFileClip(filename)
clip.write_audiofile(mp3_file)
clip.close()

# Optional: remove original file (usually .webm or .m4a)
if os.path.exists(filename):
    os.remove(filename)

print(f"\n✅ Downloaded and converted successfully: {mp3_file}")
