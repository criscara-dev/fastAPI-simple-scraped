# FastAPI webs craper

## website to scrape

- [Quotes](https://quotes.toscrape.com/tag/life/)

## libraries

- [pip3 install requests-html](https://pypi.org/project/requests-html/)

create the 'meat' of the app in scfrape.py

- [pip3 install fastapi](https://pypi.org/project/fastapi/)
- pip3 install uvicorn

im main.py build the FastAPI

to execute the API:

```python
uvicorn main:app --reload
```

### and navigate to http://127.0.0.1:8000/docs

- navigate to [life](http://127.0.0.1:8000/life) that is a category and you'll see 10 entry. the URL now is an API that we can query from data we have scrape in asynch.
