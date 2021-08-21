from pygments.lexer import RegexLexer, bygroups, words, using
from pygments.token import *
from pygments.lexers.data import JsonLexer

__all__ = ("ProfilesLexer")

class ProfilesLexer(RegexLexer):
    name = 'Inventory-Profiles-Next profiles'
    aliases = ['profiles']
    filenames = ['profiles-*.txt']
    mimetypes = ['text/inventory-profiles-next-profiles']

    tokens = {
        'root': [
            (
                r'\[.*\]',
                using(JsonLexer)
            ),
            (
                r'(profile)( )([A-z1-9]*)',
                bygroups(Keyword, Whitespace, Name)
            ),
            (
                words(
                    (
                        'profile',
                        'activate'
                    )
                ),
                Number
            ),
            (
                r'->',
                Operator
            ),
            (
                r'(HOT[1-9]|OFFHAND|HEAD|CHEST|LEGS|FEET)',
                Keyword
            ),
            (
                r'[1-9]+',
                Number
            ),
            (
                r'\".*?\"',
                String
            )
        ]
    }
