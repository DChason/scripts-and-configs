import re

sql_file = "path-to-sql-file-here.sql"

mysql_reserved_keywords = {
    "abort", "accessible", "add", "all", "alter", "analyze", "and", "as",
    "asc", "asensitive", "atan", "atan2", "avg", "before", "benchmark",
    "between", "bigint", "binary", "bit_and", "bit_or", "bit_xor", "blob",
    "both", "by", "call", "cascade", "case", "cast", "change", "char",
    "char_length", "character", "check", "collate", "column", "condition",
    "connection", "constraint", "continue", "convert", "create", "cross",
    "curdate", "current_date", "current_time", "current_timestamp",
    "current_user", "cursor", "database", "databases", "day_hour",
    "day_microsecond", "day_minute", "day_second", "dec", "decimal",
    "declare", "default", "delayed", "delete", "desc", "describe",
    "deterministic", "distinct", "distinctrow", "div", "do", "double",
    "drop", "dual", "each", "else", "elseif", "end", "exists", "exit",
    "explain", "false", "fetch", "for", "force", "foreign", "from",
    "fulltext", "generated", "grant", "group", "having", "high_priority",
    "hour_microsecond", "hour_minute", "hour_second", "if", "ifnull",
    "ignore", "in", "increment", "index", "infile", "inner", "inout",
    "insensitive", "insert", "int", "int1", "int2", "int3", "int4",
    "int8", "integer", "interval", "into", "is", "isolation", "join",
    "key", "kill", "length", "leading", "leave", "left", "like",
    "limit", "linear", "lines", "load", "localtime", "localtimestamp",
    "lock", "long", "longblob", "longtext", "loop", "low_priority",
    "match", "mediumblob", "mediumint", "mediumtext", "min",
    "minute_microsecond", "minute_second", "mod", "modifies", "natural",
    "not", "no_write_to_binlog", "null", "numeric", "now", "on",
    "optimize", "option", "optionally", "or", "order", "out", "outer",
    "outfile", "partition", "precision", "primary", "procedure",
    "purge", "range", "read", "reads", "real", "recursive",
    "references", "regexp", "rename", "replace", "require", "restrict",
    "return", "revoke", "right", "rlike", "row", "rows", "schema",
    "schemas", "select", "sensitive", "separator", "set", "show",
    "signal", "smallint", "spatial", "specific", "sql", "sqlexception",
    "sqlstate", "sqlwarning", "ssl", "starting", "stored", "table",
    "terminated", "then", "time", "timestamp", "timestampdiff",
    "timestampadd", "to", "trailing", "trigger", "true", "uncommitted",
    "union", "unique", "unlock", "unsigned", "update", "usage", "use",
    "using", "utc_date", "utc_time", "utc_timestamp", "values",
    "varbinary", "varchar", "varcharacter", "varying", "when", "where",
    "while", "with", "write", "x509", "year_month", "zerofill"
}


def extract_tables_with_column_names(sql_file):
    tables = {}
    table_pattern = re.compile(r'CREATE TABLE `([^`]+)` \(')
    column_pattern = re.compile(r'`([^`]+)`\s+')

    with open(sql_file, 'r') as file:
        lines = file.readlines()

    current_table = None

    for line in lines:
        table_match = table_pattern.search(line)
        if table_match:
            current_table = table_match.group(1)
            tables[current_table] = []
            continue

        if current_table:
            if line.strip() == "/*!40101 SET character_set_client = @saved_cs_client */;":
                current_table = None
                continue

            column_match = column_pattern.findall(line)
            if column_match:
                tables[current_table].extend(column_match)

        if current_table and line.strip() == ");":
            current_table = None

    return tables

def check_reserved_keywords(tables, reserved_keywords):
    for table, columns in tables.items():
        for column in columns:
            if column in reserved_keywords:
                print(f"Table: {table}, Column: {column} is a reserved keyword.")

def main():
    tables = extract_tables_with_column_names(sql_file)
    check_reserved_keywords(tables, mysql_reserved_keywords)

if __name__ == "__main__":
    main()

