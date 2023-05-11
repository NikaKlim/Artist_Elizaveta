from languages.lang.en import en
from languages.lang.pl import pl
from languages.lang.ru import ru


def choose_lang(lang):
    if lang == 'pl':
        return pl
    elif lang == 'en':
        return en
    else:
        return ru
