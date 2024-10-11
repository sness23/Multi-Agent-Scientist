# Multi-Agent-Scientist

Multi-Agent Scientist
The Multi-Agent Scientist is an AI pipeline designed to automate the process of generating scientific research ideas and drafting patent applications. It consists of four interconnected agents that work sequentially to produce novel scientific ideas and corresponding patents based on the latest research literature.

# Table of Contents
1. Overview
2. Features
3. Project Structure
4. Installation
5. Prerequisites
6. Steps
7. Usage
8. Customization

Agents and Their Functionality
1. Literature Review Agent
2. Scientific Research Agent
3. Patent Search Agent
4. Patent Writing Agent

    Dependencies
    License
    Acknowledgments
    Contact
    Overview
    The Multi-Agent Scientist leverages OpenAI's o1-preview and o1-mini models to process and generate text, and utilizes APIs from arXiv, PubMed, and patent databases. The pipeline includes:

Literature Review Agent: Gathers and summarizes relevant scientific papers.
Scientific Research Agent: Generates new scientific ideas based on the literature review.
Patent Search Agent: Checks the originality of each idea by searching existing patents.
Patent Writing Agent: Drafts patent applications for original ideas.

Features
Automated Literature Review: Fetches and summarizes recent scientific papers on a chosen topic.
Idea Generation: Produces novel scientific research ideas using AI language models.
Patent Originality Check: Searches patent databases to verify the uniqueness of generated ideas.
Automated Patent Drafting: Creates patent application documents for original ideas.
Project Structure

# Installation
## Prerequisites
Python 3.7 or higher
OpenAI account with access to o1-preview or o1-mini models
NCBI Entrez email registration for PubMed API access
API keys for patent databases (if applicable)


# Agents and Their Functionality
## 1. Literature Review Agent
Purpose: Collects and summarizes scientific papers relevant to the chosen topic.

Data Sources: arXiv, PubMed
Functionality:
Searches for papers using the specified query.
Summarizes abstracts using OpenAI's language models.
Compiles summaries into a cohesive literature review.
Output: outputs/literature_review.md

## 2. Scientific Research Agent
Purpose: Generates new scientific ideas based on the literature review.

Input: The literature review from the first agent.
Functionality:
Analyzes the literature review to identify gaps and opportunities.
Generates novel ideas using AI models.
Output: data/ideas.json

## 3. Patent Search Agent
Purpose: Determines the originality of generated ideas by searching existing patents.

Input: List of generated ideas.
Functionality:
Searches patent databases (e.g., USPTO, EPO, Google patents) for each idea.
Marks ideas as original ('y') or not ('n').
Output: Updated data/ideas.json with originality status.

## 4. Patent Writing Agent
Purpose: Drafts patent applications for original ideas.

# Acknowledgments
OpenAI: For providing powerful language models.
arXiv: For access to pre-print scientific papers.
PubMed: For access to biomedical literature.
Patent Offices: For providing patent search APIs.
Contact
For questions or support, please contact [angelovskiandrej5@gmail.com].

Note: This project is intended for educational and research purposes only. 


----------------------------------------

We present a general biological research agent designed to accelerate discoveries in biology, medicine, and cancer research. Our agent combines a powerful Python-based backend with an intuitive chatbot front end, creating a seamless interface for researchers to interact with complex computational tools using natural language. This project showcases how artificial intelligence can be harnessed to streamline research processes, from literature mining to data analysis and hypothesis generation. Our biological research agent assists researchers in navigating the vast expanse of scientific literature and data. By integrating advanced natural language processing models and machine learning algorithms, the agent can process large datasets, extract pertinent information, and provide context-aware responses to complex queries. The Python backend leverages robust computational libraries, ensuring efficient data handling and analysis, while the chatbot interface allows users to engage with the system conversationally, lowering the barrier to entry for those without extensive technical expertise. One of the key features of our agent is advanced literature mining. It can perform comprehensive searches across multiple scientific databases, including PubMed Central and arXiv. Utilizing natural language processing models, the agent extracts key findings, summarizes articles, and identifies emerging trends, helping researchers stay abreast of the latest developments in their fields. Beyond information retrieval, the agent can analyze experimental data, identify statistically significant results, and suggest biological interpretations based on existing literature. This capability aids in uncovering novel insights and generating new research hypotheses. The web-based chatbot allows researchers to interact with the agent using natural language queries. This design ensures accessibility for users with varying levels of technical skills, facilitating a more dynamic and responsive research environment. To demonstrate the practical utility of our agent, we conducted a case study focusing on IDH-wildtype glioblastoma, an aggressive and hard-to-treat form of brain cancer. Our goal was to identify antigens that are elevated in this cancer subtype to aid in the development of targeted therapies. We directed the agent to search for full-text articles related to IDH-wildtype glioblastoma in PubMed Central. Using Cohere's advanced natural language processing models, the agent extracted mentions of antigens reported to be overexpressed in this cancer subtype. The agent successfully identified over 50 potential antigens, including EGFRvIII, PD-L1, and CD44. These antigens are associated with tumor progression and immune evasion mechanisms, making them valuable targets for therapeutic intervention. With these findings, researchers can explore the creation of bispecific T-cell engagers, similar to tebentafusp, which can redirect the immune system to target cancer cells more effectively. The agent's ability to streamline this discovery process exemplifies its potential impact on cancer research.  Researchers can pose questions, request summaries, or seek data analysis support directly through this interface. Our general biological research agent represents a significant advancement in integrating artificial intelligence into biomedical research. By automating time-consuming tasks and providing intelligent insights, the agent allows researchers to focus on critical thinking and innovation. The agent reduces the time required for literature reviews and data analysis, speeding up the research cycle and enabling quicker progress toward discoveries. The natural language interface makes sophisticated computational tools accessible to a broader range of researchers, promoting inclusivity in scientific exploration. By providing a centralized platform for data and insights, the agent fosters collaboration among researchers from different disciplines. We envision several avenues for expanding and enhancing the agent's capabilities. While our focus has been on cancer research, the agent's framework can be adapted to other areas of biology and medicine, broadening its applicability. Incorporating functionalities that interface with laboratory equipment could allow for experimental planning and even direct control of automated experiments. Implementing machine learning models that improve over time with user interaction will make the agent more efficient and accurate in understanding and responding to queries. Submitting this project to the lablab.ai hackathon, we aim to showcase how artificial intelligence-powered tools can revolutionize biomedical research. Our general biological research agent, with its Python backend and chatbot front end, provides a powerful yet accessible platform for researchers. By automating complex tasks and facilitating deeper insights, it has the potential to significantly impact the way scientific research is conducted. Our successful application of the agent in identifying potential therapeutic targets in IDH-wildtype glioblastoma demonstrates its practical utility and sets the stage for future developments. We are excited about the possibilities this tool presents and look forward to refining it further, integrating new features, and collaborating with the research community to maximize its impact.

We present a general biological research agent designed to accelerate discoveries in biology, medicine, and cancer research. Our agent combines a powerful Python-based backend with an intuitive chatbot front end, creating a seamless interface for researchers to interact with complex computational tools using natural language. This project demonstrates how artificial intelligence can streamline research processes, from literature mining to data analysis and hypothesis generation. By integrating advanced natural language processing models and machine learning algorithms, the agent assists researchers in navigating vast scientific literature and data. It can process large datasets, extract pertinent information, and provide context-aware responses to complex queries. The Python backend leverages robust computational libraries, ensuring efficient data handling and analysis, while the chatbot interface allows users to engage conversationally, lowering the barrier to entry for those without extensive technical expertise. One key feature is advanced literature mining; the agent performs comprehensive searches across databases like PubMed Central and arXiv. Utilizing natural language processing models, it extracts key findings, summarizes articles, and identifies emerging trends, helping researchers stay updated with the latest developments. Beyond information retrieval, the agent can analyze experimental data, identify statistically significant results, and suggest biological interpretations based on existing literature, aiding in uncovering novel insights and generating new research hypotheses. To demonstrate its practical utility, we conducted a case study focusing on IDH-wildtype glioblastoma, an aggressive and hard-to-treat form of brain cancer. Our goal was to identify antigens elevated in this cancer subtype to aid in developing targeted therapies. The agent searched for full-text articles related to IDH-wildtype glioblastoma in PubMed Central. Using Cohere's advanced natural language processing models, it extracted mentions of antigens reported to be overexpressed in this subtype. The agent successfully identified over 50 potential antigens, including EGFRvIII, PD-L1, and CD44, which are associated with tumor progression and immune evasion mechanisms, making them valuable targets for therapeutic intervention. With these findings, researchers can explore creating bispecific T-cell engagers, similar to tebentafusp, to redirect the immune system to target cancer cells more effectively.  Our general biological research agent represents a significant advancement in integrating artificial intelligence into biomedical research. By automating time-consuming tasks and providing intelligent insights, it allows researchers to focus on critical thinking and innovation. The agent reduces the time required for literature reviews and data analysis, speeding up the research cycle and enabling quicker progress toward discoveries. The natural language interface makes sophisticated computational tools accessible to a broader range of researchers, promoting inclusivity in scientific exploration. Submitting this project to the lablab.ai hackathon, we aim to showcase how AI-powered tools can revolutionize biomedical research. We are excited about the possibilities this tool presents and look forward to refining it further, integrating new features, and collaborating with the research community to maximize its impact.
