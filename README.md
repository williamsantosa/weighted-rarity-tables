# Weighted Rarity Tables

Weighted rarity tables implementation in Python.

## Usage

Initialize program by running

```
python3 main.py <file_location>
```

The following commands are available:

```
Commands:
- exit
- help
- simulate <table_name> <n>
- set_luck_rate <n>
- get_weighted_random <table>
- table_total_weight <table>
- get_item_pairs <table>
- display
```

## Data Table Format

JSON Format

```json
{
    "table_1": {
        "item_1": 7,
        "item_2": 3,
        ...
    },
    "table_2": {
        "item_1": 8,
        "item_2": 2,
        ...
    }
}
```

YAML Format

```yaml
table_1:
  "item_1": 0.2
  "item_2": 0.15
  ...

table_2:
  "item_1": 0.2
  "item_2": 0.15
  ...

```