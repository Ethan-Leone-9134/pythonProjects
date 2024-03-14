def count_comment_and_blank_lines(file_path):
    line_count = 0
    comment_count = 0
    blank_count = 0
    docstring_count = 0
    in_docstring = False

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()

            line_count += 1

            # Check for docstring start
            if (line.startswith("'''") or line.startswith('"""')) and not in_docstring:
                in_docstring = True
                # docstring_count += 1
            # Check for docstring end
            elif (line.endswith("'''") or line.endswith('"""')) and in_docstring:
                in_docstring = False
                docstring_count += 1

            if in_docstring:
                docstring_count += 1

            # Check for comment lines
            if line.startswith('#') and not in_docstring:
                comment_count += 1

            # Check for blank lines
            if not line and not in_docstring:
                blank_count += 1

    return line_count, comment_count, blank_count, docstring_count



# Example usage
input_file = r'C:\Users\zaper\Github\pythonProjects-1\pyGames\bingo4.py'
all_lines, comment_lines, blank_lines, docstring_lines = count_comment_and_blank_lines(input_file)

print("All lines:", all_lines)
print("Comment lines:", comment_lines)
print("Blank lines:", blank_lines)
print("Docstring lines:", docstring_lines)
print("Code Lines:", all_lines - comment_lines - blank_lines - docstring_lines)