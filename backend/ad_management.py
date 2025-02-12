import sqlite3

def get_total_ads_from_db(db_path: str, db: object):
    """
    Retrieves the total number of ads from the database.

    Args:
        db_path (str): Path to the database file.

    Returns:
        int: The total number of ads.
    """

    # Connect to the database
    # conn = sqlite3.connect(db_path)

    # Create a cursor object
    # cursor = conn.cursor()

    # Execute the query to get the total number of users
    db.execute("SELECT COUNT(*) FROM ads")

    # Fetch the result
    total_ads = db.fetchone()[0]

    # Close the database connection
    # conn.close()

    return total_ads

def get_ads_from_db(db_path: str, db: object):
    """
    Gets a list of ads from a SQLite database.

    Args:
        db_path: The path to the SQLite database file.

    Returns:
        A list of ads, where each ad is a dictionary with the following keys:
        - id: The ad's ID.
        - adname: The ad's adname.
        - creator: The ad's creator.
        - object-url: The object url of the ad
    """
    # conn = sqlite3.connect(db_path)
    # cursor = conn.cursor()

    # Execute the query to get all ads
    db.execute("SELECT * FROM ads")

    # Fetch all rows as a list of dictionaries
    ads = [
        dict(id=row[0], adname=row[1], creator=row[2], object_url=row[3])
        for row in db.fetchall()
    ]

    # Close the database connection
    # conn.close()

    return ads

def get_spcific_ad_from_db(db_path: str, ad_id: int, db: object):
    """
    Gets a specific ad from a SQLite database based on its ID.

    Args:
        db_path: The path to the SQLite database file.
        ad_id: The ID of the ad to retrieve.

    Returns:
        A dictionary representing the ad, or None if the ad is not found.
    """
    # conn = sqlite3.connect(db_path)
    # cursor = conn.cursor()

    # Execute the query to get the specific ad
    db.execute("SELECT * FROM ads WHERE id =%s", (ad_id,))

    # Fetch the result
    row = db.fetchone()

    # Close the database connection
    # conn.close()

    if row:
        # Convert the row to a dictionary
        ad = dict(id=row[0], adname=row[1], creator=row[2], object_url=row[3])
        return ad
    else:
        return None

def update_ad(db_path: str, ad_data: dict, db: object):
    """
    Updates an existing ad in the database.

    Args:
        db_path: The path to the SQLite database file.
        ad_id: The ID of the ad to update.
        ad_data: A dictionary containing the updated ad data.
               The keys should match the column names in the 'ads' table.

    Returns:
        True if the update is successful, False otherwise.
    """
    # Connect to the database
    # conn = sqlite3.connect(db_path)

    # Create a cursor object
    # cursor = conn.cursor()

    # Prepare the SQL statement
    sql = """
        UPDATE ads
        SET adname = :adname, creator = :creator, "object-url" = :object_url
        WHERE id = :ad_id
    """

    # Execute the SQL statement with the updated ad data
    db.execute(sql, ad_data)

    # Commit the changes
    # conn.commit()

    # Close the database connection
    # conn.close()

    # Check if any rows were updated
    if db.rowcount > 0:
        return True
    else:
        return False

def get_active_ads_from_db(db_path: str, db: object):
    """
    Gets a list of active ads from a SQLite database.

    An ad is considered active if its 'object-url' field is not empty.

    Args:
        db_path: The path to the SQLite database file.

    Returns:
        A list of active ads, where each ad is a dictionary with the following keys:
        - id: The ad's ID.
        - adname: The ad's adname.
        - creator: The ad's creator.
        - object-url: The object url of the ad
    """
    # conn = sqlite3.connect(db_path)
    # cursor = conn.cursor()

    # Execute the query to get active ads (where 'object-url' is not empty)
    db.execute("SELECT * FROM ads WHERE 'object-url' != ''")

    # Fetch all rows as a list of dictionaries
    active_ads = [
        dict(id=row[0], adname=row[1], creator=row[2], object_url=row[3])
        for row in db.fetchall()
    ]

    # Close the database connection
    # conn.close()

    return active_ads