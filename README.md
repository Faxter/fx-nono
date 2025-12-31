# fx-nono
A pygame app for solving nonograms

![screenshot of large solved nonogram](res/screenshot-1.png?raw=true)

## prepare environment
```
uv sync
source .venv/bin/activate
```

## run application
Run without argument to get a file chooser dialog to select the puzzle file or provide path to file as argument.

```
./run.sh
./run.sh puzzles/example-2.json
```

## run tests
```
./test.sh
./test.sh coverage
```

## how to nonogram
![screenshot of small nonogram being solved](res/screenshot-0.png?raw=true)

The numbers on the top and to the left are called `hints`. They tell you how long the blocks need to be in that column or row.

* Left-click to mark a cell as `full`
* Right-click to mark a cell as `empty`
* Click a cell again to reset it
* Middle-click to mark a cell as `unsure` (for temporary markings, use is optional)

You can click a hint to strike it through. Do so again to toggle.

You can click and drag to mark multiple cells quicker.

Once every cell is marked either as `full` or `empty`, the resulting image is locked in for you to admire in your success. If your solution does not match the hints, you can continue puzzling until you find a correct configuration.

## save and load
State of the puzzle can be saved and loaded using the menu bar at the top of the application.

Loading a state must fit the currently opened puzzle. You can't load a save file belonging to a puzzle with a different amount of rows/columns than currently opened.

This uses the file format of `jsonpickle` - do not load any files that you did not create yourself as they could contain malicious code!

## load different puzzle
To load a different puzzle, create a `.json` file as desribed below and provide it to `run.sh` as described above. For reference, have a look at `puzzles/example.json`.

| key     | type                | description                                                     |
| ------- | ------------------- | --------------------------------------------------------------- |
| width   | int                 | number of columns                                               |
| height  | int                 | number of rows                                                  |
| rows    | list of list of int | row hints (each inner list contains the hints for one row)      |
| columns | list of list of int | column hints (each inner list contains the hints for one column)|

Theoretically, we could do without width and height because they are implicitly given by the length of the hint lists. But this way it is easier to immediately read to size of the puzzle.

    
## feature ideas
* display cell states with sprites instead of plain colour
* highlight rows and columns with contradiction on failed verification

## initiative ideas
* hint system with reasoning on the next step to help when getting stuck
