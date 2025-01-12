from flask import Flask, render_template, request, jsonify
import openai
import os
import traceback
import time
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get API key from environment variable
TOGETHER_API_KEY = os.getenv('TOGETHER_API_KEY')
if not TOGETHER_API_KEY:
    raise ValueError("TOGETHER_API_KEY not found in environment variables")

# Configure OpenAI with Together API
openai.api_key = TOGETHER_API_KEY
openai.api_base = "https://api.together.xyz/v1"

def generate_with_retry(prompt, max_retries=3, delay=2):
    last_error = None
    for attempt in range(max_retries):
        try:
            print(f"\nAttempt {attempt + 1} for prompt: {prompt}")
            response = openai.Image.create(
                model="black-forest-labs/FLUX.1-schnell-Free",
                prompt=prompt,
                n=1,
                size="1024x1024"
            )
            print(f"Success! Response: {json.dumps(response, indent=2)}")
            return response
        except Exception as e:
            last_error = e
            error_msg = f"Attempt {attempt + 1} failed: {str(e)}"
            print(error_msg)
            if attempt < max_retries - 1:
                print(f"Waiting {delay} seconds before retry...")
                time.sleep(delay)
            else:
                print("All attempts failed.")
                raise last_error

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_image():
    try:
        prompt = request.form.get('prompt')
        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400

        print(f"\nReceived generation request with prompt: {prompt}")
        response = generate_with_retry(prompt)
        
        if not response or 'data' not in response or not response['data']:
            return jsonify({'error': 'No image data in response'}), 500
            
        image_url = response['data'][0]['url']
        print(f"Successfully generated image: {image_url}")
        return jsonify({'image_url': image_url})
    except Exception as e:
        error_msg = f"Error: {str(e)}\n{traceback.format_exc()}"
        print(f"\nError during generation:\n{error_msg}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 