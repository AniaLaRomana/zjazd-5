from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# otwieram przegladarke chrome
# definiuje zmienna

driver = webdriver.Chrome

# nawigacja do strony www

driver.get("https://pl.wikipedia.org/wiki/Wikipedia:Strona_g%C5%82%C3%B3wna")

