import streamlit as st

from without_sample import without_sample
from with_sample import with_sample
from network_timeseries import network_timeseries

def main():
    main_choice = None
    with st.sidebar:
        st.header("Synthetic Data Generator")
        
        main_choice = st.radio(
            label = "",
            options = [ "**Without Sample**", "**With Sample**", "**Network Timeseries**"], 
            captions = ["Increase volume of existing data", "Generate new data from scratch", "Interconnected data that changes over time"], 
            index=0 # set to choice during devalopment
        )
    
    if main_choice == "**Without Sample**":
        without_sample()
    elif main_choice == "**With Sample**":
        with_sample()
    elif main_choice == "**Network Timeseries**":
        network_timeseries()
    else:
        st.error("Select an option from sidebar")

if __name__ == "__main__":
    main()