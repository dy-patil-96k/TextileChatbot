# Textile Website + Chatbot Demo

This project includes:
- A dummy textile website homepage.
- An attached textile chatbot.
- A simple "training" dataset in `data/textile_knowledge.json`.

## Run locally

1. Activate your virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the app:
   ```bash
   python main.py
   ```
4. Open:
   ```text
   http://127.0.0.1:5000
   ```

## Train / update chatbot knowledge

Edit `data/textile_knowledge.json` and add more Q&A entries.
The chatbot reads this file at startup and uses similarity matching on questions.
