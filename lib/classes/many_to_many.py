class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.__class__.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if (
            isinstance(title, str)
            and 4 < len(title) < 51
            and not hasattr(self, "_title")
        ):
            self._title = title
        else:
            raise Exception(
                "title must be a string between 5 and 50 characters and cannot be changed"
            )

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise Exception("author must be of class type Author")
        else:
            self._author = author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be of class type Magazine")
        else:
            self._magazine = magazine


class Author:
    def __init__(self, name):
        self.name = name

    def articles(self):
        return [
            article
            for article in Article.all
            if isinstance(article, Article) and article.author is self
        ]

    def magazines(self):
        return list(
            {
                article.magazine
                for article in Article.all
                if isinstance(article.magazine, Magazine) and article.author is self
            }
        )

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topics = list(
            {
                article.magazine.category
                for article in Article.all
                if article.author is self
            }
        )
        if len(topics) > 0:
            return topics
        return None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0 and not hasattr(self, "_name"):
            self._name = name
        else:
            raise Exception(
                "name must be a string with greater than 0 characters and cannot be changed"
            )

class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.__class__.all.append(self)

    def articles(self):
        return [
            article
            for article in Article.all
            if isinstance(article, Article) and article.magazine is self
        ]

    def contributors(self):
        return list(
            {
                article.author
                for article in Article.all
                if isinstance(article.author, Author) and article.magazine is self
            }
        )

    def article_titles(self):
        articles = [
            article.title for article in Article.all if article.magazine is self
        ]
        if len(articles) > 0:
            return articles
        return None

    def contributing_authors(self):
        authors = [
            article.author
            for article in Article.all
            if isinstance(article.author, Author) and article.magazine is self
        ]
        more_than_two_articles = []
        for author in authors:
            if authors.count(author) > 2:
                more_than_two_articles.append(author)

        if len(more_than_two_articles) > 0:
            return more_than_two_articles
        return None

    def num_articles(self):
        return len([article for article in Article.all if article.magazine is self])

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 < len(name) < 17:
            self._name = name
        else:
            raise Exception(
                "name must be a string between 2 and 16 characters in length"
            )

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise Exception("category must be a string greater than 0 characters")

    @classmethod
    def top_publisher(cls):
        if len(cls.all) > 0:
            top_publisher = max(cls.all, key=lambda magazine: magazine.num_articles())
            if top_publisher.num_articles() > 0:
                return top_publisher
            return None
        return None