import logging
from pyrogram import Client, emoji, filters
from pyrogram.errors.exceptions.bad_request_400 import QueryIdInvalid
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultCachedDocument, InlineQuery, InlineQueryResultArticle, InputTextMessageContent

from database.ia_filterdb import get_search_results
from utils import get_size
from info import CUSTOM_FILE_CAPTION

logger = logging.getLogger(__name__)


buttons = [
    [
        InlineKeyboardButton("🔍Search Music...", switch_inline_query_current_chat="s ")
    ]
]


@Client.on_inline_query()
async def answer(bot, query):
    string_given = query.query.strip()
    iq = string_given.lower()
    if iq == "":
        answer = [
            InlineQueryResultArticle(
                title="🎵 @SongsAf_bot",
                description="💙You can Search Music.",
                thumb_url="https://telegra.ph/file/1d586532543a0084eabcd.jpg",
                input_message_content=InputTextMessageContent("💭 Welcome to Music Search inline Bot."),
                reply_markup=InlineKeyboardMarkup(buttons)
            )
        ]
        await query.answer(results=answer, cache_time=5, switch_pm_text="💫 Welcome To @SongsAf_bot", switch_pm_parameter="help")

    elif iq.startswith("s"):
        results = []
        string, file_type = (iq.iq.split('s', maxsplit=1)[1]).strip()
        string = string.strip()
        file_type = file_type.strip().lower()
    else:
        string = iq.iq.strip()
        file_type = None

    offset = int(iq.offset or 0)
    reply_markup = get_reply_markup(query=string)
    files, next_offset, total = await get_search_results(string,
                                                  file_type=file_type,
                                                  max_results=50,
                                                  offset=offset)

    for file in files:
        title=file.file_name
        size=get_size(file.file_size)
        f_caption=file.caption
        if CUSTOM_FILE_CAPTION:
            try:
                f_caption=CUSTOM_FILE_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='' if f_caption is None else f_caption)
            except Exception as e:
                logger.exception(e)
                f_caption=f_caption
        if f_caption is None:
            f_caption = f"{file.file_name}"
        results.append(
            InlineQueryResultCachedDocument(
                title=file.file_name,
                document_file_id=file.file_id,
                caption=f_caption,
                description=f'Size: {get_size(file.file_size)}\nType: {file.file_type}\n©️ @SongsAf_bot',
                reply_markup=reply_markup))

    if results:
        switch_pm_text = f"🎵 Total Songs in my Database--> {total}"
        if string:
            switch_pm_text += f" for {string}"
        try:
            await query.answer(results=results,
                           is_personal = True,
                           switch_pm_text=switch_pm_text,
                           switch_pm_parameter="start",
                           next_offset=str(next_offset))
        except QueryIdInvalid:
            pass
        except Exception as e:
            logging.exception(str(e))
    else:
        switch_pm_text = f'{emoji.CROSS_MARK} No results'
        if string:
            switch_pm_text += f' for "{string}"'

        await query.answer(results=[],
                           is_personal = True,
                           switch_pm_text=switch_pm_text,
                           switch_pm_parameter="okay")


def get_reply_markup(query):
    buttons = [
        [
            InlineKeyboardButton('🔍Search Again🔎', switch_inline_query_current_chat=f"s {query}")
        ]
        ]
    return InlineKeyboardMarkup(buttons)




