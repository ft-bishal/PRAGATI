import os

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

            if "llama-3.3-70b-versatile" in content:
                content = content.replace("llama-3.3-70b-versatile", "llama-3.3-70b-versatile")
                with open(filepath, 'w') as f:
                    f.write(content)
                print(f"Updated {filepath}")
                count += 1
print(f"Total files updated: {count}")
