# Database Sync
Database Sync is a script made in python to automate the process of dumping a production database, parsing the personal info (like real names and documents), then seeding a development database with the same structure and similar data, for testing and simulations.

# Instructions
## This repository comes with a docker pre configured for simulations!
1. make build
2. make up
3. make python-test
4. make pip
5. make sh
- cd db && cp .env.example .env

## Then you can test the code with
1. make parse-sql
2. make seed-w-dump

### Soon parse-sql script will be used alongside the seeding one, and the dump function will be available too.

## Considerations

1. Database info can be configured directly into **.env**, do not hard code any information into the script!
2. This code uses BSD-3 license so you can do almost anything with it, modify and even merge into proprietary code, it's up to you.
