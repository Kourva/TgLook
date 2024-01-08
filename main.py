#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standard library import
import json
import tempfile
from typing import Dict, ClassVar, Any, NoReturn

# Related third party imports
from telethon import TelegramClient, events
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.messages import GetDialogsRequest, ReportSpamRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.contacts import ResolveUsernameRequest

# Get account credential
try:
    with open("credential.json", "r") as data:
        credits: Dict[str, int] = json.load(data)

except FileNotFoundError:
    raise SystemExit(":: No credential file found!")


# initialize client
client: ClassVar[Any] = TelegramClient(
    session="testApp", 
    api_id=credits["api-ID"], 
    api_hash=credits["api-Hash"]
)


# Event handler for new incoming messages
@client.on(events.NewMessage(incoming=True, func=lambda x: x.is_private))
async def incoming_message_handler(event: ClassVar[Any]) -> NoReturn:
    """
    Async function to handle incoming messages in private chat
    Used to handle commands coming from users

    Parameters:
        event: Update event from telegram

    Returns:
        None (typing.NoReturn)
    """
    # Fetch incoming message text and chat id
    incoming_message: str = event.message.message
    message_chat_id: int = event.chat_id

    # Get all conversations in account
    conversations: ClassVar[Any] = await client(
        GetDialogsRequest(
            offset_date=None,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=50,
            hash=0
        )
    )

    # Extract groups out of conversation
    groups: List[ClassVar[Any]] = []
    for chat in conversations.chats:
        try:
            groups.append(chat) if chat.megagroup else None
        except:
            pass

    try:

        # Handle $chats command to get conversation
        if incoming_message.startswith("$chats"):
            # Index and list groups in text
            groups_message: str = "".join(
                [f"┆ Idx{index}: {group.title}\n" for index, group in enumerate(groups)]
            )

            # Send message to user which contains list of groups
            async with client.action(event.chat_id, 'typing'):
                await client.send_message(
                    entity=message_chat_id,
                    message=(
                        "×͜× Please choose group to get member from it:\n\n"
                        f"{groups_message}\n\n⁀➴ Send $get [index] to get members.\nE.G. $get 0"
                    ),
                    reply_to=event.message,
                    link_preview=False
                )

            # Seen the message and mark it as read
            await client.send_read_acknowledge(
                entity=message_chat_id,
                message=event.message
            )

        # Handle $get command to get list of members from specific chat
        elif incoming_message.startswith("$get"):
            # Get index of chat from message text
            index: int = min(int(incoming_message.split()[1].strip()), len(groups))
            target_group: ClassVar[Any] = groups[index]

            # Open temporary file in /tmp
            with tempfile.TemporaryFile(mode="w+b") as tf:
                # Write first row for CSV data
                tf.write((
                    "chat_id,first_name,last_name,username,phone,access_hash,group_title,group_id\n"
                    ).encode("utf-8")
                )

                # Iterate through group members and scrape information and add to database
                async for member in client.iter_participants(target_group, aggressive=True):
                    tf.write((
                        f"{member.id},"
                        f"{member.first_name},"
                        f"{member.last_name},"
                        f"{member.username},"
                        f"{member.phone},"
                        f"{member.access_hash},"
                        f"{target_group.title},"
                        f"{target_group.id}\n"
                        ).encode("utf-8")
                    )

                # Send the database as document to user
                tf.seek(0)
                async with client.action(message_chat_id, 'document'):
                    await client.send_file(
                        entity=message_chat_id,
                        file=tf.read(),
                        force_document=True,
                        caption=f"⁀➴ {target_group.title}\n★ ID: {target_group.id}\nᯤ Data format: CSV",
                        reply_to=event.message,
                        link_preview=False
                    )

            # Seen the message and mark it as read
            await client.send_read_acknowledge(
                entity=message_chat_id,
                message=event.message
            )

        # Handle $whois command to get information for member
        elif incoming_message.startswith("$whois"):
            # Get target's username
            target: str = incoming_message.split()[1]
            target_info: ClassVar[Any] = await client(
                GetFullUserRequest(id=target)
            )

            # Send user information
            async with client.action(event.chat_id, 'typing'):
                await client.send_message(
                    entity=message_chat_id,
                    message=(
                        "×͜× Who IS Lookup\n"
                        f"┆ Chat-ID: {target_info.users[0].id}\n"
                        f"┆ Access Hash: {target_info.users[0].access_hash}\n"
                        f"┆ First Name: {target_info.users[0].first_name}\n"
                        f"┆ Last Name: {target_info.users[0].last_name}\n"
                        f"┆ Username: {target_info.users[0].username}\n\n"
                        f"𖣠 Account status\n"
                        f"┆ Is restricted: {target_info.users[0].restricted}\n"
                        f"┆ Is scam: {target_info.users[0].scam}\n"
                        f"┆ Is fake: {target_info.users[0].fake}\n"
                        f"┆ Is bot: {target_info.users[0].bot}\n"
                        f"┆ Is self: {target_info.users[0].is_self}\n"
                        f"┆ Is premium: {target_info.users[0].premium}\n\n"
                        f"⊹ Bio\n{target_info.full_user.about}\n\n"
                        f"ᨒ Restriction Reason:\n{target_info.users[0].restriction_reason}\n"
                    ),
                    reply_to=event.message,
                    link_preview=False
                )

            # Seen the message and mark it as read
            await client.send_read_acknowledge(
                entity=message_chat_id,
                message=event.message
            )

        # Handle $username command to get checking username availability
        elif incoming_message.startswith("$username"):
            try:
                # Get target's username
                target: str = incoming_message.split()[1]
                target_info: ClassVar[Any] = await client(
                    ResolveUsernameRequest(
                        username=target
                ))
                # Send username information
                async with client.action(event.chat_id, 'typing'):
                    await client.send_message(
                        entity=message_chat_id,
                        message=(
                            "×͜× Username Checker\n\n"
                            f"┆ Username: t.me/{target}\n"
                            f"┆ Available: Taken"
                        ),
                        reply_to=event.message,
                        link_preview=False
                    )
        
            # Handle username check exception
            except Exception as ex:
                if "The username is not in use by anyone else yet" in str(ex):
                    async with client.action(event.chat_id, 'typing'):
                        await client.send_message(
                            entity=message_chat_id,
                            message=(
                                "×͜× Username Checker\n"
                                f"┆ Username: t.me/{target}\n"
                                f"┆ Available: Available"
                            ),
                            reply_to=event.message,
                            link_preview=False
                        )
                else:
                    async with client.action(event.chat_id, 'typing'):
                        await client.send_message(
                            entity=message_chat_id,
                            message=(
                                "×͜× Username Checker\n"
                                f"┆ Username: t.me/{target}\n"
                                f"┆ Available: Not Valid or Banned"
                            ),
                            reply_to=event.message,
                            link_preview=False
                        )

            finally:
                # Seen the message and mark it as read
                await client.send_read_acknowledge(
                    entity=message_chat_id,
                    message=event.message
                )

    except IndexError:
        # Send failure message to user
        async with client.action(event.chat_id, 'typing'):
            await client.send_message(
                entity=message_chat_id,
                message="𓆏 Please Use valid index!\nThis usually causes when you enter invalid index or use command without argument",
                reply_to=event.message,
                link_preview=False
            )

        # Seen the message and mark it as read
        await client.send_read_acknowledge(
            entity=message_chat_id,
            message=event.message
        )

    except ValueError:
        # Send failure message to user
        async with client.action(event.chat_id, 'typing'):
            await client.send_message(
                entity=message_chat_id,
                message="𓆏 Please Use valid username!",
                reply_to=event.message,
                link_preview=False
            )

        # Seen the message and mark it as read
        await client.send_read_acknowledge(
            entity=message_chat_id,
            message=event.message
        )

    except UnboundLocalError:
         # Send failure message to user
        async with client.action(event.chat_id, 'typing'):
            await client.send_message(
                entity=message_chat_id,
                message="𓆏 Please Use valid argument!",
                reply_to=event.message,
                link_preview=False
            )

        # Seen the message and mark it as read
        await client.send_read_acknowledge(
            entity=message_chat_id,
            message=event.message
        )

# Run the bot
with client:
    print(":: Self is running... [Ctrl+C to break]")
    client.run_until_disconnected()
