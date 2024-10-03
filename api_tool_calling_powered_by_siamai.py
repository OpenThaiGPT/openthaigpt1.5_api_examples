import openai
import json

def get_current_temperature(location: str, unit: str = "celsius"):
    """Get current temperature at a location.

    Args:
        location: The location to get the temperature for, in the format "City, State, Country".
        unit: The unit to return the temperature in. Defaults to "celsius". (choices: ["celsius", "fahrenheit"])

    Returns:
        the temperature, the location, and the unit in a dict
    """
    print(f"Calling get_current_temperature with location: {location}, unit: {unit}")
    result = {
        "temperature": 26.1,
        "location": location,
        "unit": unit,
    }
    print(f"get_current_temperature result: {result}")
    return result


def get_temperature_date(location: str, date: str, unit: str = "celsius"):
    """Get temperature at a location and date.

    Args:
        location: The location to get the temperature for, in the format "City, State, Country".
        date: The date to get the temperature for, in the format "Year-Month-Day".
        unit: The unit to return the temperature in. Defaults to "celsius". (choices: ["celsius", "fahrenheit"])

    Returns:
        the temperature, the location, the date and the unit in a dict
    """
    print(f"Calling get_temperature_date with location: {location}, date: {date}, unit: {unit}")
    result = {
        "temperature": 25.9,
        "location": location,
        "date": date,
        "unit": unit,
    }
    print(f"get_temperature_date result: {result}")
    return result


def get_function_by_name(name):
    print(f"Getting function by name: {name}")
    if name == "get_current_temperature":
        return get_current_temperature
    if name == "get_temperature_date":
        return get_temperature_date
    print(f"Function not found: {name}")
    return None

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_temperature",
            "description": "Get current temperature at a location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": 'The location to get the temperature for, in the format "City, State, Country".',
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": 'The unit to return the temperature in. Defaults to "celsius".',
                    },
                },
                "required": ["location"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_temperature_date",
            "description": "Get temperature at a location and date.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": 'The location to get the temperature for, in the format "City, State, Country".',
                    },
                    "date": {
                        "type": "string",
                        "description": 'The date to get the temperature for, in the format "Year-Month-Day".',
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": 'The unit to return the temperature in. Defaults to "celsius".',
                    },
                },
                "required": ["location", "date"],
            },
        },
    },
]

messages = [
    {"role": "system", "content": "You are OpenThaiGPT, created by AIEAT. คุณคือผู้ช่วยตอบคำถามที่ฉลาดและซื่อสัตย์\n\nCurrent Date: 2024-10-03"},
    {"role": "user",  "content": "อุณหภูมิของ San Francisco ตอนนี้และพรุ่งนี้เป็นไง?"},
]

print("Initial messages:", messages)

# Configure OpenAI client to use vLLM server
openai.api_base = "https://api.aieat.or.th/v1"
openai.api_key = "dummy"  # vLLM doesn't require a real API key
print(f"OpenAI API base: {openai.api_base}")
print(f"OpenAI API key: {openai.api_key}")

import json

def get_current_temperature(location, unit="celsius"):
    # Simulated function to get current temperature
    print(f"Simulated get_current_temperature called with location: {location}, unit: {unit}")
    result = {"temperature": 26.1, "location": location, "unit": unit}
    print(f"Simulated get_current_temperature result: {result}")
    return result

def get_temperature_date(location, date, unit="celsius"):
    # Simulated function to get temperature for a specific date
    print(f"Simulated get_temperature_date called with location: {location}, date: {date}, unit: {unit}")
    result = {"temperature": 25.9, "location": location, "date": date, "unit": unit}
    print(f"Simulated get_temperature_date result: {result}")
    return result

def get_function_by_name(name):
    print(f"Getting function by name: {name}")
    result = globals()[name]
    print(f"Function retrieved: {result}")
    return result

while True:
    try:
        print("Creating ChatCompletion...")
        response = openai.ChatCompletion.create(
            model=".",  # Specify the model you're using with vLLM
            messages=messages,
            tools=tools,
            temperature=0.7,
            top_p=0.8,
            max_tokens=512,
            stop=["<|im_end|>"]
        )
        print(f"ChatCompletion response: {response}")
        
        assistant_message = response.choices[0].message
        print(f"Assistant message: {assistant_message}")
        messages.append(assistant_message)
        print(f"Updated messages: {messages}")

        if tool_calls := assistant_message.get("tool_calls", None):
            print(f"Tool calls found: {tool_calls}")
            for tool_call in tool_calls:
                call_id = tool_call["id"]
                print(f"Processing tool call with id: {call_id}")
                if fn_call := tool_call.get("function"):
                    fn_name = fn_call["name"]
                    fn_args = json.loads(fn_call["arguments"])
                    print(f"Function call: {fn_name}, arguments: {fn_args}")
                
                    fn = get_function_by_name(fn_name)
                    fn_res = json.dumps(fn(**fn_args))
                    print(f"Function result: {fn_res}")

                    messages.append({
                        "role": "tool",
                        "content": fn_res,
                        "tool_call_id": call_id,
                    })
                    print(f"Updated messages after tool call: {messages}")
        else:
            print("No tool calls made, exiting loop")
            break  # Exit the loop if no tool calls are made

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        break

# Final response
if assistant_message.content:
    print(f"Generated Text: {assistant_message.content}")
else:
    print("No final response generated.")