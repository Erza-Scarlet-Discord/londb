# LonDB (redis type database)
A module to make json file handling easier 

- supports firebase storage 
- supports local storage

## Local
```
from londb import database

db = database("database name") # create a database connection

db.add("users",{"username":"erza"}) #updates json data

print(db.get("users")) # shows json data
```

## Firebase

```
from londb import FirebaseDatabase

db = FirebaseDatabase("Database Name", Firebase Config) # Firebase config is a dictonary

db.add("users",{"username":"erza"}) #updates json data

print(db.get("users")) # shows json data
```



