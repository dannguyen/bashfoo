
# bashfoo.yaml

[https://github.com/dannguyen/bashfoo](https://github.com/dannguyen/bashfoo)

Dan Nguyen's personally curated list of bash/command-line commands and snippets
  that are useful but yet he keeps forgetting


## TOC

- [calculate total kilobytes of hard disk space for files with given extension(s)](#manifest-calculate-total-kilobytes-of-hard-disk-space-for-files-with-given-extension-s-)
- [echo to stderr](#manifest-echo-to-stderr)
- [Filename stem, i.e. without the path or extension](#manifest-filename-stem-i-e-without-the-path-or-extension)
- [`pkill` using a file pattern](#manifest--pkill-using-a-file-pattern)
- [`pgrep` and get all process info](#manifest--pgrep-and-get-all-process-info)
- [`tar` extraction, verbose](#manifest--tar-extraction-verbose)
- [`find` file by name](#manifest--find-file-by-name)
- [`find` directory name recursively](#manifest--find-directory-name-recursively)
- [`find` and execute command on each file](#manifest--find-and-execute-command-on-each-file)

------



<a name="manifest-calculate-total-kilobytes-of-hard-disk-space-for-files-with-given-extension-s-" id="manifest-calculate-total-kilobytes-of-hard-disk-space-for-files-with-given-extension-s-"></a>

### calculate total kilobytes of hard disk space for files with given extension(s)

```sh
# Example

echo $(find . -type f \
        \( -name "*.csv" -o -name '*.xls*' \) \
        -printf "%k+" \
        2>/dev/null; \
        echo 0;) | bc
```

Output:

```
15732
```

**Reference**: [Find the total size of certain files within a directory branch](https://unix.stackexchange.com/questions/41550/find-the-total-size-of-certain-files-within-a-directory-branch/148472)

**Notes**: 



- Requires the use of gnu-find (gfind on my MacOS)
- use `-printf "%s+"` to print size by bytes
- `2>/dev/null` hides error messages


<a name="manifest-echo-to-stderr" id="manifest-echo-to-stderr"></a>

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


<a name="manifest-filename-stem-i-e-without-the-path-or-extension" id="manifest-filename-stem-i-e-without-the-path-or-extension"></a>

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


<a name="manifest--pkill-using-a-file-pattern" id="manifest--pkill-using-a-file-pattern"></a>

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


<a name="manifest--pgrep-and-get-all-process-info" id="manifest--pgrep-and-get-all-process-info"></a>

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


<a name="manifest--tar-extraction-verbose" id="manifest--tar-extraction-verbose"></a>

### `tar` extraction, verbose

```sh
# Example

tar xzfv ARCHIVE.TAR.GZ
```

**Reference**: [The tar command explained](https://www.howtoforge.com/tutorial/linux-tar-command/)


<a name="manifest--find-file-by-name" id="manifest--find-file-by-name"></a>

### `find` file by name

```sh
# Example

find . -name "foo*"
```

**Reference**: [How can I recursively find all files in current and subfolders based on wildcard matching?](https://stackoverflow.com/questions/5905054/how-can-i-recursively-find-all-files-in-current-and-subfolders-based-on-wildcard)


<a name="manifest--find-directory-name-recursively" id="manifest--find-directory-name-recursively"></a>

### `find` directory name recursively

```sh
# Example

find START_DIR -type d -name "PATTERN"
```

**Reference**: [How can I recursively search for directory names with a particular string where the string is only part of the directory name](https://askubuntu.com/questions/153144/how-can-i-recursively-search-for-directory-names-with-a-particular-string-where)


<a name="manifest--find-and-execute-command-on-each-file" id="manifest--find-and-execute-command-on-each-file"></a>

### `find` and execute command on each file

```sh
# Example

find ./PATTERN -exec FOO BAR {} \;

find PlainText/*.md -exec wc -l {} \;
```

**Reference**: [How to run find -exec?](https://unix.stackexchange.com/questions/12902/how-to-run-find-exec)
