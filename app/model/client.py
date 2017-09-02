#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
from datetime import datetime, timedelta
from itertools import product
from random import shuffle
import logging

from app.service import sncf_routes

logger = logging.getLogger("scraper_sncf")


class Client(object):

    def __init__(self, trips_list, horizon=5):
        self.convert_to_single_trip(trips_list)
        self.set_segments()
        self.set_dates(horizon=horizon)
        self.schedules = pd.DataFrame()

    def set_dates(self,  horizon, dt_start=datetime.today().date().isoformat()):
        self.date_range = []
        dt_start = datetime.strptime(dt_start, '%Y-%m-%d')

        for delta in range(0, horizon):
            dt_string = dt_start + timedelta(days=delta)
            self.date_range.append(dt_string.isoformat())
        shuffle(self.date_range)

    def convert_to_single_trip(self, trip_list):
        self.legs = list()
        for trip in trip_list:
            trips_outbound = list(
                product([trip['origin']], trip['destination']))

            trips_inbound = [tuple(reversed(t)) for t in trips_outbound]

            self.legs += trips_outbound + trips_inbound

    def set_segments(self):
        self.segments = []
        for trip in self.legs:
            self.add_segment(trip[0], trip[1])
        shuffle(self.segments)

    def add_segment(self, departure, arrivals):
        new_segment = {'origin': departure, 'destination': arrivals}
        self.segments.append(new_segment)

    def drop_segment(self, drop_segment):
        pass

    def get_routes(self):

        for segment in self.segments:
            origin = segment['origin']
            destination = segment['destination']
            for dt in self.date_range:
                df_trip = sncf_routes.get_routes(origin, destination, dt)
                self.schedules = pd.concat([self.schedules, df_trip])
        self.save_to_db()

    def save_to_db(self):
        sncf_routes.save_to_db(self.schedules)

    def read_from_db(self):
        return sncf_routes.read_from_db()
