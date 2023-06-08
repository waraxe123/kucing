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
    STRING_SESSION = "1BVtsOGYBuxind1tUesbWyz9YjzAsiNxU4HvcWb9eqkCo4X-quCF77Yeu-mUXURDYd6RMv-Pd8FBXGRbjIh6_eMBDuTNyKp8KHiV9r4iwQDH7paLT2WqcFSKQIfx_E76CdsvOcWmbFPWUxOf5Ns02BSz8T68kRYUbgyswk83f4PmuBcW6wWPdy-wBmRw9UAUFm81YcoLLix7FIoToGuspd0JQPevZwDBVoxgz4syw1jiDbOfSoeZXgYsJfmtAcunP4IYCXeoUbvK-N42H_Rv_1G_4IG-4DOCR_aKtKfKIuByOvlvj3p5-RuXqrf8leKxKdjcTBAYr2WfGBggk8eT7xijDItIcLwU="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6033555992:AAEdWmWv5ZiSXNQrjTBNHHtI0WWiTA-gf0A"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001911043901
    # command handler
    COMMAND_HAND_LER = "!"
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "!"
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/waraxe123/plugin"
    # if you need badcat plugins set "True"
    BADCAT = "True"
    #Upstream repo
    UPSTREAM_REPO = "https://github.com/waraxe123/kucing"
    #montet
    OPENAI_API_KEY = "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"
    #jsjs
    PRIVATE_GROUP_ID = -1001911043901
    #sjsjjsjs
    FBAN_GROUP_ID = -1001911043901
    #sjsjjs
    PRIVATE_CHANNEL_BOT_API_ID = -1001911043901
    #sjsj
    PM_LOGGER_GROUP_ID = -1001911043901