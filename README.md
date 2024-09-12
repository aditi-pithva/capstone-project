##GPT-2 Fine-tuning and Flask Deployment for Healthcare Text Generation

This project involves fine-tuning a GPT-2 model using PyTorch and deploying it with a Flask API for generating healthcare-related text based on user input. The model is trained on the PubMed dataset and can be accessed via an API for inference.

**Project Overview**
The goal of this project is to build a text generation model that is fine-tuned on healthcare-specific data. The model is then deployed using Flask, allowing users to generate text by providing an initial prompt through a REST API.

**Key Features**
* Fine-tune GPT-2 on healthcare-specific text (e.g., PubMed articles).
* Deploy a Flask API for real-time text generation.
* Handle requests via HTTP to generate text based on user input.
* GPU Support: The model can run on CUDA-enabled devices for faster inference.
