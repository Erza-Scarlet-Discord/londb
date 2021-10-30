import json


class database:

    def __init__(self, db_name):
        """Define a database for the package, It is used to connect or create a database."""
        self.db = db_name
        try:
            file = open('databases/' + self.db + '.londb', 'r+')
            print(f"Successfully Connected to database {self.db} ")
        except FileNotFoundError:

            with open('databases/' + str(self.db) + '.londb', 'w') as f:
                f.write("{}")
                print("Database with name " + self.db + " Does not exist, creating a new one")

    def get(self, key):
        """Get the value for a key, Can be str, Int or Dict"""
        try:
            with open('databases/' + self.db + '.londb', 'r+') as f:
                data = json.load(f)

                print(data[key])
                f.close()
                return data[key]
        except KeyError:
            print(f"Key \"{key}\" Does not exist")

    def add(self, key, value):
        new_data = {key: value}
        try:
            with open('databases/' + self.db + '.londb', 'r+') as f:
                data = json.load(f)
                data.update(new_data)
                f.seek(0)
                json.dump(data, f)
                print("Updated database")

        except Exception as e:
            print(f"Error {str(e)}")
