import google.generativeai as genai
import base64

# Ensure API key is set up
genai.configure(api_key="AIzaSyBxjk6iFYUHg4SC_Wfr_R8RaYEv72n9shg")

# Function to load and encode image in Base64
def load_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")  # Convert to Base64

# Function to classify e-waste
def classify_e_waste(image_path):
    model = genai.GenerativeModel("gemini-1.5-flash")
    image_data = load_image(image_path)

    response = model.generate_content(
        ["Classify this e-waste item as Recyclable, Repairable, or Disposable.", {"mime_type": "image/png", "data": image_data}]
    )

    return response.text  # AI's prediction

# Test the function
if __name__ == "__main__":
    test_image = "sample.jpg.webp"  # Use your actual image file
    result = classify_e_waste(test_image)
    print("Predicted Category:", result)


