import asyncio
import ssl
import csv
import json
import openai
import os
from dotenv import load_dotenv


class GET_REGULAR_BEHAVIOUR:
    
    @staticmethod
    def remove_empty_lines(content):
        lines = content.split('\n')
        cleaned_lines = [line.strip() for line in lines if line.strip()]
        return '\n'.join(cleaned_lines)
    
    @staticmethod
    def ask_gpt(prompt, category):
        try:
            response = openai.ChatCompletion.create(
                model='gpt-4',
                messages=[
                    {"role": "system", "content": "You are an expert in analyzing the regular behavior of Android applications based on the privacy policy and category of that application."},
                    {"role": "user", "content": "Based on the content of the privacy policy below with category: " + category + ". What is regular behavior ?\n\n" + str(prompt)}
                ]
            )
            assistant_reply = response.choices[0].message['content']
            return assistant_reply
        except Exception as e:
            return "Error"
        

    @staticmethod
    async def loop_csv(input_csv_path, output_csv_path):
        with open(input_csv_path, "r", newline="", encoding="utf-8") as csvfile, \
            open(output_csv_path, "w", newline="", encoding="utf-8") as outputfile:
            
            reader = csv.reader(csvfile)
            writer = csv.writer(outputfile)

            headers = next(reader)
            writer.writerow(headers)

            for index, row in enumerate(reader):
                print("\n_____________ Run times " +
                    row[0] + " <" + row[2] + "> " + "_____________")
                
                regular = GET_REGULAR_BEHAVIOUR().ask_gpt(row[7], row[3])
                row[headers.index("regular")] = GET_REGULAR_BEHAVIOUR().remove_empty_lines(regular)
                print(GET_REGULAR_BEHAVIOUR().remove_empty_lines(regular))
                writer.writerow(row)
                print("~~~~~~~~~~~~~~ Success ~~~~~~~~~~~~~~\n")



async def main():
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    input_csv_path = "/Users/nghiempt/Observation/sr-ftq/src/gpt_helper/section_result_10.csv"
    output_csv_path = "/Users/nghiempt/Observation/sr-ftq/src/gpt_helper/regular.csv"
    
    await GET_REGULAR_BEHAVIOUR().loop_csv(input_csv_path, output_csv_path)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
