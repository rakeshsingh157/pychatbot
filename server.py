from flask import Flask, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)

# Replace with your actual API key (use environment variables in production)
genai.configure(api_key=os.environ.get("AIzaSyBcVtv-DZT4vXvldt68kTIPgLKRN0HRxjQ"))

model = genai.GenerativeModel('gemini-1.0-pro')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('message')

    if not user_input:
        return jsonify({'error': 'Message is required'}), 400

    try:
        response = model.generate_content(user_input)
        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))