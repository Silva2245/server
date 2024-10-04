import selenium.webdriver as s

d = s.Chrome()
r = d.get('https://www.google.com')
print(str(r))