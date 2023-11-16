import requests
from bs4 import BeautifulSoup

def fetch_headlines(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 

        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all('h2') 

        return [headline.get_text().strip() for headline in headlines]
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return []

def save_to_file(filename, data):
   
    try:
        with open(filename, 'w',encoding='utf-8') as file:
            for line in data:
                file.write(line + '\n')
        print(f"Data successfully written to {filename}")
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")

def main():
    # URL of the website to scrape - this should be replaced with the actual URL
    url = 'https://www.w3schools.com/js/'

    # Fetch headlines from the website
    headlines = fetch_headlines(url)

    if headlines:
        # Ask user for the filename
        filename = input("Enter the name of the file to save: ")

        # Save the headlines to the file
        save_to_file(filename, headlines)
    else:
        print("No headlines fetched.")

if __name__ == "__main__":
    main()
