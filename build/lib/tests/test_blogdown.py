

import unittest, sys

sys.path.insert(0, '../')
from blogdown import Blogdown, parse


class BlogdownTest(unittest.TestCase):

    def test_init(self):
        author = 'Someone'
        title = 'Something'

        b = Blogdown(title=title, author=author)

        self.assertEqual(title, b.title)
        self.assertEqual(author, b.author)
        self.assertEqual('', b.content)

    def test_parse(self):
        title = 'Cheese shoppe'
        author = 'King Arthur'
        content = 'this is teh content.\n and so is this.'
        text = """title: {}\nauthor: {}\n{}""".format(title, author, content)
        b = parse(text)
        self.assertEqual(title, b.title)
        self.assertEqual(author, b.author)
        self.assertEqual(content, b.content)

    def test_complex_parse(self):
        title = 'Cheese shoppe'
        author = 'King Arthur'
        content = """
        This is some cool: colon seperated: content.
        and even a...
        fake-tag: with a value
        <heres>even</some>fake html
        this is teh content.\n and so is this.
        """
        text = """
        title: {}
        author: {}

        {}""".format(title, author, content)
        b = parse(text)
        self.assertEqual(title, b.title)
        self.assertEqual(author, b.author)
        self.assertEqual(content.strip(), b.content)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BlogdownTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
