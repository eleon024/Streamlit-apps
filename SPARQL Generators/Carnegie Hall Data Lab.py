import streamlit as st
import requests
import json
import urllib.parse

def render_sparql_query(query):
    encoded_query_url = get_encoded_url(query)
    html_link = f'<a href="{encoded_query_url}" target="_blank">Encoded Query</a>'
    st.components.v1.html(html_link, height=30)

def get_encoded_url(query):
    base_url = "https://data.carnegiehall.org/sparql/#"
    encoded_query = urllib.parse.quote(query)
    encoded_query_url = f"{base_url}query={encoded_query}"
    return encoded_query_url


st.title("Carnegie Hall Data Lab SPARQL Query Generator")


query_options = {

	"Find people": """
		PREFIX schema: <http://schema.org/>
		SELECT ?person ?name WHERE {
			?person a schema:Person ;
			schema:name ?name .
		}
		LIMIT %s""",
	"Find a specific person by name": """
		PREFIX schema: <http://schema.org/>
		select ?s ?p ?o where {
		?s ?p ?o ;
		a schema:Person ;
		schema:name "%s" .
		}""",
	"Find works": """
		PREFIX schema: <http://schema.org/>
		PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
		select ?work ?title where {
		?work a schema:MusicComposition ;
			rdfs:label ?title .
		}
		limit %s""",
	"Find works by string in the title (case-insensitive)": """
		PREFIX dcterms: <http://purl.org/dc/terms/>
		PREFIX schema: <http://schema.org/>
		PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
		select distinct ?work ?composer ?title where {
		?work a <http://schema.org/MusicComposition> ;
			  dcterms:creator ?creator ;
			  rdfs:label ?title .
		?creator schema:name ?composer
			  filter regex(?title, %s, "i")
		}
		limit %l """,
	# Add more query options here
}

selected_option = st.selectbox("Select an option", list(query_options.keys()))

if selected_option in ("Find people","Find works"):
	query_template = query_options[selected_option]
	search_term = st.text_input("Enter number of "+ selected_option.split()[1]+" to find:")
	if search_term:
		query = query_template % search_term

		st.subheader("Generated SPARQL Query:")
		st.code(query)
		render_sparql_query(query)

elif selected_option == "Find a specific person by name":
	query_template = query_options[selected_option]

	search_term = st.text_input("Enter search term:")
	if search_term:
		query = query_template % search_term

		st.subheader("Generated SPARQL Query:")
		st.code(query)
		render_sparql_query(query)
		
elif selected_option == "Find works by string in the title (case-insensitive)":
    query_template = query_options[selected_option]

    search_term = st.text_input("Enter title:")
    limit_term = st.text_input("Enter number of pieces:")
    if search_term and limit_term:
        query = query_template.replace("%s", f'"{search_term}"').replace("%l", limit_term)

        st.subheader("Generated SPARQL Query:")
        st.code(query)
        render_sparql_query(query)

		





