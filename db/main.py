import os 
from dotenv import load_dotenv

load_dotenv()

HOST=os.getenv("HOST")
PORT=os.getenv("PORT")
DB_USER=os.getenv("DB_USER")
DB_PASS=os.getenv("DB_PASS")
DUMP_ARCHIVE_NAME=os.getenv("DUMP_ARCHIVE_NAME")
database=os.getenv("database")

#def get_dump(database):
#    filestamp = time.strftime('%Y-%m-%d-%I')
#    os.popen("mysql -h %s -P %s -u %s -p%s %s > %s.sql" % (HOST,PORT,DB_USER,DB_PASS,database,database+"_"+filestamp))
#
#   print("\n|| Database dumped to "+database+"_"+filestamp+".sql || ")

def import_dump():
    try:
        result = os.system("mysql -u{} -p{} {} < {}".format(DB_USER, DB_PASS, database, DUMP_ARCHIVE_NAME))
    except:
        print("Error seeding database!")
    return result 


def main():
    result = import_dump()
    if result == 0:
        print("Sucessfully seeded database using dump.")
    else: 
        print("An error has ocurred!") 

if __name__ == "__main__":
    main()