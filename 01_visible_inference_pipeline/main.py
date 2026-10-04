import math


class Pipeline:
    PAD_ID = 2
    UNKNOWN_ID = 3

    def __init__(self, text: str, labels=None):
        self.word_to_id = {"fantastic": 0, "awful": 1}
        self.score_model = {
            0: 3,
            1: -3,
            self.PAD_ID: 0,
            self.UNKNOWN_ID: 0,
        }
        self.input = text.strip()
        # Logit order is always [negative score, positive score].
        self.labels = ["negative", "positive"] if labels is None else list(labels)

    def tokenize(self):
        return [
            self.word_to_id.get(word, self.UNKNOWN_ID)
            for word in self.input.lower().split()
        ]

    def run(self, token_ids):
        sentiment_score = 0
        visited_positions = 0

        for token_id in token_ids:
            visited_positions += 1
            sentiment_score += self.score_model[token_id]

        logits = [-sentiment_score, sentiment_score]
        return logits, visited_positions

    def apply_stable_softmax(self, logits):
        maximum = max(logits)
        exponentials = [math.exp(value - maximum) for value in logits]
        denominator = sum(exponentials)

        return [value / denominator for value in exponentials]

    def execute_pipeline(self, pad_count=0):
        token_ids = self.tokenize() + [self.PAD_ID] * pad_count
        logits, visited_positions = self.run(token_ids)
        probabilities = self.apply_stable_softmax(logits)

        # On a tie, choose index 1: positive with the correct mapping.
        predicted_index = 1 if logits[1] >= logits[0] else 0

        return {
            "token_ids": token_ids,
            "logits": logits,
            "probabilities": probabilities,
            "predicted_index": predicted_index,
            "label": self.labels[predicted_index],
            "visited_positions": visited_positions,
        }


def test_positive_label(result):
    """Check both the winning index and its meaning."""
    assert result["predicted_index"] == 1, "Wrong winning index"
    assert result["label"] == "positive", "Wrong label mapping"


# 1A: Basic examples.
for text in [
    "the movie was fantastic",
    "the movie was awful",
    "not fantastic",
]:
    result = Pipeline(text).execute_pipeline()
    print(f"{text!r}: {result}")


# 1B, part 1: Deliberately reverse the label mapping.
correct = Pipeline("fantastic").execute_pipeline()
broken = Pipeline(
    "fantastic",
    labels=["positive", "negative"],
).execute_pipeline()

assert correct["logits"] == broken["logits"]
assert correct["probabilities"] == broken["probabilities"]

test_positive_label(correct)

try:
    test_positive_label(broken)
except AssertionError as error:
    print(f"\nCaught the deliberate bug: {error}")
else:
    raise AssertionError("The test failed to detect the reversed mapping")


# 1B, part 2: Same numeric output, more positions processed.
pipeline = Pipeline("fantastic")
original = pipeline.execute_pipeline()
padded = pipeline.execute_pipeline(pad_count=10)

assert original["logits"] == padded["logits"]
assert original["probabilities"] == padded["probabilities"]
assert original["label"] == padded["label"]
assert padded["visited_positions"] == original["visited_positions"] + 10

print("\nPadding comparison:")
for name, result in [("Original", original), ("Padded", padded)]:
    print(
        f"{name}: logits={result['logits']}, "
        f"label={result['label']}, "
        f"visited_positions={result['visited_positions']}"
    )
