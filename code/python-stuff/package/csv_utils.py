import pandas as pd

# display all rows and columns for a dataframe temporarily
def print_in_full(*args: any) -> None: 
    with pd.option_context(
        "display.max_rows", 
        None, 
        "display.max_columns", 
        None,
        "display.max_colwidth",
        120
    ):
        print(*args)
