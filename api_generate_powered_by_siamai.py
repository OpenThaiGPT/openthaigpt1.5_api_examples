import openai

# Configure OpenAI client to use vLLM server
openai.api_base = "https://api.aieat.or.th/v1"
openai.api_key = "dummy"  # vLLM doesn't require a real API key

prompt = "<|im_start|>system\nคุณคือผู้ช่วยตอบคำถามที่ฉลาดและซื่อสัตย์<|im_end|>\n<|im_start|>user\nกรุงเทพมหานครคืออะไร<|im_end|>\n<|im_start|>assistant\n"

try:
    # Model = '.' = OpenThaiGPT 1.5 72b
    response = openai.Completion.create(
        model=".",  # Specify the model you're using with vLLM
        prompt=prompt,
        max_tokens=512,
        temperature=0.7,
        top_p=0.8,
        top_k=40,
        stop=["<|im_end|>"]
    )
    print("Generated Text:", response.choices[0].text)
except Exception as e:
    print("Error:", str(e))