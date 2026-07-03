```python
from chatbot.model import FAQModel


class FAQChatbot:

    def __init__(self):

        self.model = FAQModel("faq.csv")

    def reply(self, question):

        return self.model.get_answer(question)


chatbot = FAQChatbot()
```
