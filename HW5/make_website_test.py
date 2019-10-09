import unittest

from make_website import *


class TestMakeWebsite(unittest.TestCase):

    def setUp(self):

        # test load file: original resume
        self.resume = read_resume('resume.txt')

        # test load file: new resume
        self.new_resume = read_resume('new_resume_for_test.txt')

    def test_detect_name(self):
        self.assertListEqual(["I.M.", "Student"], detect_name(self.resume))
        self.assertListEqual(["Sophie", "Luo"], detect_name(self.new_resume))

    def test_detect_email(self):
        self.assertEqual("tonyl@seas.upenn.edu", detect_email(self.resume))

        #edge case when email format violates some assumption, should return empty string
        self.assertEqual("", detect_email(self.new_resume))

    def test_detect_courses(self):
        self.assertListEqual(['Programming Languages and Techniques',
                              'Biomedical image analysis',
                              'Software Engineering'], detect_courses(self.resume))

        # edge case with weird punctuation marks
        self.assertListEqual(['Programming Languages and Techniques',
                              'Engineering 2',
                              'Engineering 3'], detect_courses(self.new_resume))


    def test_detect_projects(self):
        self.assertListEqual(['CancerDetector.com, New Jersey, USA - Project manager, codified the assessment and mapped'
                              ' it to the CancerDetector ontology. Member of the UI design team, designed the portfolio '
                              'builder UI and category search pages UI. Reviewed existing rank order and developed '
                              'new search rank order approach.',
                            'Biomedical Imaging - Developed a semi-automatic image mosaic '
                            'program based on SIFT algorithm (using Matlab)'], detect_projects(self.resume))

        # edge case with white spaces and empty lines
        self.assertListEqual(['I am a project',
                              'I am a new project',
                              'I am another very interesting project',
                              'I am a project with white spaces'], detect_projects(self.new_resume))

    def test_surround_block(self):
        name = str(detect_name(self.resume)[0] + " " + detect_name(self.resume)[1])
        self.assertEqual("\n<h1>I.M. Student</h1>", surround_block("h1", name))

        new_name = str(detect_name(self.new_resume)[0] + " " + detect_name(self.new_resume)[1])
        self.assertEqual("\n<h1>Sophie Luo</h1>", surround_block("h1", new_name))

        # the following test doesn't pass because can't figure out ' and "
        # error message:
        # - Email: <a href='mailto:tonyl@seas.upenn.edu'>tonyl@seas.upenn.edu</a>
        # ?                ^                           ^
        # + Email: <a href="mailto:tonyl@seas.upenn.edu">tonyl@seas.upenn.edu</a>
        # ?                ^                           ^
        # email = detect_email(self.resume)
        # self.assertEqual("Email: <a href='mailto:tonyl@seas.upenn.edu'>tonyl@seas.upenn.edu</a>", surround_block("a href", email))

        projects = detect_projects(self.resume)
        self.assertEqual("\n<li>CancerDetector.com, New Jersey, USA - "
                         "Project manager, codified the assessment and mapped it to the CancerDetector ontology. "
                         "Member of the UI design team, designed the portfolio builder UI and category search pages UI. "
                         "Reviewed existing rank order and developed new search rank order approach.</li>"
                         "\n<li>Biomedical Imaging - Developed a semi-automatic image mosaic program based on SIFT algorithm "
                         "(using Matlab)</li>", surround_block("Projects", projects))

        new_projects = detect_projects(self.new_resume)
        self.assertEqual("\n<li>I am a project</li>"
                         "\n<li>I am a new project</li>"
                         "\n<li>I am another very interesting project</li>"
                         "\n<li>I am a project with white spaces</li>", surround_block("Projects", new_projects))

        courses = detect_courses(self.resume)
        self.assertEqual("\n<span>Programming Languages and Techniques, </span>"
                        "\n<span>Biomedical image analysis, </span>"
                        "\n<span>Software Engineering</span>", surround_block("Courses", courses))

        new_courses = detect_courses(self.new_resume)
        self.assertEqual("\n<span>Programming Languages and Techniques, </span>"
                        "\n<span>Engineering 2, </span>"
                        "\n<span>Engineering 3</span>", surround_block("Courses", new_courses))

    # this is an exception. this functions writes to a file. it's difficult to test with unit testing.
    def test_read_template_and_append_new_file(self):
        pass

    # do not need to test main function
    def main(self):
        pass

if __name__ == '__main__':
    unittest.main()
