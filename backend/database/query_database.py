import sqlite3
from flask.helpers import url_for

COUNTRY_LIST = [
    ('INDONESIA','MEDAN',1),
    ('INDONESIA','JAKARTA',1),
    ('JAPAN','TOKYO',1),
    ('SINGAPORE','CHANGI',1),
    ('ENGLAND','LONDON',1),
    ('SOUTH KOREA','SEOUL',1),
    ('CHINA','BEIJING',0),
    ('AUSTRALIA','MELBOURNE',1),
    ('SWITZERLAND','ZURICH',1)
]

def create_table():
    sql_table = sqlite3.connect('flight_list.db')
    sql_table.execute("""
CREATE TABLE CountryList(
    CountryId int NOT NULL,
    CountyName VARCHAR(255) NOT NULL,
    CityName VARCHAR(255) NOT NULL,
    AllowedFlight BIT NOT NULL
);
        """)
    sql_table.execute("""
    CREATE TABLE FlightList(
    flightId int NOT NULL UNIQUE,
    airlineName VARCHAR(255) NOT NULL,
    destinationFrom int NOT NULL,
    destinationTo int Not NULL,
    seatType VARCHAR(255) NOT NULL,
    departureDate date NOT NULL,
    returnDate date NOT NULL,
    PRIMARY KEY (flightId),
    FOREIGN KEY (destinationFrom) REFERENCES country(countryId),
    FOREIGN KEY (destinationTo) REFERENCES country(countryId)
);
    """)
    return sql_table

def insert_table(sql_table):
    country_id = 1
    for country in COUNTRY_LIST:
        sql_table.execute(
        f"""
            INSERT INTO country_list(countryId,countyName,cityName,allowedFlight)
            VALUES ({country_id,country[0],country[1],country[2]});
        """
        )
        country_id += 1
    return sql_table