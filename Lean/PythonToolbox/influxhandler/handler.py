from os import environ as env
from influxdb import InfluxDBClient, exceptions


class InfluxHelper:

    def __init__(self, db_name=None):
        self.db_name = db_name
        try:
            self.dbclient = InfluxDBClient(host=env.get('INFLUX_HOST'), port=8086,
                                      username=env.get('INFLUX_USER'),
                                      password=env.get('INFLUX_PWD'))
            print("Connected to DB")

            if not db_name:
                env.get('INFLUX_DB')

            if db_name not in self.dbclient.get_list_database():
                # Create DB
                self.dbclient.create_database(db_name)
                self.dbclient.switch_database(db_name)

        except (exceptions.InfluxDBClientError, ConnectionError):
            print("Failed to connect to InfluxDB")

    def get_database_client(self):
        return self.dbclient
