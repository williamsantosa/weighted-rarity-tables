import weights
import os
import argparse

def main():
    parser = argparse.ArgumentParser(prog='main', description='Weighted Rarity Table loading, manipulation, and querying')
    parser.add_argument('file_location', help='The location of the file')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')
    args = parser.parse_args()

    if not os.path.isfile(args.file_location):
        print(f"Error: Invalid file location '{args.file_location}'")
        return

    weighted_rarity_table = weights.WeightedRarityTable(args.file_location)
    print(weighted_rarity_table.get_item_pairs('gear'))

if __name__ == "__main__":
    main()