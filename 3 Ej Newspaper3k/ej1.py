import re
from collections import Counter
from newspaper import Article

def body(url):
    article = Article(url)
    article.download()
    article.parse()
    texto = article.text
    texto = texto.lower()
    lista = re.split(r'\W+',texto)
    return Counter(lista)