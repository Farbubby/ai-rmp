from flask import Flask, request, jsonify
from dotenv import load_dotenv
from groq import Groq
from pinecone import Pinecone
from webscraper import webscraper as ws
import requests
import os

app = Flask(__name__)

system_prompt = """You are a rate my professor agent to help students find their professors for their classes.
                   Using a dictionary of information for a professor which will be provided, create a really 
                   detailed and generalized paragraph summary containing all of the information in the
                   dictionary."""

def getEmbeddings(model_id: str, hf_token: str, data: list[str]):
    api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
    headers = {"Authorization": f"Bearer {hf_token}"}

    response = requests.post(api_url, headers=headers, json={"inputs": data, "options":{"wait_for_model":True}})
    return response.json()


@app.route('/api/link', methods=['POST'])
def gen_data():
    link = request.json['link']

    if not link:
        return jsonify({ 'error': 'Please provide a link to RateMyProfessor' })

    data = ws.scrape_rmp_link(link)

    if data['prof_name'] == "N/A":
        return jsonify({ 'error': 'Could not find professor information on RateMyProfessor' })
    
    load_dotenv()

    # initialize the APIs
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    groq = Groq(api_key=os.getenv("GROQ_API_KEY"))

    response = groq.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": str(data)
            }
        ],
        model="llama3-8b-8192",
    )

    model_id = "intfloat/multilingual-e5-large"
    hf_token = os.getenv("HUGGINGFACE_API_KEY")

    summary = response.choices[0].message.content

    embeddings = getEmbeddings(model_id, hf_token, summary)

    processed_data = [{
        "values": embeddings,
        "id": data['prof_name'],
        "metadata": {
            "summary": summary,
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

    print(f"Upserted count: {upsert_response['upserted_count']}")

    # Print index statistics
    print(index.describe_index_stats())

    data.update({ 'summary': summary })

    return jsonify(data)
