import requests
import PyPDF2

API_KEY = "your_personal_api_key_here"  # Replace with your VoiceRSS API key

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text[:2000]  # VoiceRSS free tier = 2000 chars

def text_to_speech(text, output_file="audiobook.mp3"):
    """Convert text to speech using VoiceRSS API."""
    url = "https://api.voicerss.org/"
    params = {
        "key": API_KEY,
        "hl": "en-us",
        "src": text,
        "c": "MP3",
        "f": "44khz_16bit_stereo"
    }

    response = requests.get(url, params=params)
    print("Request URL:", response.url)  # Debug

    if response.status_code == 200:
        if response.headers.get("Content-Type", "").startswith("audio"):
            with open(output_file, "wb") as f:
                f.write(response.content)
            print(f"✅ Audio saved as {output_file}")
        else:
            print("❌ API Error:", response.text[:500])
    else:
        print("❌ Request failed:", response.status_code, response.text[:500])


if __name__ == "__main__":
    pdf_path = "user_sample.pdf"
    print("Extracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)

    if text:
        print("Converting to speech...")
        text_to_speech(text, "audiobook.mp3")
    else:
        print("❌ No text found in PDF!")
