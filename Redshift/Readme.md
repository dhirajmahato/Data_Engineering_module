## Redshift
A cloud-based data warehouse by AWS

In Amazon Redshift, there are several system catalog tables and views that provide metadata about the database, tables, views, and other objects. Here are some of the key system catalog tables and views in Redshift:

1. **pg_table_def**: Contains metadata about table columns, such as column names, data types, and constraints.
2. **pg_namespace**: Provides information about database schemas.
3. **pg_class**: Contains metadata about database objects such as tables and indexes.
4. **pg_attribute**: Contains information about table columns, including data types, nullability, and default values.
5. **pg_user**: Provides information about database users.
6. **pg_group**: Contains information about database groups.
7. **pg_roles**: Provides information about database roles.
8. **pg_database**: Contains metadata about databases in the Redshift cluster.
9. **information_schema.tables**: A view that provides information about tables in the current database, such as table names and schemas.
10. **information_schema.columns**: A view that provides information about table columns, such as column names, data types, and constraints.
11. **svv_table_info**: A system view that provides detailed information about tables, including their size, distribution style, and sort keys.
12. **stl_query**: Contains information about queries executed on the cluster, including their start time, end time, status, and resource usage.

These catalog tables and views can be queried to retrieve various metadata about your Redshift database and its objects.
