![The opened hive with no mark anywhere: grass and clover near, comb filling the middle with workers crossing in ordinary traffic and one longer abdomen moving slowly near the centre with attendants turning toward her, hedge shade and a second hive closed and quiet far off, with no text and no letters](intro-banner.png)

# crypto-hash

Title block: the name above is set in Bilbo in dusk mauve on pale lamplight, ruled beneath in silver like a field guide plate, with a small marking pen drawn once at the left of the first heading only and nowhere repeated as decoration.

![A queen marking pen with a soft sponge tip and a plunger cap resting beside a single hive frame at a slight angle, one dusk mauve marking dot dried on the sponge, and the name hand lettered below](logo.png)

![An observation hive open in a garden apiary: frames leaning in a crate and a veil on a peg at the left, exposed comb in the middle, one bee with a dusk mauve dot in her court at the right, the marking pen cap off on the hive stand, a hive tool beside it and a smoker cold at the far edge, the repo name painted small on the stand](banner.png)

![The apiary in three bands: hedge and a closed hive still in the far band, workers crossing the comb in the middle band while the marked queen walks to the centre and pauses and the nearest workers turn to face her, a returning forager walking a small figure of eight on the comb, and one worker crossing the lower edge in the near band](scene.svg)

![Major separator](sep-heavy.svg)


## Crypto Hash

> Inspection note, opened in late morning: a digest, like a marking dot, is a small fixed sign by which a much larger thing can be known again later.

![Minor separator](sep-light.svg)

### Project Description

Crypto Hash prints the hex digest of a text string or of a file's
contents, using Python's standard library `hashlib`. It has no
third-party dependencies and no subcommands; there is no verify mode,
so checking a file means hashing it and comparing the printed digest
yourself.

> Inspection note, entered before the frames are lifted: give either the text option or the file option, never both together, since the parser refuses the pair.

![Minor separator](sep-light.svg)

### Usage Examples

```
# SHA-256 of a string (sha256 is the default algorithm)
python3 main.py --text "Hello World"

# MD5 of a file's contents
python3 main.py --file file.txt --algorithm md5

# Quiet mode prints only the digest line
python3 main.py --text "Hello World" --quiet
```

Give either `--text` or `--file`, not both. The SHAKE algorithms are
not offered: their digests need a length argument, which this tool does
not take.

> Inspection note, closing the record: the licence line below stands exactly as the README prints it.

![Minor separator](sep-light.svg)

### License

Crypto Hash is licensed under the GNU General Public License v3.0. See LICENSE.

![Major separator](sep-heavy.svg)

## Facts from the code, stated in the prose

Facts from the code, stated in the prose. This record names: hashlib, utf-8, 4096 bytes, sha256, SHAKE, Hashed text, Hashed file, exit 1, -t, -f, -a, -q, GNU General Public License v3.0. The file is read in blocks of 4096 bytes. The quiet option silences logging for the whole process, error lines included, leaving the exit code as the only sign of a failed run. Logging is switched on at import time for any process that imports the file.
