import mysql.connector


class CreateDatabase:
    """ Class to create a new database. """

    def __init__(self, my_base):
        """ Initialization of the class."""
        self.my_base = my_base

    def create(self):
        """"""
        # Create the database
        cursor = self.my_base.cursor()
        cursor.execute(f"CREATE DATABASE store;")
        self.my_base.commit()
        cursor.close()

        # Create the table category
        cursor = self.my_base.cursor()
        cursor.execute(f"CREATE TABLE category (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL);")
        self.my_base.commit()
        cursor.close()

        # Create the table product
        cursor = self.my_base.cursor()
        cursor.execute(f"CREATE TABLE product (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL,"
                       f"description TEXT, price INT NOT NULL, quantity INT, id_category INT NOT NULL,"
                       f"FOREIGN KEY (id_category) REFERENCES category(id));")
        self.my_base.commit()
        cursor.close()
