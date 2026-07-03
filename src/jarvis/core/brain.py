#DONDE SE ALOJA OLLAMA

from ollama import chat


class Brain:
    """
    Se encarga de comunicarse con el modelo de IA.
    """

    def __init__(self, model: str = "gemma3:4b"):
        self.model = model

    def ask(self, message: str) -> str:
        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": message,
                }
            ],
        )

        return response["message"]["content"]