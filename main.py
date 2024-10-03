from words import WordScraper

milim =[]
for word in milim:
        scraper = WordScraper(word)
        scraper.print_info()
        scraper.save_definitions_to_file('milim.txt')
