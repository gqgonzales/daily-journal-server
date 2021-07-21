import sqlite3
import json
from models import mood, Mood


def get_all_moods():
    # Open a connection to the database, save it as conn
    with sqlite3.connect("./dailyjournal.db") as conn:

        # The type of rows returned when we fetch
        conn.row_factory = sqlite3.Row
        # What let's us execute queries
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT
            m.id,
            m.label
        FROM moods m
        """
        )

        # Initialize an empty list to hold all mood representations
        moods = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an mood instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # mood class above.
            mood = Mood(
                row["id"],
                row["label"]
            )

            # Converting an object into a dictionary
            moods.append(mood.__dict__)

            # Use `json` package to properly serialize list as JSON
        return json.dumps(moods)
