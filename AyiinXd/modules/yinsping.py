# Ayiin - Userbot
# NathXee
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

import time
from datetime import datetime
from secrets import choice


from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, StartTime
from AyiinXd import DEVS
from AyiinXd.events import register
from .ping import get_readable_time


absen = [
    "**𝗱𝘂𝗵𝗵 𝗸𝗮𝗴𝗲𝘁𝘁 𝘁𝗼𝗱 𝘀𝗸𝘀𝗸** 😁",
    "**𝗮𝗻𝗷𝗶𝗻𝗴 𝗱𝗮𝗱𝗮 𝗴𝘂𝗮 𝘀𝗮𝗸𝗶𝘁 𝘄𝗸𝘄𝗸** 😉",
    "**𝗱𝗼𝗿𝗿𝗿 𝗸𝗮𝗴𝗲𝘁𝘁𝘁 𝗮𝘄𝗼𝗸𝗮𝘄𝗼𝗸** 😁",
    "**𝗱𝘂𝗵 𝗸𝗮𝗴𝗲𝘁 𝗷𝗮𝗱𝗶 𝗮𝗻𝗴𝗲 𝘄𝗸𝘄𝗸** 🥵",
    "**𝗹𝗮𝗶𝗻𝗸𝗮𝗹𝗶 𝗷𝗴𝗻 𝗯𝗲𝗴𝗶𝘁𝘂 𝘆𝗮 𝗯𝗼𝘀𝘀𝗾𝘂𝗲** 😎",
    "**𝗮𝗮𝗮𝗮 𝗸𝗮𝗴𝗲𝘁𝘁𝘁** 🥺",
    "**𝗯 𝗮𝗷𝗮 𝗴𝗮 𝗸𝗮𝗴𝗲𝘁𝘁 𝘄𝗹𝗲𝗲** 😎",
]

nathcakep = [
    "**𝗶𝘆𝗮 𝗴𝗮𝗻𝘁𝗲𝗻𝗴 𝗯𝗮𝗻𝗴𝗲𝘁** 😍",
    "**𝗴𝗮𝗻𝘁𝗲𝗻𝗴𝗻𝘆𝗮 𝗴𝗮𝗮𝗱𝗮 𝗹𝗮𝘄𝗮𝗻** 😚",
    "**𝗴𝗮𝗻𝘁𝗲𝗻𝗴 𝗯𝗮𝗻𝗴𝗲𝘁 𝗴𝗮𝗱𝗮 𝗼𝗯𝗮𝘁𝘁** 😍",
    "**𝗶𝘆𝗮𝗮 𝗴𝗮𝗮𝗱𝗮 𝘀𝗮𝗶𝗻𝗴𝗮𝗻𝗻𝘆𝗮** 😎",
    "**𝗲𝗹𝗹 𝗷𝗮𝗺𝗲𝘁 𝗽𝗶 𝗯𝗼𝗼𝗻𝗴𝗴** 😚",
    "**𝗴𝗮𝗻𝘁𝗲𝗻𝗴 𝗯𝗴𝘁 𝗮𝗻𝗷𝗮𝘆𝘆𝘆** 🥵", 
]


@register(incoming=True, from_users=DEVS, pattern=r"^Pong$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    message = "**✯ 𝖓𝖆𝖙𝖍-𝖚𝖘𝖊𝖗𝖇𝖔𝖙 ✯**\n\n✯ **𝖕𝖎𝖓𝖌𝖊𝖗 :** `{} ms`\n✯ **𝖚𝖕𝖙𝖎𝖒𝖊 :** `{}`\n✯ **𝖔𝖜𝖓𝖊𝖗 :** `{}`\n✯ **𝖎𝖉 :** `{}`"
    await ping.reply(message.format(duration, uptime, user.first_name, user.id)
                     )


# KALO NGEFORK absen ini GA USAH DI HAPUS YA GOBLOK 😡
# JANGAN DI HAPUS GOBLOK 😡 LU COPY AJA TINGGAL TAMBAHIN
# DI HAPUS GUA GBAN YA 🥴 GUA TANDAIN LU AKUN TELENYA 😡

# Absen by : mrismanaziz <https://github.com/mrismanaziz/man-userbot>
# recode by : nathxe

@register(incoming=True, from_users=DEVS, pattern=r"^Duarr$")
async def nathabsen(ganteng):
    await ganteng.reply(choice(absen))


@register(incoming=True, from_users=DEVS, pattern=r"^Nath ganteng kan$")
async def nath(ganteng):
    await ganteng.reply(choice(nathcakep))


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "yinsping": f"**Plugin:** `yinsping`\
        \n\n  »  **Perintah : **`Perintah Ini Hanya Untuk Devs Nath-Userbot Tod.`\
        \n  »  **Kegunaan :** __Silahkan Ketik `{cmd}ping` Untuk Publik.__\
    "
    }
)
