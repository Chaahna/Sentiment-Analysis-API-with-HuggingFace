# Sentiment-Analysis-API-with-HuggingFace
Containerized sentiment analysis API using HuggingFace’s DistilBERT model, powered by FastAPI and Uvicorn. Includes parallel request demonstration via Jupyter Notebook.

1. Project Overview
This project deploys a sentiment analysis model using Hugging Face's transformers library, served via a FastAPI application. The system is containerized with Docker and supports concurrent inference requests. A Jupyter Notebook demonstrates parallel POST requests to the endpoint.

2. Model Used
distilbert-base-uncased-finetuned-sst-2-english
https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english#how-to-get-started-with-the-model 

3. Tech Stack
•	Python 3.10+
•	FastAPI
•	HuggingFace Transformers
•	Docker
•	Uvicorn (ASGI server)
•	Jupyter Notebook
•	aiohttp and asyncio (for parallel requests demo)

4. Project Structure
├── main.py                 # FastAPI app with /predict endpoint
├── Dockerfile             # Instructions for containerizing the app
├── requirements.txt       # Python dependencies
├── .dockerignore          # Files to exclude from Docker builds
├── parallel_requests_demo.ipynb  # Notebook to test multiple requests
└── README.md              # Project documentation

5. How to Run the Server
Using Docker:
docker build -t sentiment-api .
docker run -p 8000:8000 sentiment-api
Access the API at http://localhost:8000/docs.

6. API Usage
Endpoint: POST /predict
Payload example:
{
  "text": "This product is amazing!"
}
Response example:
{
  "label": "POSITIVE",
  "score": 0.9993
}

7. Parallel Request Demo
The parallel_requests_demo.ipynb file shows how to simulate multiple users hitting the endpoint in parallel using aiohttp and asyncio.

8. Future Enhancements
•	Add support for batch inference.
•	Deploy on cloud (AWS/GCP) with autoscaling.
•	Integrate logging and monitoring tools.
