# NOTES FOR DEVS


## How to edit this thing

The [README.md](README.md) acts as the "homepage" for all my bashfoo entries. The actual entries are serialzed in [bashfoo.yaml](bashfoo.yaml), and the [Makefile](Makefile) runs the [make_readme.py](make_readme.py) script to build [README.md](README.md).

So to add to this repo:

- Make changes to [bashfoo.yaml](bashfoo.yaml)
  - New entries go at the top of the file (README.md lists them in alphabetical order by their title)
- Run `make`, which will generate a new README.md



