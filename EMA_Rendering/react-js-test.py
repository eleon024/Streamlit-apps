import streamlit as st
import urllib.parse

st.set_page_config(layout="wide")

# Set initial values for the textboxes
pieceURL = st.text_input("Piece URL", "https://raw.githubusercontent.com/CRIM-Project/CRIM-online/master/crim/static/mei/MEI_4.0/CRIM_Mass_0002_2.mei")
ema_expression = st.text_input("EMA Expression", "/4-5/3+5,3+5/@2-4+@2-all,@1+@1/highlight")
measure_range = st.text_input("Measure Range", '{"measureRange": "4-5"}')

show_hide_checkbox = st.checkbox("Show/Hide")

react_app_url = "https://eleon024.github.io/ema_react_app/"  # Replace with the URL of your deployed React app

params = {
    "pieceURL": pieceURL,
    "ema_expression": ema_expression,
    "measure_range": measure_range
}

# URL-encode the measure_range parameter
params["measure_range"] = urllib.parse.quote(params["measure_range"])

# Construct the query string
query_string = urllib.parse.urlencode(params)

full_url = react_app_url + "?" + query_string

if show_hide_checkbox:
    st.write(full_url)

    html_code = f"""
    <style>
        body {{
            margin: 0;
            padding: 0;
            overflow: hidden;
        }}
        iframe {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            border: none;
        }}
    </style>
    <div>
        <iframe src="{full_url}"></iframe>
    </div>
    """
    html_code = None
    html_code = f"""
    <style>
        body {{
            margin: 0;
            padding: 0;
            overflow: hidden;
        }}
        iframe {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            border: none;
        }}
    </style>
    <div>
        <iframe src="{full_url}"></iframe>
    </div>
    """
    st.components.v1.html(html_code, height = 1500)


