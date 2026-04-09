from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Training data (VERY IMPORTANT)
questions = [

    # 🔹 Runs
    "who scored most runs",
    "top batsman",
    "highest run scorer",
    "who is the best batsman",
    "who has most runs in ipl",
    "leading run scorer",

    # 🔹 Sixes
    "who hit most sixes",
    "king of sixes",
    "most sixes in ipl",
    "which batsman hit most sixes",

    # 🔹 Fours
    "who hit most fours",
    "most fours",
    "who scored most fours",
    "most boundaries",
    "who hit most boundaries",
    "which batsman hit most fours",

    # 🔹 Wickets
    "who took most wickets",
    "top wicket taker",
    "leading wicket taker",
    "who is best bowler",
    "most wickets in ipl",

    # 🔹 Economy
    "best economy bowler",
    "who has best economy",
    "most economical bowler",

    # 🔹 Teams
    "which team won most matches",
    "most successful team",
    "which team has most wins",
    "top team in ipl",

    # 🔹 Match
    "who won the match",
    "latest match winner",
    "who won last match",

    # 🔹 Season
    "who won in 2015",
    "winner of 2018 ipl",
    "ipl 2020 winner",
    "who won ipl 2017",

    # 🔹 Tricky / Natural
    "who is king of ipl",
    "best player in ipl",
    "which player is best",
    "which team dominates ipl"
]

labels = [
    # Runs
    "runs","runs","runs","runs","runs","runs",

    # Sixes
    "sixes","sixes","sixes","sixes",

    # Fours
    "fours","fours","fours","fours","fours","fours",

    # Wickets
    "wickets","wickets","wickets","wickets","wickets",

    # Economy
    "economy","economy","economy",

    # Teams
    "wins","wins","wins","wins",

    # Match
    "match","match","match",

    # Season
    "season","season","season","season",

    # Tricky
    "runs","runs","runs","wins"
]
# Convert text → numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

# Train model
model = LogisticRegression()
model.fit(X, labels)

# Save model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Model trained successfully!")