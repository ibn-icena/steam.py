# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: steammessages_clientserver_friends.proto
# plugin: python-betterproto
# Last updated 09/09/2021

from dataclasses import dataclass

import betterproto


@dataclass(eq=False, repr=False)
class CMsgClientFriendMsg(betterproto.Message):
    steamid: int = betterproto.fixed64_field(1)
    chat_entry_type: int = betterproto.int32_field(2)
    message: bytes = betterproto.bytes_field(3)
    rtime32_server_timestamp: int = betterproto.fixed32_field(4)
    echo_to_sender: bool = betterproto.bool_field(5)


@dataclass(eq=False, repr=False)
class CMsgClientFriendMsgIncoming(betterproto.Message):
    steamid_from: int = betterproto.fixed64_field(1)
    chat_entry_type: int = betterproto.int32_field(2)
    from_limited_account: bool = betterproto.bool_field(3)
    message: bytes = betterproto.bytes_field(4)
    rtime32_server_timestamp: int = betterproto.fixed32_field(5)


@dataclass(eq=False, repr=False)
class CMsgClientAddFriend(betterproto.Message):
    steamid_to_add: int = betterproto.fixed64_field(1)
    accountname_or_email_to_add: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class CMsgClientAddFriendResponse(betterproto.Message):
    eresult: int = betterproto.int32_field(1)
    steam_id_added: int = betterproto.fixed64_field(2)
    persona_name_added: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class CMsgClientRemoveFriend(betterproto.Message):
    friendid: int = betterproto.fixed64_field(1)


@dataclass(eq=False, repr=False)
class CMsgClientHideFriend(betterproto.Message):
    friendid: int = betterproto.fixed64_field(1)
    hide: bool = betterproto.bool_field(2)


@dataclass(eq=False, repr=False)
class CMsgClientFriendsList(betterproto.Message):
    bincremental: bool = betterproto.bool_field(1)
    friends: "list[CMsgClientFriendsListFriend]" = betterproto.message_field(2)
    max_friend_count: int = betterproto.uint32_field(3)
    active_friend_count: int = betterproto.uint32_field(4)
    friends_limit_hit: bool = betterproto.bool_field(5)


@dataclass(eq=False, repr=False)
class CMsgClientFriendsListFriend(betterproto.Message):
    ulfriendid: int = betterproto.fixed64_field(1)
    efriendrelationship: int = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class CMsgClientFriendsGroupsList(betterproto.Message):
    bremoval: bool = betterproto.bool_field(1)
    bincremental: bool = betterproto.bool_field(2)
    friend_groups: "list[CMsgClientFriendsGroupsListFriendGroup]" = betterproto.message_field(3)
    memberships: "list[CMsgClientFriendsGroupsListFriendGroupsMembership]" = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class CMsgClientFriendsGroupsListFriendGroup(betterproto.Message):
    n_group_id: int = betterproto.int32_field(1)
    str_group_name: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class CMsgClientFriendsGroupsListFriendGroupsMembership(betterproto.Message):
    ul_steam_id: int = betterproto.fixed64_field(1)
    n_group_id: int = betterproto.int32_field(2)


@dataclass(eq=False, repr=False)
class CMsgClientPlayerNicknameList(betterproto.Message):
    removal: bool = betterproto.bool_field(1)
    incremental: bool = betterproto.bool_field(2)
    nicknames: "list[CMsgClientPlayerNicknameListPlayerNickname]" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class CMsgClientPlayerNicknameListPlayerNickname(betterproto.Message):
    steamid: int = betterproto.fixed64_field(1)
    nickname: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class CMsgClientSetPlayerNickname(betterproto.Message):
    steamid: int = betterproto.fixed64_field(1)
    nickname: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class CMsgClientSetPlayerNicknameResponse(betterproto.Message):
    eresult: int = betterproto.uint32_field(1)


@dataclass(eq=False, repr=False)
class CMsgClientRequestFriendData(betterproto.Message):
    persona_state_requested: int = betterproto.uint32_field(1)
    friends: list[int] = betterproto.fixed64_field(2)


@dataclass(eq=False, repr=False)
class CMsgClientChangeStatus(betterproto.Message):
    persona_state: int = betterproto.uint32_field(1)
    player_name: str = betterproto.string_field(2)
    is_auto_generated_name: bool = betterproto.bool_field(3)
    high_priority: bool = betterproto.bool_field(4)
    persona_set_by_user: bool = betterproto.bool_field(5)
    persona_state_flags: int = betterproto.uint32_field(6)
    need_persona_response: bool = betterproto.bool_field(7)
    is_client_idle: bool = betterproto.bool_field(8)


@dataclass(eq=False, repr=False)
class CMsgPersonaChangeResponse(betterproto.Message):
    result: int = betterproto.uint32_field(1)
    player_name: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class CMsgClientPersonaState(betterproto.Message):
    status_flags: int = betterproto.uint32_field(1)
    friends: "list[CMsgClientPersonaStateFriend]" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class CMsgClientPersonaStateFriend(betterproto.Message):
    friendid: int = betterproto.fixed64_field(1)
    persona_state: int = betterproto.uint32_field(2)
    game_played_app_id: int = betterproto.uint32_field(3)
    game_server_ip: int = betterproto.uint32_field(4)
    game_server_port: int = betterproto.uint32_field(5)
    persona_state_flags: int = betterproto.uint32_field(6)
    online_session_instances: int = betterproto.uint32_field(7)
    persona_set_by_user: bool = betterproto.bool_field(10)
    player_name: str = betterproto.string_field(15)
    query_port: int = betterproto.uint32_field(20)
    steamid_source: int = betterproto.fixed64_field(25)
    avatar_hash: bytes = betterproto.bytes_field(31)
    last_logoff: int = betterproto.uint32_field(45)
    last_logon: int = betterproto.uint32_field(46)
    last_seen_online: int = betterproto.uint32_field(47)
    clan_rank: int = betterproto.uint32_field(50)
    game_name: str = betterproto.string_field(55)
    gameid: int = betterproto.fixed64_field(56)
    game_data_blob: bytes = betterproto.bytes_field(60)
    clan_data: "CMsgClientPersonaStateFriendClanData" = betterproto.message_field(64)
    clan_tag: str = betterproto.string_field(65)
    rich_presence: "list[CMsgClientPersonaStateFriendKv]" = betterproto.message_field(71)
    broadcast_id: int = betterproto.fixed64_field(72)
    game_lobby_id: int = betterproto.fixed64_field(73)
    watching_broadcast_accountid: int = betterproto.uint32_field(74)
    watching_broadcast_appid: int = betterproto.uint32_field(75)
    watching_broadcast_viewers: int = betterproto.uint32_field(76)
    watching_broadcast_title: str = betterproto.string_field(77)
    is_community_banned: bool = betterproto.bool_field(78)
    player_name_pending_review: bool = betterproto.bool_field(79)
    avatar_pending_review: bool = betterproto.bool_field(80)


@dataclass(eq=False, repr=False)
class CMsgClientPersonaStateFriendClanData(betterproto.Message):
    ogg_app_id: int = betterproto.uint32_field(1)
    chat_group_id: int = betterproto.uint64_field(2)


@dataclass(eq=False, repr=False)
class CMsgClientPersonaStateFriendKv(betterproto.Message):
    key: str = betterproto.string_field(1)
    value: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class CMsgClientFriendProfileInfo(betterproto.Message):
    steamid_friend: int = betterproto.fixed64_field(1)


@dataclass(eq=False, repr=False)
class CMsgClientFriendProfileInfoResponse(betterproto.Message):
    eresult: int = betterproto.int32_field(1)
    steamid_friend: int = betterproto.fixed64_field(2)
    time_created: int = betterproto.uint32_field(3)
    real_name: str = betterproto.string_field(4)
    city_name: str = betterproto.string_field(5)
    state_name: str = betterproto.string_field(6)
    country_name: str = betterproto.string_field(7)
    headline: str = betterproto.string_field(8)
    summary: str = betterproto.string_field(9)


@dataclass(eq=False, repr=False)
class CMsgClientCreateFriendsGroup(betterproto.Message):
    steamid: int = betterproto.fixed64_field(1)
    groupname: str = betterproto.string_field(2)
    steamid_friends: list[int] = betterproto.fixed64_field(3)


@dataclass(eq=False, repr=False)
class CMsgClientCreateFriendsGroupResponse(betterproto.Message):
    eresult: int = betterproto.uint32_field(1)
    groupid: int = betterproto.int32_field(2)


@dataclass(eq=False, repr=False)
class CMsgClientDeleteFriendsGroup(betterproto.Message):
    steamid: int = betterproto.fixed64_field(1)
    groupid: int = betterproto.int32_field(2)


@dataclass(eq=False, repr=False)
class CMsgClientDeleteFriendsGroupResponse(betterproto.Message):
    eresult: int = betterproto.uint32_field(1)


@dataclass(eq=False, repr=False)
class CMsgClientManageFriendsGroup(betterproto.Message):
    groupid: int = betterproto.int32_field(1)
    groupname: str = betterproto.string_field(2)
    steamid_friends_added: list[int] = betterproto.fixed64_field(3)
    steamid_friends_removed: list[int] = betterproto.fixed64_field(4)


@dataclass(eq=False, repr=False)
class CMsgClientManageFriendsGroupResponse(betterproto.Message):
    eresult: int = betterproto.uint32_field(1)


@dataclass(eq=False, repr=False)
class CMsgClientAddFriendToGroup(betterproto.Message):
    groupid: int = betterproto.int32_field(1)
    steamiduser: int = betterproto.fixed64_field(2)


@dataclass(eq=False, repr=False)
class CMsgClientAddFriendToGroupResponse(betterproto.Message):
    eresult: int = betterproto.uint32_field(1)


@dataclass(eq=False, repr=False)
class CMsgClientRemoveFriendFromGroup(betterproto.Message):
    groupid: int = betterproto.int32_field(1)
    steamiduser: int = betterproto.fixed64_field(2)


@dataclass(eq=False, repr=False)
class CMsgClientRemoveFriendFromGroupResponse(betterproto.Message):
    eresult: int = betterproto.uint32_field(1)


@dataclass(eq=False, repr=False)
class CMsgClientGetEmoticonList(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class CMsgClientEmoticonList(betterproto.Message):
    emoticons: "list[CMsgClientEmoticonListEmoticon]" = betterproto.message_field(1)
    stickers: "list[CMsgClientEmoticonListSticker]" = betterproto.message_field(2)
    effects: "list[CMsgClientEmoticonListEffect]" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class CMsgClientEmoticonListEmoticon(betterproto.Message):
    name: str = betterproto.string_field(1)
    count: int = betterproto.int32_field(2)
    time_last_used: int = betterproto.uint32_field(3)
    use_count: int = betterproto.uint32_field(4)
    time_received: int = betterproto.uint32_field(5)
    appid: int = betterproto.uint32_field(6)


@dataclass(eq=False, repr=False)
class CMsgClientEmoticonListSticker(betterproto.Message):
    name: str = betterproto.string_field(1)
    count: int = betterproto.int32_field(2)
    time_received: int = betterproto.uint32_field(3)
    appid: int = betterproto.uint32_field(4)
    time_last_used: int = betterproto.uint32_field(5)
    use_count: int = betterproto.uint32_field(6)


@dataclass(eq=False, repr=False)
class CMsgClientEmoticonListEffect(betterproto.Message):
    name: str = betterproto.string_field(1)
    count: int = betterproto.int32_field(2)
    time_received: int = betterproto.uint32_field(3)
    infinite_use: bool = betterproto.bool_field(4)
    appid: int = betterproto.uint32_field(5)
