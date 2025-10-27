# YouTube Video to Audio Converter

A simple web application built with Flask that allows users to download and convert YouTube videos to MP3 audio files.

## Features

- Download audio from YouTube videos
- Convert videos to high-quality MP3 format
- Clean web interface with responsive design
- Error handling and user feedback
- Temporary file management for security

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kamalnath22/You-tube-video-to-audio-converter-.git
   cd You-tube-video-to-audio-converter-
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Enter a valid YouTube video URL in the input field
2. Click the "Download MP3" button
3. The audio file will be downloaded automatically as an MP3

## Deployment

### Heroku Deployment

1. Sign up for a Heroku account at https://www.heroku.com/
2. Install Heroku CLI from https://devcenter.heroku.com/articles/heroku-cli
3. Login to Heroku:
   ```bash
   heroku login
   ```
4. Create a new Heroku app:
   ```bash
   heroku create your-app-name
   ```
5. Push to Heroku:
   ```bash
   git push heroku master
   ```
6. Open the deployed app:
   ```bash
   heroku open
   ```

Your app will be live at `https://your-app-name.herokuapp.com`

## Dependencies

- Flask: Web framework
- yt-dlp: YouTube video downloader
- moviepy: Video/audio processing library

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is for educational purposes only. Please respect YouTube's Terms of Service and copyright laws when downloading content.
