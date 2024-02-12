from bs4 import BeautifulSoup
import csv
import os

# Directory containing XML files
folder_path = 'file'
file = open("scripts_11_12.csv","w")
writer = csv.writer(file)

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.xml'):  # Process only XML files
        file_path = os.path.join(folder_path, filename)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            xml_content = file.read()

        soup = BeautifulSoup(xml_content, features="xml")  # Using lxml parser here
        text_content = soup.get_text(separator='\n', strip=True)
        writer.writerow([filename, text_content])
file.close()
