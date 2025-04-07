🧠 AI Sentiment Analysis API
This is an AI-powered API that performs sentiment analysis on text using a pre-trained DistilBERT model (distilbert-base-uncased-finetuned-sst-2-english). The API is built with FastAPI and containerized using Docker.

🚀 GitHub Repository
You can find the source code and contributions on GitHub:

AI Sentiment Analysis API - GitHub Repository

This repository contains:
- Deployed AI model API service code
- Branches, commits, and Pull Requests showcasing collaboration
- Detailed setup and usage instructions

⚙️ Setup and Run Locally
🐳 Docker Method (Recommended)
Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/sentiment-api.git
cd sentiment-api
Build the Docker image:
```
```bash

docker build -t sentiment-api .
Run the container:
```
```bash

docker run -d -p 8000:8000 sentiment-api
```
Check the API status:
Open your browser or use Postman to visit:

```bash
http://localhost:8000/docs
This will show the Swagger UI documentation, where you can test the API directly.
```
🔥 Python Method (If you prefer not using Docker)
Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/sentiment-api.git
cd sentiment-api
```
Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
pip install -r requirements.txt
```
Run the API server:

```bash

uvicorn main:app --reload
```
Check the API status:
Visit:

```bash

http://localhost:8000/docs
```

🎯 API Endpoints
POST /predict
Request Body:

json
Copy
{
  "text": "I am happy!"
}
Response:

json
Copy
{
  "label": "POSITIVE",
  "score": 0.9998
}
🧪 How to Test the API
Using Postman or cURL:

POST Request: Send a POST request to http://localhost:8000/predict with the body containing the text field.

Example using cURL:

```bash

curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"text": "I feel great!"}'
Swagger UI: Visit the Swagger UI to test all API endpoints interactively.
```
📂 Project Structure
```sentiment-api/
│
├── main.py            # FastAPI app with /predict endpoint
├── requirements.txt   # Python dependencies
├── Dockerfile         # Docker container setup
├── .dockerignore      # Files/folders to ignore during Docker build
└── README.md          # This file
```
🧑‍🤝‍🧑 GitHub Collaboration Guidelines
Branches: Always work in branches for new features or bug fixes.

```bash
git checkout -b feature-name
Pull Requests (PRs): After completing a feature or fix, open a PR to merge into the master branch.
```

📦 Dependencies
Install them via requirements.txt:

```bash
Copy
pip install -r requirements.txt
```

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.
