#!/usr/bin/env python

"""The worst markdown generator ever"""
from pathlib import Path
import re
import yaml

SRC_PATH = Path(".", "bashfoo.yaml")
DEST_PATH = Path(".", "README.md")

HEADER = """
# bashfoo.yaml

[https://github.com/dannguyen/bashfoo](https://github.com/dannguyen/bashfoo)

Dan Nguyen's personally curated list of bash/command-line commands and snippets
  that are useful but yet he keeps forgetting

"""


def anchorify(txt):
    return f"manifest-{slugify(txt)}"


def slugify(txt):
    return re.sub(r"\W+", "-", txt.strip()).lower()


def make_toc(manifest):
    toc = "\n## TOC\n\n"
    for title, m in manifest.items():
        toc += f"- [{title}](#{anchorify(title)})\n"
    toc += "\n\n\n"
    return toc


def make_body(manifest):
    body = "\n"
    for title, m in manifest.items():
        # anchor
        body += "\n\n-------------------------------\n"
        body += f"""<a name="{anchorify(title)}" id="{anchorify(title)}"></a>\n"""

        # title
        body += f"\n### {title}\n"
        # code
        body += f"""\n```sh\n# Example\n{m['code']}```\n"""

        # output
        if m.get("output"):
            body += "\nOutput:\n"
            body += f"""\n```\n{m['output']}```\n"""

        if m.get("article"):
            a = m["article"]
            body += "\n**Reference**: "
            body += f"[{a['title']}]({a['url']})\n"

        if m.get("notes"):
            n = m["notes"]
            body += "\n**Notes**: \n\n"
            body += f"\n{m['notes']}"
    return body


def main():
    def _load_manifest():
        mani = yaml.load(SRC_PATH.open(), Loader=yaml.BaseLoader)
        mani = {
            k: vals for k, vals in sorted(mani.items(), key=lambda x: slugify(x[0]))
        }
        return mani

    manifest = _load_manifest()
    with open(DEST_PATH, "w") as outs:
        outs.write(HEADER)
        outs.write(make_toc(manifest))
        outs.write(make_body(manifest))


if __name__ == "__main__":
    main()
