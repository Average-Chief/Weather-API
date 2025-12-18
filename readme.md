# 🌦️ Weather API with Caching (Flask)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask">
  <img src="https://img.shields.io/badge/Jinja2-Templates-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Redis-Caching-red?style=for-the-badge&logo=redis">
</p>

<p align="center">
  <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmdmaGQycWk1YmxuN3JodzVxMjZza3V0MmRubHAyamJmb3gwdGp3dSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QNFhOolVeCzPQ2Mx85/giphy.gif" alt="gif"/>
</p>

A backend-focused Flask project that fetches weather data from a **3rd‑party API**, caches responses using a **Redis‑like in‑memory cache**, and serves results via a clean server‑rendered UI.

This project is intentionally designed to emphasize **API integration, caching logic, environment variables, and clean architecture** — not frontend complexity.

## 📷 Screenshots
### Home Screen
<p align="center">
  <img src="https://media.discordapp.net/attachments/1163559454000816242/1451112879368441991/Screenshot_2025-12-18_014733.png?ex=6944fdae&is=6943ac2e&hm=752da7ef12e34c2482dac65607322996bf05ca8ac1b8a0056f167d183a46b682&=&format=webp&quality=lossless&width=758&height=526" alt="image1"/>
</p>

### Backend Output
<p align="center">
  <img src="https://media.discordapp.net/attachments/1163559454000816242/1451113282441187452/Screenshot_2025-12-18_014804.png?ex=6944fe0e&is=6943ac8e&hm=54ede2b8246f9b2169c665454f9dcb202f63aa8e24e98b68ab013e1442a9ebec&=&format=webp&quality=lossless&width=729&height=818" alt="image2"/>
</p>

## 🚀 Features

* 🔌 Fetches weather data from a 3rd‑party provider (Visual Crossing)
* 🧠 Caching layer with TTL (Redis‑like behavior, pure Python)
* ⏱️ Automatic cache expiry (12 hours)
* 🔐 Environment variable–based configuration
* 🧩 Clean separation of concerns (Flask / service / cache)
* 🖥️ Simple server‑rendered UI (no JavaScript required)


## 🏗️ Project Structure

```
project/
│
├── app.py                # Flask app (routes & orchestration)
├── weather_service.py    # 3rd‑party weather API logic
├── cache.py              # In‑memory Redis‑like cache with TTL
│
├── templates/
│   └── index.html        # UI template
│
├── static/
│   └── styles.css        # Basic styling
│
├── .env                  # Environment variables (not committed)
├── .env.example          # Env template
├── requirements.txt
└── README.md
```


## ⚙️ How It Works (High‑Level Flow)

```
User submits form
      ↓
Flask route (/weather)
      ↓
Check cache (key = city + date range)
      ↓
Cache hit? → return cached data
Cache miss? → call 3rd‑party API
                     ↓
                store in cache (with TTL)
                     ↓
                return result
```


## 🧠 Caching Strategy

* Implemented a **Redis‑like in‑memory cache** using Python dictionaries
* Each cache entry stores:

  * the response data
  * an expiration timestamp (TTL)
* Expired entries are automatically removed on access

### Why fake Redis?

Redis does not officially support Windows. To avoid unnecessary setup complexity, this project uses an **in‑memory cache that mimics Redis behavior**.

The cache layer is **abstracted**, so swapping to real Redis later requires minimal changes.


## 🔁 Swapping to Real Redis (Future‑Ready)

When deploying to Linux / Docker / Cloud:

* Replace cache internals with `redis-py`
* Keep the same `get_cache()` and `set_cache()` interface

No changes required in `app.py`.


## 🔐 Environment Variables

Create a `.env` file based on `.env.example`:

```
BASE_URL=https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/
API_KEY=your_api_key_here
```

> ⚠️ Never commit `.env` to version control.


## ▶️ Running the Project

### 1️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 2️⃣ Run Flask app

```
python app.py
```

### 3️⃣ Open in browser

```
http://127.0.0.1:5000
```


## 📦 Example Output

The application currently displays the **raw JSON response** from the weather provider for transparency and debugging purposes.

This is intentional and aligns with API‑first design principles.


## 🧪 Error Handling

* Missing form fields → user‑friendly error
* API failure → graceful message
* Cache handles expiration automatically


## 📌 Notes

* This project focuses on **backend engineering**, not frontend design
* No JavaScript is used (by choice)
* Ideal for demonstrating API usage, caching, and clean architecture


## 📈 Possible Enhancements

* Normalize weather response (temperature, humidity, condition)
* Add rate limiting
* Add logging
* Replace fake cache with real Redis
* Expose a pure JSON API endpoint


## 🧠 Key Takeaway

> Redis is not magic — it’s a fast key‑value store with expiration.
> This project demonstrates that concept clearly and cleanly.


## 👤 Author

Built with focus on backend fundamentals and practical system design.


⭐ If you found this useful, consider starring the repo!

Project: https://roadmap.sh/projects/blogging-platform-api
