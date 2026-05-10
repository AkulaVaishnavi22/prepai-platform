PRACTICE_TYPES = {

    "python": [
        "coding",
        "mcq",
        "interview"
    ],

    "javascript": [
        "coding",
        "mcq"
    ],

    "react": [
        "project",
        "interview"
    ],

    "machine learning": [
        "project",
        "interview"
    ],

    "deep learning": [
        "project"
    ],

    "nlp": [
        "research",
        "project"
    ]
}


def get_practice(skill):

    return PRACTICE_TYPES.get(
        skill,
        ["general practice"]
    )