import pandas as pd
from datetime import datetime, timedelta

from service import sncf_routes


class Client(object):

    def __init__(self):
        self.segments = []
        self.date_range = []
        self.trips = pd.DataFrame()

    def set_dates(self, dt_start, length):
        dt_start = datetime.strptime(dt_start, '%Y-%m-%d')
        print dt_start

        for delta in range(0, length):
            dt_string = dt_start + timedelta(days=delta)
            self.date_range.append(dt_string.isoformat())

    def add_segment(self, departure, arrivals):
        new_segment = {'origin': departure, 'destinations': arrivals}
        self.segments.append(new_segment)

    def drop_segment(self, drop_segment):
        pass

    def get_routes(self):

        for segment in self.segments:
            origin = segment['origin']

            for destination in segment['destinations']:
                for dt in self.date_range:

                    df_trip = sncf_routes.get_routes(origin, destination, dt)
                    self.trips = pd.concat([self.trips, df_trip])

    def save_to_db(self):
        sncf_routes.save_to_db(self.trips)

    def read_from_db(self):
        return sncf_routes.read_from_db()
