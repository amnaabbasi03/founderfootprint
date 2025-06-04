# app.py
import streamlit as st
from scrape_utils import get_articles_for_person
from summarize import generate_summary_report

st.set_page_config(page_title="FounderFootprint", layout="wide")
st.title("FounderFootprint: Digital Profile Generator")

name = st.text_input("Enter the name of the founder or CEO")
company = st.text_input("(Optional) Company name")
num_results = st.slider("Number of articles to fetch", min_value=1, max_value=10, value=5)

if st.button("Generate Profile") and name:
    with st.spinner("Fetching and analyzing data..."):
        articles = get_articles_for_person(name, company, num_results)

        if not articles:
            st.error("No relevant articles found. Try a different name.")
        else:
            sections = generate_summary_report(name, articles)

            st.success("Summary generated!")
            for section, content in sections.items():
                st.subheader(section)
                st.write(content)

            with st.expander("🔗 Article Sources"):
                for art in articles:
                    st.markdown(f"- [{art['url']}]({art['url']})")

