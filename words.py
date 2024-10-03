import requests
from bs4 import BeautifulSoup

class WordScraper:
    def __init__(self, word):
        self.word = word
        self.url = f'https://milog.co.il/{word}'
        self.soup = None
    
    def fetch_content(self):
        # Send a GET request to fetch the raw HTML content
        response = requests.get(self.url)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            self.soup = BeautifulSoup(response.content, 'html.parser')
        else:
            raise Exception(f"Failed to retrieve the page. Status code: {response.status_code}")
    
    def get_definitions(self):
        if self.soup is None:
            self.fetch_content()
        
        # Find all elements with the class 'sr_e_txt'
        elements = self.soup.find_all(class_='sr_e_txt')
        
        # Collect definitions
        definitions = []
        for index, element in enumerate(elements, 1):
            definitions.append(f"פירוש {self.word} {index}: {element.text.strip()}")
        
        return definitions
    
    def get_summary(self):
        if self.soup is None:
            self.fetch_content()

        # Find all elements with the class 'sr_below_text'
        summary_elements = self.soup.find_all(class_='sr_below_text')
        
        summary = []
        for element in summary_elements:
            summary.append(element.text.strip())
        
        return summary
    
    def print_info(self):
        # Fetch and print definitions
        definitions = self.get_definitions()
        for definition in definitions:
            print(definition)
        
        # Fetch and print summary
        print("לסיכום:")
        summary = self.get_summary()
        for line in summary:
            print(line)

    def save_definitions_to_file(self, file_name):
        # Get definitions
        definitions = self.get_definitions()
        
        # Save to file
        with open(file_name, 'w', encoding='utf-8') as file:
            for definition in definitions:
                file.write(definition + '\n')
        
        print(f"Definitions saved to {file_name}")
