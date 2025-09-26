# modules/chatbot.py

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class ChatBot:
    """
    A simple Transformer-based chatbot using a pre-trained language model.
    """


    def __init__(self, model_name: str = "distilgpt2", device: str = "cpu"):  # 👈 force CPU
        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name).to(self.device)

    def generate_response(self, user_input: str, max_length: int = 100) -> str:
        """
        Generate a text response for a given user input.
        """
        inputs = self.tokenizer.encode(user_input + self.tokenizer.eos_token, return_tensors="pt").to(self.device)
        outputs = self.model.generate(inputs, max_length=max_length, pad_token_id=self.tokenizer.eos_token_id)
        response = self.tokenizer.decode(outputs[:, inputs.shape[-1]:][0], skip_special_tokens=True)
        return response
