.DEFAULT_GOAL := readme




readme: README.md

README.md: bashfoo.yaml make_readme.py
	./make_readme.py
