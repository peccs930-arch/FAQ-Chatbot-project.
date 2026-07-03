```python
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from chatbot.preprocess import preprocess


class FAQModel:

    def __init__(self, csv_file):

        self.data = pd.read_csv(csv_file)

        self.questions = self.data["Question"].tolist()

        self.answers = self.data["Answer"].tolist()

        self.cleaned_questions = [
            preprocess(q)
            for q in self.questions
        ]

        self.vectorizer = TfidfVectorizer()

        self.question_vectors = self.vectorizer.fit_transform(
            self.cleaned_questions
        )

    def get_answer(self, user_question):

        cleaned = preprocess(user_question)

        user_vector = self.vectorizer.transform([cleaned])

        similarity = cosine_similarity(
            user_vector,
            self.question_vectors
        )

        best_index = similarity.argmax()

        score = similarity[0][best_index]

        if score < 0.30:
            return (
                "Sorry, I couldn't find a suitable answer. "
                "Please try asking in a different way."
            )

        return self.answers[best_index]
```
