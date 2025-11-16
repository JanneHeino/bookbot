def words_in_book(book):
    return len(book.split())


def count_characters(book):
    book = book.lower()
    characters = {}
    
    for a in book:
        if a in characters:
            characters[a] += 1
        else:
            characters[a] = 1
    
    return characters


def sort_on(chars):
    return chars["num"]


def sort_dict(char_dict):
    sorted_list = []
    for a in char_dict:
        sorted_list.append({"char": a, "num": char_dict[a]})
    
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list
