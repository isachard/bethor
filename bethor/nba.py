import requests

from bs4 import BeautifulSoup

def url_loop():
    file = open("nba_links.txt","r")
    links = file.readlines()
    file.close()
    return links

def format_url(_url):

    #put this in a function!

    team_name = _url[58].upper() + _url[59:]
    print(team_name)
    result = requests.get(_url)
    content = result.content
    soup = BeautifulSoup(content, features="html.parser")
    return soup

def get_streak(soup):
    win = lose = push = 0
    matches = soup.find_all('td', class_=["viCellBg1 cellBorderR1 cellTextNorm padLeft","viCellBg2 cellBorderR1 cellTextNorm padLeft"])
    for i in matches:
        i = i.text.strip()
        if (len(i) > 0):
            if(i[0] == 'W'):
                win +=1
            if(i[0] == 'L'):
                lose +=1
            if(i[0] == 'P'):
                push += 1

    return [win,lose, push]

def percentages_spread(values):
    total_games = values[0] + values[1]
    cover_spread = str(round(values[0] / total_games * 100,2))
    print("Cover : " + cover_spread + "%")



def main():
    links = url_loop()
    for i in links:
        values =[]
        soup = format_url(i.strip())
        values = get_streak(soup)
        percentages_spread(values)
        print(values)
        print()

main()
