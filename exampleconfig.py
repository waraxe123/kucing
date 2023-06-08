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
    STRING_SESSION = "1BVtsOGYBu1bTQMEuc6LpiChtFbpHjXeF6Ur5AjbTSuvl4FMqMpDdzDzB89-qjRysawpfQyM2m_fDVxRV1ZVcgjABsCeYQD7VPZB8EPUaW2VACXK5N4Ut8B0j1IPmKxn0x51KI7_hIcIxMyNoDgtcE0GQwMEZjI1uIFx8Bb4QyiB8ZTOG4urOuQLwJq_poxDHz5fbssfXkVdkgQnRyybiSf3TkYXuXh-ghzGwf4exPg5EpJd-kaGuLN5aid7WIQw5MVwgRa_uCYwe9c-O22IJKzpkS1G1Sz60C2hgQJCfNLMpnNiuJo9DMhOFwfMVkhXPfz9ccFq1Hk6csqhGeUEoU3IkM4CelxI="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6134002800:AAHgl7NzUqg97WHC8iY7dqfFUBTmU3Gn8cI"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001911043901
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
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
