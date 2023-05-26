import wikipediaapi


def get_wiki_page(text: str):
    # en, de, ru, uz, fr
    wiki = wikipediaapi.Wikipedia('uz')
    result = wiki.page(text)

    return result.summary
