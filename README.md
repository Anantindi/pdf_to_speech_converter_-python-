# PDF to Speech Converter (Python)

Convert your PDF files into MP3 audiobooks with ease! This Python script extracts text from any PDF file and converts it into speech using the [VoiceRSS Text-to-Speech API](https://www.voicerss.org/).

## Features
- Extracts text from PDF files using PyPDF2.
- Converts text to speech with high-quality MP3 output.
- Supports English (US) language.
- Handles up to 2000 characters per request (VoiceRSS free tier limit).
- Easy to use with minimal setup.

## Demo

python main.py
Input PDF: user_sample.pdf

Output MP3: audiobook.mp3

Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/pdf-to-speech.git
cd pdf-to-speech
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Dependencies:

requests

PyPDF2

Place your PDF file in the project folder (e.g., user_sample.pdf).

Getting Your Own VoiceRSS API Key
Visit VoiceRSS.

Click on Get Free API Key.

Register with your email to receive a free API key.

Replace the API_KEY value in main.py with your personal key:

python
Copy code
API_KEY = "your_personal_api_key_here"
Usage
Open main.py and update the pdf_path variable if your PDF has a different name.

Run the script:

bash
Copy code
python main.py
Your MP3 audiobook will be generated as audiobook.mp3.

Notes
The free tier of VoiceRSS allows up to 2000 characters per request. For longer PDFs, only the first 2000 characters will be converted.

Ensure your PDF contains selectable text (not scanned images) for proper extraction.

css
Copy code



requests
PyPDF2

yaml
Copy code



