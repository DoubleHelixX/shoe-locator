# Ideas

## OOPs : Object-Oriented Programming
Since these three methods insert, update, delete have the same definition in every class then what you can do is you can make a class inheritedClassName which can be inherited in other classes and so you can use the same code.

-   This will also make your code reusable and will increase code readability as well!

-   `For Example:`
    ```
    '''
    Extend the base Model class to add common methods
    '''
    class inheritedClassName(db.Model):
        __abstract__ = True

        def insert(self):
            db.session.add(self)
            db.session.commit()

        def delete(self):
            db.session.delete(self)
            db.session.commit()

        def update(self):
            db.session.commit()


    '''
    Vehicle
    '''
    @dataclass
    class Vehicle(inheritedClassName):
        id: int
        license_plate: String
        model: String
        make: String

        __tablename__ = "vehicles"

        id = Column(Integer, primary_key=True)
        license_plate = Column(String, unique=True)
        model = Column(String)
        make = Column(String)
        seats = Column(Integer)
        ```
## Defining every config constant in .sh
- You should define these credentials in the file setup.sh and then import from there!