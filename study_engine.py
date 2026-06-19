def generate_answer(question,notes):

    if notes:

        return f"""
Based on your study material:

Question:
{question}


Explanation:

Study this concept carefully.
Your notes mention:

{notes[:500]}

"""

    else:

        return "No study material found."




def create_quiz(topic):


    return f"""

Quiz Topic: {topic}


1. Explain the definition of {topic}.

2. What are the important points of {topic}?

3. Give one real world example.


Answer these and improve your knowledge.

"""
