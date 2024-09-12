from flask import Flask, request, jsonify
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

# Step 1: Load the fine-tuned model and tokenizer
model = GPT2LMHeadModel.from_pretrained('./fine-tuned-gpt2-pytorch')
tokenizer = GPT2Tokenizer.from_pretrained('./fine-tuned-gpt2-pytorch')

# Set the model to evaluation mode
model.eval()

# Step 2: Initialize Flask app
app = Flask(__name__)

# Step 3: Define a route for generating text
@app.route('/generate', methods=['POST'])
def generate_text():
    # Get input from the request
    input_text = request.json.get('input_text')
    
    # Tokenize the input text
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    
    # Generate text using the fine-tuned model
    with torch.no_grad():
        output = model.generate(input_ids, max_length=100, num_return_sequences=1)
    
    # Decode the output text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    # Return the generated text as a JSON response
    return jsonify({"generated_text": generated_text})

# Step 4: Define the main function to run the app
if __name__ == '__main__':
    app.run(debug=True)