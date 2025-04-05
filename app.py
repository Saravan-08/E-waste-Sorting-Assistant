import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import io

def classify_waste(ai_response):
    ai_response = ai_response.lower()
    
    if "recyclable" in ai_response:
        category = "Recyclable"
        disposal_info = "Send to an e-waste recycling facility."
    elif "repairable" in ai_response:
        category = "Repairable"
        disposal_info = "Consider repairing or donating."
    elif "disposable" in ai_response or "not repairable" in ai_response:
        category = "Disposable"
        disposal_info = "Dispose at an authorized e-waste collection center."
    else:
        category = "Unknown"
        disposal_info = "Proper disposal method not found."

    return {"classification": ai_response, "category": category, "disposal_info": disposal_info}

# Configure Gemini API
API_KEY = "AIzaSyCc8q8A-Iyw-NDWvcfxCax0WGaXBAUdxFk"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize Flask app
app = Flask(__name__)
CORS(app)

@app.route("/classify", methods=["POST"])
def classify_image():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    img = Image.open(io.BytesIO(file.read()))

    # Call Gemini API for classification
    response = model.generate_content(["Classify this e-waste item as Recyclable, Repairable, or Disposable:", img])

    classification_text = response.text.strip()
    result = classify_waste(classification_text)

    return jsonify(result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Railway's dynamic port
    app.run(host="0.0.0.0", port=port)        # Listen on all interfaces