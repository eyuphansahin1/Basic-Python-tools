import requests
from bs4 import BeautifulSoup
import pyfiglet
from colorama import Fore, Style, init




class WebScraper:
    banner = pyfiglet.figlet_format("Eyuphan Web Scraper")

    @staticmethod
    def display_banner():
        print(Fore.CYAN + WebScraper.banner + Style.RESET_ALL)
    
    @staticmethod
    def request_url(url):
        try:
            response = requests.get(url)
            return BeautifulSoup(response.text, 'html.parser')
        except requests.RequestException as e:
            print(f"Error: {e}")
            return None
    
    @staticmethod
    def extract_info(parser):
        if not parser:
            return
        
        for question in parser.find_all("div", {"class": "s-post-summary"}):
            title = question.find('h3', {"class": "s-post-summary--content-title"})
            content = question.find('div', {"class": "s-post-summary--content-excerpt"})
            time = question.find('span', {"class": "relativetime"})['title']
            
            print(Fore.BLUE + str(title.text).strip() + Style.RESET_ALL)
            print(Fore.GREEN + str(content.text).strip() + Style.RESET_ALL)
            print(Fore.WHITE + str(time).strip() + Style.RESET_ALL)
            print(Fore.RED + "---" + Style.RESET_ALL)

    @staticmethod
    def scrape(base_url, page_number):
        WebScraper.display_banner()
        for sayfa in range(1, page_number + 1):
            url = f"{base_url}?tab=newest&page={sayfa}&pagesize=50"
            parser = WebScraper.request_url(url)
            WebScraper.extract_info(parser)



WebScraper.scrape(base_url="https://stackoverflow.com/questions/tagged/python-requests", page_number=3)
