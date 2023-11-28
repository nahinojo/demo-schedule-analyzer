def dissect_description(description: str):
    description = description.strip()
    index_additional_info = description.find("Additional Information")
    demos = description[:index_additional_info]
    additional_info = description[index_additional_info+1:]
    print(demos)
    print(additional_info)
    return
