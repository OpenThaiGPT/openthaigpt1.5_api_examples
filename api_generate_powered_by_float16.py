import openai

# Configure OpenAI client
api_base = "https://api.float16.cloud/dedicate/78y8fJLuzE/v1"
api_key = "float16-AG0F8yNce5s1DiXm1ujcNrTaZquEdaikLwhZBRhyZQNeS7Dv0X"
model = "openthaigpt/openthaigpt1.5-7b-instruct"

openai.api_base = api_base
openai.api_key = api_key

prompt = "<|im_start|>system\nคุณคือผู้ช่วยตอบคำถามที่ฉลาดและซื่อสัตย์<|im_end|>\n<|im_start|>user\nกรุงเทพมหานครคืออะไร<|im_end|>\n<|im_start|>assistant\n"

print("Non Stream Example: ")
try:
    response = openai.Completion.create(
        model=model,
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
    
print("")
print("Streaming Example: ")
# Streaming Example
try:
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        max_tokens=512,
        temperature=0.7,
        top_p=0.8,
        top_k=40,
        stop=["<|im_end|>"],
        stream=True  # Enable streaming
    )
    
    print("Generated Text (Streaming):")
    for chunk in response:
        if chunk.choices[0].text:
            print(chunk.choices[0].text, end='', flush=True)
    print()  # New line after streaming is complete
except Exception as e:
    print("Error in streaming:", str(e))