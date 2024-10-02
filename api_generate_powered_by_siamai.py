import openai

# Configure OpenAI client to use vLLM server
openai.api_base = "http://210.79.130.19:8000/v1"
openai.api_key = "dummy"  # vLLM doesn't require a real API key

prompt = "<|im_start|>system\nคุณคือผู้ช่วยตอบคำถามที่ฉลาดและซื่อสัตย์<|im_end|>\n<|im_start|>user\nกรุงเทพมหานครคืออะไร<|im_end|>\n<|im_start|>assistant\n"

try:
    response = openai.Completion.create(
        model=".",  # Specify the model you're using with vLLM
        prompt=prompt,
        max_tokens=512,
        temperature=0.7
    )
    print("Generated Text:", response.choices[0].text)
except Exception as e:
    print("Error:", str(e))