""""
    █▀▄▀█ █▀█ █▀█ █ █▀ █ █ █▀▄▀█ █▀▄▀█ █▀▀ █▀█
    █ ▀ █ █▄█ █▀▄ █ ▄█ █▄█ █ ▀ █ █ ▀ █ ██▄ █▀▄
    Copyright 2022 t.me/morisummerzxc
    Licensed under the Apache License, Version 2.0
"""
# requires: qrcode[pil]
import qrcode
from .. import loader, utils
from telethon.tl.types import *
import logging

logger = logging.getLogger(__name__)


@loader.tds
class QRMod(loader.Module):
    """QR code generator"""
    strings = {"name": "QR"}

    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client

    async def qrcmd(self, message: Message) -> None:
        """Generate QR code"""
        text = utils.get_args_raw(message)
        img = qrcode.make(text)
        await self.client.send_file(message.peer_id, img, caption='')