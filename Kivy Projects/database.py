class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = []
        self.load_users()

    def load_users(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    email, password, name = line.strip().split(',')
                    self.users.append({'email': email, 'password': password, 'name': name})
        except FileNotFoundError:
            pass

    def save_users(self):
        with open(self.filename, 'w') as file:
            for user in self.users:
                file.write(f"{user['email']},{user['password']},{user['name']}\n")

    def fetch(self):
        return self.users

    def add_user(self, email, password, name):
        self.users.append({'email': email, 'password': password, 'name': name})
        self.save_users()

    def remove_user(self, email):
        self.users = [user for user in self.users if user['email'] != email]
        self.save_users()

    def update_user(self, email, password, name):
        for user in self.users:
            if user['email'] == email:
                user['password'] = password
                user['name'] = name
                self.save_users()
                break

    def get_user(self, email):
        for user in self.users:
            if user['email'] == email:
                return user['password'], user['name'], None
        return None, None, None

    def validate(self, email, password):
        for user in self.users:
            if user['email'] == email and user['password'] == password:
                return True
        return False

# Exemplo de uso
#db = DataBase("users.txt")
#db.add_user("test@example.com", "password123", "Test User")
#print(db.fetch())
