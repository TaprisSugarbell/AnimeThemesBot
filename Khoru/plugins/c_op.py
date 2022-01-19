from pyromod.nav import Pagination
from pyrogram import Client, filters
from AnimeThemes.moe import AnimeThemes
from pyromod.helpers import ikb, array_chunk


def page_data(page):
    return f'page_{page}_{anime_id}'


def item_data(item, page):
    return f'theme_{item["id"]}'


def item_title(item, page):
    # return f'Item {item} of page {page}'
    return f'{item["slug"]}'


link = lambda x, y="staging.": x.replace(y, "")


@Client.on_callback_query()
# @Client.on_callback_query(filters.regex(r"op_.*"))
async def __op__(bot, update):
    global anime_id
    print(update)
    inline_message_id = update.inline_message_id
    data = update.data.split("_")
    mode = data[0]
    a = AnimeThemes()
    if mode == "at":
        anime_id = int(data[-1])
        anime = a.search_anime(anime_id=anime_id)["anime"][0]
        print(anime)
        page = Pagination(
            anime["animethemes"],
            page_data=page_data,
            item_data=item_data,
            item_title=item_title
        )
        index = 0
        lines = 5
        columns = 3
        kb = page.create(index, lines, columns)
        await bot.edit_inline_reply_markup(
            inline_message_id,
            ikb(kb)
        )
    elif mode == "theme":
        animetheme = a.animethemes(int(data[-1]))["animetheme"]
        print(animetheme)
        anime_id = animetheme["anime"]["id"]
        entry = animetheme["animethemeentries"][0]
        print(entry)
        _link = link(entry["videos"][0]["link"])
        print(_link)
        kb = array_chunk(
            [(f'{entry["videos"][0]["resolution"]}p', _link, "url")], 1
        )
        await bot.edit_inline_reply_markup(
            inline_message_id,
            ikb(kb)
        )
    elif mode == "page":
        anime_id = int(data[-1])
        anime = a.search_anime(anime_id=anime_id)["anime"][0]
        print(anime)
        page = Pagination(
            anime["animethemes"],
            page_data=page_data,
            item_data=item_data,
            item_title=item_title
        )
        index = int(data[1])
        lines = 5
        columns = 3
        kb = page.create(index, lines, columns)
        await bot.edit_inline_reply_markup(
            inline_message_id,
            ikb(kb)
        )

