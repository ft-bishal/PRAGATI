import os
import re

directory = "/Users/bishal/Downloads/Capital_One_Launchpad-main"

count = 0
for root, dirs, files in os.walk(directory):
    if "venv" in root or "__pycache__" in root or ".git" in root:
        continue
    for file in files:
        if file.endswith(".py"):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()

            if "from agno.models.groq import Groq" in content:
                # Replace import
                content = content.replace("from agno.models.groq import Groq", "from agno.models.groq import Groq")
                
                # Replace Groq(id=...) with Groq(id=...)
                content = re.sub(r'Gemini\(', r'Groq(', content)
                
                # Replace Gemini models with Groq equivalents
                content = re.sub(r'"llama-3.3-70b-versatile"]+"', r'"llama-3.3-70b-versatile"', content)
                content = re.sub(r"'llama-3.3-70b-versatile']+'", r"'llama-3.3-70b-versatile'", content)

                with open(filepath, 'w') as f:
                    f.write(content)
                count += 1
                print(f"Updated {filepath}")

print(f"Total files updated: {count}")
