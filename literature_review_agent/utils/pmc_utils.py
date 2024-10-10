from Bio import Entrez
from tqdm import tqdm
import os

def fetch_pmc_papers(query, max_results=5):
    # Set the Entrez email
    Entrez.email = os.getenv("EMAIL")
    
    # Search PMC for the query
    search_handle = Entrez.esearch(db='pmc', term=query, retmax=max_results)
    search_results = Entrez.read(search_handle)
    search_handle.close()

    # Retrieve the full articles
    paper_ids = search_results['IdList']
    papers = []
    for pmc_id in tqdm(paper_ids, total=len(paper_ids), desc='Fetching PMC papers'):
        # Fetch full article XML
        fetch_handle = Entrez.efetch(db='pmc', id=pmc_id, rettype='full', retmode='xml')
        article_xml = fetch_handle.read()
        fetch_handle.close()

        # Here, you would parse the XML to extract title, authors, abstract,
        # and full text. We'll just store the raw XML for simplicity.
        # Consider using libraries such as 'xml.etree.ElementTree' for parsing.
        papers.append({
            'pmc_id': pmc_id,
            'article_xml': article_xml
        })
    return papers
import os
from Bio import Entrez
from tqdm import tqdm

def fetch_and_save_pmc_papers(query, max_results=5, email='your_email@example.com', output_dir='pmc_papers'):
    # Set the Entrez email
    Entrez.email = email

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Search PMC for the query
    search_handle = Entrez.esearch(db='pmc', term=query, retmax=max_results)
    search_results = Entrez.read(search_handle)
    search_handle.close()

    # Retrieve and save the full articles
    paper_ids = search_results['IdList']
    for pmc_id in tqdm(paper_ids, total=len(paper_ids), desc='Fetching and saving PMC papers'):
        # Fetch full article XML
        fetch_handle = Entrez.efetch(db='pmc', id=pmc_id, rettype='full', retmode='xml')
        article_xml = fetch_handle.read()
        fetch_handle.close()

        # Define the filename for the article
        filename = f"{output_dir}/PMC_{pmc_id}.xml"
        
        # Save the XML to a file
        with open(filename, 'w') as file:
            file.write(article_xml)

        print(f"Saved article {pmc_id} to {filename}")
