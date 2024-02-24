# script created by LLM using symbolic composition rules to generate compatible data
import random
import csv

# List of keywords in the C language
keywords = ['auto', 'double', 'int', 'struct', 'break', 'else', 'long', 'switch', 'case', 'enum', 'register', 'typedef',
            'char', 'extern', 'return', 'union', 'const', 'float', 'short', 'unsigned', 'continue', 'for', 'signed',
            'void', 'default', 'goto', 'sizeof', 'volatile', 'do', 'if', 'static', 'while']

# List of data types for variables
data_types = ['char', 'int', 'float', 'double', 'void']

# List of labels for comments
comment_labels = ['Useful', 'Not Useful']

# Function to generate a random valid identifier
def generate_identifier():
    first_char = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_')
    rest_chars = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_', k=random.randint(0, 10)))
    return first_char + rest_chars

# Function to generate a random valid line of code
def generate_line_of_code():
    keyword_or_data_type = random.choice(keywords + data_types)
    identifier = generate_identifier()
    value = random.choice(['', f' = {random.randint(0, 100)}'])
    return f'{keyword_or_data_type} {identifier}{value};'

# Function to generate a random comment
def generate_comment():
    level_of_detail = random.choice(['', ' // ' + ' '.join(generate_identifier() for _ in range(random.randint(1, 5)))])
    return random.choice(['', '/* ' + generate_identifier() + ' */']) + level_of_detail

# Function to generate a useful comment for a given line of code
def generate_useful_comment(line_of_code):
    purpose_keywords = ['Declaration', 'Initialization', 'Calculation', 'Function', 'Definition', 'Usage', 'Explanation']
    variable_keywords = ['Variable', 'Value', 'Data', 'Result', 'Parameter']

    purpose = random.choice(purpose_keywords)
    variable = random.choice(variable_keywords)

    return f'// {purpose} of {variable} in the line of code:\n// {line_of_code}'

# Function to generate a random label for a comment
def generate_comment_label():
    return random.choice(comment_labels)

# Generate 5000 lines of code, comments, and labels
data = []
for _ in range(5000):
    line_of_code = generate_line_of_code()
    comment = generate_comment()
    label = generate_comment_label()

    # Ensure the comment is useful if labeled as Useful
    if label == 'Useful':
        comment = generate_useful_comment(line_of_code)

    data.append((line_of_code, comment, label))

# Function to write data to a CSV file
def write_to_csv(file_path, data):
    with open(file_path, mode='w', newline='') as csv_file:
        fieldnames = ['Line of Code', 'Comment', 'Class']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow({'Line of Code': row[0], 'Comment': row[1], 'Class': row[2]})

# Specify the file path
csv_file_path = 'test.csv'

# Write data to the CSV file
write_to_csv(csv_file_path, data)

print(f'Data has been generated and saved to {csv_file_path}')
