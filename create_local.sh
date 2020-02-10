#!/bin/bash

rm -rf _site/
python pages/categories/generate_category_pages.py
jekyll serve