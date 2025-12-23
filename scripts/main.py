#!/usr/bin/env python3

import argparse
import sys
from readme import Readme
from tags import Tags

argparse = argparse.ArgumentParser(
    prog="build", description="Build Scripts for Cookbook"
)

argparse.add_argument(
    "--generate_readme", action="store_true", help="Generates the top level README.md"
)

if __name__ == "__main__":
    args, others = argparse.parse_known_args(sys.argv)

    tags = Tags("./src")
    tags.create_tag_pages("./tags")

    if args.generate_readme:
        readme = Readme("./templates/README.template.md", "./src", "./tags")
        readme.generate("README.md")
