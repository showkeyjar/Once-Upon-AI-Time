"""
Generate prompts for different tasks.
"""


def plot() -> str:
    """
    Generate the prompt for creating the plot of a story.
    
    Returns:
        prompt
    """
    return "Create a detailed prompt and plot for a new happy children's short story. The story can be about animals, people, children, adventure, morals, or anything you want.\n\n"


def story_expansion(existing_story: str) -> str:
    """
    Expand a given story.

    Returns:
        prompt
    """
    return f"Rewrite this as a 2 page story with much more detail, a climax, and a happy ending. Give the characters names and describe the environment and plot in greater detail:\n\n{existing_story}\n\n"


def illustration(story: str) -> str:
    """
    Illustrate a part of the story.

    Returns:
        prompt
    """
    return f"Watercolor in the style of John DuVal for:\n\n{story}"


def title_translation(title: str) -> str:
    """
    Translate title into english

    Returns:
        prompt
    """
    return f'You are a professional Chinese to English translator, Translate this poem title into english, Only one answer is required, put the answer in quotes, Only keep the translation, no other content is needed, the poem title is "{title}"'


def dynasty_translation(dynasty: str) -> str:
    """
    Translate dynasty into english
    """
    return f'You are a professional Chinese to English translator, Translate this dynasty into english, Only one answer is required, put the answer in quotes, Only keep the translation, no other content is needed, the dynasty is "{dynasty}"'


def author_translation(author: str) -> str:
    """
    Translate author name into english
    """
    return f'You are a professional Chinese to English translator, Translate author name into english, Only one answer is required, put the answer in quotes, Only keep the translation, no other content is needed, the author name is "{author}"'


def author_profile(title: str, dynasty: str, author: str, gender: str, poem: str) -> str:
    """
    image user profile from giving info
    """
    # 去除多余的Dynasty
    dynasty = dynasty.replace('dynasty', 'Dynasty').replace('Dynasty', '') + " Dynasty"
    return f'You are an imaginative portrait painter, please use the information below to imagine what ancient Chinese poets looked like: name "{author}", gender {gender}, wrote a pome named <{title}>, lived in {dynasty}, the poem content is "{poem}", Only one answer is required, put the answer in quotes, keep only character descriptions, no other content is needed'


def poem_translation(poem: str) -> str:
    """
    Translate poem
    """
    return f'You are a professional Chinese ancient poetry expert, Please decipher these verses first and then translate them into English, please use ";" separate between each sentence, Only one answer is required, put the answer in quotes, Only keep the translation, no other content is needed, the pome content is "{poem}"'


def line_translation(poem: str) -> str:
    """
    Translate line
    """
    return f'You are a professional Chinese ancient poetry expert, Please decipher these verses first and then translate them into English, Just one answer, Only keep the translation, no other content is needed, the pome line is "{poem}"'


def poem_interpret(poem: str) -> str:
    """
    Interpret poem
    """
    return f'You are a professional Chinese ancient poetry expert, paraphrase this poem with chinese and english, Limit to 200 words or less, Only keep the paraphrase, no other content is needed, the pome content is "{poem}"'


def poem_associate_story(poem: str) -> str:
    """
    Associate poem with story
    """
    return f'You are a professional Chinese ancient poetry expert, please imagine the story behind the poem with chinese and english, Limit to 200 words or less, no other content is needed, the pome content is "{poem}"'


def poem_view(poem: str) -> str:
    """
    View poem
    """
    return f'You are a professional Chinese ancient poetry expert, please imagine the scene with english when the author wrote this poem, Only one scene is required, put the scene in quotes, Only keep the scene, no other content is needed, the pome content is "{poem}"'

