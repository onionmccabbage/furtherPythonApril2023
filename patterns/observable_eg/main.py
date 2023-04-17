# the Observer pattern implements a publish-subscribe model

# here is our publisher (also known as the observable)
from news_pub import NewsPublisher

# here are the subscribers (also refered to as listeners or observers)
from print_sub import PrintSubscriber
from email_sub import EmailSubscriber
from media_sub import MediaSubscriber
from other_sub import OtherSubscriber
# put them in a tuple
subs = (MediaSubscriber, PrintSubscriber, EmailSubscriber, OtherSubscriber)

def main():
    '''iterate over all subscribers, notifying of fresh news'''
    news_publisher = NewsPublisher()
    for subscriber in subs:
        subscriber(news_publisher)
        news_publisher.add_news('News Flash: we are nearly there!!')
    news_publisher.notify_subscribers() # they all get notified

if __name__ == '__main__':
    main()