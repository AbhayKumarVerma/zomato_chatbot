import os
from transformers import pipeline
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if hf_token:
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = hf_token
else:
    raise EnvironmentError("HUGGINGFACEHUB_API_TOKEN not found in .env file")

# Initialize the text-generation pipeline with Mistral-7B-Instruct-v0.3
# Adjust device_map or other settings as needed for your hardware
generator = pipeline(
    task="text-generation",
    model="mistralai/Mistral-7B-Instruct-v0.3",
    trust_remote_code=False,
    device_map="auto"
)

def get_response(user_input: str) -> str:
    """
    Generate a response using the Mistral instruct model.
    """
    outputs = generator(
        user_input,
        max_new_tokens=512,
        do_sample=True,
        top_p=0.9,
        temperature=0.7
    )
    # The pipeline returns a list of generations; we take the first
    return outputs[0].get("generated_text", "")
