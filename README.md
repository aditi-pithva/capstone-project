## GPT-2 Fine-tuning and Flask Deployment for Healthcare Text Generation

This project involves fine-tuning a GPT-2 model using PyTorch and deploying it with a Flask API for generating healthcare-related text based on user input. The model is trained on the PubMed dataset and can be accessed via an API for inference.

**Project Overview**

The goal of this project is to build a text generation model that is fine-tuned on healthcare-specific data. The model is then deployed using Flask, allowing users to generate text by providing an initial prompt through a REST API.

**Key Features**
* Fine-tune GPT-2 on healthcare-specific text (e.g., PubMed articles).
* Deploy a Flask API for real-time text generation.
* Handle requests via HTTP to generate text based on user input.
* GPU Support: The model can run on CUDA-enabled devices for faster inference.

---
## MedQA Data
**Source**:  https://github.com/jind11/MedQA?tab=readme-ov-file
[Download the data from the above link]

The MedQA dataset consists of medical questions and answers from various sources like the US, Mainland China, and Taiwan, alongside textbooks in English and Chinese. The data is essential for training the medical chatbot to answer medical-related queries accurately.

---

## Project Overview

### What We Have Completed
- **Data Preprocessing**: 
  We cleaned and tokenized medical textbook data from various sources, removing irrelevant characters, lowercasing text, and tokenizing the text into manageable units. This process ensured the dataset was ready for machine learning models.

- **Data Management**: 
  We structured the cleaned data into a format suitable for training a machine learning model, organizing the content into tokenized text and corresponding categories (e.g., medical topics).



### Our Goal
The goal of this project is to develop a **medical chatbot** that can intelligently answer medical-related questions using the processed MedQA dataset. By leveraging machine learning models like BERT, we aim to:
- Enable the chatbot to understand and process complex medical queries.
- Provide accurate and relevant medical answers based on the underlying data.

This chatbot can potentially serve as a tool for medical professionals or students seeking quick, reliable medical information from authoritative textbooks.

---
