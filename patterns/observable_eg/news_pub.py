# here we will publish items of news
class NewsPublisher():
    def __init__(self):
        # remember the leading double-underscore effectively 'hides' this proerty from external access
        # it is similar to 'private' in other languages
        # it is known as 'name mangling'
        self.__subscribers = [] # start with an empty list
        self.latest_news = None
    def attach(self, new_sub):
        self.__subscribers.append(new_sub)
    def detach(self):
        self.__subscribers.pop() # just remove the most recent member
    def iter_subscribers(self):
        # we use type() here to access the __name__ assigned by Python
        return [type(x).__name__ for x in self.__subscribers]
    def notify_subscribers(self):
        for sub in self.__subscribers:
            sub.update() # call the update method on each subscriber
    # we need to be able ot add to the news flow
    def add_news(self, news):
        self.latest_news = news
    def get_news(self):
        return f'News just in: {self.latest_news}'