ETH_DAO_FORK_TS = 1469020840  # 2016-07-20 13:20:40 UTC
BTC_BCH_FORK_TS = 1501593374  # 2017-08-01 13:16:14 UTC
BCH_BSV_FORK_TS = 1542304352  # 2018-11-15 18:52:00 UTC

ROTKEHLCHEN_SERVER_TIMEOUT = 5
GLOBAL_REQUESTS_TIMEOUT = 5  # perhaps consolidate this and the one above?

DAY_IN_SECONDS = 24 * 3600
WEEK_IN_SECONDS = DAY_IN_SECONDS * 7
MONTH_IN_SECONDS = WEEK_IN_SECONDS * 4
YEAR_IN_SECONDS = 31536000  # 60 * 60 * 24 * 365

# For queries that are attempted multiple times:
# How many times to retry an external query before giving up
QUERY_RETRY_TIMES = 5

# Seconds for which cached api queries will be cached
# By default 10 minutes.
# TODO: Make configurable!
CACHE_RESPONSE_FOR_SECS = 600

DEFAULT_CONNECT_TIMEOUT = 5
DEFAULT_READ_TIMEOUT = 30
DEFAULT_TIMEOUT_TUPLE = (DEFAULT_CONNECT_TIMEOUT, DEFAULT_READ_TIMEOUT)

# Multiplier for query limits
QUERY_LIMIT_MULTIPLIER = 5
