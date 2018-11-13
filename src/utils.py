""" Flask app index """

import os
from collections import OrderedDict

import oyaml as yaml
from markdown import markdown

PATH_CONTENT = "src/content/"


def get_skills():
    """ Get skills as ordered dict """
    with open(PATH_CONTENT + "skills.yaml") as file:
        return yaml.load(file)


def get_tools():
    """ Get tools as ordered dict """

    with open(PATH_CONTENT + "tools.yaml") as file:
        return yaml.load(file)


def get_portfolio():
    """ Return list of portfolio items with info as dict"""

    out = OrderedDict()

    for filename in os.listdir(PATH_CONTENT + "portfolio"):
        num, name = filename.split("-")

        # Strip extensions
        name = name.split(".")[0]

        with open('{}portfolio/{}-{}.yaml'.format(PATH_CONTENT, num, name)) as file:
            out[name] = yaml.load(file)

            # Transform some blocks from markdown to html
        for x in ["brief", "results"]:
            out[name][x] = markdown(out[name][x])

    return out
