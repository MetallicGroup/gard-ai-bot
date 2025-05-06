
from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@app.route("/generare", methods=["POST"])
def generate_image():
    data = request.json

    model = data.get("model_gard", "MX25")
    image_url = data.get("poza_gard", "")

    if not image_url or not OPENAI_API_KEY:
        return jsonify({"error": "Missing image or API key"}), 400

    # Example prompt for DALL·E – you can customize this to match your styles
    prompt = f"Montare gard model {model}, cu lamele orizontale, în fața casei din imagine."

    # Simulate image generation (real integration with OpenAI API would be more complex)
    response = {
        "image_url": f"https://via.placeholder.com/1024x768.png?text=Gard+{model.replace(' ', '+')}"
    }

    # Return the simulated image URL
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
