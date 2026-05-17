# app.py – główny plik aplikacji Flask
# Uruchom: python app.py, a następnie otwórz http://localhost:5000

from flask import Flask, render_template
from datetime import datetime

# Inicjalizacja aplikacji Flask
app = Flask(__name__)

# ── Konfiguracja ──────────────────────────────────────────────
# Data i godzina rozpoczęcia wakacji – zmień według potrzeb!
WAKACJE_START = datetime(2026, 6, 25, 0, 0, 0)
# ──────────────────────────────────────────────────────────────


@app.route("/")
def index():
    """
    Widok strony głównej.
    Przekazuje datę wakacji do szablonu HTML jako napis ISO 8601,
    dzięki czemu JavaScript może ją poprawnie sparsować.
    """
    wakacje_iso = WAKACJE_START.isoformat()  # np. "2025-06-20T00:00:00"
    return render_template("index.html", wakacje_iso=wakacje_iso)


if __name__ == "__main__":
    # Tryb debug = True ułatwia development (auto-reload przy zmianach)
    app.run(debug=True)
