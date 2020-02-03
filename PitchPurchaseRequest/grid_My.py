ax.query = f"""
    SELECT {ax.db_fields} 
    FROM "{ax_table}"
    WHERE "requester"="{ax.user_email}";
"""
