from flask import Flask, request, jsonify
from dotenv import load_dotenv
from groq import Groq
from pinecone import Pinecone, ServerlessSpec
from webscraper import webscraper as ws
import requests
import os

app = Flask(__name__)

def getEmbeddings(model_id: str, hf_token: str, data: list[str]):
    api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
    headers = {"Authorization": f"Bearer {hf_token}"}

    response = requests.post(api_url, headers=headers, json={"inputs": data, "options":{"wait_for_model":True}})
    return response.json()


@app.route('/link', methods=['POST'])
def rmp_link():
    link = request.json['link']

    if not link:
        return jsonify({ 'error': 'Please provide a link to RateMyProfessor' })

    data = ws.scrape_rmp_link(link)

    if data['prof_name'] == "N/A":
        return jsonify({ 'error': 'Could not find professor information on RateMyProfessor' })
    
    load_dotenv()

    # initialize the APIs
    groq = Groq(api_key=os.getenv("GROQ_API_KEY"))
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

    model_id = "sentence-transformers/all-MiniLM-L6-v2"
    hf_token = os.getenv("HUGGINGFACE_API_KEY")

    embeddings = getEmbeddings(model_id, hf_token, data['prof_name'])

    processed_data = [{
        "values": embeddings,
        "id": data['prof_name'],
        "metadata": {
            "comments": data['comments'],
            "department": data['prof_dept'],
            "university": data['university_name'],
            "rating": data['rating'],
            "top_tags": data['top_tags'],
            "difficulty": data['difficulty'],
            "classes_taught": data['classes_taught'],
        }
    }]

    # Insert the embeddings into the Pinecone index
    index = pc.Index("rmp-index")
    upsert_response = index.upsert(
        vectors=processed_data,
        namespace="professors",
    )
    
    return jsonify(upsert_response)
