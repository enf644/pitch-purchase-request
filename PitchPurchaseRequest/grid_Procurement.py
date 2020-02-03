ax.query = f"""
    SELECT {ax.db_fields}
    FROM "{ax_table}"
    WHERE "axState"="Procurement Processing";
"""
