# trann

A simple Python command-line tool for working with tabs (`.csv`, `.xlsx`) and phylogenetic tree in newick format files (like PhyML and FastTree outputs).  
It automatically detects file types, reads their contents using the csv and openpyxl library, and provides clear error messages with colored console output.

---
## Project structure

```
trann/
├── src/
│   ├── trann.py        # main CLI logic (entry point)
│   ├── scripts.py       # helper functions
│   └── __init__.py
├── pyproject.toml       # project configuration
└── README.md
```
## Dependencies
- python>=3.10
- biopython>=1.86
- numpy>=2.3.4
- openpyxl>=3.1.5

## Installation
> It is recommended to use virtual environment (conda or venv)

Clone the repository and install the package:

```commandline
git clone https://github.com/pour221/trann.git
cd trann
uv pip install -e .
```
or without uv:

```commandline
pip install -e .
```
## Usage

```commandline
trann -i info_table.csv -t newik.tree -o res_tree.tree
```
If no paths are provided (`.` as default), the tool automatically searches the current directory for:

the first .csv file (for --info)

the first .tree file (for --tree)

For instance:
```commandline
trann
```
will use the first .csv file and the first .tree file.

