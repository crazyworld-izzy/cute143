#
# Copyright (C) 2024 by TheTeamVivek@Github, < https://github.com/TheTeamVivek >.
#
# This file is part of < https://github.com/TheTeamVivek/YukkiMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TheTeamVivek/YukkiMusic/blob/master/LICENSE >
#
# All rights reserved.
#

import sys
from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import BotCommand
import config

from ..logging import LOGGER

self.app2 = Client(
    "YukkiMusic",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN2,
)

class YukkiBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot")
        super().__init__(
            "YukkiMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )
        self.two = app2

    async def start(self):

        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.mention = self.me.mention

        try:
            await self.send_message(
                config.LOG_GROUP_ID,
                text=f"<u><b>{self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b><u>\n\nɪᴅ : <code>{self.id}</code>\nɴᴀᴍᴇ : {self.name}\nᴜsᴇʀɴᴀᴍᴇ : @{self.username}",
            )
        except:
            LOGGER(__name__).error(
                "Bot has failed to access the log Group. Make sure that you have added your bot to your log channel and promoted as admin!"
            )
            sys.exit()
        if config.SET_CMDS:
            try:
                await self.set_bot_commands(
                    [
                        BotCommand("help", "ɢᴇᴛ ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ"),
                        BotCommand("ping", "ᴄʜᴇᴄᴋ ʙᴏᴛ ɪs ᴀʟɪᴠᴇ ᴏʀ ᴅᴇᴀᴅ"),
                        BotCommand("play", "sᴛᴀʀᴛ ᴘʟᴀʏɪɴɢ ʀᴇǫᴜᴇᴛᴇᴅ sᴏɴɢ"),
                        BotCommand("skip", "ᴍᴏᴠᴇ ᴛᴏ ɴᴇxᴛ ᴛʀᴀᴄᴋ ɪɴ ǫᴜᴇᴜᴇ"),
                        BotCommand("pause", "ᴘʟᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ sᴏɴɢ"),
                        BotCommand("resume", "ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴘᴀᴜsᴇᴅ sᴏɴɢ"),
                        BotCommand("end", "ᴄʟᴇᴀʀ ᴛʜᴇ ǫᴜᴇᴜᴇ ᴀᴍᴅ ʟᴇᴀᴠᴇ ᴠᴏɪᴄᴇᴄʜᴀᴛ"),
                        BotCommand("shuffle", "Rᴀɴᴅᴏᴍʟʏ sʜᴜғғʟᴇs ᴛʜᴇ ǫᴜᴇᴜᴇᴅ ᴘʟᴀʏʟɪsᴛ."),
                        BotCommand(
                            "playmode",
                            "Aʟʟᴏᴡs ʏᴏᴜ ᴛᴏ ᴄʜᴀɴɢᴇ ᴛʜᴇ ᴅᴇғᴀᴜʟᴛ ᴘʟᴀʏᴍᴏᴅᴇ ғᴏʀ ʏᴏᴜʀ ᴄʜᴀᴛ",
                        ),
                        BotCommand(
                            "settings",
                            "Oᴘᴇɴ ᴛʜᴇ sᴇᴛᴛɪɴɢs ᴏғ ᴛʜᴇ ᴍᴜsɪᴄ ʙᴏᴛ ғᴏʀ ʏᴏᴜʀ ᴄʜᴀᴛ.",
                        ),
                    ]
                )
            except:
                pass
        else:
            pass
        try:
            a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
            if a.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER(__name__).error("Please promote Bot as Admin in Logger Group")
                sys.exit()
        except Exception:
            pass
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"MusicBot Started as {self.name}")


        if config.BOT_TOKEN2:
            await self.two.start()
            get_me = await self.two.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            self.one.name = get_me.first_name + " " + (get_me.last_name or "")
            self.one.mention = get_me.mention

            try:
                await self.one.send_message(
                    config.LOG_GROUP_ID,
                    text=f"<u><b>{self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b><u>\n\nɪᴅ : <code>{self.id}</code>\nɴᴀᴍᴇ : {self.name}\nᴜsᴇʀɴᴀᴍᴇ : @{self.username}",
                )
            except:
                LOGGER(__name__).error(
                "Bot2 has failed to access the log Group. Make sure that you have added your bot to your log channel and promoted as admin!"
                )
                sys.exit()
            if config.SET_CMDS:
                try:
                    await self.set_bot_commands(
                    [
                        BotCommand("help", "ɢᴇᴛ ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ"),
                        BotCommand("ping", "ᴄʜᴇᴄᴋ ʙᴏᴛ ɪs ᴀʟɪᴠᴇ ᴏʀ ᴅᴇᴀᴅ"),
                        BotCommand("play", "sᴛᴀʀᴛ ᴘʟᴀʏɪɴɢ ʀᴇǫᴜᴇᴛᴇᴅ sᴏɴɢ"),
                        BotCommand("skip", "ᴍᴏᴠᴇ ᴛᴏ ɴᴇxᴛ ᴛʀᴀᴄᴋ ɪɴ ǫᴜᴇᴜᴇ"),
                        BotCommand("pause", "ᴘʟᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ sᴏɴɢ"),
                        BotCommand("resume", "ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴘᴀᴜsᴇᴅ sᴏɴɢ"),
                        BotCommand("end", "ᴄʟᴇᴀʀ ᴛʜᴇ ǫᴜᴇᴜᴇ ᴀᴍᴅ ʟᴇᴀᴠᴇ ᴠᴏɪᴄᴇᴄʜᴀᴛ"),
                        BotCommand("shuffle", "Rᴀɴᴅᴏᴍʟʏ sʜᴜғғʟᴇs ᴛʜᴇ ǫᴜᴇᴜᴇᴅ ᴘʟᴀʏʟɪsᴛ."),
                        BotCommand(
                            "playmode",
                            "Aʟʟᴏᴡs ʏᴏᴜ ᴛᴏ ᴄʜᴀɴɢᴇ ᴛʜᴇ ᴅᴇғᴀᴜʟᴛ ᴘʟᴀʏᴍᴏᴅᴇ ғᴏʀ ʏᴏᴜʀ ᴄʜᴀᴛ",
                        ),
                        BotCommand(
                            "settings",
                            "Oᴘᴇɴ ᴛʜᴇ sᴇᴛᴛɪɴɢs ᴏғ ᴛʜᴇ ᴍᴜsɪᴄ ʙᴏᴛ ғᴏʀ ʏᴏᴜʀ ᴄʜᴀᴛ.",
                        ),
                        ]
                    )
                except:
                    pass
            else:
                pass
            try:
                a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
                if a.status != ChatMemberStatus.ADMINISTRATOR:
                     LOGGER(__name__).error("Please promote Bot2 as Admin in Logger Group")
                    sys.exit()
            except Exception:
                pass
            if get_me.last_name:
                self.one.name = get_me.first_name + " " + get_me.last_name
            else:
                self.one.name = get_me.first_name
            LOGGER(__name__).info(f"MusicBot Started as {self.one.name}")
