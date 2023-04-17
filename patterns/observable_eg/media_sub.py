from sub import Sub

class MediaSubscriber(Sub):
    def __init__(self, publisher):
        super().__init__(publisher)