import asyncio
import ssl
import csv
import json
import openai
import os
from dotenv import load_dotenv


class GET_THIRD_PARTY_SERVICE:
    
    @staticmethod
    def remove_empty_lines(content):
        lines = content.split('\n')
        cleaned_lines = [line.strip() for line in lines if line.strip()]
        return '\n'.join(cleaned_lines)
    
    @staticmethod
    def ask_gpt(prompt):
        try:
            print(prompt)
            response = openai.ChatCompletion.create(
                model='gpt-4',
                messages=[
                    {"role": "system", "content": "You are an expert at detecting links to third-party services that privacy policy content refers to."},
                    {"role": "user", "content": "Based on the content of the privacy policy below. Please list the third-parties that the application links with to use the service and the purpose of linking and using that third-party (If any).\n\n" + str(prompt)}
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
                
                privacy_policy_section = GET_THIRD_PARTY_SERVICE().ask_gpt(row[7])
                row[headers.index("third_party")] = GET_THIRD_PARTY_SERVICE().remove_empty_lines(privacy_policy_section)
                print(GET_THIRD_PARTY_SERVICE().remove_empty_lines(privacy_policy_section))
                writer.writerow(row)
                print("~~~~~~~~~~~~~~ Success ~~~~~~~~~~~~~~\n")



async def main():
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    input_csv_path = "/Users/nghiempt/Observation/sr-ftq/src/regular_behaviour/result/third_party.csv"
    output_csv_path = "/Users/nghiempt/Observation/sr-ftq/src/regular_behaviour/result/third_party2.csv"
    
    await GET_THIRD_PARTY_SERVICE().loop_csv(input_csv_path, output_csv_path)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())