🧠 AI Sentiment Analysis API
This is an AI-powered API that performs sentiment analysis on text using a pre-trained DistilBERT model (distilbert-base-uncased-finetuned-sst-2-english). The API is built with FastAPI and containerized using Docker.

🚀 GitHub Repository
You can find the source code and contributions on GitHub:

AI Sentiment Analysis API - GitHub Repository

This repository contains:

Deployed AI model API service code

Branches, commits, and Pull Requests showcasing collaboration

Detailed setup and usage instructions

⚙️ Setup and Run Locally
🐳 Docker Method (Recommended)
Clone the repository:

bash

git clone https://github.com/YOUR_USERNAME/sentiment-api.git
cd sentiment-api
Build the Docker image:

bash

docker build -t sentiment-api .
Run the container:

bash

docker run -d -p 8000:8000 sentiment-api
Check the API status: Open your browser or use Postman to visit:

bash

http://localhost:8000/docs
This will show the Swagger UI documentation, where you can test the API directly.

🔥 Python Method (If you prefer not using Docker)
Clone the repository:

bash

git clone https://github.com/YOUR_USERNAME/sentiment-api.git
cd sentiment-api
Create a virtual environment and install dependencies:

bash

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
Run the API server:

bash
uvicorn main:app --reload
Check the API status: Visit:

http://localhost:8000/docs
🎯 API Endpoints
POST /predict
Request Body:

json

{
  "text": "I am happy!"
}
Response:

json

{
  "label": "POSITIVE",
  "score": 0.9998
}
🧪 How to Test the API
Using Postman or cURL:

POST Request: Send a POST request to http://localhost:8000/predict with the body containing the text field.

Example using Postman:

Set the method to POST

URL: http://localhost:8000/predict

Add Content-Type: application/json header

In the body, send a JSON with the text you want to analyze, for example:

json


{
  "text": "I feel horrible!"
}
Example using cURL:

bash
Copy
Edit
curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"text": "I feel great!"}'
Swagger UI: Visit the Swagger UI to test all API endpoints interactively.

📂 Project Structure
graphql
Copy
Edit
sentiment-api/
│
├── main.py              # FastAPI app with /predict endpoint
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker container setup
├── .dockerignore        # Files/folders to ignore during Docker build
└── README.md            # This file
🧑‍🤝‍🧑 GitHub Collaboration Guidelines
Branches: Always work in branches for new features or bug fixes.

bash
Copy
Edit
git checkout -b feature-name
Commits: Make frequent commits with clear, meaningful commit messages.

Pull Requests (PRs): After completing a feature or fix, open a PR to merge into the master branch.

Review Code: Review each other's code through the PR process and leave constructive feedback.

Example of how to open a PR:

Open a PR from your feature branch to the master branch on GitHub.

Provide a meaningful description of the changes and ask for a review.

🔄 Version Control and Model Updates
The default branch for this repository is master.

Ensure all version updates to the model or changes to the code are documented in your commits and PR descriptions.

You can use the CHANGELOG.md (if needed) to track changes over time.

📦 Dependencies
FastAPI: Web framework for building APIs

Transformers: Hugging Face Transformers for model handling

Uvicorn: ASGI server for serving the FastAPI app

Install them via requirements.txt:

bash

pip install -r requirements.txt


📝 License
This project is licensed under the MIT License - see the LICENSE file for details.