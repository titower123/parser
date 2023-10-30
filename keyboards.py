from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

from main import get_10_new_article

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Показать новости'),
        ],
        [
            KeyboardButton(text='Выбор новостей'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Что хотите сделать?",
    selective=True
)

news_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить еще новостей"),
        ],
        [
            KeyboardButton(text="НАЗАД"),
        ]
    ],
    resize_keyboard=True,
)



# filter_kb = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="Новые"),
#             InlineKeyboardButton(text="Лучшие"),
#         ],
#         [
#             InlineKeyboardButton(text="За сутки"),
#             InlineKeyboardButton(text="За неделю"),
#             InlineKeyboardButton(text="За месяц"),
#             InlineKeyboardButton(text="За год"),
#             InlineKeyboardButton(text="За все время"),
#         ],
#         [
#             InlineKeyboardButton(text="Любой уровень сложности"),
#             InlineKeyboardButton(text="Простые"),
#             InlineKeyboardButton(text="Средний"),
#             InlineKeyboardButton(text="Сложный"),
#         ]
#     ],
#     resize_keyboard=True
# )

# class Pagination(CallbackData, prefix="pag"):
#     action: str
#     page: int
#
# def paginator(page: int=0):
#     builder = InlineKeyboardBuilder()
#     builder.row(
#         InlineKeyboardButton(text=)
#     )



def filter_kb():
    filters = [
        "Новые", "Лучшие",
        "За сутки", "За неделю","За месяц","За год","За все время",
        "Любой уровень сложности","Простые", "Средний", "Сложный"
    ]
    builder = ReplyKeyboardBuilder()
    [builder.button(text=filter) for filter in filters]
    builder.button(text="НАЗАД")
    builder.adjust(2, 5, 4, 1)
    return builder.as_markup(resize_keyboard=True)

