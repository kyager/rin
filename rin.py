# filepath: /home/keith/src/rin/rin.py
#!/usr/bin/env python3
import argparse
import os
from dotenv import load_dotenv
from openai import OpenAI

parser = argparse.ArgumentParser()
parser.add_argument("message", nargs='+', help="Message to send to OpenAI")
parser.add_argument("-f", "--file", type=argparse.FileType('r'), help="File to send to OpenAI")
parser.add_argument("-d", "--directory", type=str, help="Directory to send file and directory names to OpenAI")

args = parser.parse_args()

if args.file:
    message_content = args.file.read()
elif args.directory:
    if os.path.isdir(args.directory):
        message_content = '\n'.join(os.listdir(args.directory))
    else:
        raise NotADirectoryError(f"{args.directory} is not a valid directory")
else:
    message_content = ' '.join(args.message)

load_dotenv()
client = OpenAI()
completion = client.chat.completions.create(
    model=os.getenv('OPENAI_MODEL'),
    store=True,
    messages=[
        {"role": "user", "content": message_content}
    ]
)
message = completion.choices[0].message.content

print(message)