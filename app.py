from flask import Flask, request, jsonify, send_file
import os
import shutil
from gradio_client import Client, exceptions
import re
import time

app = Flask(__name__)

client = Client("SahaniJi/FLUX.1-schnell")

def sanitize_filename(prompt):
    return re.sub(r'[^a-zA-Z0-9_\- ]', '', prompt).replace(' ', '_')

@app.route("/")
def home():
    return "Flask is installed!"

@app.route('/generate-image', methods=['GET'])
def send_message()
    return "This is image"

@app.route('/generate-image', methods=['POST'])
def generate_image():
    data = request.json
    prompt_text = data.get("prompt", "")
    timestamp = time.strftime("%Y%m%d-%H%M%S")

    try:
        result = client.predict(
            prompt=prompt_text,
            seed=0,
            randomize_seed=True,
            width=1024,
            height=1024,
            num_inference_steps=28,
            api_name="/infer"
        )
        image_temp_path, response_timestamp = result
        output_image_path = f"output/image_{timestamp}.png"

        os.makedirs(os.path.dirname(output_image_path), exist_ok=True)

        if os.path.isfile(image_temp_path):
            shutil.copyfile(image_temp_path, output_image_path)
            return send_file(output_image_path, mimetype='image/png')
        else:
            return jsonify({"error": "No image file found."}), 400

    except exceptions.AppError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
