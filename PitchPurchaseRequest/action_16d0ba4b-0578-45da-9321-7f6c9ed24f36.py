if ax.row.catItems:

    cat_guids_str = ', '.join(f'"{k}"' for k in ax.row.catItems)

    sql_query = f'SELECT * FROM "PitchPurchaseRequestItems" WHERE guid IN({cat_guids_str})'

    total = 0

    result = ax.sql(sql_query)

    if result:

        for row in result:

            total += float(row['quantity']) * float(row['indicativePrice'])

        ax.row.total = total