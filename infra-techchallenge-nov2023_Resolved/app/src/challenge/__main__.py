#!/usr/bin/env python
""" A simple web app based on bottle.py """
import argparse
import json
import os
import re
import sys
import urllib.request

import markdown
import redis
from bottle import abort, route, run, template

SAFE_NAME = re.compile(r'^\w{1,253}$')
DB = dict()
template_dir = "/app/challenge/templates"


@route('/')
def v_index():
    """ view for the main index """
    return template(f'{template_dir}/index.html.tmpl',
                    {"when": "November 2023"}) # Bug Fix 4 - Typo in the name


@route('/puppy/<puppyid>')
def json_puppy(puppyid):
    """ return the url of the given puppy """
    if 'init' not in DB:
        DB['init'] = True
        DB['redis'] = redis.StrictRedis(host='redis', port=6379, db=0)
        populate_puppies()

    if not safe_name(puppyid):
        abort(401, "Access to invalid puppy denied")

    puppyurl=dbget(puppyid)
    if puppyurl is None:
        abort(404, "No such key")

    return dict(url=puppyurl)


@route('/content/<name>')
def render_markdown(name):
    """
    renders the named markdown file (from the /content directory) and
    returns the content as html
    """
    if not safe_name(name):
        abort(401, "Access to invalid name denied")

    source_file_path = "/articles/{}.md".format(name)
    if not os.path.exists(source_file_path):
        abort(404, "File not found")

    with open(source_file_path, 'r') as src:
        return markdown.markdown(src.read())


def safe_name(name):
    """
    return true if the given name is a valid markdown file basename
    """
    return bool(SAFE_NAME.match(name))


def dbget(key):
    """
    quick and dirty redis get
    """
    return json.loads(DB['redis'].get(key))


def dbset(key, value):
    """
    quick and dirty redis set
    """
    return DB['redis'].set(key, json.dumps(value))


def get_json_doc(url):
    """ helper method for getting a json document from the internet """
    response = urllib.request.urlopen(url)
    return json.loads(response.read())


def populate_puppies():
    """
    fills the database with puppy pictures
    """
    # load a list of puppy pictures from giphy. then put the pictures in the
    # database at numeric indexes
    # via https://github.com/jdorfman/awesome-json-datasets
    api_key="g06bJcarFyayGqz7PLksnLdQpuxBw9md"
    puppy_url="https://api.giphy.com/v1/gifs/search?q=puppies&rating=g&api_key=" + api_key
    puppies = get_json_doc(puppy_url)
    for idx, entry in enumerate(puppies['data']):
        url = entry['images']['fixed_height']['url']
        dbset(idx, url)
        print("populating puppy {} = {}".format(idx, url))


def main():
    """
    direct program entry point
    return an exit status integer suitable for use with sys.exit
    """
    argp = argparse.ArgumentParser(
        description="demo web app which uses bottle.py",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    argp.add_argument('-p', '--port', type=int, default=80, help=(
        "server port to listen on"))
    argp.add_argument('-d', '--debug', action="store_true", help=(
        "enable debugging output"))
    args = argp.parse_args()

    # do things
    run(host="0.0.0.0", port=args.port, debug=args.debug)

    return 0


if __name__ == '__main__':
    try:
        RESULT = main()
    except KeyboardInterrupt:
        sys.stderr.write("\n")
        RESULT = 1
    sys.exit(RESULT)
