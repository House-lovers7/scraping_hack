import requests
from bs4 import BeautifulSoup

url = "https://ja.wikipedia.org"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
today = soup.find("div", attrs={"id": "on_this_day"})
entries = today.find_all("li")
today_list = []
index = 1

for entry in entries:
  today_list.append([index, entry.get_text()])
  index += 1

print(today_list)
