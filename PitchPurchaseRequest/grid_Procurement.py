ax.query = f"""
    SELECT <ax_fields> 
    FROM "<ax_table>"
    WHERE "axState"="Procurement Processing";
"""