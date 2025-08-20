import openpyxl
from datetime import datetime


def read_and_format_excel(file_path: str):
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active

    headers = [cell.value for cell in ws[4]]
    data = []

    for row in ws.iter_rows(min_row=5, values_only=True):
        row_dict = dict(zip(headers, row))

        # Convert Active (True/False) → Yes/No
        if isinstance(row_dict.get("Resource Status"), bool):
            row_dict["Active"] = "Yes" if row_dict["Resource Status"] else "No"
        else:
            row_dict["Active"] = "Yes" if str(row_dict.get("Resource Status")).strip().lower() == "true" else "No"

        # Format Resource Start Date
        row_dict["Resource Start Date"] = format_excel_date(row_dict.get("Resource Start Date"))

        # Format Project Start Date
        row_dict["Project Start Date"] = format_excel_date(row_dict.get("Project Start Date"))

        # Format Is Future Resource (True/False → Yes/No)
        if isinstance(row_dict.get("Is Future Resource"), bool):
            row_dict["Is Future Resource"] = "Yes" if row_dict["Is Future Resource"] else "No"
        else:
            row_dict["Is Future Resource"] = "Yes" if str(row_dict.get("Is Future Resource")).strip().lower() == "true" else "No"

        data.append({
            "Resource Id": row_dict.get("Resource Id"),
            "Resource Name": row_dict.get("Resource Name"),
            "Active": row_dict.get("Active"),
            "Resource Start Date": row_dict.get("Resource Start Date"),
            "Resource End Date": row_dict.get("Resource End Date") or "-",
            "Project Name": row_dict.get("Project Name") or "-",
            "Project Start Date": row_dict.get("Project Start Date"),
            "Project End Date": row_dict.get("Project End Date") or "-",
            "Project Allocation": row_dict.get("Project Allocation") or "-",
            "Is Future Resource": row_dict.get("Is Future Resource")
        })

    return data


def format_excel_date(excel_date):
    """Convert Excel datetime or string to UI format dd-MMM-yyyy"""
    if not excel_date:
        return "-"
    if isinstance(excel_date, datetime):
        return excel_date.strftime("%d-%b-%Y")
    try:
        parsed = datetime.strptime(str(excel_date), "%Y-%m-%d")
        return parsed.strftime("%d-%b-%Y")
    except ValueError:
        return str(excel_date)
