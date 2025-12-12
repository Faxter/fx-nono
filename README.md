# fx-nono
A pygame app for solving nonograms

## prepare environment
```
uv sync
source .venv/bin/activate
```

## run application
```
./run.sh
```

## run tests
```
./test.sh
./test.sh coverage
```

## development plan
1. puzzle is supplied as config file, containing:
    * ✅️ grid size
    * ✅️ column hints
    * ✅️ row hints
1. display:
    * ✅️ interactive grid
    * ✅️ column hints on the top
    * ✅️ row hints on the left
1. control features:
    * ✅️ left-click to mark as filled in
    * ✅️ right-click to mark free
    * ✅️ middle-click for a temporary helper mark
    * ✅️ matching click on cell clears it
    * ✅️ left-click on hint crosses it out
    * ✅️ left-click on crossed out hint removes the crossing out
1. once every cell is marked, checks for success
    * ✅️ on success: displays win message
        * ✅️ keep window open in 'read-only' until quit
    * ✅️ on fail: displays fail message
        * ✅️ continue interaction until success or quit
    
## future features
* menu for selecting puzzle file to load
* saving/loading progress in personal save file
* click and drag to mark multiple cells in a row
* highlight rows and columns with contradiction on failed verification

## future initiatives
* hint system with reasoning on the next step to help when getting stuck
