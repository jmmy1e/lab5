"""Contact class for the Rolodex program"""

class Contact:
    """Represents one Rolodex entry.

    Attributes:
        fn (str): first name
        ln (str): last name
        ph (str): phone number
        addr (str): street address
        city (str): city
        zip (str): zip code
    """

    def __init__(self, fn, ln, ph, addr, city, zip):
        """Stores basic fields as strings"""
        self.fn = fn
        self.ln = ln
        self.ph = ph
        self.addr = addr
        self.city = city
        self.zip = zip


    def __lt__(self, other):
        """Sort by last name, then first name"""
        if self.ln != other.ln:
            return self.ln < other.ln
        return self.fn < other.fn

    def __str__(self):
        """Readable display for the console"""
        return f"{self.fn} {self.ln}\n{self.ph}\n{self.addr}\n{self.city} {self.zip}"

    def __repr__(self):
        """CSV format for file"""
        return f"{self.fn},{self.ln},{self.ph},{self.addr},{self.city},{self.zip}"