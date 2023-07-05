import os
import csv
import time
import openai
from PyPDF2 import PdfReader

# Add your OpenAI API key here
openai.api_key = "{API KEY GOES HERE}"

def extract_text_from_pdf(file_path):
    with open(file_path, "rb") as file:
        pdf = PdfReader(file)
        text = " ".join([page.extract_text() for page in pdf.pages])
    return text

def analyze_chunk(chunk):
    # Retry loop
    while True:
        try:
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"The article text is as follows:\n{chunk}"},
                {"role": "assistant", "content": "Please provide a list of human ancestries/ethnicities mentioned in the text, as well as any human cell types (cell lines, primary cell cultures) mentioned. Format your response as two arrays, [],[] where the first array represents the ancestries/ethnicities and the second array represents the cell types. If none are mentioned, please provide the arrays as empty, [],[]. Do not include any sentences or additional information in your response."}
            ]

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0,
            )
            return response.choices[0].message['content']
        except openai.error.ServiceUnavailableError:
            # Wait for a short delay before retrying
            time.sleep(2)
        except openai.error.APIError as e:
            # Handle other API errors
            print(f"An API error occurred: {e}")
            return ""  # Return an empty string in case of errors to proceed with the analysis



pdf_folder_path = "{PATH TO ARTICLES FOLDER}"
data_folder_path = "{PATH TO DATA FOLDER}"

os.makedirs(data_folder_path, exist_ok=True)

csv_file_path = os.path.join(data_folder_path, "data.csv")

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)

    # Write CSV header
    writer.writerow(["File ID", "Chunk ID", "Chunk Text", "Sentences"])

    for i, filename in enumerate(os.listdir(pdf_folder_path), start=1):
        if filename.endswith(".pdf"):
            file_path = os.path.join(pdf_folder_path, filename)
            text = extract_text_from_pdf(file_path)

            # Split text into chunks of approximately 240 words
            words = text.split()
            for chunk_id, j in enumerate(range(0, len(words), 240), start=1):
                chunk = " ".join(words[j:j+240])

                # Analyze the chunk using GPT-3.5-turbo.
                sentences = analyze_chunk(chunk)

                # Write the analysis results to the CSV file.
                writer.writerow([i, chunk_id, chunk, sentences])
