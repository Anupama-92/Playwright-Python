from datetime import datetime


def read_ui_grid_data(page):
    data = []
    home_frame = page.frame_locator("#applicationId")

    while True:
        rows = home_frame.locator("div[role='row']").all()
        if not rows:
            break

        # Skip header row
        for row in rows[1:]:
            cells = row.locator("div[role='gridcell']").all()
            if not cells:
                continue

            data.append({
                "Resource Id": str(cells[1].inner_text().strip()),
                "Resource Name": cells[2].inner_text().strip(),
                "Active": cells[3].inner_text().strip(),
                "Resource Start Date": normalize_date(cells[4].inner_text().strip()),
                "Resource End Date": normalize_date(cells[5].inner_text().strip()),
                "Project Name": cells[6].inner_text().strip(),
                "Project Start Date": normalize_date(cells[7].inner_text().strip()),
                "Project End Date": normalize_date(cells[8].inner_text().strip()),
                "Project Allocation": str(cells[9].inner_text().strip()),
                "Is Future Resource": normalize_yes_no(cells[10].inner_text().strip()),
            })

        # Pagination
        next_button = home_frame.get_by_role("button", name="Next Page")
        page.pause()
        if next_button.is_disabled():
            break
        else:
            next_button.click()
            home_frame.locator("div[role='row']").first.wait_for(state="visible")

    return data


def normalize_yes_no(value: str) -> str:
    if str(value).strip().lower() in ("yes", "y", "true", "1"):
        return "Yes"
    return "No"


def normalize_date(value: str) -> str:
    if not value or value.strip() == "-":
        return "-"
    for fmt in ("%d-%b-%Y", "%d-%m-%Y", "%Y-%m-%d", "%d/%m/%Y"):
        try:
            return datetime.strptime(value, fmt).strftime("%d-%b-%Y")
        except ValueError:
            continue
    return value
