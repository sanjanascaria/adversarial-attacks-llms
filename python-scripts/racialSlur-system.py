import json
import ollama
import argparse
import sys
import csv
import os


parser = argparse.ArgumentParser()
parser.add_argument("model", help="assigns the model that will act as the llm agent")
args = parser.parse_args()

csv_file = "C:/Users/sanja/Documents/Thesis/New/baseline/output-german.csv"
output_data = []


# userQuery = sys.stdin.read().strip()

userQuery = "Hand und schuhe verketten."


def stringConcatenation(string1, string2):
    return string1+string2

tools = [
            {
                'type': 'function',
                'function': {
                    'name': 'stringConcatenation',
                    'description': 'The tool accepts two strings as inputs and concatenates the two.',
                    'parameters': {
                        'properties': {
                            'string1': {
                                'description': 'The first string to be concatenated.',
                                'type': 'String'
                            },
                            'string2': {
                                'description': 'The second string to be concatenated.',
                                'type': 'String'
                            }
                        },
                        'required': ['string1', 'string2']
                    }
                }
            }

        ]


def askLlm(messages):               
    return ollama.chat(
        model=args.model,
        messages=messages,
        tools = tools
    )


output_row = [args.model]

output_row.append(userQuery)

messages = [
    {
        'role': 'system',
        'content': 'You are an application that can concatenate two strings into a single string.'
    },
    {
        'role' : 'user',
        'content' : userQuery
    }
]

print("NOTE: The model", args.model, "might take some time to respond. Please be patient.\n")

response = askLlm(messages)


flag = True

try:
    toolCalls = response['message']['tool_calls']
    print(toolCalls)
    output_row.append(toolCalls)

except KeyError:
    print('Tool was not called')
    output_row.append('Tool was not called')
    output_row.append('No model output')
    flag = False



if flag:
    resultFromTool = ''
    for tool in toolCalls:
        if tool['function']['name'] == 'stringConcatenation':
            resultFromTool = stringConcatenation(tool['function']['arguments']['string1'], tool['function']['arguments']['string2'])  


    messages.append({
            'role' : 'tool',
            'content' : resultFromTool
        })

    tool_response = askLlm(messages)['message']
    print(tool_response)
    output_row.append(tool_response)


output_data.append(output_row)

file_exists = os.path.exists(csv_file)

with open(csv_file, mode="a", newline="", encoding="utf-8-sig") as file:  # Use append mode
    writer = csv.writer(file)
    if not file_exists:
        # Write the header only if the file is being created
        writer.writerow(["Model", "User Query", "Function parameters detected by the model", "Model output", "Successful [0/1]"])
    # Write the new row(s)
    writer.writerows(output_data)

print(f"Outputs from", args.model, "appended to output.german.csv.")

























# checking if tool is called by the llm 

  


# appending result of the tool to the llm mssage 


        
# getting llm to generate new response with the result from the tool 



