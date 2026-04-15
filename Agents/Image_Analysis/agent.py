from agno.agent import Agent
from pathlib import Path
from agno.models.groq import Groq
from agno.media import Image
from dotenv import load_dotenv

load_dotenv()

class ImageAgent:
    def __init__(self, model_id="llama-3.2-90b-vision-preview"):
        self.agent = Agent(
            model=Groq(id=model_id), 
            markdown=True,
            debug_mode=False,
            # add_history_to_messages=True,
            # num_history_responses=5,
            # show_tool_calls=False,
            instructions=[
                "You are an AI agent that can generate text descriptions based on an image.",
                "You have to return a text response describing the image.",
            ],
        )
    
    def describe_image(self, image_path):
        image = Image(filepath=Path(image_path))
        prompt = "Describe the image properly."
        result = self.agent.run(prompt, images=[image]).content
        return result
    
if __name__ == "__main__":
    agent = ImageAgent()
    result = agent.describe_image("test/jpg_0.jpg")
    print(result)
