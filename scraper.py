from requests_html import HTMLSession

class Scraper():

    def scrapedata(self,tag):
        url = f'https://quotes.toscrape.com/tag/{tag}'
        session = HTMLSession()
        req = session.get(url)
        print(req.status_code)

        qlist = []
        quotes = req.html.find('div.quote')

        for q in quotes:
            # print(q.find('span.text', first=True).text.strip()) # tranform the result into a dict -> API
            item = {
                'text':q.find('span.text', first=True).text.strip(),
                'author': q.find('small.author', first=True).text.strip()
                }
            print(item)
            qlist.append(item)
        return qlist

quotes = Scraper()
quotes.scrapedata('life')