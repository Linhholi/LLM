from bs4 import BeautifulSoup
import requests
import csv

page_to_scrap = requests.get("https://bigbangtrans.wordpress.com/")
soup = BeautifulSoup(page_to_scrap.text,"html.parser")
non_breaking_space = u'\xa0'
html_text = str(soup)  # Convert the soup object to a string
html_text = html_text.replace(non_breaking_space, ' ')

# Parse the modified HTML string
soup = BeautifulSoup(html_text, "html.parser")
link_to_scrap = soup.findAll("li", attrs={"class":"page_item"})
file = open("scripts.csv","w")
writer = csv.writer(file)
for link in link_to_scrap:
    url= requests.get("https://bigbangtrans.wordpress.com/"+
                     link.text.lower()
                     .replace("series 0","series ")
                     .replace("1 episode 0","1 episode ")
                     .replace("2 episode 05","2 episode 5")
                     .replace("2 episode 08","1 episode 08")
                     .replace("2 episode 10","2 episode 11")
                     .replace("6 episode 23","06 episode 23")
                     .replace("6 episode 24","06 episode 24")
                     .replace("8 episode 05","7 episode 05")
                     .replace("-"," ").replace("–","")
                     .replace("/","").replace("  "," ")
                     .replace(" ","-")
                      )
    # print(url)
    soup_link = BeautifulSoup(url.text,"html.parser")
    title = soup_link.find("h2", class_="title").text
    scripts = soup_link.find("div", class_="entrytext").text
    writer.writerow([title, scripts])
file.close()