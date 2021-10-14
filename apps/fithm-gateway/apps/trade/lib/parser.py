from flask_restx import reqparse
from flask import Request


class TradeParser():

    def __init__(self):
        self.update = None
        self.instructions = None
        self.update_portfolios = None
        self.update_positions = None
        self.update_prices = None


    def parse_update(self, req: Request) -> dict:
        if not self.update:
            self.update = reqparse.RequestParser()
            self.update.add_argument('status', type=bool, required=True, location='json')

        return self.update.parse_args(req)


    def parse_instructions(self, req: Request) -> dict:
        if not self.instructions:
            self.instructions = reqparse.RequestParser()
            self.instructions.add_argument('portfolio', type=dict, required=True, location='json')

        return self.instructions.parse_args(req)


    def parse_update_portfolios(self, req: Request) -> dict:
        if not self.update_portfolios:
            self.update_portfolios = reqparse.RequestParser()
            self.update_portfolios.add_argument('portfolios', type=list, required=True, location='json')

        return self.update_portfolios.parse_args(req)


    def parse_update_positions(self, req: Request) -> dict:
        if not self.update_positions:
            self.update_positions = reqparse.RequestParser()
            self.update_positions.add_argument('positions', type=list, required=True, location='json')

        return self.update_positions.parse_args(req)


    def parse_update_prices(self, req: Request) -> dict:
        if not self.update_prices:
            self.update_prices = reqparse.RequestParser()
            self.update_prices.add_argument('prices', type=list, required=True, location='json')

        return self.update_prices.parse_args(req)


    
