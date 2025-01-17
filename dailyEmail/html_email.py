def html_table_column(titles):
    yield "\t    <tr>"
    for column in titles:
        yield f"\t\t<th>{column}</th>"
    yield "\t    </tr>\n"


def html_table_row(rows, columns):
    for row in rows:
        yield "\t    <tr>"
        for column in columns:
            if column not in row:
                row[column] = ""
            if column in row and column == 'Task':
                href = "href=\"" + row['url'] + "\""
                yield f"\t\t<td><a {href}>{row[column]}</a></td>"
            else:
                yield f"\t\t<td>{row[column]}</td>"
        yield "\t    </tr>"


def construct_html_table(columns, rows):
    return '<table class="styled-table">\n' + columns + rows + "\n\t</table>"


def construct_html_msg(table, style):
    html_template = f"""\
<html>
    <head>
    <style>
{style}
    </style>
    </head>
    <body>
        <h1>Tasks for today ✅</h1>
        {table}
    </body>
</html>
"""
    return html_template


# Reference https://dev.to/dcodeyt/creating-beautiful-html-tables-with-css-428l
style = """\
        .styled-table {
            border-collapse: collapse;
            margin: 25px 0;
            font-size: 0.9em;
            font-family: sans-serif;
            min-width: 400px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
        }

        .styled-table thead tr {
            background-color: #009879;
            color: #ffffff;
            text-align: left;
        }

        .styled-table th,
        .styled-table td {
            padding: 12px 15px;
        }

        .styled-table tbody tr {
            border-bottom: 1px solid #dddddd;
        }

        .styled-table tbody tr:nth-of-type(even) {
            background-color: #f3f3f3;
        }

        .styled-table tbody tr:last-of-type {
            border-bottom: 2px solid #009879;
        }

        .styled-table tbody tr.active-row {
            font-weight: bold;
            color: #009879;
        }

        h1 {
            color: #009879;
            font-family: arial, sans-serif;
            font-size: 16px;
            font-weight: bold;
            margin-top: 0px;
            margin-bottom: 1px;
        }
"""
