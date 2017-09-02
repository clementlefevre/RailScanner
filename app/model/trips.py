#!/usr/bin/python
# -*- coding: utf-8 -*-

from itertools import product


class Trips(object):
    def __init__(self, trip_list):
        self.legs = list()
        self.convert_to_single_trip(trip_list)

    def convert_to_single_trip(self, trip_list):
        for trip in trip_list:
            trips_outbound = list(
                product([trip['origin']], trip['destination']))

            trips_inbound = [tuple(reversed(t)) for t in trips_outbound]

            self.legs += trips_outbound + trips_inbound
