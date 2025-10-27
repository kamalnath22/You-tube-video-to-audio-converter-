# TODO: Convert YouTube Audio Downloader Script to Website

## Tasks
- [x] Create requirements.txt with dependencies (flask, yt-dlp, moviepy)
- [x] Create app.py: Main Flask app with routes for form display and processing download/conversion
- [x] Create templates/index.html: HTML template for input form
- [x] Create static/styles.css: Basic CSS styling
- [x] Update app.py to include download link for the converted MP3 file after processing
- [x] Install dependencies from requirements.txt
- [x] Run the Flask app locally
- [x] Fix playlist download issue by adding 'noplaylist': True to yt-dlp options
- [x] Fix file access error by using NamedTemporaryFile for MP3 output
- [x] Fix file locking issue by serving MP3 data from memory instead of file
- [ ] Test the website with a single video URL to ensure it downloads and converts only that video to MP3
- [ ] Verify that the MP3 file is correctly generated and triggers a browser download prompt
- [ ] Test error handling (e.g., invalid URL, network issues)
- [ ] Confirm the website interface loads properly and handles form submissions without issues
