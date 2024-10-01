import openai

class OpenAIClient:
    def __init__(self, api_base, api_key, model):
        self.api_base = api_base
        self.api_key = api_key
        self.model = model

        # Configure OpenAI client with base URL and API key
        openai.api_base = self.api_base
        openai.api_key = self.api_key

    def generate_text(self, prompt, max_tokens=100, temperature=0.7):
        try:
            # Use OpenAI's `openai.Completion.create()` method
            response = openai.Completion.create(
                model=self.model,
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=temperature
            )
            
            # Return the generated text from the first choice
            return response['choices'][0]['text']
        except Exception as e:
            raise Exception(f"Error during API request: {str(e)}")


# Example usage:
api_base = "https://api.float16.cloud/dedicate/78y8fJLuzE/v1"
api_key = "float16-AG0F8yNce5s1DiXm1ujcNrTaZquEdaikLwhZBRhyZQNeS7Dv0X"
model = "openthaigpt/openthaigpt1.5-7b-instruct"


client = OpenAIClient(api_base, api_key, model)
prompt = "<|im_start|>system\nคุณคือผู้ช่วยตอบคำถามที่ฉลาดและซื่อสัตย์<|im_end|>\n<|im_start|>user\nกรุงเทพมหานครคืออะไร<|im_end|>\n<|im_start|>assistant\n"

try:
    response = client.generate_text(prompt, max_tokens=512, temperature=0.7)
    print("Generated Text:", response)
except Exception as e:
    print("Error:", str(e))