import sqlite3
import json
from models import Entry, Mood


def get_all_entries():
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
            e.id,
            e.entry_date,
            e.concept,
            e.body,
            e.mood_id,
            m.id mood_id,
            m.label mood_label
        FROM Entries e
            JOIN Moods m ON m.id = e.mood_id;
        """
        )

        # Initialize an empty list to hold all entry representations
        entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an entry instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # entry class above.
            entry = Entry(
                row["id"],
                row["entry_date"],
                row["concept"],
                row["body"],
                row["mood_id"],
            )

            # Create a mood instance from the current row
            mood = Mood(
                row['mood_id'], row['mood_label'])

            # Add the dictionary representation of the mood to the entry
            entry.mood = mood.__dict__

            # Converting an object into a dictionary
            entries.append(entry.__dict__)

            # Use `json` package to properly serialize list as JSON
        return json.dumps(entries)


def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute(
            """
        SELECT
            e.id,
            e.entry_date,
            e.concept,
            e.body,
            e.mood_id,
            m.id mood_id,
            m.label mood_label
        FROM Entries e
            JOIN Moods m ON m.id = e.mood_id
        WHERE e.id = ?
        """,
            (id,),
        )

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an entry instance from the current row.
        # Note that the database fields are specified in
        # exact order of the parameters defined in the
        # entry class above.
        entry = Entry(
            data["id"],
            data["entry_date"],
            data["concept"],
            data["body"],
            data["mood_id"],
        )

        # Create a mood instance from the current row
        mood = Mood(
            data['mood_id'], data['mood_label'])

        # Add the dictionary representation of the mood to the entry
        entry.mood = mood.__dict__

        # Use `json` package to properly serialize list as JSON
        return json.dumps(entry.__dict__)


def delete_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Entries
        WHERE id = ?
        """, (id, ))


def get_entries_from_search(searchTerm):
    with sqlite3.connect("./dailyjournal.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute(f"""
        SELECT e.id,
            e.entry_date,
            e.concept,
            e.body,
            e.mood_id,
            m.label mood_label
        FROM Entries e
            JOIN Moods m ON m.id = e.mood_id
        WHERE concept LIKE "%{searchTerm}%"
            OR body LIKE "%{searchTerm}%";
        """)
        entries = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'], row['entry_date'], row['concept'],
                          row['body'], row['mood_id'])
            entries.append(entry.__dict__)

    return json.dumps(entries)


def create_entry(new_entry):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        INSERT INTO Entries
            ( entry_date, concept, body, mood_id)
        VALUES
            ( ?, ?, ?, ?);
        """, (new_entry['entry_date'], new_entry['concept'], new_entry['body'], new_entry['mood_id']))
        new_id = db_cursor.lastrowid
        new_entry['id'] = new_id

    return json.dumps(new_entry)
