import math


class Pipeline:
    def __init__(self, input: str):
        self.score_model = [30, -30]
        self.word_to_id = {"fantastic": 0, "awful": 1}
        self.input = input
        self.logger(
            "initialization of the pipeline is complete", "__init__ (constructor)"
        )

    def run(self):
        # remove spaces:
        self.input.strip()
        self.logger("trailing spaces removed", "run")

        # split from spaces
        list_of_input_words = self.input.split()
        self.logger(
            "input string converted into a list of words, separated by spaces", "run"
        )

        # get the logits for both scores
        sentiment_score = 0
        for word in list_of_input_words:
            index_of_word = self.word_to_id.get(word, -1)
            if index_of_word >= 0:
                score = self.score_model[index_of_word]
                sentiment_score += score
            semantic_not = "not " if index_of_word < 0 else ""
            self.logger(
                f"word is '{word}', is {semantic_not}present in the score model.",
                "run",
            )
        logits = {"positive": sentiment_score, "negative": -sentiment_score}
        self.logger(f"computed the logits: {logits}", "run")

        return logits

    def softmax(self, logits, key, denominator, M):
        numerator = math.e ** (logits[key] - M)
        return numerator / denominator

    def apply_stable_softmax(self, logits):
        M = max(v for v in logits.values())
        denominator = sum(math.e ** (v - M) for v in logits.values())
        positive_label_softmax = self.softmax(logits, "positive", denominator, M)
        negative_label_softmax = self.softmax(logits, "negative", denominator, M)

        self.logger(
            f"positive label softmax = {positive_label_softmax}", "apply_stable_softmax"
        )
        self.logger(
            f"negative label softmax = {negative_label_softmax}", "apply_stable_softmax"
        )

        return (
            "positive"
            if positive_label_softmax >= negative_label_softmax
            else "negative"
        )

    def execute_pipeline(self):
        self.logger("execution of the pipeline started", "execute_pipeline")
        logits = self.run()
        label_output = self.apply_stable_softmax(logits)

        self.logger(
            f"the output label predicted is: '{label_output}' for the input: '{self.input}'",
            "execute_pipeline",
        )

    def logger(self, log: str, method: str):
        print(f"method:- {method} ===> '{log}'")


print()
Pipeline("the movie was fantastic").execute_pipeline()
print()
Pipeline("the movie was awful").execute_pipeline()
print()
Pipeline("not fantastic").execute_pipeline()
print()
Pipeline("fantastic awful").execute_pipeline()
