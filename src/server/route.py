from flask import Flask, request, jsonify
from dotenv import load_dotenv
from groq import Groq
from pinecone import Pinecone, ServerlessSpec
from webscraper import webscraper as ws
import os

app = Flask(__name__)

@app.route('/rmp-link', methods=['POST'])
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

    response = groq.embeddings.create(input=data['comments'], model="multilingual-e5-large")
    embeddings = response.data[0].embedding

    processed_data = {
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
    }
    
    return jsonify(processed_data)
