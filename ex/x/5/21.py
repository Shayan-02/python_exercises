# https://leetcode.com/problems/combine-two-tables/description/?lang=pythondata

import pandas as pd


def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    # Perform a left join on the 'personId' column
    result = person.merge(address, on="personId", how="left")

    # Select the required columns
    result = result[["firstName", "lastName", "city", "state"]]

    return result
