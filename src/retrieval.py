import pandas as pd

# =========================
# 🔹 SAFE COLUMN HANDLING
# =========================
def get_batsman_col(df):
    return "batter" if "batter" in df.columns else "batsman"


# =========================
# 🔹 TOP SCORER (ALL TIME)
# =========================
def get_top_scorer(deliveries):
    col = get_batsman_col(deliveries)
    runs = deliveries.groupby(col)["batsman_runs"].sum()
    return runs.idxmax(), int(runs.max())


# =========================
# 🔹 SIXES
# =========================
def get_most_sixes(deliveries):
    col = get_batsman_col(deliveries)
    sixes = deliveries[deliveries["batsman_runs"] == 6]
    count = sixes.groupby(col).size()
    return count.idxmax(), int(count.max())


# =========================
# 🔹 FOURS
# =========================
def get_most_fours(deliveries):
    col = get_batsman_col(deliveries)
    fours = deliveries[deliveries["batsman_runs"] == 4]
    count = fours.groupby(col).size()
    return count.idxmax(), int(count.max())


# =========================
# 🔹 WICKETS (FIXED)
# =========================
def get_most_wickets(deliveries):
    valid = deliveries[
        deliveries["dismissal_kind"].notna() &
        (deliveries["dismissal_kind"] != "run out")
    ]
    count = valid.groupby("bowler").size()
    return count.idxmax(), int(count.max())


# =========================
# 🔹 TEAM WINS
# =========================
def get_most_wins(matches):
    wins = matches["winner"].value_counts()
    return wins.idxmax(), int(wins.max())


# =========================
# 🔹 LATEST MATCH
# =========================
def get_latest_match_winner(matches):
    matches["date"] = pd.to_datetime(matches["date"], dayfirst=True)
    latest = matches.sort_values("date").iloc[-1]
    return latest["winner"]


# =========================
# 🔹 SEASON WINNER
# =========================
def get_season_winner(matches, year):
    matches["date"] = pd.to_datetime(matches["date"], dayfirst=True)
    matches["year"] = matches["date"].dt.year

    season = matches[matches["year"] == int(year)]
    if season.empty:
        return "No data"

    final = season.sort_values("date").iloc[-1]
    return final["winner"]


# =========================
# 🔹 ECONOMY
# =========================
def get_best_economy(deliveries):
    balls = deliveries.groupby("bowler").size()
    runs = deliveries.groupby("bowler")["total_runs"].sum()
    economy = runs / (balls / 6)
    return economy.idxmin(), round(economy.min(), 2)


# =========================
# 🔹 FILTER YEAR
# =========================
def filter_by_year(deliveries, matches, year):
    matches["date"] = pd.to_datetime(matches["date"], dayfirst=True)
    matches["year"] = matches["date"].dt.year

    match_ids = matches[matches["year"] == int(year)]["id"]
    return deliveries[deliveries["match_id"].isin(match_ids)]


# =========================
# 🔹 YEAR FUNCTIONS
# =========================
def get_top_scorer_year(data):
    col = get_batsman_col(data)
    runs = data.groupby(col)["batsman_runs"].sum()
    return runs.idxmax(), int(runs.max())


def get_most_sixes_year(data):
    col = get_batsman_col(data)
    sixes = data[data["batsman_runs"] == 6]
    count = sixes.groupby(col).size()
    return count.idxmax(), int(count.max())


def get_most_fours_year(data):
    col = get_batsman_col(data)
    fours = data[data["batsman_runs"] == 4]
    count = fours.groupby(col).size()
    return count.idxmax(), int(count.max())


def get_most_wickets_year(data):
    valid = data[
        data["dismissal_kind"].notna() &
        (data["dismissal_kind"] != "run out")
    ]
    count = valid.groupby("bowler").size()
    return count.idxmax(), int(count.max())


# =========================
# 🔹 STRIKE RATE
# =========================
def get_best_strike_rate(stats):
    row = stats.loc[stats["strike_rate"].idxmax()]
    return row["player"], row["strike_rate"]


# =========================
# 🔹 AVERAGE
# =========================
def get_best_average(stats):
    row = stats.loc[stats["average"].idxmax()]
    return row["player"], row["average"]


# =========================
# 🔹 TOP 5 BATSMEN
# =========================
def get_top5_batsmen(data):
    col = get_batsman_col(data)
    runs = data.groupby(col)["batsman_runs"].sum()
    return runs.sort_values(ascending=False).head(5)


# =========================
# 🔹 TOP 5 BOWLERS
# =========================
def get_top5_bowlers(data):
    valid = data[
        data["dismissal_kind"].notna() &
        (data["dismissal_kind"] != "run out")
    ]
    count = valid.groupby("bowler").size()
    return count.sort_values(ascending=False).head(5)


# =========================
# 🔹 MOST TITLES
# =========================
def get_most_titles(matches):
    matches["date"] = pd.to_datetime(matches["date"], dayfirst=True)
    matches["year"] = matches["date"].dt.year

    finals = matches.sort_values("date").groupby("year").tail(1)
    titles = finals["winner"].value_counts()

    return titles.idxmax(), int(titles.max())