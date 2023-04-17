from sub import Sub

class OtherSubscriber(Sub):
    def __init__(self, publisher):
        super().__init__(publisher)