import allure
from tabulate import tabulate


def attach_score_table_to_allure(title: str, table_data: list[dict], headers: list[str]):

    if not table_data:
        return

    # Generate HTML table using tabulate
    html_table = f"""
    <html>
        <head>
            <style>
                table {{
                    width: 100%;
                    border-collapse: collapse;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: center;
                }}
                th {{
                    background-color: #003554;
                    color: white;
                }}
                tr:nth-child(even) {{
                    background-color: #f2f2f2;
                }}
            </style>
        </head>
        <body>
            <h3>{title}</h3>
            {tabulate(table_data, headers="keys", tablefmt="html")}
        </body>
    </html>
    """

    allure.attach(html_table, name=title, attachment_type=allure.attachment_type.HTML)