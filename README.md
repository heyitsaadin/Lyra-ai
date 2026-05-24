#  Jarvis AI

A personal AI chatbot web app powered by **Groq LLaMA**, built with Flask and deployed on Vercel. Jarvis has a warm, conversational personality, supports image generation and analysis, real-time math, and a full user authentication system with a PostgreSQL backend.

 **Live Demo:** [jarvis-ai-aadin.vercel.app](https://jarvis-ai-aadin.vercel.app/)

---

##  Features

- **AI Chat** — Powered by Groq's LLaMA 3.1 model. Jarvis replies conversationally, matches user energy, uses emojis naturally, and keeps responses short unless detail is asked for.
- **Image Generation** — Generate images from text prompts via Pollinations.ai (no API key needed). Supports download of generated images.
- **Image Analysis & Editing** — Upload an image and ask Jarvis to describe, analyse, or edit it. Analysis uses Groq's LLaMA 4 Scout vision model; editing uses NVIDIA's Qwen image-edit model.
- **Smart Math** — Automatically detects arithmetic expressions and evaluates them safely, saving results to calculation history.
- **Time & Date Awareness** — Jarvis knows the current IST time and date and answers naturally when asked.
- **Code Formatting** — Detects code requests and responds with proper markdown code blocks with syntax highlighting.
- **User Profiles** — Tracks user interests, message patterns, peak hours, and sentiment using keyword scoring. Every 15 messages, Groq enriches the profile with a smarter AI-generated summary.
- **User Authentication** — Sign up / log in with hashed passwords (Werkzeug). Sessions persist for 30 days.
- **Admin Dashboard** — Password-protected panel showing registered users, visit stats (last 7 days), calculation history, and user profiles.
- **Security Alerts** — Discord webhook alerts fire when a user attempts to extract secrets, claims owner identity, or uses abusive language.
- **Dark / Light Mode** — Full theme toggle with smooth transitions across all pages.
- **Privacy & Terms Page** — Dedicated beta terms and privacy policy page.
- **Custom 404 / 500 Pages** — Friendly error pages instead of raw Flask errors.

---

##  Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| AI / LLM | Groq API (LLaMA 3.1 8B, LLaMA 4 Scout 17B vision) |
| Image Generation | Pollinations.ai |
| Image Editing | NVIDIA API (Qwen image-edit) |
| Database | PostgreSQL via Neon (psycopg2) |
| Frontend | HTML, CSS, Vanilla JS, Marked.js |
| Deployment | Vercel |
| Analytics | Vercel Web Analytics |
| Alerts | Discord Webhooks |

---

## Project Structure

```
Jarvis-Ai/
├── app.py              # Main Flask app — all routes and logic
├── templates/
│   ├── landing.html    # Post-login landing page
│   ├── chat.html       # Main chat interface
│   ├── login.html      # Login page
│   ├── signup.html     # Sign up page
│   ├── privacy.html    # Beta terms & privacy policy
│   ├── quiz.html       # Quiz page
│   ├── 404.html        # Custom 404 error page
│   └── 500.html        # Custom 500 error page
└── README.md
```

---

## Environment Variables

Never commit secrets. Set these in your Vercel project settings (or a local `.env` file):

| Variable | Description |
|---|---|
| `SECRET_KEY` | Flask session secret key |
| `DATABASE_URL` | Neon PostgreSQL connection string |
| `GROQ_API_KEY` | Primary Groq API key (chat + profile) |
| `GROQ_API_KEY_2` | Secondary Groq key for vision (higher limits) |
| `NVIDIA_API_KEY` | NVIDIA API key for image editing |
| `ADMIN_PASSWORD` | Password for the `/admin` dashboard |
| `OWNER_CODE` | Secret owner verification code |
| `DISCORD_WEBHOOK` | Discord webhook URL for security alerts |

---

##  Running Locally

```bash
# 1. Clone the repo
git clone https://github.com/heyitsaadin/Jarvis-Ai.git
cd Jarvis-Ai

# 2. Install dependencies
pip install flask requests psycopg2-binary werkzeug

# 3. Set environment variables (create a .env or export manually)
export GROQ_API_KEY=your_key_here
export DATABASE_URL=your_neon_db_url
export SECRET_KEY=any_random_string
export ADMIN_PASSWORD=your_admin_password
export OWNER_CODE=your_owner_code
export DISCORD_WEBHOOK=your_webhook_url

# 4. Run
python app.py
```

Then open [http://localhost:5000](http://localhost:5000)

---

##  Database

Uses **Neon PostgreSQL**. Tables are auto-created on first run via `init_db()`:

- `users` — username + hashed password
- `history` — per-user calculation history
- `visits` — timestamped page visits for analytics
- `user_profiles` — JSON-stored interest profiles, sentiment, message stats

---

##  Security Notes

- Passwords are hashed using Werkzeug's `generate_password_hash`
- Flask secret key is randomly generated if not set via env
- Math evaluation uses a strict regex allowlist — no arbitrary `eval`
- Owner identity verification uses a secret code flow, not just a claim
- Attempted secret extraction and abusive messages trigger Discord alerts
- All API keys and secrets are loaded from environment variables only — never hardcoded

---

## Built By

**Aadin KC** — [Portfolio](https://aadinkc-portfolio.vercel.app/) · [GitHub](https://github.com/heyitsaadin) · [LinkedIn](https://www.linkedin.com/in/aadin-kc-128bb3371)
