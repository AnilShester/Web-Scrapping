import requests
from bs4 import BeautifulSoup
import pandas as pd

url = requests.get("https://www.skysports.com/premier-league-table")
soup = BeautifulSoup(url.content, 'html.parser')

epl_table = soup.find(class_='standing-table standing-table--full block')

pos = epl_table.select('.standing-table__row td:first-child')
position = [p.get_text() for p in pos]

teams = epl_table.select('.standing-table__cell--name a')
team_name = [t.get_text() for t in teams]

gp = epl_table.select('.standing-table__row td:nth-child(3)')
games_played = [w.get_text() for w in gp]

wins = epl_table.select('.standing-table__row td:nth-child(4)')
total_wins = [w.get_text() for w in wins]

draws = epl_table.select('.standing-table__row td:nth-child(5)')
total_draws = [w.get_text() for w in draws]

losses = epl_table.select('.standing-table__row td:nth-child(6)')
total_loss = [w.get_text() for w in losses]


points = epl_table.select('.standing-table__row td:nth-child(10)')
total_points = [w.get_text() for w in points]

# print(position)
# print(team_name)
# print(games_played)
# print(total_points)
# print(total_wins)
# print(total_draws)
# print(total_loss)


table = pd.DataFrame({
    "position": position,
    "Team": team_name,
    "Games Playes": games_played,
    "Wins": total_wins,
    "Draws": total_draws,
    "Losses": total_loss,
    "Points": total_points
})

print(table)