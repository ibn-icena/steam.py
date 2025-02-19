# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: steammessages_econ.steamclient.proto
# plugin: python-betterproto
# Last updated 09/09/2021

from dataclasses import dataclass

import betterproto


@dataclass(eq=False, repr=False)
class GetTradeOfferAccessTokenRequest(betterproto.Message):
    generate_new_token: bool = betterproto.bool_field(1)


@dataclass(eq=False, repr=False)
class GetTradeOfferAccessTokenResponse(betterproto.Message):
    trade_offer_access_token: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class GetItemShopOverlayAuthUrlRequest(betterproto.Message):
    return_url: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class GetItemShopOverlayAuthUrlResponse(betterproto.Message):
    url: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class GetAssetClassInfoRequest(betterproto.Message):
    language: str = betterproto.string_field(1)
    appid: int = betterproto.uint32_field(2)
    classes: "list[GetAssetClassInfoRequestClass]" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class GetAssetClassInfoRequestClass(betterproto.Message):
    classid: int = betterproto.uint64_field(1)
    instanceid: int = betterproto.uint64_field(2)


@dataclass(eq=False, repr=False)
class ItemDescriptionLine(betterproto.Message):
    type: str = betterproto.string_field(1)
    value: str = betterproto.string_field(2)
    color: str = betterproto.string_field(3)
    label: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class ItemAction(betterproto.Message):
    link: str = betterproto.string_field(1)
    name: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class ItemDescription(betterproto.Message):
    appid: int = betterproto.int32_field(1)
    classid: int = betterproto.uint64_field(2)
    instanceid: int = betterproto.uint64_field(3)
    currency: bool = betterproto.bool_field(4)
    background_color: str = betterproto.string_field(5)
    icon_url: str = betterproto.string_field(6)
    icon_url_large: str = betterproto.string_field(7)
    descriptions: "list[ItemDescriptionLine]" = betterproto.message_field(8)
    tradable: bool = betterproto.bool_field(9)
    actions: "list[ItemAction]" = betterproto.message_field(10)
    owner_descriptions: "list[ItemDescriptionLine]" = betterproto.message_field(11)
    owner_actions: "list[ItemAction]" = betterproto.message_field(12)
    fraudwarnings: list[str] = betterproto.string_field(13)
    name: str = betterproto.string_field(14)
    name_color: str = betterproto.string_field(15)
    type: str = betterproto.string_field(16)
    market_name: str = betterproto.string_field(17)
    market_hash_name: str = betterproto.string_field(18)
    market_fee: str = betterproto.string_field(19)
    market_fee_app: int = betterproto.int32_field(28)
    contained_item: "ItemDescription" = betterproto.message_field(20)
    market_actions: "list[ItemAction]" = betterproto.message_field(21)
    commodity: bool = betterproto.bool_field(22)
    market_tradable_restriction: int = betterproto.int32_field(23)
    market_marketable_restriction: int = betterproto.int32_field(24)
    marketable: bool = betterproto.bool_field(25)
    tags: "list[ItemTag]" = betterproto.message_field(26)
    item_expiration: str = betterproto.string_field(27)
    market_buy_country_restriction: str = betterproto.string_field(30)
    market_sell_country_restriction: str = betterproto.string_field(31)


@dataclass(eq=False, repr=False)
class ItemTag(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    category: str = betterproto.string_field(2)
    internal_name: str = betterproto.string_field(3)
    localized_category_name: str = betterproto.string_field(4)
    localized_tag_name: str = betterproto.string_field(5)
    color: str = betterproto.string_field(6)


@dataclass(eq=False, repr=False)
class GetAssetClassInfoResponse(betterproto.Message):
    descriptions: "list[ItemDescription]" = betterproto.message_field(1)
