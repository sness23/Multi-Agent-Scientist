import os
from openai import OpenAI
from config import SUMMARIZATION_MODEL
from tqdm import tqdm

aiml_api_key = os.getenv('AIML_API_KEY')

client = OpenAI(
    api_key=aiml_api_key,
    base_url="https://api.aimlapi.com/",
)

def summarize_papers(papers):
    for paper in tqdm(papers, desc='Summarizing papers'):
        abstract = paper.get('abstract', '')
        if abstract:
            summary = summarize_text(abstract)
            paper['summary'] = summary
        else:
            paper['summary'] = 'No abstract available.'
    return papers

def summarize_text(text):
    prompt = f"Summarize the following scientific abstract in for an expert in the field:\n\n{text}"
    try:
        chat_completion = client.chat.completions.create(
            model=SUMMARIZATION_MODEL,
            messages=[
                {'role': 'user', 'content': prompt}
            ],
            max_tokens=2000
        )
        response = chat_completion.choices[0].message.content
        return response
    
    except Exception as e:
        print(f"An error occurred during summarization: {e}")
        return "Summary not available due to an error."
