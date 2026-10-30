![Banner](banner.png)

## Crypto Hash

### Project Description

Crypto Hash prints the hex digest of a text string or of a file's
contents, using Python's standard library `hashlib`. It has no
third-party dependencies and no subcommands; there is no verify mode,
so checking a file means hashing it and comparing the printed digest
yourself.

### Usage Examples

```
# SHA-256 of a string (sha256 is the default algorithm)
python main.py --text "Hello World"

# MD5 of a file's contents
python main.py --file file.txt --algorithm md5

# Quiet mode prints only the digest line
python main.py --text "Hello World" --quiet
```

Give either `--text` or `--file`, not both. The SHAKE algorithms are
not offered: their digests need a length argument, which this tool does
not take.

### License

Crypto Hash is licensed under the GNU General Public License v3.0. It is owned and maintained by CY83R-3X71NC710N.
