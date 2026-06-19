import random


def generate_answer(question, notes):

    question = question.lower().strip()


    # Greetings

    if "hello" in question or "hi" in question:
        return """
Hello 👋

I am StudyMate AI.
Ask me questions about your study topics.
"""


    # Apple question

    if "apple" in question and ("colour" in question or "color" in question):
        return """
🍎 Apple colours:

- Red apple
- Green apple
- Yellow apple

The colour depends on the type of apple.
"""


    # Python

    if "python" in question:

        return """
🐍 Python:

Python is a high-level programming language.

Features:
• Easy syntax
• Object-oriented
• Used in AI, web development, and automation
• Large library support
"""


    # Java

    if "java" in question:

        return """
☕ Java:

Java is an object-oriented programming language.

Features:
• Platform independent
• Secure
• Supports classes and objects
• Used for applications and Android development
"""


    # Data Structures

    if "data structure" in question or "datastructure" in question:

        return """
📚 Data Structures:

Data structures are methods to organize and store data efficiently.

Examples:

• Array
• Linked List
• Stack
• Queue
• Tree
• Graph
"""


    # Array

    if "array" in question:

        return """
Array:

An array stores multiple values of the same type in a single variable.

Example:

Numbers = [10,20,30]

Advantages:
• Fast access
• Easy data storage
"""


    # If notes contain answer

    words = question.split()

    for word in words:

        if word in notes.lower():

            return f"""
📖 From your study notes:

{notes[:500]}
"""


    # Default response

    return """
I could not find the exact answer.

Try asking questions like:

• What is Python?
• Explain Java
• What is an Array?
• Explain Data Structure
• What is the colour of an apple?
"""





def create_quiz(topic):

    quiz = f"""

📝 Quiz: {topic}


1. Define {topic}.

2. Explain the important features of {topic}.

3. Give one real-world example of {topic}.

4. Why is {topic} useful?


"""

    return quiz
