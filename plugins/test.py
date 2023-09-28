from pyrogram import Client, errors
from youtubesearchpython import SearchVideos
from pyrogram.types import (
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultPhoto,
)
import os
import requests ,os, wget 


@Client.on_inline_query()
async def inline_spotify(client: Client, query: InlineQuery):
    string_given = query.query.strip()
    iq = string_given.lower()
    if iq.startswith("yt"):
        result = []
        input_quer = (iq.split("yt", maxsplit=1)[1]).strip()
        search = SearchVideos(str(input_quer), offset=1, mode="dict", max_results=20)
        result_yt = search.result()["search_result"]
        for i in result_yt:
            link = i["link"]
            vid_title = i["title"]
            yt_id = i["id"]
            uploader = i["channel"]
            views = i["views"]
            time = i["duration"]
            publish = i["publishTime"]
            thumb = f"https://img.youtube.com/vi/{yt_id}/hqdefault.jpg"
            caption = f"""
🎧**Title:** {vid_title}
📺**Channel:** {uploader}
👁️‍🗨️**Views:** {views}
⏱️**Duration:** {time}
📆**Published:** {publish}
🔗**Link:** {link}
            """
            result.append(
                InlineQueryResultPhoto(
                    photo_url=thumb,
                    title=vid_title,
                    description=f"Channel: {uploader}\nDuration: {time}\n🔎 By: 𝗠ᴜsɪᴄ•𝕏•𝗗ʟ♪",
                    caption=caption,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="🎥 Watch On YouTube",
                                    url=link
                                ),
                                InlineKeyboardButton(
                                    text="🔎 Search Again",
                                    switch_inline_query_current_chat="yt "
                                ),
                            ]
                        ]
                    )
                )
            )
        await query.answer(results=result, cache_time=0)
