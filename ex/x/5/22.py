# https://leetcode.com/problems/find-followers-count/description/?lang=pythondata

import pandas as pd


def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    # Group by user_id and count the number of followers
    follower_counts = (
        followers.groupby("user_id").size().reset_index(name="followers_count")
    )

    # Sort the result by user_id in ascending order
    follower_counts = follower_counts.sort_values("user_id")

    return follower_counts
