DASHBOARD_LOG_FILENAME = "dashboard.log"
DASHBOARD_AGENT_PORT_PREFIX = "DASHBOARD_AGENT_PORT_PREFIX:"
DASHBOARD_AGENT_LOG_FILENAME = "dashboard_agent.log"
DASHBOARD_AGENT_CHECK_PARENT_INTERVAL_SECONDS = 2
MAX_COUNT_OF_GCS_RPC_ERROR = 10
RETRY_REDIS_CONNECTION_TIMES = 10
UPDATE_NODES_INTERVAL_SECONDS = 5
CONNECT_GCS_INTERVAL_SECONDS = 2
CONNECT_REDIS_INTERNAL_SECONDS = 2
PURGE_DATA_INTERVAL_SECONDS = 60 * 10
ORGANIZE_DATA_INTERVAL_SECONDS = 2
REDIS_KEY_DASHBOARD = "dashboard"
REDIS_KEY_DASHBOARD_RPC = "dashboard_rpc"
REDIS_KEY_GCS_SERVER_ADDRESS = "GcsServerAddress"
REPORT_METRICS_TIMEOUT_SECONDS = 2
REPORT_METRICS_INTERVAL_SECONDS = 10
# aiohttp_cache
AIOHTTP_CACHE_TTL_SECONDS = 2
AIOHTTP_CACHE_MAX_SIZE = 128
AIOHTTP_CACHE_DISABLE_ENVIRONMENT_KEY = "RAY_DASHBOARD_NO_CACHE"
# Named signals
SIGNAL_NODE_INFO_FETCHED = "node_info_fetched"
SIGNAL_NODE_SUMMARY_FETCHED = "node_summary_fetched"
SIGNAL_WORKER_INFO_FETCHED = "worker_info_fetched"
# Default value for datacenter (the default value in protobuf)
DEFAULT_LANGUAGE = "PYTHON"
DEFAULT_JOB_ID = "ffff"