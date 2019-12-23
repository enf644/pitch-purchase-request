ax.query = f"""
    SELECT <ax_fields> 
    FROM "<ax_table>"
    WHERE "requester"="{ax.user_email}";
"""