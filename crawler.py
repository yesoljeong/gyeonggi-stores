import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'https://www.google.com/search?newwindow=1&sxsrf=ALeKk03Q7wahc6cC8OH0qays3a1bZq0fyw:1586917676197&q=%EA%B0%95%EB%82%A8+%EB%A7%9B%EC%A7%91&npsic=0&rflfq=1&rlha=0&rllag=37511919,127039019,1944&tbm=lcl&ved=2ahUKEwj_loKDsenoAhXCaN4KHSNBBpkQtgN6BAgLEAQ&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:9&rldoc=1#rlfi=hd:;si:;mv:[[37.5274364,127.05976659999999],[37.493515099999996,127.0214333]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:9',
    headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
restaurants = soup.select(

    '#rl_ist0 > div.rl_tile-group.r-iq4OW4lebfXg > div.rlfl__tls.rl_tls.r-i4bV85olYCnw > div > div > div.uMdZh.rl-qs-crs-t.mnr-c')

for restaurant in restaurants:
    yummy_name = restaurant.select_one(' div > a > div > div.dbg0pd > div')
    print(yummy_name)

    yummy_adr = restaurant.select_one('span > div > span')

    yummy_grade = restaurant.select_one('span > div> span.BTtC6e')

    yummy_star = restaurant.select_one('span > div > g-review-stars > span > span')

    yummy_review = restaurant.select_one('span > div.rllt__wrapped.RHsRSe > div > div.b4vunb > div')
