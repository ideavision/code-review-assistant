import display
import streamlit as st


def download_markdown(recommendations):
    if recommendations:
        st.download_button(
            "Download Markdown",
            data=display.generate_markdown(recommendations),
            file_name="code_review_assistant_recommendations.md",
            mime="text/markdown",
        )
    else:
        st.download_button(
            "Download Markdown",
            data="",
            file_name="code_review_assistant_recommendations.md",
            mime="text/markdown",
            disabled=True,
        )
