from app.models import Demo

from .is_similar_strings import is_similar_strings
from .remove_html import remove_html


def dissect_description(description: str):
    """
    Dissects description string into demos and additional information.

    Parameters
    ----------
    description: str
        The description to dissect.

    Returns
    -------
    demos: list
        The list of Demo objects.
    additional_information: str
        The additional information.
    """
    description = description.strip()
    has_html = "<" in description
    demo_indices = []
    demo_names = []
    additional_info = ''
    if has_html:
        idx_demo_start, idx_demo_end = 0, 0
        for i, char in enumerate(description):
            if not idx_demo_start:
                if char == ">":
                    next_five_characters = description[i + 1: i + 6]
                    is_demo_start = True
                    if next_five_characters in "Additional Information:":
                        break
                    for c5 in next_five_characters:
                        if c5 in {"<", ">", "/"}:
                            is_demo_start = False
                            break
                    if is_demo_start:
                        for c5 in next_five_characters:
                            if c5.isdigit() or c5.isupper():
                                idx_demo_start = i + 1
            elif not idx_demo_end:
                if char == "<":
                    prev_five_characters = description[i - 6: i - 1]
                    is_demo_end = True
                    for c5 in prev_five_characters:
                        if c5 in {"<", ">", "/"}:
                            is_demo_end = False
                    if is_demo_end:
                        idx_demo_end = i
            else:
                demo_indices.append((idx_demo_start, idx_demo_end))
                idx_demo_start, idx_demo_end = 0, 0
        for indices in demo_indices:
            demo_names.append(description[indices[0]: indices[1]])
            idx_additional_info_start = demo_indices[len(demo_indices) - 1][1]
            idx_additional_info_end = len(description) - 1
            additional_info = description[
                              idx_additional_info_start:idx_additional_info_end
                              ]
            additional_info = remove_html(additional_info)
            additional_info = additional_info.strip()
            info_start = additional_info.find("ation") + 5
            if additional_info.find("ation:") != -1:
                info_start += 1
            additional_info = additional_info[info_start:]
            if len(additional_info) < 5 or "&nbsp;" == additional_info.strip():
                additional_info = ''
    else:
        description_lines = description.splitlines()
        has_demos = False
        for i, line in enumerate(description_lines):
            if i > 0:
                line_is_addtional_info = is_similar_strings(
                    line, "Additional Information:"
                )
                if len(line) > 5 and not line_is_addtional_info:
                    has_demos = True
                elif line_is_addtional_info:
                    break
        description_lines = description_lines[1:]
        idx_additional_info_title = 0
        idx_description_line = 0
        # Scanning for 'Additional Information'
        while idx_description_line < len(description_lines):
            line = description_lines[idx_description_line]
            if len(line) <= 5:
                description_lines.pop(idx_description_line)
                idx_description_line = 0
                continue
            elif is_similar_strings(
                    line[: len("Additional Informaiton:")],
                    "Additional Information:",
                    threshold=0.6,
            ):
                idx_additional_info_title = idx_description_line
                additional_info = description_lines[idx_additional_info_title]
                if (
                        len(additional_info[0])
                        > len("Additional Information:") + 5
                ):
                    # Case 1: Additional information content is on the same
                    # line as "Additional Information" Title
                    idx_additional_info_title_end = (
                            additional_info.find(":")
                            + 1
                    )
                    if not idx_additional_info_title_end:
                        idx_additional_info_title_end = (
                                additional_info[18:].find("on") + 2
                        )
                    additional_info = additional_info[
                                      idx_additional_info_title_end:
                                      ]
                    break
                elif idx_description_line < len(description_lines) - 1:
                    # Case 2: Additional information content in the lines
                    # following "Additional Information:" Title
                    idx_additional_info = idx_description_line + 1
                    additional_info_first_line = description_lines[
                        idx_additional_info
                    ]
                    while is_similar_strings(
                        additional_info_first_line,
                        "Additional Information:",
                        threshold=0.6,
                    ):
                        # This while loops runs forever. How to resolve?
                        if len(description_lines) - 1 > idx_additional_info:
                            idx_additional_info += 1
                            additional_info_first_line = description_lines[
                                idx_additional_info
                            ]
                        else:
                            additional_info = ''
                    if idx_additional_info == len(description_lines) - 1:
                        additional_info = additional_info_first_line
                    else:
                        additional_info_list = description_lines[
                                               idx_additional_info:
                                               ]
                        additional_info = ""
                        for idx, additional_info_line in enumerate(
                                additional_info_list
                        ):
                            additional_info_line = (additional_info_line
                                                    .strip(". "))
                            if not idx:
                                additional_info += additional_info_line
                            else:
                                additional_info += f". {additional_info_line}"
                    break
                elif additional_info.find("formation") != -1:
                    # Case 3: Additional Information is empty
                    additional_info = ''
                    break
            idx_description_line += 1
        if has_demos:
            if idx_additional_info_title == 0:
                demo_names = description_lines
            else:
                demo_names = description_lines[:idx_additional_info_title]

    i = 0
    while i < len(demo_names):
        demo_names[i] = demo_names[i].strip()
        demo_name = demo_names[i]
        if len(demo_name) <= 5:
            demo_names.pop(i)
            i = 0
        elif (
                is_similar_strings(demo_name, "Additional Information")
                or is_similar_strings(demo_name, "DEMONSTRATIONS:")
        ):
            demo_names.pop(i)
            i = 0
        elif "&" in demo_name:
            idx_extra_ampersand = demo_name.index("&")
            demo_names[i] = demo_name[:idx_extra_ampersand]
            i = 0
        else:
            i += 1
    if additional_info != '':
        additional_info = additional_info.replace("&nbsp;", "")
        additional_info.strip(". ")
        if additional_info[-1] not in {".", "\""}:
            additional_info += "."
        while additional_info[0] == " ":
            additional_info = additional_info[1:]
    demos = []
    for name in demo_names:
        demos.append(Demo(name=name))
    return demos, additional_info
