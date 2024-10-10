# main.py

import os
from utils.arxiv_utils import fetch_arxiv_papers
from utils.pubmed_utils import fetch_pubmed_papers
from utils.summarization_utils import summarize_papers
from config import NUM_PAPERS, SEARCH_QUERY, OUTPUT_FILE, ARXIV_ABSTRACTS_FILE, SUMMARIZED_FILE
from tqdm import tqdm
import json

def main():
    # Ensure necessary directories exist
    os.makedirs('data', exist_ok=True)
    os.makedirs('outputs', exist_ok=True)
    
    if not os.path.exists(ARXIV_ABSTRACTS_FILE):
        arxiv_papers = fetch_arxiv_papers(SEARCH_QUERY, max_results=NUM_PAPERS)
        with open(ARXIV_ABSTRACTS_FILE, 'w', encoding='utf-8') as f:
            json.dump(arxiv_papers, f, ensure_ascii=False, indent=4)
    
    if not os.path.exists(SUMMARIZED_FILE):
        summarized_papers = summarize_papers(ARXIV_ABSTRACTS_FILE)
        with open(SUMMARIZED_FILE, 'w', encoding='utf-8') as f:
            json.dump(summarized_papers, f, ensure_ascii=False, indent=4)

    if not os.path.exists(OUTPUT_FILE):
        document = create_literature_review(SUMMARIZED_FILE, SEARCH_QUERY)
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(document)
            #json.dump(document, f, ensure_ascii=False, indent=4)
            print(f"Literature review saved to '{OUTPUT_FILE}'.")

def create_literature_review(input_filename, topic):
    with open(input_filename, 'r') as file:
        papers = json.load(file)

    document = ''
    # Introduction
    document += f"# Literature Review on {topic}\n\n"
    document += "This document summarizes recent advancements based on 10 selected scientific papers.\n\n"
    # Paper Summaries
    for idx, paper in enumerate(papers, 1):
        document += f"## Paper {idx}: {paper['title']}\n"
        document += f"**Authors**: {', '.join(paper['authors'])}\n"
        if paper['url']:
            document += f"**URL**: {paper['url']}\n"
        document += f"\n### Summary\n{paper['summary']}\n\n"
    # Conclusion
    document += "## Conclusion\n"
    document += "This literature review highlights the significant progress in the field and identifies areas for future research.\n"
    return document

if __name__ == '__main__':
    main()
