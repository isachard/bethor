
import requests
from bs4 import BeautifulSoup
import csv

def extracting_url_links():
    file = open("nba_links.txt","r")
    links = file.readlines()
    file.close()
    return links

def from_links_to_data_extraction(_url):
    
    team_name =  _url[58].upper() + _url[59:]
    result = requests.get(_url)
    content = result.content
    soup = BeautifulSoup(content, features="html.parser")
        
    return [team_name, soup]

def get_totals_teams(soup):
    over = 0
    under = 0
    push = 0
    matches = soup[1].find_all('td', class_=["viCellBg1 cellBorderR1 cellTextNorm padLeft","viCellBg2 cellBorderR1 cellTextNorm padLeft"])
     
    for i in matches:
        i = i.text.strip()
        if (len(i) > 0):
            if(i[0] == 'W'):
                over +=1
            if(i[0] == 'L'):
                under +=1
            if(i[0] == 'P'):
                push += 1

    return [soup[0],over,under,push]

def percentages_spread(values):
    total_games = values[0] + values[1]
    cover_spread = str(round(values[0] / total_games * 100,2))
    print("Cover : " + cover_spread + "%")


def main():
    teams_links = extracting_url_links()

    for t in teams_links:
        raw_data_from_url = from_links_to_data_extraction(t.strip())
        teams_trends= get_totals_teams(raw_data_from_url)
        print(teams_trends)
        values = [teams_trends[1],teams_trends[2]]
        percentages_spread(values)



main()


