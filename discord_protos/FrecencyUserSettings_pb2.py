# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FrecencyUserSettings.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x46recencyUserSettings.proto\x12\x34\x64iscord_protos.discord_users.v1.FrecencyUserSettings\"\xd0\x16\n\x14\x46recencyUserSettings\x12j\n\x08versions\x18\x01 \x01(\x0b\x32S.discord_protos.discord_users.v1.FrecencyUserSettings.FrecencyUserSettings.VersionsH\x00\x88\x01\x01\x12s\n\rfavorite_gifs\x18\x02 \x01(\x0b\x32W.discord_protos.discord_users.v1.FrecencyUserSettings.FrecencyUserSettings.FavoriteGIFsH\x01\x88\x01\x01\x12{\n\x11\x66\x61vorite_stickers\x18\x03 \x01(\x0b\x32[.discord_protos.discord_users.v1.FrecencyUserSettings.FrecencyUserSettings.FavoriteStickersH\x02\x88\x01\x01\x12y\n\x10sticker_frecency\x18\x04 \x01(\x0b\x32Z.discord_protos.discord_users.v1.FrecencyUserSettings.FrecencyUserSettings.StickerFrecencyH\x03\x88\x01\x01\x12w\n\x0f\x66\x61vorite_emojis\x18\x05 \x01(\x0b\x32Y.discord_protos.discord_users.v1.FrecencyUserSettings.FrecencyUserSettings.FavoriteEmojisH\x04\x88\x01\x01\x12u\n\x0e\x65moji_frecency\x18\x06 \x01(\x0b\x32X.discord_protos.discord_users.v1.FrecencyUserSettings.FrecencyUserSettings.EmojiFrecencyH\x05\x88\x01\x01\x12\x90\x01\n\x1c\x61pplication_command_frecency\x18\x07 \x01(\x0b\x32\x65.discord_protos.discord_users.v1.FrecencyUserSettings.FrecencyUserSettings.ApplicationCommandFrecencyH\x06\x88\x01\x01\x12\x8c\x01\n\x1a\x66\x61vorite_soundboard_sounds\x18\x08 \x01(\x0b\x32\x63.discord_protos.discord_users.v1.FrecencyUserSettings.FrecencyUserSettings.FavoriteSoundboardSoundsH\x07\x88\x01\x01\x1aP\n\x08Versions\x12\x16\n\x0e\x63lient_version\x18\x01 \x01(\r\x12\x16\n\x0eserver_version\x18\x02 \x01(\r\x12\x14\n\x0c\x64\x61ta_version\x18\x03 \x01(\r\x1a\xac\x01\n\x0b\x46\x61voriteGIF\x12\x62\n\x06\x66ormat\x18\x01 \x01(\x0e\x32R.discord_protos.discord_users.v1.FrecencyUserSettings.FrecencyUserSettings.GIFType\x12\x0b\n\x03src\x18\x02 \x01(\t\x12\r\n\x05width\x18\x03 \x01(\r\x12\x0e\n\x06height\x18\x04 \x01(\r\x12\r\n\x05order\x18\x05 \x01(\r\x1a\x9b\x02\n\x0c\x46\x61voriteGIFs\x12o\n\x04gifs\x18\x01 \x03(\x0b\x32\x61.discord_protos.discord_users.v1.FrecencyUserSettings.FrecencyUserSettings.FavoriteGIFs.GifsEntry\x12\x14\n\x0chide_tooltip\x18\x02 \x01(\x08\x1a\x83\x01\n\tGifsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x65\n\x05value\x18\x02 \x01(\x0b\x32V.discord_protos.discord_users.v1.FrecencyUserSettings.FrecencyUserSettings.FavoriteGIF:\x02\x38\x01\x1a\'\n\x10\x46\x61voriteStickers\x12\x13\n\x0bsticker_ids\x18\x01 \x03(\x06\x1aX\n\x0c\x46recencyItem\x12\x12\n\ntotal_uses\x18\x01 \x01(\r\x12\x13\n\x0brecent_uses\x18\x02 \x03(\x04\x12\x10\n\x08\x66recency\x18\x03 \x01(\x05\x12\r\n\x05score\x18\x04 \x01(\x05\x1a\x98\x02\n\x0fStickerFrecency\x12z\n\x08stickers\x18\x01 \x03(\x0b\x32h.discord_protos.discord_users.v1.FrecencyUserSettings.FrecencyUserSettings.StickerFrecency.StickersEntry\x1a\x88\x01\n\rStickersEntry\x12\x0b\n\x03key\x18\x01 \x01(\x06\x12\x66\n\x05value\x18\x02 \x01(\x0b\x32W.discord_protos.discord_users.v1.FrecencyUserSettings.FrecencyUserSettings.FrecencyItem:\x02\x38\x01\x1a \n\x0e\x46\x61voriteEmojis\x12\x0e\n\x06\x65mojis\x18\x01 \x03(\t\x1a\x8e\x02\n\rEmojiFrecency\x12t\n\x06\x65mojis\x18\x01 \x03(\x0b\x32\x64.discord_protos.discord_users.v1.FrecencyUserSettings.FrecencyUserSettings.EmojiFrecency.EmojisEntry\x1a\x86\x01\n\x0b\x45mojisEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x66\n\x05value\x18\x02 \x01(\x0b\x32W.discord_protos.discord_users.v1.FrecencyUserSettings.FrecencyUserSettings.FrecencyItem:\x02\x38\x01\x1a\xd1\x02\n\x1a\x41pplicationCommandFrecency\x12\x9c\x01\n\x14\x61pplication_commands\x18\x01 \x03(\x0b\x32~.discord_protos.discord_users.v1.FrecencyUserSettings.FrecencyUserSettings.ApplicationCommandFrecency.ApplicationCommandsEntry\x1a\x93\x01\n\x18\x41pplicationCommandsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x66\n\x05value\x18\x02 \x01(\x0b\x32W.discord_protos.discord_users.v1.FrecencyUserSettings.FrecencyUserSettings.FrecencyItem:\x02\x38\x01\x1a-\n\x18\x46\x61voriteSoundboardSounds\x12\x11\n\tsound_ids\x18\x01 \x03(\x06\")\n\x07GIFType\x12\x08\n\x04NONE\x10\x00\x12\t\n\x05IMAGE\x10\x01\x12\t\n\x05VIDEO\x10\x02\x42\x0b\n\t_versionsB\x10\n\x0e_favorite_gifsB\x14\n\x12_favorite_stickersB\x13\n\x11_sticker_frecencyB\x12\n\x10_favorite_emojisB\x11\n\x0f_emoji_frecencyB\x1f\n\x1d_application_command_frecencyB\x1d\n\x1b_favorite_soundboard_soundsb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'FrecencyUserSettings_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FRECENCYUSERSETTINGS_FAVORITEGIFS_GIFSENTRY._options = None
  _FRECENCYUSERSETTINGS_FAVORITEGIFS_GIFSENTRY._serialized_options = b'8\001'
  _FRECENCYUSERSETTINGS_STICKERFRECENCY_STICKERSENTRY._options = None
  _FRECENCYUSERSETTINGS_STICKERFRECENCY_STICKERSENTRY._serialized_options = b'8\001'
  _FRECENCYUSERSETTINGS_EMOJIFRECENCY_EMOJISENTRY._options = None
  _FRECENCYUSERSETTINGS_EMOJIFRECENCY_EMOJISENTRY._serialized_options = b'8\001'
  _FRECENCYUSERSETTINGS_APPLICATIONCOMMANDFRECENCY_APPLICATIONCOMMANDSENTRY._options = None
  _FRECENCYUSERSETTINGS_APPLICATIONCOMMANDFRECENCY_APPLICATIONCOMMANDSENTRY._serialized_options = b'8\001'
  _FRECENCYUSERSETTINGS._serialized_start=85
  _FRECENCYUSERSETTINGS._serialized_end=2981
  _FRECENCYUSERSETTINGS_VERSIONS._serialized_start=1112
  _FRECENCYUSERSETTINGS_VERSIONS._serialized_end=1192
  _FRECENCYUSERSETTINGS_FAVORITEGIF._serialized_start=1195
  _FRECENCYUSERSETTINGS_FAVORITEGIF._serialized_end=1367
  _FRECENCYUSERSETTINGS_FAVORITEGIFS._serialized_start=1370
  _FRECENCYUSERSETTINGS_FAVORITEGIFS._serialized_end=1653
  _FRECENCYUSERSETTINGS_FAVORITEGIFS_GIFSENTRY._serialized_start=1522
  _FRECENCYUSERSETTINGS_FAVORITEGIFS_GIFSENTRY._serialized_end=1653
  _FRECENCYUSERSETTINGS_FAVORITESTICKERS._serialized_start=1655
  _FRECENCYUSERSETTINGS_FAVORITESTICKERS._serialized_end=1694
  _FRECENCYUSERSETTINGS_FRECENCYITEM._serialized_start=1696
  _FRECENCYUSERSETTINGS_FRECENCYITEM._serialized_end=1784
  _FRECENCYUSERSETTINGS_STICKERFRECENCY._serialized_start=1787
  _FRECENCYUSERSETTINGS_STICKERFRECENCY._serialized_end=2067
  _FRECENCYUSERSETTINGS_STICKERFRECENCY_STICKERSENTRY._serialized_start=1931
  _FRECENCYUSERSETTINGS_STICKERFRECENCY_STICKERSENTRY._serialized_end=2067
  _FRECENCYUSERSETTINGS_FAVORITEEMOJIS._serialized_start=2069
  _FRECENCYUSERSETTINGS_FAVORITEEMOJIS._serialized_end=2101
  _FRECENCYUSERSETTINGS_EMOJIFRECENCY._serialized_start=2104
  _FRECENCYUSERSETTINGS_EMOJIFRECENCY._serialized_end=2374
  _FRECENCYUSERSETTINGS_EMOJIFRECENCY_EMOJISENTRY._serialized_start=2240
  _FRECENCYUSERSETTINGS_EMOJIFRECENCY_EMOJISENTRY._serialized_end=2374
  _FRECENCYUSERSETTINGS_APPLICATIONCOMMANDFRECENCY._serialized_start=2377
  _FRECENCYUSERSETTINGS_APPLICATIONCOMMANDFRECENCY._serialized_end=2714
  _FRECENCYUSERSETTINGS_APPLICATIONCOMMANDFRECENCY_APPLICATIONCOMMANDSENTRY._serialized_start=2567
  _FRECENCYUSERSETTINGS_APPLICATIONCOMMANDFRECENCY_APPLICATIONCOMMANDSENTRY._serialized_end=2714
  _FRECENCYUSERSETTINGS_FAVORITESOUNDBOARDSOUNDS._serialized_start=2716
  _FRECENCYUSERSETTINGS_FAVORITESOUNDBOARDSOUNDS._serialized_end=2761
  _FRECENCYUSERSETTINGS_GIFTYPE._serialized_start=2763
  _FRECENCYUSERSETTINGS_GIFTYPE._serialized_end=2804
# @@protoc_insertion_point(module_scope)