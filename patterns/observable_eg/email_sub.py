from sub import Sub

class EmailSubscriber(Sub):
    def __init__(self, publisher):
        super().__init__(publisher)