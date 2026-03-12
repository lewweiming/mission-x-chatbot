# Maritime Intelligence Chatbot

## Step-by-Step Implementation

1.  Create your "Brain" (AI API):
    
    -   Sign up at Groq Console.
    -   Generate a free API Key. While it doesn't host Llamarine specifically, you can use Llama 3 70B as a highly capable substitute for general reasoning.
    
2.  Setup your "Memory" (Vector Database):
    
    -   Create a free account at [Pinecone](https://www.pinecone.io/).
    -   Initialize an index with "1536 dimensions" (standard for high-quality maritime data embeddings).
    
3.  Plug in Free Maritime Data:
    
    -   Regulatory Docs: Download free PDFs of IMO Conventions or IACS Blue Books.
    -   Live/Historical Data: Connect to Global Fishing Watch for vessel movement datasets.
    -   Marine Conditions: Use the Copernicus Marine Data Store for free oceanographic data (currents, waves, salinity).
    
4.  The "Glue" Code (Streamlit):
    
    -   On a computer (or using a web-based code editor like GitHub Codespaces on your tablet), create a simple `app.py` script.
    -   Use the `langchain` library to connect the Groq API to your Pinecone database.
    -   Upload your code to a GitHub repository.
    
5.  Launch on your Tablet:
    
    -   Go to Streamlit Community Cloud and connect your GitHub repo.
    -   It will give you a URL (e.g., `maritime-twin.streamlit.app`).
    -   Open this link in Chrome on your Honor X9. You now have a fully functional, free AI maritime assistant. [5, 6, 7, 8, 9]
