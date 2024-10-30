from bs4 import BeautifulSoup
from json import dumps

soup = BeautifulSoup(open("index.html", encoding="utf-8"), 'html5lib')

problems = []

i = 1

for divs in soup.findAll("div", attrs={"class":"text-body max-w-[75%] font-medium text-lc-text-primary dark:text-dark-lc-text-primary"}):
    problem = divs.contents[0].text
    if problem is not None:
        problems.append({"sr": i, "statement" : problem})
        i+=1

levels = []
i = 0


for ps in soup.findAll("div", attrs={"class":"relative flex h-full w-full items-center"}):
    level = ps.contents[1].text
    problems[i]["level"] = level
    print(level)
    i+=1

print(problems)

with open("problems.json", "w", encoding="utf-8") as f:
    f.write(dumps(problems))