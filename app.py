import streamlit as st

from without_sample import without_sample
from with_sample import with_sample
from network_timeseries import network_timeseries
from llm_tabular import few_shot
from llm_relation import llm_relation

def main():
    main_choice = None
    choices =  [ 
                    "**Without Sample**", 
                    "**With Sample**", 
                    "**Network Timeseries**",
                    "**LLM based Tabular Data**",
                    "**LLM based Entitiy Relationship**"
                ]
    with st.sidebar:
        st.header("Synthetic Data Generator")
        
        main_choice = st.radio(
            label = "",
            options = choices,
            captions = [
                "Increase volume of existing data", 
                "Generate new data from scratch", 
                "Interconnected data that changes over time",
                "Tabular Data generated from context using LLMs",
                "Foreign Key relation generation between 2 tables"
                ], 
            index=0 # set to choice during devalopment
        )
    
    if main_choice == choices[0]:
        without_sample()
    elif main_choice == choices[1]:
        with_sample()
    elif main_choice == choices[2]:
        network_timeseries()
    elif main_choice == choices[3]:
        few_shot()
    elif main_choice == choices[4]:
        llm_relation()
    else:
        st.error("Select an option from sidebar")

if __name__ == "__main__":
    main()