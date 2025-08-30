# 🧠Alice — Terminal Voice Assistant

**Alice** is a lightweight, voice-activated assistant that runs entirely inside your terminal. It's designed to be fast, modular, and intelligent — capable of listening to your voice, processing it through a local LLM, and replying in real time.

Just say **"Hey Alice"**, and she’s ready to talk, act, or assist.

---

## 🎯 Features

- 🎤 Wake word detection with real-time microphone listening
- 🗣️ Converts speech to text using local STT modules
- 🔊 Responds via text-to-speech using `pyttsx3` or `gTTS`
- 🧠 Smart conversation flow powered by a local LLM
- 💬 Keeps memory of your current session for contextual replies
- ⚙️ Modular structure — each component (voice, prompt, model) is separated
- 🧵 Runs smoothly with multithreading and asynchronous tasks
- 🖥️ Fully terminal-based — no external UI or bloat

---

## 🚧 Under Development

Alice is still under active development. The project is modularized into components like voice input, wake-word detection, prompt handling, and local model inference. You can contribute or follow along as features like command execution, clipboard access, and custom actions are added.

---

## 📦 Dependencies

- Python 3.10+
- `speechrecognition`
- `pyttsx3` or `gTTS`
- `pyaudio`
- `ollama`
- `asyncio`, `threading`, `dotenv`

Install dependencies:

```bash
pip install -r requirements.txt
- Minor doc tweak 1755283524
- Minor doc tweak 1755283526
- Minor doc tweak 1755283533
- Extra note added on Fri Sep  5 11:28:03 IST 2025
- Extra note added on Fri Sep  5 11:28:06 IST 2025
- Extra note added on Fri Sep  5 11:28:08 IST 2025
- Extra note added on Fri Sep  5 11:28:09 IST 2025
- Extra note added on Fri Sep  5 11:28:09 IST 2025
- Extra note added on Fri Sep  5 11:28:12 IST 2025
- Extra note added on Fri Sep  5 11:28:13 IST 2025
- Extra note added on Fri Sep  5 11:28:15 IST 2025
