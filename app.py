import streamlit as st
from data_ingestion import load_notes
from study_engine import generate_answer, create_quiz


st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚",
    layout="wide"
)


# Header

st.title("📚 StudyMate AI")
st.subheader("Your Personal AI Study Companion")


menu = st.sidebar.selectbox(
    "Choose Feature",
    [
        "Ask Doubts",
        "Generate Quiz",
        "Study Planner"
    ]
)


notes = load_notes()


if menu == "Ask Doubts":

    st.header("🤖 Ask your study questions")

    question = st.text_input(
        "Enter your question"
    )


    if st.button("Get Answer"):

        if question:

            response = generate_answer(
                question,
                notes
            )

            st.success(response)

        else:
            st.warning(
                "Please enter a question"
            )



elif menu == "Generate Quiz":

    st.header("📝 AI Quiz Generator")


    topic = st.text_input(
        "Enter topic"
    )


    if st.button("Create Quiz"):

        quiz = create_quiz(topic)

        st.write(quiz)



elif menu == "Study Planner":

    st.header("📅 Study Planner")


    subject = st.text_input(
        "Subject"
    )

    hours = st.number_input(
        "Study Hours",
        min_value=1,
        max_value=12
    )


    if st.button("Generate Plan"):

        st.success(
            f"""
            Study Plan Created:

            Subject:
            {subject}

            Daily Time:
            {hours} hours

            Revision:
            30 minutes

            Practice:
            1 hour
            """
        )
