import asyncio
import ssl
import csv
import json
import openai
import os
from dotenv import load_dotenv


class GET_SECTION_PRIVACY_POLICY:
    
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
                    {"role": "system", "content": "You are an expert at extracting information from text into separate parts."},
                    {"role": "user", "content": "Based on the content of the privacy policy below. Please classify and give me new information in the form (retain raw data): \nI. Data Shared: content ...\nII. Data Collected: content ... \nIII. Security Practices: content ...\n\n" + str(''' Last updated: July 1, 2023
TEGNA Inc. (with its affiliates, “TEGNA” “we,” “us” or “our”) is a national media company. This “Privacy Policy” describes our collection, use, and sharing of personal information related to our services provided online. This privacy policy doesn't apply to information given offline or through other means.
You can access this Privacy Policy online at www.tegna.com/privacy-policy.
Table of Contents
1. Personal Information We Collect
2. How We Use Your Personal Information
3. How We Share Your Personal Information
4. Retention
5. Your Choices
6. Other Sites and Services
7. Security
8. International Data Transfers
9. Children
10. Changes to this Privacy Policy
11. Your Privacy Rights
1. Personal Information We Collect
- Contact data
- Registration data
- Communications
- Marketing data
- Other information
Data collected automatically includes Device data and Online activity data.
2. How We Use Your Personal Information
- Service delivery
- Research and development
- Marketing and Targeted Advertising
- Compliance and operations
We may share your personal information with:
- Affiliates
- Service providers
- Advertising partners
- Business Partners
- Public authorities
- Business transferees
We either delete or anonymize personal information we no longer require.
3. Your Choices
- You can opt-out of marketing emails
- You can control text message alerts
- You can limit use of your information for targeted advertising
- You can decline to provide information
4. Other Sites and Services
We may contain links to other websites and online services operated by third parties.
5. Security
The security of your personal information is important to us. We have various safeguards in place.
6. International Data Transfers
Our services are intended for use only by residents of the United States.
7. Children
Our services are not designed for children under the age of 16.
8. Changes to this Privacy Policy
We reserve the right to modify this Privacy Policy at any time.
9. Your Privacy Rights
If you're a resident of certain states, you have the rights as described.
Please direct any queries or comments to:
TEGNA Inc.
8350 Broad Street
Suite 2000
Tysons, VA 22102
Attention: Law Department (Privacy)
Email: privacy@tegna.com ''')}
                ]
            )
            assistant_reply = response.choices[0].message['content']
            print(assistant_reply)
            return assistant_reply
        except Exception as e:
            return "Error"


async def main():
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    await GET_SECTION_PRIVACY_POLICY().ask_gpt('abc')

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
