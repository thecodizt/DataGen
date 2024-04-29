import streamlit as st
import pandas as pd

from llm_relation.input import load_data
from llm_relation.evaluate import evaulate_model

def llm_relation():
    st.title("LLM Based Entity Relation Mapping")
    
    st.subheader("Model")
    model = st.selectbox(label="Choose the LLM to be used", options=["mistral", "vicuna"])
    
    st.subheader("Relation Context")
    context = st.text_input(label="Enter the base context for linking items")
    
    st.subheader("Table 1")
    dataset_1 = load_data("t1")
    
    if dataset_1 is not None and len(dataset_1) > 0:
        st.subheader("Table 2")
        dataset_2 = load_data("t2")
        
        st.header("Generated Pairing")
        
        if dataset_2 is not None and len(dataset_2) > 0:
            relation = evaulate_model(dataset_1=dataset_1,dataset_2=dataset_2, model=model, context=context)
            
            if relation:
                st.dataframe(relation)