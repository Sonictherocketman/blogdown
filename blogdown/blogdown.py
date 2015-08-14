""" A markdown parser for blog posts.

Blogdown is a subset of Markdown that has metadata fields
at the top.

author: Brian Schrader
since: 2015-08-12
"""


from markdown import markdown


metadata = ['template','title', 'author', 'status', 'tags',
        'slug', 'published', 'updated', 'summary']


class Blogdown(object):

    def __repr__(self):
        if getattr(self, 'title' , True):
            self.title = '[no title]'
        return '<Blogdown: {}>'.format(self.title)

    def __init__(self, **entries):
        self.content = ''
        for item in metadata:
            self.__dict__[item] = ''
        self.__dict__.update(entries)


def parse(text):
    """ Parses the given raw text and returns a blogdown
    object containing the associated metadata and markdown
    content.
    """
    data, lines = {}, []
    for line in text.splitlines():
        haystack = line.strip().split(':')
        try:
            marker, val = haystack[0], ':'.join(haystack[1:])
        except ValueError as e:
            marker, val = None, None

        if marker in metadata:
            data[marker] = val.strip()
        else:
            lines.append(line)

    data['markdown'] = '\n'.join(lines).rstrip()
    data['content'] = markdown(data['markdown'])
    return Blogdown(**data)
