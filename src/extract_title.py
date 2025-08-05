def extract_title(markdown):
    print(f"extracting title from {markdown}")
    main_heading = ""
    lines = markdown.split("\n")
    if len(lines) == 0 or markdown.strip() == "":
        raise Exception(f"Error: invalid markdown provided {markdown}")
    for line in lines:
        if line.lstrip().startswith("# "):
            main_heading = line.strip()
            break
    if main_heading.strip() == "":
        raise Exception(f"Error: Main heading not found in {markdown}")
    return main_heading.lstrip("#").strip()
