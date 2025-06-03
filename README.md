# Sentiment-Analysis-API-with-HuggingFace
Containerized sentiment analysis API using HuggingFace’s DistilBERT model, powered by FastAPI and Uvicorn. Includes parallel request demonstration via Jupyter Notebook.

1. Project Overview
This project deploys a sentiment analysis model using Hugging Face's transformers library, served via a FastAPI application. The system is containerized with Docker and supports concurrent inference requests. A Jupyter Notebook demonstrates parallel POST requests to the endpoint.

2. Model Used
distilbert-base-uncased-finetuned-sst-2-english<br>
https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english#how-to-get-started-with-the-model 

3. Tech Stack<br>
•	Python 3.10+<br>
•	FastAPI<br>
•	HuggingFace Transformers<br>
•	Docker<br>
•	Uvicorn (ASGI server)<br>
•	Jupyter Notebook<br>
•	aiohttp and asyncio (for parallel requests demo)<br>

4. Project Structure<br>
   main.py                 # FastAPI app with /predict endpoint<br>
   Dockerfile             # Instructions for containerizing the app<br>
   requirements.txt       # Python dependencies<br>
   .dockerignore          # Files to exclude from Docker builds<br>
   parallel_requests_demo.ipynb  # Notebook to test multiple requests<br>
   README.md              # Project documentation<br>

5. How to Run the Server<br>
Using Docker:<br>
docker build -t sentiment-api .<br>
docker run -p 8000:8000 sentiment-api<br>
Access the API at http://localhost:8000/docs.<br>

6. API Usage<br>
Endpoint: POST /predict<br>
Payload example:<br>
{<br>
  "text": "This product is amazing!"<br>
}<br>
Response example:<br>
{<br>
  "label": "POSITIVE",<br>
  "score": 0.9993<br>
}<br>

7. Parallel Request Demo
The parallel_requests_demo.ipynb file shows how to simulate multiple users hitting the endpoint in parallel using aiohttp and asyncio.

8. Future Enhancements<br>
•	Add support for batch inference.<br>
•	Deploy on cloud (AWS/GCP) with autoscaling.<br>
•	Integrate logging and monitoring tools.<br>
