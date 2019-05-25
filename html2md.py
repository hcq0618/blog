#!/usr/bin/python
# -*- coding: utf-8 -*-
import io
import os
import sys

import html2text
from bs4 import BeautifulSoup

# import urllib

reload(sys)
sys.setdefaultencoding('utf8')


def convert_keyword(key_word):
    return key_word.replace('RN', 'ReactNative')


def convert(file_path, _for_hexo):
    with io.open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    html_output = ""
    for line in lines:
        html_output += line
    # convert local image path
    soup = BeautifulSoup(html_output, 'html.parser', from_encoding='utf-8')
    imgs = soup.find_all({'img'})
    for img in imgs:
        src = img.get('src')
        if not (src.startswith('http://') or src.startswith('https://')):
            html_output = html_output.replace(src, src[src.rindex(os.sep) + 1:])
    # print(html_output)

    h = html2text.HTML2Text()
    md_output = h.handle(html_output)
    # print(md_output)

    # special handling for jianshu.com
    md_output = md_output.replace("![](http://upload-\n", "![](http://upload-").replace('/auto-\norient/',
                                                                                        '/auto-orient/')
    prefix = ''
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    file_dir = os.path.dirname(file_path)

    if _for_hexo:
        title = file_name
        title = convert_keyword(title)

        # get thumbnail from content
        thumbnail = ''
        # soup = BeautifulSoup(html_output, 'html.parser', from_encoding='utf-8')
        # if soup.find('img'):
        #     thumbnail = urllib.unquote(str(soup.img['src']))

        # get categories from parent dir name
        categories_last_split = file_path.rindex(os.sep)
        categories_pre_split = len(
            os.path.dirname(os.path.dirname(file_path))) + 1
        categories = file_path[categories_pre_split:categories_last_split]
        categories = convert_keyword(categories)

        # get tags from categories and title
        tags = categories
        tag_from_tile = None
        if '[' in title and ']' in title:
            tag_from_tile = title[title.index('[') + 1:title.index(']')]
            tag_from_tile = convert_keyword(tag_from_tile)
        if tag_from_tile is not None and not (tag_from_tile == categories):
            tags += ',' + tag_from_tile
        tags = convert_keyword(tags)

        # print(title)
        # print(thumbnail)
        # print(categories)
        # print(tags)

        # remove prefix before '-' in title
        if "-" in title:
            title = title.replace(title[0:title.index("-") + 1], "")

        # create prefix for hexo
        prefix = '---\ntitle: %s\nthumbnail: %s\ncategories: %s\ntags: [%s]\n---\n' % (
            title, thumbnail, categories, tags)

        # if first line is h1 then remove it
        first_line = md_output[0:md_output.index('\n') + 1]
        if first_line.startswith("# "):
            md_output = md_output.replace(first_line, "")

    # remove prefix before '-' in file name
    if "-" in file_name:
        title_prefix = file_name[0:file_name.index("-") + 1]
        if '[' in title_prefix and ']' in title_prefix:
            file_name = file_name.replace(title_prefix, "")

    # need to url encode file name
    with io.open(file_dir + os.sep + file_name + ".md", 'w', encoding='utf-8') as f:
        f.write(prefix + md_output)


def convert_all_files(root_dir, _for_hexo):
    _files = []
    _list = os.listdir(root_dir)
    for i in range(0, len(_list)):
        path = os.path.join(root_dir, _list[i])
        if os.path.isdir(path):
            _files.extend(convert_all_files(path, _for_hexo))
        if os.path.isfile(path) and os.path.splitext(path)[1] == '.html':
            print(path)
            convert(path, _for_hexo)
            _files.append(path)
    return _files


# for_hexo = len(sys.argv) > 2 and sys.argv[2] == '-hexo'
convert_all_files(sys.argv[1], True)
