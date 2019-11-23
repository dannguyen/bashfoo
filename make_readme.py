#!/usr/bin/env python

"""The worst markdown generator ever"""
from pathlib import Path
import yaml

SRC_PATH = Path('.', 'bashfoo.yaml')
DEST_PATH = Path('.', 'README.md')

HEADER = """
# bashfoo.yaml

[https://github.com/dannguyen/bashfoo](https://github.com/dannguyen/bashfoo)

Dan Nguyen's personally curated list of bash/command-line commands and snippets
  that are useful but yet he keeps forgetting

-----

"""


def main():
    mani = yaml.load(SRC_PATH.open(), Loader=yaml.BaseLoader)

    with open(DEST_PATH, 'w') as outs:
        outs.write(HEADER)

        for title, m in mani.items():
            outs.write(f"\n### {title}\n")
            # code
            outs.write(f"""\n```sh\n# Example\n\n{m['code']}```\n""")


            # output
            if m.get('output'):
                outs.write("\nOutput:\n")
                outs.write(f"""\n```\n{m['output']}```\n""")

            if m.get('article'):
                a = m['article']
                outs.write("\n**Reference**: ")
                outs.write(f"[{a['title']}]({a['url']})\n")


if __name__ == '__main__':
    main()
