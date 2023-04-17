from sub import Sub

class PrintSubscriber(Sub):
    def __init__(self, publisher):
        super().__init__(publisher)