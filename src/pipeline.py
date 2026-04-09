from src.data_loader import load_data
from src.retrieval import *
import pickle
import re

# Load data
matches, deliveries, players, stats, teams, home_away = load_data()

# Load ML model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict(q):
    return model.predict(vectorizer.transform([q]))[0]


# =========================
# 🔹 FORMAT FUNCTION
# =========================
def format_top5(data, title, label):
    result = f"{title}:\n"
    for i, (player, value) in enumerate(data.items(), 1):
        result += f"{i}. {player} - {value} {label}\n"
    return result


# =========================
# 🔹 MAIN FUNCTION
# =========================
def answer_question(q):

    q = q.lower()

    # =========================
    # 🔥 TOP PRIORITY (FIX WRONG OUTPUT ISSUE)
    # =========================

    year = re.findall(r"\d{4}", q)


    if year:
      y = int(year[0])

    # ✅ VALID IPL YEARS CHECK
      if y < 2008 or y > 2019:
        return "Data available only for IPL seasons between 2008 and 2019."

    # continue normal processing
      data = filter_by_year(deliveries, matches, y)

    # ---------- TOP 5 BATSMEN ----------
    if "top 5 batsmen" in q:
        if year:
            y = year[0]
            data = filter_by_year(deliveries, matches, y)
            return format_top5(get_top5_batsmen(data), f"Top 5 Batsmen in {y}", "runs")
        return format_top5(get_top5_batsmen(deliveries), "Top 5 Batsmen (All Time)", "runs")

    # ---------- TOP 5 BOWLERS ----------
    if "top 5 bowlers" in q:
        if year:
            y = year[0]
            data = filter_by_year(deliveries, matches, y)
            return format_top5(get_top5_bowlers(data), f"Top 5 Bowlers in {y}", "wickets")
        return format_top5(get_top5_bowlers(deliveries), "Top 5 Bowlers (All Time)", "wickets")

    # ---------- TITLES ----------
    if "titles" in q:
        t, c = get_most_titles(matches)
        return f"{t} won most IPL titles ({c})"

    # =========================
    # 🔹 YEAR BASED
    # =========================

    if year:
        y = year[0]
        data = filter_by_year(deliveries, matches, y)

        if "best batsman" in q or "best player" in q:
            p, r = get_top_scorer_year(data)
            return f"{p} is the best batsman in {y} with {r} runs"

        if "run" in q:
            p, r = get_top_scorer_year(data)
            return f"{p} scored most runs in {y} ({r})"

        if "six" in q:
            p, s = get_most_sixes_year(data)
            return f"{p} hit most sixes in {y} ({s})"

        if "four" in q or "boundar" in q:
            p, f = get_most_fours_year(data)
            return f"{p} hit most fours in {y} ({f})"

        if "wicket" in q or "bowler" in q:
            p, w = get_most_wickets_year(data)
            return f"{p} took most wickets in {y} ({w})"

        return f"Winner in {y}: {get_season_winner(matches, y)}"
    
    # Detect non-IPL / future questions
    if any(x in q for x in ["will", "future", "next year", "predict"]):
        return "Sorry, I can only answer IPL historical statistics questions."

    # =========================
    # 🔹 ML INTENT
    # =========================

    intent = predict(q)

    if intent == "runs":
        p, r = get_top_scorer(deliveries)
        return f"{p} is the top batsman in IPL with {r} runs"

    if intent == "sixes":
        p, s = get_most_sixes(deliveries)
        return f"{p} hit most sixes ({s})"

    if intent == "fours":
        p, f = get_most_fours(deliveries)
        return f"{p} hit most fours ({f})"

    if intent == "wickets":
        p, w = get_most_wickets(deliveries)
        return f"{p} took most wickets ({w})"

    if intent == "wins":
        t, w = get_most_wins(matches)
        return f"{t} won most matches ({w})"

    if intent == "match":
        return f"Latest match winner: {get_latest_match_winner(matches)}"

    # =========================
    # 🔹 EXTRA RULES
    # =========================

    if "strike rate" in q:
        p, sr = get_best_strike_rate(stats)
        return f"{p} has best strike rate ({sr})"

    if "average" in q:
        p, avg = get_best_average(stats)
        return f"{p} has best average ({avg})"

    if "economy" in q:
        b, e = get_best_economy(deliveries)
        return f"{b} has best economy ({e})"

    if "best batsman" in q or "king" in q:
        p, r = get_top_scorer(deliveries)
        return f"{p} is the best batsman with {r} runs"
    
    

    # =========================
    # 🔹 FALLBACK
    # =========================

    return "Sorry, I cannot answer this question."