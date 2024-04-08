# Continue taking input until "stop" is entered
while True:
    input_fileName = input("Enter the text you want to format (type 'stop' to finish): ")
    if input_fileName.lower() == "stop":
        break
    input_DepartmentName = input("Enter Department name. example: IT (type 'stop' to finish): ")
    if input_DepartmentName.lower() == "stop":
        break
    input_date = input("Enter the date. example 04/24 (type 'stop' to finish): ")
    if input_date.lower() == "stop":
        break

    # Replace spaces with underscores in the input text
    input_text_with_underscore = input_fileName.replace(" ", "_")

    # Text to insert
    text_to_insert1 = input_DepartmentName + "_"
    text_to_insert2 = "_" + input_date
    text_underscore = input_text_with_underscore

    # Insert the text into the input text with formatting
    formatted_text = f"{text_to_insert1}{text_underscore}{text_to_insert2}"

    # Output the formatted text
    print("Formatted text:", formatted_text)
