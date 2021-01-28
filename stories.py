



"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a code, a title, a list of prompts,
    and the text of the template.

        >>> s = Story(
        ...     "simple",
        ...     "A Simple Tale",
        ...     ["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, genre, title, words, text):
        """Create story with words and template text."""

        self.genre = genre
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story(
    "history",
    "A History Tale",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    "omg",
    "An Excited Adventure",
    ["noun", "verb"],
    """OMG!! OMG!! I love to {verb} a {noun}!"""
)

kind_story = Story(
    "Nice",
    "Be Kind",
    ["Noun","Noun(plural)","Noun","Noun(Plural)","Adjective"],
    """Be kind to your {Noun}-footed {Noun}
For a duck may be somebody`s {Noun},
Be kind to your {Noun} in Place
Where the weather is always {Adjective}.

You may think that this is the {Noun},
Well it is.
"""
)

# Make dict of {code:story, code:story, ...}

stories = { "history":story1, "omg":story2, "Nice":kind_story}
