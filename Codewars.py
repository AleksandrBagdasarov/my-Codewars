def duplicate_count(text):
    duplicate = ''
    for x in text:
        if text.lower().count(x) > 1:
            duplicate += x
    print(len(set(duplicate)))



duplicate_count("abcdeaB")# 2)
duplicate_count("abcdea")# 1)
duplicate_count("indivisibility")# 1)