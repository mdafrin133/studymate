import os


def load_notes():

    folder="data"

    text=""

    if not os.path.exists(folder):
        return "No notes available"


    for file in os.listdir(folder):

        path=os.path.join(
            folder,
            file
        )


        if file.endswith(".txt"):

            with open(
                path,
                "r",
                encoding="utf-8"
            ) as f:

                text += f.read()


    return text



def save_notes(filename,content):

    os.makedirs(
        "data",
        exist_ok=True
    )


    with open(
        f"data/{filename}",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(content)
