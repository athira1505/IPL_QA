import pandas as pd

def load_data():
    matches = pd.read_csv("data/matches.csv")
    deliveries = pd.read_csv("data/deliveries.csv")
    players = pd.read_excel("data/Players.xlsx")
    stats = pd.read_csv("data/most_runs_average_strikerate.csv")
    teams = pd.read_csv("data/teams.csv")
    home_away = pd.read_csv("data/teamwise_home_and_away.csv")

    return matches, deliveries, players, stats, teams, home_away