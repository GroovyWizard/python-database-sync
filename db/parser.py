
def generate_insert_list(sql):
    for line in sql:
        if(line.startswith("INSERT")):
            yield line

def parse_sql(sql):
       line_list = generate_insert_list(sql)
       for line in line_list:
           print(line)

def main():
    with open("dump.sql", "rt") as sql:
        parse_sql(sql)
    
if __name__ == "__main__":
    main()
