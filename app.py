from flask import Flask, jsonify, render_template_string, request
from movies_data import MOVIES, ALL_GENRES, ALL_LANGUAGES
import os

app = Flask(__name__)

HTML_PATH = os.path.join(os.path.dirname(__file__), "index.html")

# ── Home page ─────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    with open(HTML_PATH, encoding="utf-8") as f:
        return render_template_string(
            f.read(),
            genres=ALL_GENRES,
            languages=ALL_LANGUAGES,
            total=len(MOVIES),
        )

# ── Browse: filter by genre + language, sort by rating desc ──────────────────
@app.route("/browse", methods=["POST"])
def browse():
    data     = request.get_json(silent=True) or {}
    genre    = (data.get("genre")    or "All").strip()
    language = (data.get("language") or "All").strip()

    results = []
    for m in MOVIES:
        genre_match    = (genre    == "All") or (genre    in m["genres"])
        language_match = (language == "All") or (language == m["language"])
        if genre_match and language_match:
            results.append({
                "title":    m["title"],
                "language": m["language"],
                "year":     m["year"],
                "rating":   m["rating"],
                "genres":   m["genres"],
                "desc":     m["desc"],
            })

    # Sort by rating (highest first)
    results.sort(key=lambda x: x["rating"], reverse=True)

    if not results:
        return jsonify({"movies": [], "count": 0,
                        "message": f"No {genre} movies found for {language}."}), 200

    return jsonify({"movies": results, "count": len(results)})

if __name__ == "__main__":
    app.run(debug=True, port=5001)   # port 5001 so both apps can run together
