import streamlit as st
import ollama
import re
import pandas as pd

def evaulate_model(dataset_1, dataset_2, model, context):
    results_df = pd.DataFrame(columns=["leftId", "rightId", "result"])
    
    res_st = st.empty()

    for leftId in range(len(dataset_1)):
        for rightId in range(leftId, len(dataset_2)):
            if leftId != rightId:

                (result, response) = evaluate_record(dataset=dataset_1, dataset_2=dataset_2, model=f'{model}', leftId=leftId, rightId=rightId, context=context)

                results_df = pd.concat([results_df, [{"leftId": leftId, "rightId": rightId, "result": result}]], ignore_index=True)

                if len(results_df)>0:
                    st.dataframe(results_df)   
                    
                                 
    return results_df

def evaluate_record(dataset_1, dataset_2, model, leftId, rightId, context):
    base_prompt = f'''
    In the context of {context} provide a score between 0 and 1 indicating the likelihood of relationship between the given two records from two tables.
    
    Records:
    
    '''
    
    message = base_prompt + convert_to_message(dataset_1, leftId) + "\n\n" + convert_to_message(dataset_2, rightId)

    response = ollama.chat(model, messages=[
        {
            'role': 'user',
            'content': message,
        },
    ])

    return (parse_response(response['message']['content']), response['message']['content'])

def convert_to_message(dataframe, id):
    cols = dataframe.columns

    record = dataframe.loc[id]

    message = ""

    for col in cols:
        message += col + ": " + str(record[col]) + "\n"

    return message

def find_last_float(s):
    matches = re.findall(r' 0\.[0-9]+', s)
    return float(matches[-1]) if matches else -1

def parse_response(response):
    return find_last_float(response)

def remove_special_chars(s):
    allowed_chars = set(".,:- ")

    s = s.replace("\n", " ")

    # Filter out special characters
    cleaned_string = "".join(c for c in s if  c.isalnum() or c in allowed_chars or c == " ")

    return cleaned_string