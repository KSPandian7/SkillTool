# SkillTool – Framework Recommendation System

## → A smart recommendation tool built with Streamlit, FAISS, and Sentence Transformers to suggest related frameworks based on a given technology name.

### 🔗 Live Demo: [skilltool.streamlit.app](https://skilltool.streamlit.app/)

### 📌 Overview
![image](https://github.com/user-attachments/assets/d26c2cb3-3faa-4943-b64f-dd0b39bc529b)

→ SkillTool helps developers discover related frameworks and technologies quickly by leveraging semantic similarity using embeddings and vector search.
<br>
→ Whether you're starting with React.js or Spring Boot, SkillTool gives you smart recommendations like Angular.js, Vue.js, or Next.js — depending on what you're looking for!

### 🧠 How It Works
→ **Data**: Loads a curated list of frameworks from skills.csv<br>
![image](https://github.com/user-attachments/assets/3dc8f921-fee2-4f0b-b3a1-5b6cd229dbac)<br>
→ **Embeddings**: Converts all skill names into vectors using SentenceTransformer (all-MiniLM-L6-v2).<br>
→ **Indexing**: Uses FAISS to build a similarity index.<br>
→ **Search**: Accepts user input and retrieves the top-k closest technologies (excluding exact matches).<br>
→ **UI**: Built with Streamlit for easy interaction.<br>

### 🧾 Requirements
→ Install the required libraries with:<br>
```base
pip install -r requirements.txt
```
#### Required packages:
→ streamlit<br>
→ pandas<br>
→ sentence-transformers<br>
→ faiss-cpu / faiss-gpu (based on your environment)<br>
→ numpy<br>

### 🛠️ Run Locally
```python
streamlit run app.py
```

### 📂 File Structure
```base
├── nlppro.py
├── skills.csv
├── requirements.txt
├── README.md   
```

### 📈 Features
→ Fast and accurate framework suggestions<br>
→ FAISS-powered vector search<br>
→ Lightweight and easy to run<br>
→ Clean UI with interactive slider<br>

### 🤖 Sample Use Case

#### Input:
→ React.js<br>
#### Output:
→ Angular.js<br>
→ Vue.js<br>
→ Next.js<br>


```base
Built by Kulasekarapandian K
```
