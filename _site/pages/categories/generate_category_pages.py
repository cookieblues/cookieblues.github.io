import os
import re

categories = set()

# Go through all posts.
for post_name in os.listdir('pages/_posts'):
    with open(os.path.join('pages/_posts', post_name), 'r') as post:
        post_content = post.read()
    # Find their category and add to set.
    post_category = re.search(r'category: (.*)', post_content)
    if post_category:
        categories.add(post_category[1])

# Category page template.
category_template = """---
title: {0}
layout: category
category: {0}
permalink: /{1}
---
"""

# Create category page for each unique category.
for category in categories:
    category_url = category.lower().replace(' ', '_')
    with open(f'pages/categories/{category_url}.md', 'w') as category_page:
        category_page.write(category_template.format(category, category_url))
