from enum import Enum

from plenum.common.transactions import PlenumTransactions


class SovrinTransactions(Enum):
    #  These numeric constants CANNOT be changed once they have been used,
    #  because that would break backwards compatibility with the ledger
    #  Also the numeric constants CANNOT collide with transactions in plenum
    NODE = PlenumTransactions.NODE.value
    NYM = PlenumTransactions.NYM.value
    ATTRIB = "100"
    SCHEMA = "101"
    ISSUER_KEY = "102"

    DISCLO = "103"
    GET_ATTR = "104"
    GET_NYM = "105"
    GET_TXNS = "106"
    GET_SCHEMA = "107"
    GET_ISSUER_KEY = "108"

    POOL_UPGRADE = "109"
    NODE_UPGRADE = "110"

    def __str__(self):
        return self.name
