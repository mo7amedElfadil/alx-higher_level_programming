#!/usr/bin/python3
"""
This is the text_indentation module.

The module supplies one function, text_indentation().
Prototype: def text_indentation(text):


Rules:
    text must be a string, otherwise:
        raise a TypeError exception with the message
            "text must be a string"
    There should be no space at the beginning or
        at the end of each printed line

"""


def text_indentation(text):
    """definition of text_indentation function
    prints a text with 2 new lines after each of these characters:
        ., ? and :

    Parameters:
        text (str): text to be indented.

    Returns:
        Nothing.

    #testing with empty string
    >>> text_indentation("")

    #testing with negative int text
    >>> text_indentation(-1)
    Traceback (most recent call last):
        ...
    TypeError: text must be a string

    #testing when text is a float
    >>> text_indentation(1.0)
    Traceback (most recent call last):
        ...
    TypeError: text must be a string

    #testing when text is a numeric str
    >>> text_indentation('3')
    3


    #testing with more than 1 arg
    >>> text_indentation('3', '56')
    Traceback (most recent call last):
        ...
    TypeError: text_indentation() takes 1 positional argument but 2 were given

    #testing when size is None
    >>> text_indentation(None)
    Traceback (most recent call last):
        ...
    TypeError: text must be a string

"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    res = []
    delim = ".?:"
    track = ""
    for c in text:
        if c in delim:
            if track:
                track += c
                res.append(track.strip())
                track = ""
        else:
            track += c
    if track:
        res.append(track.strip())
    print("\n\n".join(res), end="")


text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres"""
