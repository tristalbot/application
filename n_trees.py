import argparse

parser = argparse.ArgumentParser(description="How many trees ?")
parser.add_argument(
    "--n_trees", type=int, default=1500,
    help="Number of trees to train our model."
)
args = parser.parse_args()
n_trees = args.n_trees
print(n_trees)
