import streamlit as st
import pandas as pd
from pathlib import Path

def main() -> None:
    st.write("# The Tools")

    st.markdown(
    """
    ## Glossary
    |Meaning|Emoji|
    |:-:|:-:|
    |Build in Progress|🔮|
    |Complete|🧰|

    """
    )

if __name__ == "__main__":
    st.set_page_config(
        "The Tools by Hirawat",
        "🕴️",
        initial_sidebar_state="expanded",
        layout="wide",
        menu_items={
            "Get Help": "https://github.com/hirawatt/tools",
            "Report a bug": "https://github.com/hirawatt/tools/issues",
            "About": "# This is an *extremely* cool app!",
            },
    )
    main()