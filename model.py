import openai
import os


# os.environ["OPENAI_API_KEY"] = "your api key"
openai.api_key = "your api key"

# for the dataset
with open("swami.txt", "r", encoding="utf-8") as file:

    dataset = file.read()

# Fine-tuning configuration
config = {
    "task": "text-davinci-003",  
    "dataset": dataset,
    "model": "davinci",
    "steps": 5000,  
    "learning_rate": 1e-5,
    "warmup_steps": 100,
    "batch_size": 4,
    "save_checkpoint_steps": 1000,
    "overwrite": True,
}


openai.ChatCompletion.create(**config)
