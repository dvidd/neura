from pychromecast.controllers import BaseController

class MyController(BaseController):
    def __init__(self):
        super(MyController, self).__init__(
            "urn:x-cast:my.super.awesome.namespace")

    def receive_message(self, message, data):
        print("Wow, I received this message: {}".format(data))

        return True  # indicate you handled this message

    def request_beer(self):
        self.send_message({'request': 'beer'})