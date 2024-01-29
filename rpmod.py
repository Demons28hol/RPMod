# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: rpmod
# Author: hikariatama
# Commands:
# .rp      | .rptoggle | .rplist | .rpbackup | .rprestore
# .rpchats
# ---------------------------------------------------------------------------------

#             █ █ ▀ █▄▀ ▄▀█ █▀█ ▀
#             █▀█ █ █ █ █▀█ █▀▄ █
#              © Copyright 2022
#           https://t.me/hikariatama
#
# 🔒      Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# scope: hikka_min 1.2.10

# meta pic: https://img.icons8.com/color/480/000000/comedy.png
# meta banner: https://mods.hikariatama.ru/badges/rpmod.jpg
# meta developer: @hikarimods

import io
import json

import grapheme
from telethon.tl.types import Message
from telethon.utils import get_display_name

from .. import loader, utils


@loader.tds
class RPMod(loader.Module):
    """RPMod by HikariMods"""

    strings = {
        "name": "RPMod🖤",
        "args": "🚫 <b>Incorrect args</b>",
        "success": "✅ <b>Success</b>",
        "rp_on": "✅ <b>RPM on</b>",
        "rp_off": "✅ <b>RPM off</b>",
        "rplist": "<b>Current RP commands</b>\n\n{}",
        "backup_caption": (
            "<b>My RP commands. Restore with </b><code>.rprestore</code>"
        ),
        "no_file": "🚫 <b>Reply to file</b>",
        "restored": "✅ <b>RP Commands restored. See them with </b><code>.rplist</code>",
    }

    strings_ru = {
        "args": "🚫 <b>Неверные аргументы</b>",
        "success": "✅ <b>Успешно</b>",
        "rp_on": "✅ <b>RPM включен</b>",
        "rp_off": "✅ <b>RPM выключен</b>",
        "rplist": "<b>Текущие RP команды</b>\n\n{}",
        "backup_caption": (
            "<b>Мои RP команды. Ты можешь восстановить их используя"
            " </b><code>.rprestore</code>"
        ),
        "no_file": "🚫 <b>Ответь на файл</b>",
        "restored": (
            "✅ <b>RP команды восстановлены. Их можно посмотреть используя"
            " </b><code>.rplist</code>"
        ),
        "_cmd_doc_rp": (
            "<command> <message> - Добавить RP команду. Если не указано сообщение,"
            " команда будет удалена"
        ),
        "_cmd_doc_rptoggle": "Включить\\выключить RP режим в текущем чате",
        "_cmd_doc_rplist": "Показать RP команды",
        "_cmd_doc_rpbackup": "Сохранить RP команды в файл",
        "_cmd_doc_rprestore": "Восстановить RP команды из файла",
        "_cmd_doc_rpchats": "Показать чаты, где активен режим RP",
        "_cls_doc": "RPMod от HikariMods",
    }

    async def client_ready(self, client, db):
        self.rp = self.get(
            "rp",