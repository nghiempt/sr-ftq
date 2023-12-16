import asyncio
import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import json
import openai
import os
from dotenv import load_dotenv
from newspaper import Article


class READ_PRIVACY_POLICY:

    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")

    @staticmethod
    def get_completion(prompt, model="gpt-4"):
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0.9,
        )
        return response.choices[0].message.content

    @staticmethod
    def remove_empty_lines(content):
        lines = content.split('\n')
        cleaned_lines = [line.strip() for line in lines if line.strip()]
        return '\n'.join(cleaned_lines)

    @staticmethod
    def check_valid_token_prompt(prompt):
        return len(prompt) <= 8000
    
    @staticmethod
    def short_completion(prompt):
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
        
    @staticmethod
    def generate_result(url):
        try:
            article = Article(url)
            article.download()
            article.parse()
            text = READ_PRIVACY_POLICY.remove_empty_lines(article.text)
            return text
        except Exception as e:
            print(f"An exception occurred: {e}")
            return "An error occurred during processing"


class GET_OUTCOME:

    @staticmethod
    async def loop_csv(input_csv_path, output_csv_path, read_privacy_policy):
        with open(input_csv_path, "r", newline="", encoding="utf-8") as csvfile, \
            open(output_csv_path, "w", newline="", encoding="utf-8") as outputfile:
            
            reader = csv.reader(csvfile)
            writer = csv.writer(outputfile)

            # Write the header to the output CSV
            headers = next(reader)
            writer.writerow(headers)

            for index, row in enumerate(reader):
                print("\n_____________ Run times " +
                    row[0] + " <" + row[2] + "> " + "_____________")
                
                privacy_policy_content = read_privacy_policy.generate_result(row[6])
                
                privacy_policy_content_short = read_privacy_policy.short_completion(privacy_policy_content)

                row[headers.index("privacy_policy_short")] = privacy_policy_content_short
                
                # print("Privacy Policy: " + privacy_policy_content_short)

                writer.writerow(row)
                
                print("~~~~~~~~~~~~~~ Success ~~~~~~~~~~~~~~\n")




async def main():
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
        
    read_privacy_policy = READ_PRIVACY_POLICY()

    input_csv_path = "/Users/nghiempt/Observation/sr-ftq/src/code_v3/pp.csv"
    output_csv_path = "/Users/nghiempt/Observation/sr-ftq/src/code_v3/pp2.csv"

    await GET_OUTCOME().loop_csv(input_csv_path, output_csv_path, read_privacy_policy)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())