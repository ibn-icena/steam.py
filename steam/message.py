# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright (c) 2020 James

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from typing import TYPE_CHECKING

from .abc import Messageable
from .enums import EChatEntryType

if TYPE_CHECKING:
    from .user import User
    from .protobufs.steammessages_friendmessages import (
        CFriendMessages_IncomingMessage_Notification as MessageNotification
    )

__all__ = (
    'Message',
)


class Message(Messageable):

    async def _get_channel(self):
        pass

    def __init__(self, proto: 'MessageNotification', author: 'User'):
        self.author = author
        self.content = proto.message
        self.created_at = proto.rtime32_server_timestamp
        self.type = EChatEntryType(proto.chat_entry_type)

    def __repr__(self):
        pass

    async def send(self, content: str):
        pass
