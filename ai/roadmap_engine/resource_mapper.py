RESOURCES = {

    "python": [
        "https://www.youtube.com/watch?v=_uQrJ0TkZlc",
        "https://www.freecodecamp.org/learn"
    ],

    "javascript": [
        "https://javascript.info/",
        "https://www.youtube.com/watch?v=W6NZfCO5SIk"
    ],

    "react": [
        "https://react.dev/learn",
        "https://www.youtube.com/watch?v=bMknfKXIFA8"
    ],

    "machine learning": [
        "https://www.coursera.org/learn/machine-learning",
        "https://www.youtube.com/watch?v=GwIo3gDZCVQ"
    ],

    "deep learning": [
        "https://www.deeplearning.ai/"
    ],

    "nlp": [
        "https://huggingface.co/learn"
    ]
}


def get_resources(skill):

    return RESOURCES.get(
        skill,
        ["No resources found"]
    )