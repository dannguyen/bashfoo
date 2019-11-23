
# bashfoo.yaml

[https://github.com/dannguyen/bashfoo](https://github.com/dannguyen/bashfoo)

Dan Nguyen's personally curated list of bash/command-line commands and snippets
  that are useful but yet he keeps forgetting

-----


### echo to stderr

```sh
# Example

>&2 echo "hello error"
```

Output:

```
hello error
```

**Reference**: [echo that outputs to stderr](https://stackoverflow.com/questions/2990414/echo-that-outputs-to-stderr)

### Filename stem, i.e. without the path or extension

```sh
# Example

fullname=/tmp/hello/world.txt
newname="a_whole_new_$(basename ${fullname%.*})"
echo $newname
```

Output:

```
a_whole_new_world
```

**Reference**: [Extract filename and extension in Bash](https://stackoverflow.com/questions/965053/extract-filename-and-extension-in-bash)

### `pkill` using a file pattern

```sh
# Example

pkill -fil ipython
```

Output:

```
kill -15 90396
kill -15 90523
```

**Reference**: [How to kill all processes with a given partial name?](https://stackoverflow.com/questions/8987037/how-to-kill-all-processes-with-a-given-partial-name)

### `pgrep` and get all process info

```sh
# Example

# MacOS
pgrep -fil 'rails'

# Linux
pgrep -af 'rails'
```

Output:

```

47502 rails master RBENV_VERSION=2.5.1 TERMINAL_FONT=Monaco
47517 rails worker[0] RBENV_VERSION=2.5.1 TERMINAL_FONT=Monaco
```

**Reference**: [How to get pgrep to display full process info](https://serverfault.com/questions/77162/how-to-get-pgrep-to-display-full-process-info)

### `tar` extraction, verbose

```sh
# Example

tar xzfv ARCHIVE.TAR.GZ
```

**Reference**: [The tar command explained](https://www.howtoforge.com/tutorial/linux-tar-command/)

### `find` file by name

```sh
# Example

find . -name "foo*"
```

**Reference**: [How can I recursively find all files in current and subfolders based on wildcard matching?](https://stackoverflow.com/questions/5905054/how-can-i-recursively-find-all-files-in-current-and-subfolders-based-on-wildcard)

### `find` directory name recursively

```sh
# Example

find START_DIR -type d -name "PATTERN"
```

**Reference**: [How can I recursively search for directory names with a particular string where the string is only part of the directory name](https://askubuntu.com/questions/153144/how-can-i-recursively-search-for-directory-names-with-a-particular-string-where)

### `find` and execute command on each file

```sh
# Example

find ./PATTERN -exec FOO BAR {} \;

find PlainText/*.md -exec wc -l {} \;
```

**Reference**: [How to run find -exec?](https://unix.stackexchange.com/questions/12902/how-to-run-find-exec)
