# 🤖 Jarvis – Python Voice-Controlled AI Assistant

Jarvis is a smart voice-controlled AI assistant written in Python. It uses speech recognition and OpenAI's GPT model to perform a variety of tasks including opening websites, playing music, reading the news, and answering general queries.

---

## 🎯 Features

- 🎙 Voice command recognition using Google Speech Recognition
- 🧠 AI-powered conversation with OpenAI (ChatGPT 4.1)
- 📺 Open popular websites like Google, YouTube, LinkedIn, Facebook
- 🎵 Play pre-defined music links from YouTube using custom keywords
- 📰 Fetch latest Indian news headlines via NewsAPI
- 🔊 Dual text-to-speech options: `gTTS` and `pyttsx3`
- 🧩 Modular design (`musiclibrary.py`, `client.py`)

---

## 📁 File Structure

jarvis/
├── jarvis.py # Main assistant logic and command handler
├── client.py # Sample test to use OpenAI for simple input
├── musiclibrary.py # Predefined songs mapped to YouTube links
├── apikey.txt # (Unsafe) OpenAI or NewsAPI key (DO NOT upload)
├── open ai api key .txt # Actual OpenAI key (you should use env vars)
└── README.md # Project documentation


---

## 🧠 Technologies Used

- Python 3.8+
- `speech_recognition` – speech to text
- `gTTS` / `pyttsx3` – text to speech
- `pygame` – for MP3 playback
- `requests` – API calls (news, OpenAI)
- `openai` – AI model for freeform tasks
- `webbrowser` – to open websites

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/jaiswalmegh/jarvis
cd jarvis
### 2. Install dependencies: pip install -r requirements.txt
If you don’t have a requirements.txt, use: pip install speechrecognition pyttsx3 gtts pygame openai requests

3. Add your API keys
Replace "your api key here" in jarvis.py and client.py with your OpenAI key.

For news:newsapi = {"your api here"}
4. Run Jarvis:  python jarvis.py


🎵 Example Commands
"Jarvis" (Wake Word)

"Open YouTube"

"Play skyfall"

"Open Google"

"News"

"What is quantum computing?"

Jarvis listens for "Jarvis", then activates for your next voice input.

🔐 Security Tips
🚫 Never upload your API keys to GitHub!
Use environment variables or a .env file with a loader (e.g., python-dotenv).

✅ TODO
 Add calendar/reminder integration

 Add error logging and fallback responses

 Add GUI using PyQt/Tkinter

 Add dynamic music fetching (not hardcoded)

📃 License
This project is licensed under the MIT License.

🙋‍♂️ Author
Megh Jaiswal
GitHub: @jaiswalmegh

🤝 Contributing

