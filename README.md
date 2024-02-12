# Function-Relation-Visualizer
 Creates a graph visualizing the relation between functions in a given Python file

## Installation
Using Python 3.11
1. Clone this repo
2. pip install -r requirements.txt
3. Install Graphviz from https://graphviz.org/download/ 
4. Add Graphviz bin to PATH

## Usage
Execute main from terminal with path as argument
```
main.py C:\...\Function-Relation-Visualizer\elementary.py
```

### Not finished
In order to fulfill the assignment the following must be done
* Trim trailing _, remove tier from name and add as field
* Create relations based on:
  * Base name used as parameter (without tier or trailing _)
  * Tier, must be same for function and parameter
* Match tiers, tier1 can only be used with other tier1's (Assumption)
* Add loose ends