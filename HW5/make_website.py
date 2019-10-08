import string

'''
Name: Xiexiao Luo
PennID: 70364612
'''


def read_resume(file1):
    """reads the resume file and stores it in the program's memory"""

    f = open(file1, "r")

    resume_texts_list = []

    # create a list and store info from the resume in the list
    for line in open(file1):
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

    # remove the word "Courses"
    courses[0] = courses[0][7: len(courses[0])].strip()

    # remove expressions that are not words/letters in the first element of the list courses
    for j in range(0, len(courses[0])):
        courses[0] = courses[0][1:]
        if courses[0][j] in string.ascii_lowercase or courses[0][j] in string.ascii_uppercase:
            break

    # remove heading and trailing whitespace
    for k in range(0, len(courses)):
        courses[k] = courses[k].strip()

    return courses


def detect_projects(text):
    """extracts projects from the file"""

    projects = []

    # look for the word "Projects" and extract that line
    for i in range(0, len(text)):
        if "Projects" in text[i]:

            # appends every line after the line with the word "Projects" to the projects list
            for j in range(i, len(text)-1):
                projects.append(text[j+1])

                # if there's a blank line, pop that line from the list
                if text[j] == "":
                    projects.pop(j-i-1)

                # checks if the first 10 characters in the line (string) are 10 minus signs
                # if reached the divider line, first pop the last element (the dividers already being added in),
                # then break the loop
                if text[j+1][0:10] == "----------":
                    projects.pop()
                    break

    # removes heading and trailing whitespace
    for i in range(0, len(projects)):
        projects[i] = projects[i].strip()

    return projects


def read_template_and_append_new_file(file1, file2):

    """This function writes html to the output file"""

    f = open(file1, "r+")
    fout = open(file2, 'w')

    # returns a string resume_html_template
    resume_html_template = f.readlines()

    # remove the last two lines of HTML
    resume_html_template.pop()
    resume_html_template.pop()

    # add all HTML-formatted resume content

    # add wrapper to HTML
    resume_html_template.append("<div id='page-wrap'>")

    # add name to HTML
    name_list = detect_name(resume_texts_list)
    name = str(name_list[0] + " " + name_list[1])
    resume_html_template.append("<div>")
    resume_html_template.append(surround_block('h1', name))

    # add email to HTML
    resume_html_template.append("\n<p>")
    email = detect_email(resume_texts_list)
    resume_html_template.append(surround_block('a href', email))
    resume_html_template.append("</p>")
    resume_html_template.append("</div>")

    # add projects to HTML
    resume_html_template.append("\n<div>\n<h2>Projects</h2>\n<ul>")
    projects = detect_projects(resume_texts_list)
    resume_html_template.append(surround_block('Projects', projects))
    resume_html_template.append("\n</ul>\n</div>")

    # add courses to HTML
    resume_html_template.append("\n<div>\n<h3>Courses</h3>")
    courses = detect_courses(resume_texts_list)
    resume_html_template.append(surround_block('Courses', courses))
    resume_html_template.append("\n</div>")

    # add closing tag of div
    resume_html_template.append("\n</div>")

    # add the last two lines back in
    resume_html_template.append("\n</body>")
    resume_html_template.append("\n</html>")

    # covert list to string
    resume_html_template = "".join(resume_html_template)

    # write the final html toa new file resume.html
    fout.writelines(resume_html_template)

    # close files
    f.close()
    fout.close()

    return resume_html_template


def surround_block(tag, text):
    """This function surrounds the given text with the given HTML tag and returns the string"""

    html_line = ""

    # contructs html lines with tag and text
    # case 1: writes header
    if tag == 'h1':
        html_line = '\n<' + tag + '>' + text + '</' + tag + '>'

    # case 2: writes email
    elif tag == 'a href':
        html_line = 'Email: ' + '<' + tag + '="mailto:' + text + '">' + text + '</a>'

    # case 3: writes project
    elif tag == 'Projects':
        html_line = ""

        # add each project to the end of the string
        for project in text:
            html_line = html_line + '\n<li>' + project + '</li>'

    # case 4: writes courses
    elif tag == 'Courses':
        html_line = ""

        # add each course to the end of the string
        for i in range(0, len(text)-1):
            html_line = html_line + '\n<span>' + text[i] + ', </span>'

        # last course shouldn't have comma
        html_line = html_line + '\n<span>' + text[len(text)-1] + '</span>'

    return html_line


def main():

    global resume_texts_list
    global resume_html_template

    resume_texts_list = read_resume("resume.txt")

    # returns name as a list, with first element being the first name, and last element being the last name
    print('1. student name is', detect_name(resume_texts_list))

    # returns email address
    print('2. student email address is', detect_email(resume_texts_list))

    # returns courses
    print('3. students took', detect_courses(resume_texts_list), 'courses')

    # returns projects
    print('4. student did', detect_projects(resume_texts_list), 'projects')

    # read resume html templates
    print('5. the provided resume template is', read_template_and_append_new_file('resume_template.html', "resume.html"))


if __name__ == "__main__":
    main()
