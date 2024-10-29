import openai
import json

# Define a simple temperature checking tool
tools = [{
    "type": "function",
    "function": {
        "name": "get_current_temperature",
        "description": "Get current temperature at a location.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The location to get temperature for"
                }
            },
            "required": ["location"]
        }
    }
}]

# Simple function to simulate getting temperature
def get_current_temperature(location):
    return {"temperature": 25, "location": location}

messages = [
    {"role": "system", "content": "คุณคือผู้ช่วยตอบคำถามที่ฉลาดและซื่อสัตย์\n\nCurrent Date: 2024-10-29"},
    {"role": "user", "content": "อุณหภูมิที่กรุงเทพมหานครตอนนี้เป็นไง?"}
]

# Configure OpenAI client
openai.api_base = "https://api.aieat.or.th/v1"
openai.api_key = "dummy"

# Get completion with tool calling
response = openai.ChatCompletion.create(
    model=".",
    messages=messages,
    tools=tools,
    temperature=0.7
)

# Handle the tool call
assistant_message = response.choices[0].message
messages.append(assistant_message)

if tool_calls := assistant_message.get("tool_calls"):
    for tool_call in tool_calls:
        # Get function details
        function_name = tool_call["function"]["name"]
        function_args = json.loads(tool_call["function"]["arguments"])
        
        # Execute function
        function_response = get_current_temperature(**function_args)
        
        # Add result to messages
        messages.append({
            "role": "tool",
            "content": json.dumps(function_response),
            "tool_call_id": tool_call["id"]
        })

    # Get final response
    final_response = openai.ChatCompletion.create(
        model=".",
        messages=messages,
        tools=tools,
        temperature=0.7
    )
    print(final_response.choices[0].message.content)
