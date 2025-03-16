from transformers import pipeline


class FinanceModel:
    def __init__(self):
        self.model = pipeline(
            "text-generation", model="huggingface/finance-bert")

    def generate_report(self, input_text):
        return self.model(input_text, max_length=500)
