# musicxml2chordpro
Extract chord charts from MusicXML files


## Usage

### Basic Usage
```bash
python3 xml2pro.py Song.xml > Song.pro
```

### Output Individual Notes (Instrumental Music)
For pure instrumental music without lyrics or chords, use the `--notes` flag to output individual notes in ChordPro format:
```bash
python3 xml2pro.py --notes MozartSonata.xml > MozartSonata.pro
```

Notes are output in lowercase (e.g., `[c#]`, `[d]`, `[a]`) and respects accidentals.


## What Gets Converted

The tool outputs different content depending on what's in the MusicXML file:

| File Type | Default Output | With --notes |
|-----------|----------------|--------------|
| Song with lyrics + chords | Full lead sheet | Full lead sheet |
| Bass/Chord chart (no lyrics) | Chords only | Chords only |
| Pure instrumental (no lyrics, no chords) | Title & key only | Individual notes |

### Examples

**Song with lyrics and chords:**
```
{title:My Song}
{key:C Amin}

My [C]love song [G]with chords [F]and lyrics...
```

**Chord chart:**
```
{title:Bass Line}
{key:D Bmin}

[Am][E][Am][D][A][D][E][D][A][D]
[Am][E][A][D][A][D][Em][D]
```

**Instrumental with notes (using --notes flag):**
```
{title:Piano Sonata}
{key:A Fmin}

[c#][c#][e][a][a][c#][e][a][a][a][a][d][c#][b][c#]
[d][e][a][c#][d][e][a][c#][d][e][a][c#][d][e][a][c#]
```


## Suggested Workflow

* Create ChordPro file
      python3 xml2pro.py Song_name.xml > Song_name.pro
* Transfer ChordPro file to tablet (e.g., Songbook app)
* Alternatively, use Chordii to create PostScript for printing
      chordii Song_name.pro > Song_name.ps
      

## Known Issues

* **Designed primarily for vocal music.** Instrumental music without chord symbols will only output title and key unless `--notes` flag is used.

* Does not know where to break a line. Sometimes, a line break
  every 4 bars is OK, sometimes it would be better every 2 bars.
  
* Poor line breaks for pickup bars. The line break algorithm
  always puts in a line break at the start of a bar. However, 
  for pickups, it would be better to break the line on the 
  up-beat, so that the lyrical phrase is printed as a single
  line.
  
* Does not handle multiple lines of lyrics well. If there 
  are multiple verses, each on a separate lyric line, and a
  single chorus line, it makes a bit of a hash.

* Does not handle repeats, first- and second-time endings, 
  codas, and other form markings.


## Test File Attribution

### from the original musicxml2chordpro project
https://github.com/ironss/musicxml2chordpro

- [An Affair to Remember.xml](test/An%20Affair%20to%20Remember.xml)

### Examples from musicxml.com
https://www.musicxml.com/music-in-musicxml/example-set/

- [Chant.xml](test/Chant.xml)
- [MozartPianoSonata.xml](test/MozartPianoSonata.xml)
