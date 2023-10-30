
from service import retrieveNotionDatabase
import utils
from tokens import SECRETS
from send_email import send_email
import html_email as html
import datetime
from datetime import timezone
# Notion api config
password = f"Bearer {SECRETS['notion_test_token']}"
headers = {
    "Authorization": password,
    "Notion-version": "2022-06-28"
}

today = str(datetime.datetime.now(timezone.utc).date())

query = {
    "filter": {
        "and": [
            {
                "property": "Due",
                "date": {
                    "on_or_before": today
                }
            },
            {
                "property": "Status",
                "status": {
                    "equals": "to do"
                }
            }
        ]
    },
    "sorts": [
        {
            "property": "Due",
            "direction": "ascending"
        }
    ]
}

# Notion api database block http request
database = retrieveNotionDatabase.retrieveDatabase(
    databaseId=SECRETS['database_id'],
    headers=headers,
    save_to_json=False,
    query=query
)

# Print retrieve database data
# utils.debugDatabaseObject(database)

# Get data we want from database.json object
database_list = utils.decodeDatabase(database)
dbProperties = utils.databaseProperties(database_list)

# Filter columns of the database
dbProperties = ['Task name', 'Due', 'Status', 'Project', 'Context', 'Priority', 'Summary']
# Data to html table
title = "\n".join(html.html_table_column(dbProperties))
rows = "\n".join(html.html_table_row(
    database_list,
    dbProperties
))
table_html = html.construct_html_table(title, rows)

html_msg = html.construct_html_msg(
    table_html,
    html.style
)

utils.save_html(html_msg)

# Send email with html msg
send_email(
    html_msg,
    SECRETS['email_from'],
    SECRETS['email_to'],
    SECRETS['gmail_password']
)
