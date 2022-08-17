# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad + Harshit


import regex


def regex_searcher(regex_string, string):
    try:
        search = regex.search(regex_string, string, timeout=6)
    except TimeoutError:
        return False
    except Exception:
        return False
    return search


def infinite_loop_check(regex_string):
    loop_matches = [
        r'\((.{1,}[\+\*]){1,}\)[\+\*].',
        r'[\(\[].{1,}\{\d(,)?\}[\)\]]\{\d(,)?\}',
        r'\(.{1,}\)\{.{1,}(,)?\}\(.*\)(\+|\* |\{.*\})'
    ]
    for match in loop_matches:
        match_1 = regex.search(match, regex_string)
        if match_1:
            return True
    return False

# Roses are red, Violets are blue, A face like yours, Belongs in a zoo
