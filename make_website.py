import string

"""homework 5 submissions"""

"""You will submit the following 4 files:
1. make_website.py: the program you wrote
2. make_website_test.py [and other .txt files for testing]: the unit tests you wrote
for all your functions and if you created other .txt files (
e.g. different versions of your resume) to be read by your main program or your unit tests, 
please include those in the .zip file. 
Part of grading your assignment will be to run your unit tests. 
We want to make sure they pass if they reference other .txt files.
3. resume.txt: the text file you created to be read by your program
4. resume.html: the resume file that was generated when you ran your program

Please zip all 4 of these files and name the .zip file using your PennKey. 
For example, Brandon’s submission would be lbrandon.zip. Please, no .rar files!"""


# input test file:
# resumes with some key points but unstructured
# 1. top line contain just the name
# 2. email address in single line
# 3. list of projects listed line by line below a heading called "projects", ends with "--------" (>=10 -)
# 4. list of courses, comma separated with word "Courses" in front of them, might have punctuation marks

# TODO: Step 1: create a sample resume according to the above described format

# TODO: write one function for each piece of info to extract from the text file
# will be graded according to the modularity
# graded: how well you unit test the functions


def read_resume(file):
    """reads the resume file and stores it in the program's memory"""

    f = open(file, "r")

    resume_texts_list = []

    # create a list and store info from the resume in the list
    for line in open(file):
        resume_texts_list.append(line.rstrip())

    # close file
    f.close()

    return resume_texts_list


def detect_name(text):
    """extract the first line of the resume file and set it as name.
    name is a list, with firstname as the first element, and lastname as the last element"""

    # crash: provide a message saying that the first line has to be a name with proper capitalization
    # note that the name on the first line could have leading or trailing whitespace

    # get rid of leading and trailing whitespace in name of the first line
    name = text[0].strip(' ')

    # separate first name, middle names and last name
    name = name.split(' ')

    # raise a RuntimeError if the first character in the either any name is not an uppercase letter
    for i in name:
        if i[0].upper() != i[0]:
            raise RuntimeError("You need to change the first character of all your names into uppercase")

    return name


def detect_email(text):
    """detect the person's email (the line that ends with '@xxx.com' or '@xxx.edu'"""
    # read more instructions when actually writing this part

    # get the line that has the '@' character
    for i in range(0, len(text)):
        line = text[i]
        if '@' in line:
            email = line

    # last four characters in the email are either '.com' or '.edu'
    # first letter in email is a normal lowercase English character
    end_with = email[len(email) - 4: len(email)]
    if (end_with == '.com' or end_with == '.edu') and email[0] in string.ascii_lowercase:

        # check if any character is a number
        is_digit = any(char.isdigit() for char in email)

        #if email address contains a number, set email to an empty string
        if is_digit:
            email = ""
    # if email address does not end with .com or .edu, set email to an empty string
    else:
        email = ""

    return email


def detect_courses(text):
    """extracts courses from the file"""

    # look for the word "Course" and extract that line
    for i in range(0, len(text)):
        if "Courses" in text[i]:
            courses = text[i].split(',')

    for course in courses:
        # remove trailing and heading whitespace
        course = course.strip()

# TODO: remove "all heading expressions before the first actual course"
    courses[0] = courses[0][7: len(courses[0])].strip()
    print(courses)

    return courses


def detect_projects():
    """extracts projects from the file"""
    pass


# programmatically write HTML
# get(extract) info from resume using this file, fill in the empty <body> element
# in resume-template.html, and write the final HTML to a new file resume.html
# Open and read resume-template.html
# o Read every line of HTML
# o Remove the last 2 lines of HTML (you’ll programmatically add these back later)
# o Add all HTML-formatted resume content
# o Add the last 2 lines of HTML back in
# o Write the final HTML to a new file resume.html


def surround_block(tag, text):
    # o This function surrounds the given text with the given HTML tag and returns the string
    # o For example, surround_block(‘h1’, ‘The Beatles’) would return ‘<h1>The Beatles</h1>’

    pass




def main():
    resume_texts_list = read_resume("resume.txt")

    # returns name as a list, with first element being the first name, and last element being the last name
    print('1. student name is', detect_name(resume_texts_list))

    # returns email address
    print('2. student email address is', detect_email(resume_texts_list))

    # returns courses
    print('3. students took', detect_courses(resume_texts_list), 'courses')


if __name__ == "__main__":
    main()
