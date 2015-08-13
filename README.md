Blogdown
========

A simple markdown add-on and parser for writing blog posts.

Format
------

A blog post looks like this:

    title: A title goes here!
    author: John Doe
    tags: you, can put, tags, here
    status: draft

    This is where you say something insightful. Many blog posts
    are just [links][1] to something else!

    [1]: http://example.com

A blog post can have multiple markers at the top to specify metadata about the
post. The supported markers are:

**Required**

These markers are required for every post. They are manually created by the
user.

- title: A title for the post (may contain special characters)
- status: draft, or publish depending on the status of the post.

**Optional/Automatic**

These markers are either optional or usually generated by a tool. They are not
required, but aim to provide more useful information about a given post.

- published: The time/date that the post was published.
- author: The name of the author.
- tags: A collection of tags describing the post.
- updated: The last time/date that the post was edited.
- summary: A brief summary (the tl;dr).
- template: The name of a specific template to use for this post (if not
  default).
- slug: The url slug for this post. Usually generated from the title, but it
  can be specified on it's own as well.

API
---

Once you have a blogdown formatted post, parsing it is really simple.

`python

from blogdown import Blogdown, parse

text = get_text()
post = parse(text) 

print post.title
>>> 'Here's your title'
`









