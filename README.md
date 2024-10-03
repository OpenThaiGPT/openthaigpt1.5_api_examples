# OpenThaiGPT 1.5 API Examples
This repository contains examples of how to use the OpenThaiGPT 1.5 API via ``openai`` library powered by Siam.AI, Float16.

Author: kobkrit@aieat.or.th

Hosted by: [Siam.AI](https://siam.ai)<br>
<img src="https://siam.ai/wp-content/uploads/2024/06/logo_SiamAI_full_black_blue.png" alt="Siam.AI logo" width="300">

Hosted by: [Float16](https://float16.cloud/)

![image](https://github.com/user-attachments/assets/c48f9cb6-1c03-4cb8-9bc5-7d9e6f3df695)

# CURL 
## Siam.AI
```
curl https://api.aieat.or.th/v1/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer dummy" \
  -d '{
    "model": ".",
    "prompt": "<|im_start|>system\nคุณคือผู้ช่วยตอบคำถามที่ฉลาดและซื่อสัตย์<|im_end|>\n<|im_start|>user\nกรุงเทพมหานครคืออะไร<|im_end|>\n<|im_start|>assistant\n",
    "max_tokens": 512,
    "temperature": 0.7,
    "top_p": 0.8,
    "top_k": 40,
    "stop": ["<|im_end|>"]
  }'
```

## Float16
```
curl -X POST https://api.float16.cloud/dedicate/78y8fJLuzE/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer float16-AG0F8yNce5s1DiXm1ujcNrTaZquEdaikLwhZBRhyZQNeS7Dv0X" \
  -d '{
    "model": "openthaigpt/openthaigpt1.5-7b-instruct",
    "messages": [
      {
        "role": "system",
        "content": "คุณคือผู้ช่วยตอบคำถามที่ฉลาดและซื่อสัตย์"
      },
      {
        "role": "user",
        "content": "สวัสดี"
      }
    ]
   }'
```

# OpenAI Library
## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/openthaigpt1.5_api_examples.git
   cd openthaigpt1.5_api_examples
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage (Float16)

The main example is provided in the `api_generate_powered_by_float16.py` file. Here's how to use it:

1. Open the `api_generate_powered_by_float16.py` file.

2. Replace the following variables with your actual API credentials:
   ```python
   api_base = "https://api.float16.cloud/dedicate/YOUR_DEDICATED_ID/v1"
   api_key = "YOUR_API_KEY"
   model = "openthaigpt/openthaigpt1.5-7b-instruct"
   ```

3. Run the script:
   ```
   python api_generate_powered_by_float16.py
   ```

The script demonstrates how to use the OpenAIClient class to generate text using the OpenThaiGPT 1.5 model. You can modify the prompt and other parameters as needed.

## Usage (Siam.AI)

An example for using the API powered by Siam.AI is provided in the `api_generate_powered_by_siamai.py` file. Here's how to use it:

1. Open the `api_generate_powered_by_siamai.py` file.

2. The API base URL is already set to "https://api.aieat.or.th/v1". No API key is required as it uses a dummy key.

3. Run the script:
   ```
   python api_generate_powered_by_siamai.py
   ```

This script demonstrates how to use the OpenAI library to generate text using the OpenThaiGPT 1.5 model hosted by Siam.AI. You can modify the prompt and other parameters as needed.

## Example Output

The scripts will print the generated text based on the given prompt. For example:

```
Generated Text: กรุงเทพมหานคร หรือ กรุงเทพฯ คือเมืองหลวงของประเทศไทย ซึ่งตั้งอยู่ทางภาคกลางของประเทศ ริมฝั่งแม่น้ำเจ้าพระยา กรุงเทพมหานครเป็นศูนย์กลางการปกครอง การศึกษา การคมนาคมขนส่ง การเงินการธนาคาร การพาณิชย์ การสื่อสาร และวัฒนธรรมของประเทศไทย รวมถึงเป็นศูนย์กลางทางการเมืองและการปกครองของประเทศด้วย กรุงเทพมหานครยังเป็นเมืองที่มีความสำคัญทางประวัติศาสตร์และวัฒนธรรม มีสถานที่ท่องเที่ยวที่สำคัญมากมาย เช่น วัดพระศรีรัตนศาสดาราม (วัดพระแก้ว) วัดโพธิ์ วัดอรุณ พระบรมมหาราชวัง และวังวิมานเมฆ เป็นต้น
```

## Tool Calling with OpenThaiGPT 1.5 (Siam.AI)

An example demonstrating tool calling functionality with OpenThaiGPT 1.5 powered by Siam.AI is provided in the `api_tool_calling_powered_by_siamai.py` file. This script showcases how to use the OpenAI library to interact with the model and execute function calls based on the model's responses.

### Features

- Utilizes the OpenThaiGPT 1.5 model hosted by Siam.AI
- Demonstrates function calling capabilities
- Includes example functions for getting current temperature and temperature by date
- Handles multiple tool calls in a conversation

### Usage

1. Open the `api_tool_calling_powered_by_siamai.py` file.

2. The API base URL is already set to "https://api.aieat.or.th/v1". No API key is required as it uses a dummy key.

3. Run the script:
   ```
   python api_tool_calling_powered_by_siamai.py
   ```

### How it works

1. The script defines two example functions: `get_current_temperature` and `get_temperature_date`.
2. These functions are registered as tools that the model can call.
3. A conversation is initiated with a user message asking about the temperature in San Francisco.
4. The model processes the message and decides whether to call any functions.
5. If functions are called, their results are added to the conversation.
6. The process continues until the model provides a final response without calling any functions.

### Example Output

The script will print detailed logs of the conversation, including:
- Initial messages
- API calls
- Function calls and their results
- The final generated response

This example demonstrates how OpenThaiGPT 1.5 can be used in more complex scenarios requiring external data or computations.

