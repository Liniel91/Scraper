from src import Publication


class PublicationPage:
    def __init__(self, browser):
        self.browser = browser
        self.driver = self.browser.driver
        self.article_author_elements = self.driver.find_elements_by_class_name("author-link")
        self.article_title = self.driver.find_element_by_xpath('//div[@class="articleTitle hide-bullet"]/h3')
        self.article_keywords = self.driver.find_elements_by_xpath(
            '//div[@class="articleDetails-contentCell articleDetails-contentCell-first"]/a')
        self.article_year = self.driver.find_element_by_xpath('//div[text()="Rocznik"]/../..//a')
        self.article_bibliography = self.driver.find_elements_by_xpath('//ul[@class="plainList"]/li')

    def create_publication(self):

        publication = Publication.Publciation()
        publication.title = self.article_title.text
        publication.year = self.article_year.text

        for i in range(len(self.article_author_elements)):
            publication.authors.append(self.article_author_elements[i].text)

        for i in range(len(self.article_keywords)):
            publication.key_words.append(self.article_keywords[i].text)

        for i in range(len(self.article_bibliography)):
            publication.bibliography.append(self.article_bibliography[i].text)
        return publication