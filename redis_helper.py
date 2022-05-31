import redis, pickle, os

#Redis Server URL for Local and Production
REDIS_SERVER_URL = {
    "localhost":"127.0.0.1",
    "prod":"prod-redis-engine"
    }

# This environment variable is set to "Local" and "Production"
REDIS_USER = os.environ.get("REDIS_USER") if os.environ.get("REDIS_USER") is not None \
    else "localhost"

# By default we use Redis db number 2 since this is for local
# Only if we have the environment varible set to "prod" we will use redis db number 1

redis_db_nbr: int = 2
if REDIS_USER == "prod":
    redis_db_nbr: int = 1

try:
    conn = redis.StrictRedis(host=REDIS_SERVER_URL[REDIS_USER], port=6379, db=redis_db_nbr)
except Exception as e:
    raise LookupError("Redis set Error: {}".format(e))

#Function to set the key with value(Create Key)
def set_redis(key, value):
    try:
        pickle_data = pickle.dumps(value)
        conn.set(key.lower(), pickle_data)
    except Exception as e:
        raise LookupError("Redis Error: {}".format(e))

#Function to get redis value
def get_redis(key):
    try:
        if conn.get(key.lower()) is None:
            raise LookupError("{} Key is not exist in Redis".format(key))
        else:
            return_data = pickle.loads(conn.get(key.lower()))
            return return_data
    except Exception as e:
        raise LookupError("Redis Error: {}".format(e))

#Function to delete the value from redis
def del_redis(key):
    try:
        if conn.get(key.lower()) is None:
            raise LookupError("{} Key is not exist in Redis".format(key))
        else:
            conn.delete(key.lower())
            return True
    except Exception as e:
        raise LookupError("Redis Error: {}".format(e))

#Function to get the keys or values from redis
def get_all_keys(value):
    if value.upper() == "USERS":
        master_users_list = []
        for key in conn.keys():
            master_users_list.append(key.decode("UTF-8"))
        if len(master_users_list) > 0:
            return master_users_list
        else:
            raise LookupError("No Keys Stored in Redis")
    elif value.upper() == "MESSAGES":
        master_messages_list = []
        for key in conn.keys():
            message = ""
            messagestring = conn[key].decode("UTF-8", "ignore")
            for string in messagestring:
                if (string.isalpha()) or (string.isdigit()):
                    message = message + string
            master_messages_list.append(message)
        if len(master_messages_list) > 0:
            return master_messages_list
        else:
            raise LookupError("No Keys Stored in Redis")
    elif value.upper() == "ALL":
        master_list = {}
        for key in conn.keys():
            message = ""
            messagestring = conn[key].decode("UTF-8", "ignore")
            for string in messagestring:
                if (string.isalpha()) or (string.isdigit()):
                    message = message + string
                master_list[key.decode("UTF-8")] = message
        if len(master_list) > 0:
            return master_list
        else:
            raise LookupError("No Keys Stored in Redis")
