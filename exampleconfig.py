from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 28785136
    API_HASH = "3435ed2cfee6ed694f365cabf2cfa559"
    # the name to display in your alive message
    ALIVE_NAME = "markdown"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgresql://postgres:roip@localhost:5432/catuserbot"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOGYBu6rrPW4SA0aX5dmJroFhIi7ple3b2ZUr2MI7frnpQsqLykgks3EZ_Sinxev2yuIGTOA5nVucrUCI76hD0JRf27VOLAkYlhDHwijWAKN-vs3qhKpAe3MD7q45cb8dbrKheQ0O1x9n-1mwpBTKMEqiykmq9-jhEhYIjOn8h3QCTjNPxoCaglicKVDm4f7hxC1Z1mooHlI4qqnr1hgWhJQ3lkXxptCOItnGqmC5zHArqs8aBsbJmU2i4giJAUXi3sZS5jIPI79Depzix9Yw5EVrQgxrcM9IqVOFNw1Ci2LgjQ2zUD5iAgeb0WUCi3pUIQwXVgnqeUBainMLy2EN2oDUHwU="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6033555992:AAFk8Dp0Rqfa3n4__Nb7wi3rJtRRfIwltjw"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001911043901
    # command handler
    COMMAND_HAND_LER = "!"
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "!"
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
    #Upstream repo
    UPSTREAM_REPO = "https://github.com/waraxe123/kucing"
    #montet
    OPENAI_API_KEY = ""
    #jsjs
    PRIVATE_GROUP_ID = -1001911043901
    #sjsjjsjs
    FBAN_GROUP_ID = -1001911043901
    #sjsjjs
    PRIVATE_CHANNEL_BOT_API_ID = -1001911043901
    #sjhs
    OWNER_ID = "2079755654"
    #sjsj
    PM_LOGGER_GROUP_ID = -1001911043901
