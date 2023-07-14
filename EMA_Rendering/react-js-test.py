# import streamlit as st
# import streamlit.components.v1 as components
# import pandas as pd
# import numpy as np
# st.set_page_config(layout="wide")
# 
# 
# 
# def main():
#     st.title("React.js App in Streamlit")
#     st.markdown("This is a Streamlit app.")
# 
#     # Checkbox to show/hide React.js app
#     show_app = st.checkbox("Show Verovio EMA Annotations")
# 
#     # Conditionally render React.js app
#     if show_app:
#         # Embedding React.js app
#         components.html(
#         """
#         <div id="root"></div>
# 
#         <script src="https://eleon024.github.io/ema_react_test/main.3f3bf6cc.js"></script>
#         <script>
#             // React app initialization code
#             ReactDOM.render(React.createElement(App,{measure_range: "2-3"}), document.getElementById('root'));
#         </script>
#         """ , height=500
#         )
# 
# if __name__ == "__main__":
#     main()
# 
# 
# 
# 
#  
# import streamlit as st
# import streamlit.components.v1 as components
# import pandas as pd
# import numpy as np
# 
# st.set_page_config(layout="wide")
# 
# 
# def main():
#     st.title("React.js App in Streamlit")
#     st.markdown("This is a Streamlit app.")
# 
#     # Input fields for textbook information
# #     piece_url = st.text_input("Enter Piece URL")
# #     ema_expression = st.text_input("Enter EMA Expression")
# #     measure_range = st.text_input("Enter Measure Range")
# 
# #     piece_url="https://raw.githubusercontent.com/CRIM-Project/CRIM-online/master/crim/static/mei/MEI_4.0/CRIM_Mass_0002_1.mei";
# #     ema_expression="/4-5/3+5,3+5/@2-4+@2-all,@1+@1/highlight"
# #     measure_range={"measureRange": "2-3" }
# 
# 
#     # Checkbox to show/hide React.js app
#     show_app = st.checkbox("Show Verovio EMA Annotations")
# 
#     # Conditionally render React.js app
#     if show_app:
#         # Embedding React.js app
#         components.html(
#             """
#             <div id="root"></div>
#             <script src="https://cdnjs.cloudflare.com/ajax/libs/react/16.8.0/umd/react.production.min.js"></script>
#             <script src="https://cdnjs.cloudflare.com/ajax/libs/react-dom/16.8.0/umd/react-dom.production.min.js"></script>
# 
#             <script src="https://eleon024.github.io/ema_react_test/main.0e0d1093.js"></script>
#             
#             """, height=1500
#         )
# 
# 
# if __name__ == "__main__":
#     main()
# import streamlit as st
# import streamlit.components.v1 as components
# 
# st.set_page_config(layout="wide")
# 
# # Set the initial values for the text inputs
# initial_piece_url = "https://raw.githubusercontent.com/CRIM-Project/CRIM-online/master/crim/static/mei/MEI_4.0/CRIM_Mass_0002_1.mei"
# initial_ema_expression = "/4-5/3+5,3+5/@2-4+@2-all,@1+@1/highlight"
# initial_measure_range = '{"measureRange":"2-3"}'
# 
# # Text input widgets for the arguments
# piece_url = st.text_input("Piece URL", value=initial_piece_url)
# ema_expression = st.text_input("EMA Expression", value=initial_ema_expression)
# measure_range = st.text_input("Measure Range", value=initial_measure_range)
# 
# def main():
#     st.title("React.js App in Streamlit")
#     st.markdown("This is a Streamlit app.")
# 
#     # Checkbox to show/hide React.js app
#     show_app = st.checkbox("Show Verovio EMA Annotations")
# 
#     # Conditionally render React.js app
#     if show_app:
#         # Define the React component code
#         react_app_code = f"""
#         <script src="https://eleon024.github.io/ema_react_test/main.275e780b.js"></script>
# 
#         <script>
#             const App = React.createElement(window.App.default, {{
#                 pieceURL: "{piece_url}",
#                 ema_expression: "{ema_expression}",
#                 measure_range: {measure_range}
#             }});
#             const rootElement = document.getElementById("root");
#             ReactDOM.createRoot(rootElement).render(App);
#         </script>
#         """
# 
#         # Embedding React.js app
#         components.html(react_app_code, height=1500)
# 
# if __name__ == "__main__":
#     main()

# import streamlit as st
# st.set_page_config(layout="wide")
# pieceURL = "https://raw.githubusercontent.com/CRIM-Project/CRIM-online/master/crim/static/mei/MEI_4.0/CRIM_Mass_0002_1.mei"
# ema_expression = "/4-5/3+5,3+5/@2-4+@2-all,@1+@1/highlight"
# measure_range = '{"measureRange": "2-3"}'
# 
# react_app_url = "https://eleon024.github.io/ema_react_test/main.d482283d.js"  # Replace with your React app's URL
# params = f"?pieceURL={pieceURL}&ema_expression={ema_expression}&measure_range={measure_range}"
# full_url = react_app_url + params
# 
# iframe_code = f'<iframe src="{full_url}" width="100%" height="600px"></iframe>'
# 
# st.components.v1.html(iframe_code)


# import streamlit as st
# import urllib.parse
# st.set_page_config(layout="wide")
# 
# 
# 
# # Set initial values for the textboxes
# pieceURL = st.text_input("Piece URL", "https://raw.githubusercontent.com/CRIM-Project/CRIM-online/master/crim/static/mei/MEI_4.0/CRIM_Mass_0002_1.mei")
# ema_expression = st.text_input("EMA Expression", "/4-5/3+5,3+5/@2-4+@2-all,@1+@1/highlight")
# measure_range = st.text_input("Measure Range", '{"measureRange": "3-5"}')
# 
# react_app_url = "https://eleon024.github.io/ema_react_app/"  # Replace with the URL of your deployed React app
# 
# params = {
#     "pieceURL": pieceURL,
#     "ema_expression": ema_expression,
#     "measure_range": measure_range
# }
# 
# # URL-encode the measure_range parameter
# params["measure_range"] = urllib.parse.quote(params["measure_range"])
# 
# # Construct the query string
# query_string = urllib.parse.urlencode(params)
# 
# full_url = react_app_url + "?" + query_string
# st.write(full_url)
# html_code = f"""
# <div style="width: 100%; height: 100vh; overflow: auto;">
#     <iframe src="{full_url}" style="width: 100%; height: 100%; border: none;"></iframe>
# </div>
# """
# 
# st.components.v1.html(html_code)

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
    st.components.v1.html(html_code, height = 1500)




