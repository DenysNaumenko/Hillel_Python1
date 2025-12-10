import codecs


def delete_html_tags(html_file="draft.html", result_file="cleaned.txt"):
    with codecs.open(html_file, "r", "utf-8") as file:
        html = file.read()

    result = []
    inside_tag = False

    for char in html:
        if char == "<":
            inside_tag = True
            continue
        if char == ">":
            inside_tag = False
            continue

        if not inside_tag:
            result.append(char)

    clean_text = "".join(result)

    with codecs.open(result_file, "w", "utf-8") as file:
        file.write(clean_text)


delete_html_tags("draft.html", "cleaned.txt")
