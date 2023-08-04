from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "23489701"))
API_HASH = getenv("API_HASH", "c4360edb704539385d1f2df16442887c")

BOT_TOKEN = getenv("BOT_TOKEN", "5528571909:AAGGv3tO-bO0dkFBoo_6XvV-z369UBhIVxw")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "5497627952"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/17c1edac7a039a4fd3b07.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/17c1edac7a039a4fd3b07.jpg")

SESSION = getenv("SESSION", "BQBhfltOkwqAH3ZYe05114WWuwC02o41Xi5S48QV1aOyoRFVr5cSwDHj1Hk2vs9ibfuvdDDjZY0h-UmrjLpqDqWLMt8GgYzTMNer-TVrlxsfqqSMI_vnGvlhkQ6XHR5cCchEnY8x716pbNUs1MsusQFeRU3Ri_wjN3y74AXdjJoe2TxWb25F-K7jK-s1pYU0LGSA4SxhXJU71mUzL_E5syTluJG8DOHNTI6xQlDiM1K_FLW6tEuJ1hr0MpOSuJv0V4dkVLWqW0-QFZrblpSl_eCVj7M3_gL1EXwWOpdH4_d8dyhZ1m_Iyh40r21PDMHlEezGz50UmqaqI0MJEyTOJ9ewAAAAAWCeANoA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Elisha_support")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/denvil_bots")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/17c1edac7a039a4fd3b07.jpg"
