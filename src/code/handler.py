import PyPDF2
import re
import openai
import os   

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
gpt_model = os.getenv("GPT_4")

pdf_file = "//Users/nghiempt/Corporation/scientific/sr-ftq/src/packs/03/text.pdf"
extracted_file = "/Users/nghiempt/Corporation/scientific/sr-ftq/src/packs/03/extracted_text.txt"

# Open the PDF file in binary mode
with open(pdf_file, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    page_texts = []
    for i in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[i]
        text = page.extract_text()
        page_texts.append(text)
        
    # Open a text file for writing
    with open(extracted_file, 'w') as file:
        for i, text in enumerate(page_texts):
            # Write each page's text with a page header
            file.write(f"---- Page {i+1} ----\n{text}\n\n")

# Open the text file and read its contents
with open(extracted_file, 'r') as file:
    content = file.read()

print(content)

# Function to process the text through AI
def aiprocessor(text):
    messages = [
        {
            "role": "system",
            "content": """You are a teacher for Answering Questions Based on PDF Content, a backend processor. User input is messy raw text extracted from a PDF page by PyPDF2.
                            Based on the content of the provided PDF file, answer the following questions: 
                            - Q1: What does Table 7 show?
                            - Q2: What is the formula to calculate the sports resource M(x, y)?
                            - Q3: What is the energy consumption, communication, and migration costs formular reference to?
                            - Q4: What type of education have the highest percentage in Table 4?
                            - Q5: How did the number of sports venues in province M change in Result and Discussion section?
                            - Q6: What conclusion can be draw from Figure 2?
                            - Q7: What should play an active role in the future paperwork to direct and strongly promote the  open policy of national sport?
                            - Q8: What is the thing that improves the computing power of the data in Introduction section?
                            - Q9: How can teachers obtain students’ learning data?
                            - Q10: What reference has introduced IoT technology to smart cities?
                            Ensure that the answers are derived from the information contained within the PDF, considering all relevant sections and details."""
        },
        {
            "role": "user",
            "content": "RAW PDF FILE:\n" + text
        }
    ]
    
    response = openai.ChatCompletion.create(
        model=gpt_model,
        messages=messages,
        # temperature=0.5,
    )
    print(response)
    
# Process the text through AI
# reply = aiprocessor(content)