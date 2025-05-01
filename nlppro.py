import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss


df = pd.read_csv("skills.csv")
skills = df["Skills"].tolist()


#skills = ["React.js", "Angular.js", "Vue.js", "Next.js", "Flask", "Django", "Svelte", "Laravel", "Spring Boot", "Express.js"]

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

@st.cache_data
def embed_skills(_model, skills):
    embeddings = _model.encode(skills, convert_to_numpy=True)
    return embeddings

def build_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def main():
    st.title("🤖 Framework Recommendation System")
    st.write("Enter a technology name and get related suggestions!")

    model = load_model()
    skill_embeddings = embed_skills(model, skills)
    index = build_faiss_index(skill_embeddings)

    user_input = st.text_input("Enter a framework (e.g., React.js):")
    top_k = st.slider("Number of related frameworks to show", 1, 10, 1)

    if user_input:
        query_embedding = model.encode([user_input], convert_to_numpy=True)
        distances, indices = index.search(query_embedding, top_k + 1) 

        related_skills = [skills[i] for i in indices[0] if skills[i].lower() != user_input.lower()]
        st.subheader("🔎 Related Frameworks:")
        for s in related_skills[:top_k]:
            st.write(f"• {s}")

if __name__ == "__main__":
    main()
