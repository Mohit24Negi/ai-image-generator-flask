# 🎨 AI Image Generator (Flask + Stable Diffusion XL)

A modern AI-powered web application built using Flask and HuggingFace Stable Diffusion XL that generates images from text prompts and displays them in a responsive gallery.

---

## 🚀 Features
- AI Image Generation using Stable Diffusion XL
- Modern Dark UI
- Session-based Image History
- Download Generated Images
- Clear History Button
- Secure API Key Handling using Environment Variables

---

## 🛠 Tech Stack
- Python 3
- Flask
- HuggingFace Inference API
- HTML & CSS
- Git & GitHub

---

## ⚙️ Setup & Run (Complete Steps)

1. Clone the repository:

   git clone https://github.com/Mohit24Negi/ai-image-generator-flask.git  
   cd ai-image-generator-flask  

2. Create virtual environment (recommended):

   python -m venv venv  
   venv\Scripts\activate  

3. Install dependencies:

   pip install flask requests  

4. Set HuggingFace API Key  

   Create a `.env` file (DO NOT push to GitHub):

   HF_API_KEY=your_huggingface_api_key_here  

   OR set environment variable:

   setx HF_API_KEY "your_api_key_here"  

   Restart terminal after setting.

5. Run the application:

   python app.py  

6. Open browser:

   http://127.0.0.1:5000  

---

## 🧠 How It Works
- User enters a text prompt.
- Flask sends request to HuggingFace API.
- Image is returned as bytes.
- Converted to Base64 format.
- Displayed in image gallery.
- Stored in session history.
- Users can download or clear images.

---

## 🔒 Security
- API key stored using environment variables
- `.env` excluded using `.gitignore`
- No secrets committed to repository

---

## 👨‍💻 Author
Mohit Negi  
Python Developer  
GitHub: https://github.com/Mohit24Negi
