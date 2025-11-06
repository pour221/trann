import argparse
import sys
from Bio import Phylo
import re
import numpy as np

from .scripts import get_paths, TableReader

def main():
    parser = argparse.ArgumentParser('A small script for adding information to phylogenetic trees in the newick format')

    parser.add_argument('-i', '--info', default='.',
                        help='path to info table (.csv or .xlsx). Default=./*.csv')
    parser.add_argument('-t', '--tree', default='.',
                        help='path to tree file (newick). Default=./*.tree')
    parser.add_argument('-s', '--sep', default=', ', help='Separator for forming a line for leaf labels. Default: ", "')
    parser.add_argument('-o', '--output', default='./add_annot_tree.tree',
                        help='path to file to save results. Default="./add_annot_tree.tree"')

    args = parser.parse_args()

    output = args.output
    separator = str(args.sep)

    if type(get_paths(args)) is int:
        sys.exit(1)
    else:
        info_path, tree_path = get_paths(args)

    info_reader = TableReader(info_path)
    info_table = info_reader.read()
    tree = Phylo.read(tree_path, 'newick')
    data_to_add = {}
    for row in info_table[1:]:
        data_to_add[row[0]] = separator.join([str(i).strip() for i in row])

    patterns = list(data_to_add.keys())
    for clade in tree.get_terminals():
        cur_name = clade.name.strip()
        is_info = np.array(
            [re.search(pattern.strip(), cur_name) for pattern in
             patterns])
        if any(is_info):
            is_info = is_info[is_info != None]

            if is_info.shape[0] > 1:
                f = np.vectorize(lambda x: x.group())
                match = max(f(is_info), key=len)
            else:

                match = is_info[is_info != None][0].group()
            clade.name = data_to_add[match]

    Phylo.write(tree, output, 'newick')

    print('\033[92m[SUCCESS]\033[0m The labels for the dendrogram leaves have been successfully added')
    return 0

if __name__ == "__main__":
    main()

