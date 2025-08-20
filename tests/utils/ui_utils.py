def read_ui_grid_data(page):
    data = []
    home_frame = page.frame_locator("#applicationId")

    while True:
        rows = home_frame.locator("div[role='row']").all()

        # rows.first.wait_for(state="visible", timeout=30000)
        # row_count = rows.count()
        if not rows:
            break

            # Skip header row
        for row in rows[1:]:
            cells = row.locator("div[role='gridcell']").all()
            if not cells:
                continue

        # for i in range(row_count):
        #     row = rows.nth(i)
        #     cells = row.locator("div[role='gridcell']")
        #     cell_count = cells.count()
        #
        #     if cell_count == 0:
        #         continue  # skip header or empty row

            data.append({
                "Resource Id": cells.nth(0).inner_text().strip(),
                "Resource Name": cells.nth(1).inner_text().strip(),
                "Active": cells.nth(2).inner_text().strip(),
                "Resource Start Date": cells.nth(3).inner_text().strip(),
                "Resource End Date": cells.nth(4).inner_text().strip(),
                "Project Name": cells.nth(5).inner_text().strip(),
                "Project Start Date": cells.nth(6).inner_text().strip(),
                "Project End Date": cells.nth(7).inner_text().strip(),
                "Project Allocation": cells.nth(8).inner_text().strip(),
                "Is Future Resource": cells.nth(9).inner_text().strip(),
            })

        # Pagination
        next_button = home_frame.get_by_role("button", name="Next Page")
        page.pause()
        if next_button.is_disabled():
            break
        else:
            next_button.click()
            home_frame.locator("div[role='row']").first.wait_for(state="visible")
            # rows.first.wait_for(state="visible")

    return data
