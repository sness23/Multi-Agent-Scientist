import os

# Number of papers to process
NUM_PAPERS = 1

# The search query to use
SEARCH_QUERY = "IDH-wildtype glioblastoma"

# The name of the output file
OUTPUT_FILE = "results.md"

# The summarization model to use for the literature_review_agent
SUMMARIZATION_MODEL = "o1-mini"

# Entrez email to use
ENTREZ_EMAIL = os.getenv("EMAIL")

