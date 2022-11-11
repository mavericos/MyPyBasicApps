# работи в терминала

import requests
from bs4 import BeautifulSoup

url = "https://www.codewithtomi.com/"
r = requests.get(url)
r
soup = BeautifulSoup(r.content, "lxml")
title = soup.find_all("h2", {"class":"post-title"})
title

# <h2 class="post-title">
# <a href="https://www.codewithtomi.com/2020/12/how-to-deploy-django-project-to-heroku.html">How To Deploy A Django Project To Heroku</a>
# </h2>

title[0].getText()
title1 = title[0].getText()

print(title1)

for t in title:
    print(t.getText())