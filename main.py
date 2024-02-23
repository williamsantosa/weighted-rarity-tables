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

    tables = weights.WeightedRarityTable(args.file_location)
    while True:
        command = input("Enter a command (help): ")
        command = command.split(" ")
        if command[0] == "exit":
            break
        elif command[0] == "help":
            print("Commands: \n- exit\n- help\n- simulate <table_name> <n>\n- set_luck_rate <n>\n- get_weighted_random <table>\n- table_total_weight <table>\n- get_item_pairs <table>\n- display")
        elif command[0] == "simulate":
            table_name = command[1]
            iterations = int(command[2])
            ret = tables.simulate(table_name, iterations)
            print(sorted(ret.items(), key=lambda x: x[1], reverse=True))
        elif command[0] == "set_luck_rate":
            rate = float(command[1])
            tables.set_luck_rate(rate)
        elif command[0] == "get_weighted_random":
            table = command[1]
            print(tables.get_weighted_random(table))
        elif command[0] == "table_total_weight":
            table = command[1]
            print(tables.table_total_weight(table))
        elif command[0] == "get_item_pairs":
            table = command[1]
            print(tables.get_item_pairs(table))
        elif command[0] == "display":
            print(tables)
        else:
            print(f"Error: Invalid command '{command[0]}'")

if __name__ == "__main__":
    main()