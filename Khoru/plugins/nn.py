from pyrogram import Client, filters
from AnimeThemes.moe import AnimeThemes
from pyrogram.types import (InlineKeyboardMarkup, InlineKeyboardButton,
                            InlineQueryResultArticle, InputTextMessageContent)

link = lambda x, y="staging.": x.replace(y, "")


@Client.on_inline_query(filters.regex(r".+"))
async def __nn__(bot, update):
    print(update)
    query = update.query.strip()
    query_id = update.id
    a = AnimeThemes()
    animes = a.search_anime(query)
    results = []
    for anime in animes["anime"]:
        title = anime["name"]
        anime_id = anime["id"]
        slug = anime["slug"]
        thumb = anime["images"][0]["link"]
        results.append(
            InlineQueryResultArticle(
                title,
                InputTextMessageContent(
                    title + "\n" + f"<a href='{thumb}'>&#8205;</a>"
                ),
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("AnimeThemes", "at_" + str(anime_id)),
                            InlineKeyboardButton("Url", url="https://staging.animethemes.moe/wiki/anime/" + slug)
                        ]
                    ]
                ),
                # url="https://staging.animethemes.moe/wiki/anime/" + slug,
                description=" ".join(anime["synopsis"].split()[:8]) + "...",
                thumb_url=thumb
            )
        )
    await bot.answer_inline_query(query_id,
                                  results)



