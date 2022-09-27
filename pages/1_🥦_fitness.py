import streamlit as st

def main():
    tab1, tab2, tab3 = st.tabs(["Calculator", "Workout", "Protein Chart"])

    with tab1:
        st.header("Push-Up Body Weight Calculator")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

    with tab2:
        st.header("Workout")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

    with tab3:
        st.header("Protein Chart")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

if __name__ == "__main__":
    st.set_page_config(
        "Fitness | Health",
        "🕴️",
        initial_sidebar_state="expanded",
        layout="wide",
    )
    main()