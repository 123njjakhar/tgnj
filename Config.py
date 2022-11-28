import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "15217822"))
    API_HASH = os.environ.get("API_HASH", "01224df6690e9f10fd85819cb1ef6f21")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5677591277:AAFiNzR8P4l_h3Tyr941LGI1jUeGF2Mf1MY")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKIBu0pBb64ULsdVk-QxDbL2UaUxg2jQTje-_8ITZ6juo7sJ7AUqG5Gn5iLp-yAQ3l1o_46Fusn9bh_eBudQIzXIeQ4fbs9Op2nLHa8DnXOmJpK53zX2PZSuwxqjZwNzYYNW6zqGAR1vtwVyufPoR8IfZyh-l8Fs0OPsPkqiBqw0RayHqjDnmqiH0MvAUZs9xmMbWp80O8AVGpFVh3I6Th7nhZpZ6YBOQMlIqPKeUb2Wou1WAqrKwq_AEE4WiyRQh2cFoewmZfP5PYWicyygHBGnibU6A4WX5C2akBiAco_1A9f8MImjIsB3EK_6EUqIk7eiJT5ppMXtKKcgyqD6QSZMXH8=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "OP_NJ_MUSIC_BOT")
    SUPPORT = os.environ.get("SUPPORT", "ROMEOBOT_op") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "ROMEOBOT_OP") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/261b8f5dc24de55be9bdd.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/261b8f5dc24de55be9bdd.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "1651260016")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
