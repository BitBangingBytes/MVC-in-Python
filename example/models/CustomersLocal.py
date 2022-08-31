"""
    Responsible for 'Customers' local database access
"""


class Customers:
    db = [[1, 'Fulano', 'da Silva', "98004", "321.00"],
          [2, 'Beltrano', 'da Silva', "98261", "123.23"],
          [3, 'Ciclano', 'da Silva', "12345", "21.00"],
          [4, 'Tetrano', 'da Silva', "3213", "131.00"],
          [5, 'Heptano', 'Andradas', "1321", "4.00"]]
    cust_id = 5

    # -----------------------------------------------------------------------
    #        Constructor
    # -----------------------------------------------------------------------

    def __init__(self):
        pass

    # -----------------------------------------------------------------------
    #        Methods
    # -----------------------------------------------------------------------
    """
        Adds a customer in database

        @param fields Data of the customer to be added
        @return Record of specified id
    """

    @staticmethod
    def add(fields):
        Customers.cust_id += 1
        Customers.db.append([Customers.cust_id, fields[0].get(), fields[1].get(), fields[2].get(), fields[3].get()])
        return 4  # Return the number of items edited

    """
        Returns all records in database
        @return List of all customers
    """

    @staticmethod
    def getAll():
        return Customers.db

    """
        Returns the record with a specific id

        @param int id Id of the record
        @return Record of specified id
    """

    @staticmethod
    def get(user_id):
        for sublist in Customers.db:
            if sublist[0] == user_id:
                return sublist

    """
        Updates a record in database

        @param fields Data of the customer to be updated
        @return List of affected database rows
    """

    @staticmethod
    def update(fields):
        id_customer = int(fields[0].get())
        for i, sublist in enumerate(Customers.db):
            if sublist[0] == id_customer:
                Customers.db[i] = [int(fields[0].get()), fields[1].get(),
                                   fields[2].get(), fields[3].get(), fields[4].get()]
        return 4  # Return the number of items edited

    """
        Delete a customer in database
        @param id_customer Id of the customer
    """

    @staticmethod
    def delete(id_customer):
        for i, sublist in enumerate(Customers.db):
            if sublist[0] == id_customer:
                del Customers.db[i]