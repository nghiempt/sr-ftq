import asyncio
import ssl
import csv
import json
import openai
import os
from dotenv import load_dotenv


class CHATGPT_GENERATOR:
    
    @staticmethod
    def get_completion(prompt):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.ChatCompletion.create(
            model=os.getenv("GPT_4"),
            messages=[
                {"role": "system", "content": "You are a pre-processing expert, cleaning up noisy and redundant data when data is swapped from the website."},
                {"role": "user", "content": 'Based on the data provided below because I swapped data from the application\'s privacy policy link. Eliminate noise and redundant words.\n\n' + prompt}
            ]
        )
        assistant_reply = response.choices[0].message['content']
        return assistant_reply
    

class DATASET_GENERATOR:

    @staticmethod
    def loop_csv(csv_path, chatgpt_generator):
        with open(csv_path, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for index, row in enumerate(reader):
                print("\n_____________ Run times App ID: " + row[0] + "_____________")
                print(chatgpt_generator.get_completion(row[7]))
                print("~~~~~~~~~~~~~~ Success ~~~~~~~~~~~~~~\n")


if __name__ == "__main__":
    chatgpt_generator = CHATGPT_GENERATOR()

    csv_path = "/Users/nghiempt/Observation/sr-ftq/src/code_v3/pp.csv"

    DATASET_GENERATOR().loop_csv(csv_path, chatgpt_generator)
