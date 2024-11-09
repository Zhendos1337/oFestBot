import datetime

from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)


def get_type_of_quest_special() -> InlineKeyboardMarkup:
    if datetime.datetime(2024, 11, 13) > datetime.datetime.today() > datetime.datetime(2024, 11, 11) or datetime.datetime(2024, 11, 7) > datetime.datetime.today() > datetime.datetime(2024, 11, 5):
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Очные СВ", callback_data="svirl"), InlineKeyboardButton(text='Очные Эдем', callback_data='eirl')],
            [InlineKeyboardButton(text="Онлайн СВ", callback_data="svonline"), InlineKeyboardButton(text='Онлайн Эдем', callback_data='eonline')],
        ])
    elif datetime.datetime(2024, 11, 14) > datetime.datetime.today() > datetime.datetime(2024, 11, 12) or datetime.datetime(2024, 11, 8) > datetime.datetime.today() > datetime.datetime(2024, 11, 6):
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Очные Космея", callback_data="kirl"), InlineKeyboardButton(text='Очные Лотос', callback_data='lirl')],
            [InlineKeyboardButton(text="Онлайн Космея", callback_data="konline"), InlineKeyboardButton(text='Онлайн Лотос', callback_data='lonline')],
        ])
    elif datetime.datetime(2024, 11, 15) > datetime.datetime.today() > datetime.datetime(2024, 11, 13) or datetime.datetime(2024, 11, 9) > datetime.datetime.today() > datetime.datetime(2024, 11, 7):
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Очные Орбита", callback_data="oirl"), InlineKeyboardButton(text='Очные АТОМ', callback_data='airl')],
            [InlineKeyboardButton(text="Онлайн Орбита", callback_data="oonline"), InlineKeyboardButton(text='Онлайн АТОМ', callback_data='aonline')],
        ])




def type_quests_list_online_special_l() -> InlineKeyboardMarkup:
    if datetime.datetime(2024, 11, 13) > datetime.datetime.today() > datetime.datetime(2024, 11, 11) or datetime.datetime(2024, 11, 7) > datetime.datetime.today() > datetime.datetime(2024, 11, 5):

        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Викторина", callback_data="svchoose_quiz"),
             InlineKeyboardButton(text="Сделай это", callback_data="svDO_IT")],
            [InlineKeyboardButton(text="Изучи это", callback_data="svlearn_it")]
        ])
    elif datetime.datetime(2024, 10, 14) > datetime.datetime.today() > datetime.datetime(2024, 11, 12) or datetime.datetime(2024, 11, 8) > datetime.datetime.today() > datetime.datetime(2024, 11, 6):
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Викторина", callback_data="kchoose_quiz"),
             InlineKeyboardButton(text="Сделай это", callback_data="kDO_IT")],
            [InlineKeyboardButton(text="Изучи это", callback_data="klearn_it")]
        ])
    elif datetime.datetime(2024, 11, 15) > datetime.datetime.today() > datetime.datetime(2024, 11, 13) or datetime.datetime(2024, 11, 9) > datetime.datetime.today() > datetime.datetime(2024, 11, 7):
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Викторина", callback_data="orbchoose_quiz"),
             InlineKeyboardButton(text="Сделай это", callback_data="orbDO_IT")],
            [InlineKeyboardButton(text="Изучи это", callback_data="orblearn_it")]
        ])

def type_quests_list_online_special_r() -> InlineKeyboardMarkup:
    if datetime.datetime(2024, 11, 13) > datetime.datetime.today() > datetime.datetime(2024, 11, 11) or datetime.datetime(2024, 11, 7) > datetime.datetime.today() > datetime.datetime(2024, 11, 6):
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Викторина", callback_data="echoose_quiz"),
             InlineKeyboardButton(text="Сделай это", callback_data="eDO_IT")],
            [InlineKeyboardButton(text="Изучи это", callback_data="elearn_it")]
    ])
    elif datetime.datetime(2024, 10, 14) > datetime.datetime.today() > datetime.datetime(2024, 11, 12) or datetime.datetime(2024, 11, 8) > datetime.datetime.today() > datetime.datetime(2024, 11, 6):
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Викторина", callback_data="lchoose_quiz"),
             InlineKeyboardButton(text="Сделай это", callback_data="lDO_IT")],
            [InlineKeyboardButton(text="Изучи это", callback_data="llearn_it")]
        ])
    elif datetime.datetime(2024, 10, 15) > datetime.datetime.today() > datetime.datetime(2024, 11, 13) or datetime.datetime(2024, 11, 9) > datetime.datetime.today() > datetime.datetime(2024, 11, 7):
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Викторина", callback_data="achoose_quiz"),
             InlineKeyboardButton(text="Сделай это", callback_data="aDO_IT")],
            [InlineKeyboardButton(text="Изучи это", callback_data="alearn_it")]
        ])



def get_type_of_quest_inout() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Общие", callback_data="general")],
        [InlineKeyboardButton(text="Отрядные", callback_data="special")],
        [InlineKeyboardButton(text="Задание дня", callback_data="dailyq")],
        ])


def main_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Об отрядах"), KeyboardButton(text="Анкета")],
        [KeyboardButton(text="Задания"), KeyboardButton(text="Магазин")],
        [KeyboardButton(text="Расписание"), KeyboardButton(text="Кошелек")],
        [KeyboardButton(text="Задать вопрос")]
    ], resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню')


def where_from() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Рассказал друг", callback_data="friend"),
         InlineKeyboardButton(text="Увидел QR-код", callback_data="qr")],
        [InlineKeyboardButton(text="Соц. сети", callback_data="social"),
         InlineKeyboardButton(text="Другое", callback_data="other")]
    ])

def get_type_of_quest() -> InlineKeyboardMarkup:
    if datetime.datetime(2024, 11, 10) < datetime.datetime.today() < datetime.datetime(2024, 11, 12):
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Очные", callback_data="irl")],
            [InlineKeyboardButton(text="Онлайн", callback_data="online")],
        ])
    else:
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Онлайн", callback_data="online")]
        ])

def irl_ready() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="irl_irl1"),
         InlineKeyboardButton(text="Задание 2", callback_data="irl_irl2"),
         InlineKeyboardButton(text="Задание 3", callback_data="irl_irl3")],
        [InlineKeyboardButton(text="Задание 4", callback_data="irl_irl4"),
         InlineKeyboardButton(text="Задание 5", callback_data="irl_irl5"),
         InlineKeyboardButton(text="Задание 6", callback_data="irl_irl6")],
        [InlineKeyboardButton(text="Задание 7", callback_data="irl_irl7"),
         InlineKeyboardButton(text="Задание 8", callback_data="irl_irl8"),
         InlineKeyboardButton(text="Задание 9", callback_data="irl_irl9")],
    ])


def irl_orbita_ready() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="orbitairl_oirl1"),
         InlineKeyboardButton(text="Задание 2", callback_data="orbitairl_oirl2"),
         InlineKeyboardButton(text="Задание 3", callback_data="orbitairl_oirl3")],
        [InlineKeyboardButton(text="Задание 4", callback_data="orbitairl_oirl4"),
         InlineKeyboardButton(text="Задание 5", callback_data="orbitairl_oirl5"),
         InlineKeyboardButton(text="Задание 6", callback_data="orbitairl_oirl6")]
    ])


def lirl_ready() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="lirl_lirl1"),
         InlineKeyboardButton(text="Задание 2", callback_data="lirl_lirl2"),
         InlineKeyboardButton(text="Задание 3", callback_data="lirl_lirl3")],
        [InlineKeyboardButton(text="Задание 4", callback_data="lirl_lirl4"),
         InlineKeyboardButton(text="Задание 5", callback_data="lirl_lirl5"),
         InlineKeyboardButton(text="Задание 6", callback_data="lirl_lirl6")]
    ])


def type_quests_list_online() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подпишись", callback_data="subscribe"),
         InlineKeyboardButton(text="Викторина", callback_data="choose_quiz")],
        [InlineKeyboardButton(text="Сделай это", callback_data="DO_IT"),
         InlineKeyboardButton(text="Изучи это", callback_data="learn_it")]
        ])


def squads_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Штаб", callback_data="headquearter")],
        [InlineKeyboardButton(text="Орбита", callback_data="orbita"),
         InlineKeyboardButton(text="Лотос", callback_data="lotos")],
        [InlineKeyboardButton(text="Космея", callback_data="kosmeya"),
         InlineKeyboardButton(text="Эдем", callback_data="edem")],
        [InlineKeyboardButton(text="Северная Венеция", callback_data="venetsia"),
         InlineKeyboardButton(text="АТОМ", callback_data="atom")],
        [InlineKeyboardButton(text='Словарь', callback_data='dicti')]
    ])


def learn1_4_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="learn_l1"),
         InlineKeyboardButton(text="Задание 2", callback_data="learn_l2")],
        [InlineKeyboardButton(text="Задание 3", callback_data="learn_l3"),
         InlineKeyboardButton(text="Задание 4", callback_data="learn_l4")],
        [InlineKeyboardButton(text="Другие задания", callback_data="next_to_learn_p2")]
    ])


def learn5_8_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 5", callback_data="learn_l5"),
         InlineKeyboardButton(text="Задание 6", callback_data="learn_l6")],
        [InlineKeyboardButton(text="Задание 7", callback_data="learn_l7"),
         InlineKeyboardButton(text="Задание 8", callback_data="learn_l8")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_learn_p1"),
         InlineKeyboardButton(text="Ещё задания", callback_data="next_to_learn_p3")]
    ])


def learn9_12_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 9", callback_data="learn_l9"),
         InlineKeyboardButton(text="Задание 10", callback_data="learn_l10")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_learn_p2"),
         InlineKeyboardButton(text="Ещё задания", callback_data="next_to_learn_p4")]
    ])


def quiz1() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="1948", callback_data="answer_true_q1"),
        InlineKeyboardButton(text="1956", callback_data="false_q1")],
        [InlineKeyboardButton(text="2004", callback_data="false_q1")]
    ])


def quiz2() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="6", callback_data="false_q2"),
         InlineKeyboardButton(text="5", callback_data="answer_true_q2")],
        [InlineKeyboardButton(text="3", callback_data="false_q2")]
    ])


def quiz3() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="ССО Эдем", callback_data="false_q3"),
        InlineKeyboardButton(text="ССхО Космея", callback_data="false_q3")],
        [InlineKeyboardButton(text="СПО Орбита", callback_data="answer_true_q3")]
    ])


def quiz4() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="бойцовка", callback_data="false_q4"),
         InlineKeyboardButton(text="строевка", callback_data="answer_true_q4")],
        [InlineKeyboardButton(text="целинка", callback_data="false_q4")]
    ])


def quiz5() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="СМедО АТОМ", callback_data="answer_true_q5"),
        InlineKeyboardButton(text="СПО Северная Венеция", callback_data="false_q5")],
        [InlineKeyboardButton(text="СОП Лотос", callback_data="false_q5")]
        ])


def quiz6() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="командир", callback_data="false_q6"),
        InlineKeyboardButton(text="казначей", callback_data="answer_true_q6")],
        [InlineKeyboardButton(text="методист", callback_data="false_q6")]
        ])


def quiz7() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="50-100", callback_data="false_q7"),
         InlineKeyboardButton(text="100-150", callback_data="false_q7")],
        [InlineKeyboardButton(text="150-200", callback_data="answer_true_q7")]
    ])


def quiz8() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="новичок", callback_data="false_q8"),
         InlineKeyboardButton(text="кандидат", callback_data="answer_true_q8")],
        [InlineKeyboardButton(text="молодой", callback_data="false_q8")]
    ])


def quiz9() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="молния", callback_data="false_q9"),
         InlineKeyboardButton(text="треугольик", callback_data="false_q9")],
        [InlineKeyboardButton(text="мастерок", callback_data="answer_true_q9")]
    ])


def quiz10() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="50-100", callback_data="false_q10"),
         InlineKeyboardButton(text="100-150", callback_data="false_q10")],
        [InlineKeyboardButton(text="150-200", callback_data="answer_true_q10")]
    ])


def quiz11() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="1948", callback_data="false_q11"),
        InlineKeyboardButton(text="1956", callback_data="answer_true_q11")],
        [InlineKeyboardButton(text="2004", callback_data="false_q11")]
    ])


def quiz12() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="1948", callback_data="false_q12"),
         InlineKeyboardButton(text="1956", callback_data="answer_true_q12")],
        [InlineKeyboardButton(text="2004", callback_data="false_q12")]
    ])


def quiz1_4_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="quiz_q1"),
         InlineKeyboardButton(text="Задание 2", callback_data="quiz_q2")],
        [InlineKeyboardButton(text="Задание 3", callback_data="quiz_q3"),
         InlineKeyboardButton(text="Задание 4", callback_data="quiz_q4")],
        [InlineKeyboardButton(text="Ещё задания", callback_data="next_to_quiz_p2")]
    ])


def quiz5_8_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 5", callback_data="quiz_q5"),
         InlineKeyboardButton(text="Задание 6", callback_data="quiz_q6")],
        [InlineKeyboardButton(text="Задание 7", callback_data="quiz_q7"),
         InlineKeyboardButton(text="Задание 8", callback_data="quiz_q8")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_quiz_p1"),
        InlineKeyboardButton(text="Ещё задания", callback_data="next_to_quiz_p3")]
    ])


def quiz9_12_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 9", callback_data="quiz_q9"),
         InlineKeyboardButton(text="Задание 10", callback_data="quiz_q10")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_quiz_p2"),
        InlineKeyboardButton(text="Ещё задания", callback_data="next_to_quiz_p4")]
        ])


def doit1_4_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="doit_d1"),
         InlineKeyboardButton(text="Задание 2", callback_data="doit_d2")],
        [InlineKeyboardButton(text="Задание 3", callback_data="doit_d3"),
         InlineKeyboardButton(text="Задание 4", callback_data="doit_d4")],
        [InlineKeyboardButton(text="Ещё задания", callback_data="next_to_doit_p2")]
    ])


def doit5_8_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 5", callback_data="doit_d5"),
         InlineKeyboardButton(text="Задание 6", callback_data="doit_d6")],
        [InlineKeyboardButton(text="Задание 7", callback_data="doit_d7"),
         InlineKeyboardButton(text="Задание 8", callback_data="doit_d8")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_doit_p1"),
         InlineKeyboardButton(text="Ещё задания", callback_data="next_to_doit_p3")]
    ])


def doit9_12_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 9", callback_data="doit_d9"),
         InlineKeyboardButton(text="Задание 10", callback_data="doit_d10")],
        [InlineKeyboardButton(text="Задание 11", callback_data="doitq_d11"),
         InlineKeyboardButton(text="Задание 12", callback_data="doit_d12")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_doit_p2"),
         InlineKeyboardButton(text="Ещё задания", callback_data="next_to_doit_p4")]
    ])


def doit13_16_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 13", callback_data="doit_d13"),
         InlineKeyboardButton(text="Задание 14", callback_data="doit_d14")],
        [InlineKeyboardButton(text="Задание 15", callback_data="doit_d15"),
         InlineKeyboardButton(text="Задание 16", callback_data="doit_d16")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_doit_p3"),
         InlineKeyboardButton(text="Ещё задания", callback_data="next_to_doit_p5")]
    ])


def doit17_20_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 17", callback_data="doit_d17"),
         InlineKeyboardButton(text="Задание 18", callback_data="doit_d18")],
        [InlineKeyboardButton(text="Задание 19", callback_data="doit_d19"),
         InlineKeyboardButton(text="Задание 20", callback_data="doit_d20")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_doit_p4")]
    ])


def orbita_quiz1() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="answer_true_oq1"),
         InlineKeyboardButton(text="б", callback_data="false_oq1")],
        [InlineKeyboardButton(text="в", callback_data="false_oq1")]
    ])


def orbita_quiz2() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_oq2"),
         InlineKeyboardButton(text="б", callback_data="answer_true_oq2")],
        [InlineKeyboardButton(text="в", callback_data="false_oq2")]
    ])


def orbita_quiz3() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="answer_true_oq3"),
         InlineKeyboardButton(text="б", callback_data="false_oq3")],
        [InlineKeyboardButton(text="в", callback_data="false_oq3")]
    ])


def orbita_quiz4() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_oq4"),
         InlineKeyboardButton(text="б", callback_data="false_oq")],
        [InlineKeyboardButton(text="в", callback_data="answer_true_oq4")]
    ])


def orbita_quiz5() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_oq5"),
         InlineKeyboardButton(text="б", callback_data="answer_true_oq5")],
        [InlineKeyboardButton(text="в", callback_data="false_oq5")]
    ])


def orbita_quiz6() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_oq6"),
         InlineKeyboardButton(text="б", callback_data="false_oq6")],
        [InlineKeyboardButton(text="в", callback_data="answer_true_oq")]
    ])


def orbita_quiz7() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="answer_true_oq7"),
         InlineKeyboardButton(text="б", callback_data="false_oq7")],
        [InlineKeyboardButton(text="в", callback_data="false_oq7")]
    ])


def orbita_quiz8() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_oq8"),
         InlineKeyboardButton(text="б", callback_data="false_oq8")],
        [InlineKeyboardButton(text="в", callback_data="answer_true_oq8")]
    ])


def orbita_quiz9() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_oq9"),
         InlineKeyboardButton(text="б", callback_data="answer_true_oq9")],
        [InlineKeyboardButton(text="в", callback_data="false_oq9")]
    ])


def orbita_quiz10() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_oq10"),
         InlineKeyboardButton(text="б", callback_data="false_oq10")],
        [InlineKeyboardButton(text="в", callback_data="answer_true_oq10")]
    ])


def orblearn1_4_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="orblearn_ol1"),
         InlineKeyboardButton(text="Задание 2", callback_data="orblearn_ol2")]
    ])


def llearn1_4_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="llearn_ll1"),
         InlineKeyboardButton(text="Задание 2", callback_data="llearn_ll2")]
    ])


def odoit1_4_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="odoit_od1"),
         InlineKeyboardButton(text="Задание 2", callback_data="odoit_od2")],
        [InlineKeyboardButton(text="Задание 3", callback_data="odoit_od3")]
    ])


def ldoit1_4_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="ldoit_ld1"),
         InlineKeyboardButton(text="Задание 2", callback_data="ldoit_ld2")],
        [InlineKeyboardButton(text="Задание 3", callback_data="ldoit_ld3")]
    ])


def oquiz1_4_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="oquiz_oq1"),
         InlineKeyboardButton(text="Задание 2", callback_data="oquiz_oq2")],
        [InlineKeyboardButton(text="Задание 3", callback_data="oquiz_oq3"),
         InlineKeyboardButton(text="Задание 4", callback_data="oquiz_oq4")],
        [InlineKeyboardButton(text="Ещё задания", callback_data="next_to_oquiz_p2")]
    ])


def oquiz5_8_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 5", callback_data="oquiz_oq5"),
         InlineKeyboardButton(text="Задание 6", callback_data="oquiz_oq6")],
        [InlineKeyboardButton(text="Задание 7", callback_data="oquiz_oq7"),
         InlineKeyboardButton(text="Задание 8", callback_data="oquiz_oq8")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_oquiz_p1"),
         InlineKeyboardButton(text="Ещё задания", callback_data="next_to_oquiz_p3")]
    ])


def oquiz9_12_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 9", callback_data="oquiz_oq9"),
         InlineKeyboardButton(text="Задание 10", callback_data="oquiz_oq10")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_oquiz_p2"),
         InlineKeyboardButton(text="Ещё задания", callback_data="next_to_oquiz_p4")]
    ])


def lquiz1_4_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="lquiz_lq1"),
         InlineKeyboardButton(text="Задание 2", callback_data="lquiz_lq2")],
        [InlineKeyboardButton(text="Задание 3", callback_data="lquiz_lq3"),
         InlineKeyboardButton(text="Задание 4", callback_data="lquiz_lq4")],
        [InlineKeyboardButton(text="Ещё задания", callback_data="next_to_lquiz_p2")]
    ])


def lquiz5_8_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 5", callback_data="lquiz_lq5"),
         InlineKeyboardButton(text="Задание 6", callback_data="lquiz_lq6")],
        [InlineKeyboardButton(text="Задание 7", callback_data="lquiz_lq7"),
         InlineKeyboardButton(text="Задание 8", callback_data="lquiz_lq8")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_lquiz_p1"),
         InlineKeyboardButton(text="Ещё задания", callback_data="next_to_lquiz_p3")]
    ])


def lquiz9_12_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 9", callback_data="lquiz_kq9"),
         InlineKeyboardButton(text="Задание 10", callback_data="lquiz_kq10")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_lquiz_p2"),
         InlineKeyboardButton(text="Ещё задания", callback_data="next_to_lquiz_p4")]
    ])

def lotus_quiz1() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="answer_true_lq1"),
         InlineKeyboardButton(text="б", callback_data="false_lq1")],
        [InlineKeyboardButton(text="в", callback_data="false_lq1")]
    ])


def lotus_quiz2() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_lq2"),
         InlineKeyboardButton(text="б", callback_data="false_lq2")],
        [InlineKeyboardButton(text="в", callback_data="answer_true_lq2"),
         InlineKeyboardButton(text="г", callback_data="false_lq2")]
    ])


def lotus_quiz3() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_lq3"),
         InlineKeyboardButton(text="б", callback_data="answer_true_lq3")],
        [InlineKeyboardButton(text="в", callback_data="false_lq3"),
         InlineKeyboardButton(text="г", callback_data="false_lq3")]
    ])


def lotus_quiz4() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_lq4"),
         InlineKeyboardButton(text="б", callback_data="false_lq4")],
        [InlineKeyboardButton(text="в", callback_data="answer_true_lq4")]
    ])


def lotus_quiz5() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_lq5"),
         InlineKeyboardButton(text="б", callback_data="false_lq5")],
        [InlineKeyboardButton(text="в", callback_data="false_lq5"),
         InlineKeyboardButton(text="г", callback_data="answer_true_lq5")]
    ])


def lotus_quiz6() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_lq6"),
         InlineKeyboardButton(text="б", callback_data="answer_true_lq6")],
        [InlineKeyboardButton(text="в", callback_data="false_lq6")]
    ])


def lotus_quiz7() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_lq7"),
         InlineKeyboardButton(text="б", callback_data="answer_true_lq7")],
        [InlineKeyboardButton(text="в", callback_data="false_lq7")]
    ])


def lotus_quiz8() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="answer_true_lq8"),
         InlineKeyboardButton(text="б", callback_data="false_lq8")],
        [InlineKeyboardButton(text="в", callback_data="false_lq8")]
    ])


def lotus_quiz9() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="answer_true_lq9"),
         InlineKeyboardButton(text="б", callback_data="false_lq9")],
        [InlineKeyboardButton(text="в", callback_data="false_lq9")]
    ])


def lotus_quiz10() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_lq10"),
         InlineKeyboardButton(text="б", callback_data="false_lq10")],
        [InlineKeyboardButton(text="в", callback_data="answer_true_lq10")]
    ])

def irl_lotos_ready() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="lotosirl_lirl1"),
         InlineKeyboardButton(text="Задание 2", callback_data="lotosirl_lirl2"),
         InlineKeyboardButton(text="Задание 3", callback_data="lotosirl_lirl3")],
        [InlineKeyboardButton(text="Задание 4", callback_data="lotosirl_lirl4"),
         InlineKeyboardButton(text="Задание 5", callback_data="lotosirl_lirl5"),
         InlineKeyboardButton(text="Задание 6", callback_data="lotosirl_lirl6")]
    ])


def irl_kosmeya_ready() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="kosmeyairl_kirl1"),
         InlineKeyboardButton(text="Задание 2", callback_data="kosmeyairl_kirl2"),
         InlineKeyboardButton(text="Задание 3", callback_data="kosmeyairl_kirl3")],
        [InlineKeyboardButton(text="Задание 4", callback_data="kosmeyairl_kirl4"),
         InlineKeyboardButton(text="Задание 5", callback_data="kosmeyairl_kirl5"),
         InlineKeyboardButton(text="Задание 6", callback_data="kosmeyairl_kirl6")]
    ])


def kquiz1_4_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="kquiz_kq1"),
         InlineKeyboardButton(text="Задание 2", callback_data="kquiz_kq2")],
        [InlineKeyboardButton(text="Задание 3", callback_data="kquiz_kq3"),
         InlineKeyboardButton(text="Задание 4", callback_data="kquiz_kq4")],
        [InlineKeyboardButton(text="Ещё задания", callback_data="next_to_kquiz_p2")]
    ])


def kquiz5_8_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 5", callback_data="kquiz_kq5"),
         InlineKeyboardButton(text="Задание 6", callback_data="kquiz_kq6")],
        [InlineKeyboardButton(text="Задание 7", callback_data="kquiz_kq7"),
         InlineKeyboardButton(text="Задание 8", callback_data="kquiz_kq8")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_kquiz_p1"),
         InlineKeyboardButton(text="Ещё задания", callback_data="next_to_kquiz_p3")]
    ])


def kquiz9_12_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 9", callback_data="kquiz_kq9"),
         InlineKeyboardButton(text="Задание 10", callback_data="kquiz_kq10")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_kquiz_p2"),
         InlineKeyboardButton(text="Ещё задания", callback_data="next_to_kquiz_p4")]
    ])


def kosmeya_quiz1() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="answer_true_kq1"),
         InlineKeyboardButton(text="б", callback_data="false_kq1")],
        [InlineKeyboardButton(text="в", callback_data="false_kq1")]
    ])


def kosmeya_quiz2() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="answer_true_kq2"),
         InlineKeyboardButton(text="б", callback_data="false_kq2")],
        [InlineKeyboardButton(text="в", callback_data="false_kq2")]
    ])


def kosmeya_quiz3() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="answer_true_kq3"),
         InlineKeyboardButton(text="б", callback_data="false_kq3")],
        [InlineKeyboardButton(text="в", callback_data="false_kq3"),
         InlineKeyboardButton(text="г", callback_data="false_kq3")]
    ])


def kosmeya_quiz4() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="answer_true_kq4"),
         InlineKeyboardButton(text="б", callback_data="false_kq4")],
        [InlineKeyboardButton(text="в", callback_data="false_kq4")]
    ])


def kosmeya_quiz5() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="answer_true_kq5"),
         InlineKeyboardButton(text="б", callback_data="false_kq5")],
        [InlineKeyboardButton(text="в", callback_data="false_kq5")]
    ])


def kosmeya_quiz6() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="answer_true_kq6"),
         InlineKeyboardButton(text="б", callback_data="false_kq6")],
        [InlineKeyboardButton(text="в", callback_data="false_kq6")]
    ])


def kosmeya_quiz7() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="answer_true_kq7"),
         InlineKeyboardButton(text="б", callback_data="false_kq7")],
        [InlineKeyboardButton(text="в", callback_data="false_kq7")]
    ])


def kosmeya_quiz8() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="answer_true_kq8"),
         InlineKeyboardButton(text="б", callback_data="false_kq8")],
        [InlineKeyboardButton(text="в", callback_data="false_kq8")]
    ])


def kosmeya_quiz9() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="answer_true_kq9"),
         InlineKeyboardButton(text="б", callback_data="false_kq9")],
        [InlineKeyboardButton(text="в", callback_data="false_kq9")]
    ])


def kosmeya_quiz10() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="answer_true_kq10"),
         InlineKeyboardButton(text="б", callback_data="false_kq10")],
        [InlineKeyboardButton(text="в", callback_data="false_kq10")]
    ])


def kdoit1_4_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="kdoit_kd1"),
         InlineKeyboardButton(text="Задание 2", callback_data="kdoit_kd2")],
        [InlineKeyboardButton(text="Задание 3", callback_data="kdoit_kd3")]
    ])


def klearn1_4_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="klearn_kl1"),
         InlineKeyboardButton(text="Задание 2", callback_data="klearn_kl2")]
    ])


############################################################################
###############################
#############################


def irl_sv_ready() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="sevvenirl_svirl1"),
         InlineKeyboardButton(text="Задание 2", callback_data="sevvenirl_svirl2"),
         InlineKeyboardButton(text="Задание 3", callback_data="sevvenirl_svirl3")],
        [InlineKeyboardButton(text="Задание 4", callback_data="sevvenirl_svirl4"),
         InlineKeyboardButton(text="Задание 5", callback_data="sevvenirl_svirl5"),
         InlineKeyboardButton(text="Задание 6", callback_data="sevvenirl_svirl6")]
    ])


def svquiz1_4_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="svquiz_kq1"),
         InlineKeyboardButton(text="Задание 2", callback_data="svquiz_kq2")],
        [InlineKeyboardButton(text="Задание 3", callback_data="svquiz_kq3"),
         InlineKeyboardButton(text="Задание 4", callback_data="svquiz_kq4")],
        [InlineKeyboardButton(text="Ещё задания", callback_data="next_to_svquiz_p2")]
    ])


def svquiz5_8_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 5", callback_data="svquiz_svq5"),
         InlineKeyboardButton(text="Задание 6", callback_data="svquiz_svq6")],
        [InlineKeyboardButton(text="Задание 7", callback_data="svquiz_svq7"),
         InlineKeyboardButton(text="Задание 8", callback_data="svquiz_svq8")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_svquiz_p1"),
         InlineKeyboardButton(text="Ещё задания", callback_data="next_to_svquiz_p3")]
    ])


def svquiz9_12_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 9", callback_data="svquiz_svq9"),
         InlineKeyboardButton(text="Задание 10", callback_data="svquiz_svq10")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_svquiz_p2"),
         InlineKeyboardButton(text="Ещё задания", callback_data="next_to_svquiz_p4")]
    ])


def sv_quiz1() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_svq1"),
         InlineKeyboardButton(text="б", callback_data="false_svq1")],
        [InlineKeyboardButton(text="в", callback_data="answer_true_svq1")]
    ])


def sv_quiz2() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_svq2"),
         InlineKeyboardButton(text="б", callback_data="answer_true_svq2")],
        [InlineKeyboardButton(text="в", callback_data="false_svq2")]
    ])


def sv_quiz3() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="answer_true_svq3"),
         InlineKeyboardButton(text="б", callback_data="false_svq3")],
        [InlineKeyboardButton(text="в", callback_data="false_svq3")]
    ])


def sv_quiz4() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_svq4"),
         InlineKeyboardButton(text="б", callback_data="answer_true_svq4")],
        [InlineKeyboardButton(text="в", callback_data="false_svq4")]
    ])


def sv_quiz5() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_svq5"),
         InlineKeyboardButton(text="б", callback_data="false_svq5")],
        [InlineKeyboardButton(text="в", callback_data="answer_true_svq5")]
    ])


def sv_quiz6() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="answer_true_svq6"),
         InlineKeyboardButton(text="б", callback_data="false_svq6")],
        [InlineKeyboardButton(text="в", callback_data="false_svq6")]
    ])


def sv_quiz7() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_svq7"),
         InlineKeyboardButton(text="б", callback_data="answer_true_svq7")],
        [InlineKeyboardButton(text="в", callback_data="false_svq7")]
    ])


def sv_quiz8() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_svq8"),
         InlineKeyboardButton(text="б", callback_data="false_svq8")],
        [InlineKeyboardButton(text="в", callback_data="answer_true_svq8")]
    ])


def sv_quiz9() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_svq9"),
         InlineKeyboardButton(text="б", callback_data="answer_true_svq9")],
        [InlineKeyboardButton(text="в", callback_data="false_svq9")]
    ])


def sv_quiz10() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="answer_true_svq10"),
         InlineKeyboardButton(text="б", callback_data="false_svq10")],
        [InlineKeyboardButton(text="в", callback_data="false_svqq0")]
    ])


def svdoit1_4_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="svdoit_svd1"),
         InlineKeyboardButton(text="Задание 2", callback_data="svdoit_svd2")],
        [InlineKeyboardButton(text="Задание 3", callback_data="svdoit_svd3")]
    ])


def svlearn1_4_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="svlearn_svl1"),
         InlineKeyboardButton(text="Задание 2", callback_data="svlearn_svl2")]
    ])


def orblink() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Наша группа ВК", url='https://vk.com/spo_orbita')
    ]])

def kosmeyalink() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Наша группа ВК", url='https://vk.com/ssho_kosmeya')
         ]])

def atomlink() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Наша группа ВК", url='https://vk.com/smedo_atom')
         ]])

def svlink() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Наша группа ВК", url='https://vk.com/nord_venice')
         ]])

def edemlink() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Наша группа ВК", url='https://vk.com/sso_eden')
         ]])

def lotoslink() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Наша группа ВК", url='https://vk.com/soplotos')
         ]])

def shtablink() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Наша группа ВК", url='https://vk.com/so_spbsut')
         ]])

def link1() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Наша группа ВК", url='https://vk.com/spbso')
         ]])

def link2() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Наша группа ВК", url='https://vk.com/rso_official')
         ]])

def link3() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Наш канал в ТГ", url='https://t.me/rso_official')
         ]])

def subs1_4_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="subs_s1"),
         InlineKeyboardButton(text="Задание 2", callback_data="subs_s2")],
        [InlineKeyboardButton(text="Задание 3", callback_data="subs_s3"),
         InlineKeyboardButton(text="Задание 4", callback_data="subs_s4")],
        [InlineKeyboardButton(text="Ещё задания", callback_data="next_to_subs_p2")]
    ])


def subs5_8_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 5", callback_data="subs_s5"),
         InlineKeyboardButton(text="Задание 6", callback_data="subs_s6")],
        [InlineKeyboardButton(text="Задание 7", callback_data="subs_s7"),
         InlineKeyboardButton(text="Задание 8", callback_data="subs_s8")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_subs_p1"),
         InlineKeyboardButton(text="Ещё задания", callback_data="next_to_subs_p3")]
    ])


def subs9_12_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 9", callback_data="subs_s9"),
         InlineKeyboardButton(text="Задание 10", callback_data="subs_s10")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_subs_p2"),
         InlineKeyboardButton(text="Ещё задания", callback_data="next_to_subs_p4")]
    ])

def anketa() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Заполнить заявку", url='https://vk.com/app6013442_-216336347?form_id=1#form_id=1')
         ]])

def publiclinks() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Штаб СПБГУТ', url='https://vk.com/so_spbsut')],
        [InlineKeyboardButton(text='СПО Северная Венеция', url='https://vk.com/venice_of_the_north')],
        [InlineKeyboardButton(text='Штаб СПБГУТ', url='https://vk.com/so_spbsut')],
        [InlineKeyboardButton(text='Штаб СПБГУТ', url='https://vk.com/so_spbsut')],
        [InlineKeyboardButton(text='Штаб СПБГУТ', url='https://vk.com/so_spbsut')],
        [InlineKeyboardButton(text='Штаб СПБГУТ', url='https://vk.com/so_spbsut')],
        [InlineKeyboardButton(text='Штаб СПБГУТ', url='https://vk.com/so_spbsut')],
        [InlineKeyboardButton(text='Штаб СПБГУТ', url='https://vk.com/so_spbsut')],
        [InlineKeyboardButton(text='Штаб СПБГУТ', url='https://vk.com/so_spbsut')],
        [InlineKeyboardButton(text='Штаб СПБГУТ', url='https://vk.com/so_spbsut')],
    ])

def irl_a_ready() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="atomirl_airl1"),
         InlineKeyboardButton(text="Задание 2", callback_data="atomirl_airl2"),
         InlineKeyboardButton(text="Задание 3", callback_data="atomirl_airl3")],
        [InlineKeyboardButton(text="Задание 4", callback_data="atomirl_airl4"),
         InlineKeyboardButton(text="Задание 5", callback_data="atomirl_airl5"),
         InlineKeyboardButton(text="Задание 6", callback_data="atomirl_airl6")]
    ])


def aquiz1_4_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="aquiz_aq1"),
         InlineKeyboardButton(text="Задание 2", callback_data="aquiz_aq2")],
        [InlineKeyboardButton(text="Задание 3", callback_data="aquiz_aq3"),
         InlineKeyboardButton(text="Задание 4", callback_data="aquiz_aq4")],
        [InlineKeyboardButton(text="Ещё задания", callback_data="next_to_aquiz_p2")]
    ])


def aquiz5_8_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 5", callback_data="aquiz_aq5"),
         InlineKeyboardButton(text="Задание 6", callback_data="aquiz_aq6")],
        [InlineKeyboardButton(text="Задание 7", callback_data="aquiz_aq7"),
         InlineKeyboardButton(text="Задание 8", callback_data="aquiz_aq8")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_aquiz_p1"),
         InlineKeyboardButton(text="Ещё задания", callback_data="next_to_aquiz_p3")]
    ])


def aquiz9_12_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 9", callback_data="aquiz_kq9"),
         InlineKeyboardButton(text="Задание 10", callback_data="aquiz_kq10")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_aquiz_p2"),
         InlineKeyboardButton(text="Ещё задания", callback_data="next_to_aquiz_p4")]
    ])


def a_quiz1() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_aq1"),
         InlineKeyboardButton(text="б", callback_data="false_aq1")],
        [InlineKeyboardButton(text="в", callback_data="answer_true_aq1")]
    ])


def a_quiz2() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_aq2"),
         InlineKeyboardButton(text="б", callback_data="answer_true_aq2")],
        [InlineKeyboardButton(text="в", callback_data="false_aq2")]
    ])


def a_quiz3() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="answer_true_aq3"),
         InlineKeyboardButton(text="б", callback_data="false_aq3")],
        [InlineKeyboardButton(text="в", callback_data="false_aq3")]
    ])


def a_quiz4() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_aq4"),
         InlineKeyboardButton(text="б", callback_data="answer_true_aq4")],
        [InlineKeyboardButton(text="в", callback_data="false_aq4")]
    ])


def a_quiz5() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_aq5"),
         InlineKeyboardButton(text="б", callback_data="false_aq5")],
        [InlineKeyboardButton(text="в", callback_data="answer_true_aq5")]
    ])


def a_quiz6() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="answer_true_aq6"),
         InlineKeyboardButton(text="б", callback_data="false_aq6")],
        [InlineKeyboardButton(text="в", callback_data="false_aq6")]
    ])


def a_quiz7() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_aq7"),
         InlineKeyboardButton(text="б", callback_data="answer_true_aq7")],
        [InlineKeyboardButton(text="в", callback_data="false_aq7")]
    ])


def a_quiz8() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_aq8"),
         InlineKeyboardButton(text="б", callback_data="false_aq8")],
        [InlineKeyboardButton(text="в", callback_data="answer_true_aq8")]
    ])


def a_quiz9() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_aq9"),
         InlineKeyboardButton(text="б", callback_data="answer_true_aq9")],
        [InlineKeyboardButton(text="в", callback_data="false_aq9")]
    ])


def a_quiz10() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="answer_true_aq10"),
         InlineKeyboardButton(text="б", callback_data="answer_true_aq10")],
        [InlineKeyboardButton(text="в", callback_data="answer_true_aq10")]
    ])


def adoit1_4_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="adoit_ad1"),
         InlineKeyboardButton(text="Задание 2", callback_data="adoit_ad2")],
        [InlineKeyboardButton(text="Задание 3", callback_data="adoit_ad3")]
    ])


def alearn1_4_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="alearn_al1"),
         InlineKeyboardButton(text="Задание 2", callback_data="alearn_al2")]
    ])

def irl_e_ready() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="edemirl_eirl1"),
         InlineKeyboardButton(text="Задание 2", callback_data="edemirl_eirl2"),
         InlineKeyboardButton(text="Задание 3", callback_data="edemirl_eirl3")],
        [InlineKeyboardButton(text="Задание 4", callback_data="edemirl_eirl4"),
         InlineKeyboardButton(text="Задание 5", callback_data="edemirl_eirl5"),
         InlineKeyboardButton(text="Задание 6", callback_data="edemirl_eirl6")]
    ])


def equiz1_4_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="equiz_eq1"),
         InlineKeyboardButton(text="Задание 2", callback_data="equiz_eq2")],
        [InlineKeyboardButton(text="Задание 3", callback_data="equiz_eq3"),
         InlineKeyboardButton(text="Задание 4", callback_data="equiz_eq4")],
        [InlineKeyboardButton(text="Ещё задания", callback_data="next_to_equiz_p2")]
    ])


def equiz5_8_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 5", callback_data="equiz_eq5"),
         InlineKeyboardButton(text="Задание 6", callback_data="equiz_eq6")],
        [InlineKeyboardButton(text="Задание 7", callback_data="equiz_eq7"),
         InlineKeyboardButton(text="Задание 8", callback_data="equiz_eq8")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_equiz_p1"),
         InlineKeyboardButton(text="Ещё задания", callback_data="next_to_equiz_p3")]
    ])


def equiz9_12_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 9", callback_data="equiz_eq9"),
         InlineKeyboardButton(text="Задание 10", callback_data="equiz_eq10")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_equiz_p2"),
         InlineKeyboardButton(text="Ещё задания", callback_data="next_to_equiz_p4")]
    ])


def e_quiz1() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_eq1"),
         InlineKeyboardButton(text="б", callback_data="answer_true_eq1")],
        [InlineKeyboardButton(text="в", callback_data="false_eq1")]
    ])


def e_quiz2() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_eq2"),
         InlineKeyboardButton(text="б", callback_data="false_eq2")],
        [InlineKeyboardButton(text="в", callback_data="answer_true_eq2")]
    ])


def e_quiz3() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_eq3"),
         InlineKeyboardButton(text="б", callback_data="answer_true_eq3")],
        [InlineKeyboardButton(text="в", callback_data="false_eq3")]
    ])


def e_quiz4() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_eq4"),
         InlineKeyboardButton(text="б", callback_data="false_eq4")],
        [InlineKeyboardButton(text="в", callback_data="answer_true_eq4")]
    ])


def e_quiz5() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="answer_true_eq5"),
         InlineKeyboardButton(text="б", callback_data="false_eq5")],
        [InlineKeyboardButton(text="в", callback_data="false_eq5")]
    ])


def e_quiz6() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_eq6"),
         InlineKeyboardButton(text="б", callback_data="false_eq6")],
        [InlineKeyboardButton(text="в", callback_data="answer_true_eq6")]
    ])


def e_quiz7() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_eq7"),
         InlineKeyboardButton(text="б", callback_data="false_eq7")],
        [InlineKeyboardButton(text="в", callback_data="answer_true_eq6")]
    ])


def e_quiz8() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="answer_true_eq8"),
         InlineKeyboardButton(text="б", callback_data="false_eq8")],
        [InlineKeyboardButton(text="в", callback_data="false_eq8")]
    ])


def e_quiz9() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_eq9"),
         InlineKeyboardButton(text="б", callback_data="answer_true_eq9")],
        [InlineKeyboardButton(text="в", callback_data="false_eq9")]
    ])


def e_quiz10() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="а", callback_data="false_eq10"),
         InlineKeyboardButton(text="б", callback_data="answer_true_eq10")],
        [InlineKeyboardButton(text="в", callback_data="false_eq10")]
    ])


def edoit1_4_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="edoit_ed1"),
         InlineKeyboardButton(text="Задание 2", callback_data="edoit_ed2")],
        [InlineKeyboardButton(text="Задание 3", callback_data="edoit_ed3")]
    ])


def elearn1_4_() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Задание 1", callback_data="elearn_el1"),
         InlineKeyboardButton(text="Задание 2", callback_data="elearn_el2")]
    ])


def shop_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="1", callback_data="shopping_sh1"),
         InlineKeyboardButton(text="2", callback_data="shopping_sh2"),
         InlineKeyboardButton(text="3", callback_data="shopping_sh3"),
         InlineKeyboardButton(text="4", callback_data="shopping_sh4"),
         InlineKeyboardButton(text="5", callback_data="shopping_sh5")],
        [InlineKeyboardButton(text="6", callback_data="shopping_sh6"),
         InlineKeyboardButton(text="7", callback_data="shopping_sh7"),
         InlineKeyboardButton(text="8", callback_data="shopping_sh8"),
         InlineKeyboardButton(text="9", callback_data="shopping_sh9"),
         InlineKeyboardButton(text="10", callback_data="shopping_sh10")],
        [InlineKeyboardButton(text="11", callback_data="shopping_sh11"),
         InlineKeyboardButton(text="12", callback_data="shopping_sh12"),
         InlineKeyboardButton(text="13", callback_data="shopping_sh12"),
         InlineKeyboardButton(text="14", callback_data="shopping_sh14"),
         InlineKeyboardButton(text="15", callback_data="shopping_sh15")],
        [InlineKeyboardButton(text="16", callback_data="shopping_sh16"),
         InlineKeyboardButton(text="17", callback_data="shopping_sh17"),
         InlineKeyboardButton(text="18", callback_data="shopping_sh18"),
         InlineKeyboardButton(text="19", callback_data="shopping_sh19"),
         InlineKeyboardButton(text="20", callback_data="shopping_sh20")],
        [InlineKeyboardButton(text="21", callback_data="shopping_sh21"),
         InlineKeyboardButton(text="22", callback_data="shopping_sh22"),
         InlineKeyboardButton(text="23", callback_data="shopping_sh23"),
         InlineKeyboardButton(text="24", callback_data="shopping_sh24"),
         InlineKeyboardButton(text="25", callback_data="shopping_sh25")]
    ])

def buy(n) -> InlineKeyboardMarkup:
    if n == 'sh1':
        return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Купить', callback_data='sold_sh1')]])
    elif n == 'sh2':
        return InlineKeyboardMarkup(inline_keyboard=
                                    [[InlineKeyboardButton(text='Купить', callback_data='sold_sh2')]])
    elif n == 'sh3':
        return InlineKeyboardMarkup(inline_keyboard=
                                    [[InlineKeyboardButton(text='Купить', callback_data='sold_sh3')]])
    elif n == 'sh4':
        return InlineKeyboardMarkup(inline_keyboard=
                                    [[InlineKeyboardButton(text='Купить', callback_data='sold_sh4')]])
    elif n == 'sh5':
        return InlineKeyboardMarkup(inline_keyboard=
                                [[InlineKeyboardButton(text='Купить', callback_data='sold_sh5')]])
    elif n == 'sh6':
        return InlineKeyboardMarkup(inline_keyboard=
                                    [[InlineKeyboardButton(text='Купить', callback_data='sold_sh6')]])
    elif n == 'sh7':
        return InlineKeyboardMarkup(inline_keyboard=
                                    [[InlineKeyboardButton(text='Купить', callback_data='sold_sh7')]])
    elif n == 'sh8':
        return InlineKeyboardMarkup(inline_keyboard=
                                   [[InlineKeyboardButton(text='Купить', callback_data='sold_sh8')]])
    elif n == 'sh9':
        return InlineKeyboardMarkup(inline_keyboard=
                                    [[InlineKeyboardButton(text='Купить', callback_data='sold_sh9')]])
    elif n == 'sh10':
        return InlineKeyboardMarkup(inline_keyboard=
                                    [[InlineKeyboardButton(text='Купить', callback_data='sold_sh10')]])
    elif n == 'sh11':
        return InlineKeyboardMarkup(inline_keyboard=
                                    [[InlineKeyboardButton(text='Купить', callback_data='sold_sh11')]])
    elif n == 'sh12':
        return InlineKeyboardMarkup(inline_keyboard=
                                    [[InlineKeyboardButton(text='Купить', callback_data='sold_sh12')]])
    elif n == 'sh13':
        return InlineKeyboardMarkup(inline_keyboard=
                                    [[InlineKeyboardButton(text='Купить', callback_data='sold_sh13')]])
    elif n == 'sh14':
        return InlineKeyboardMarkup(inline_keyboard=
                                    [[InlineKeyboardButton(text='Купить', callback_data='sold_sh14')]])
    elif n == 'sh15':
        return InlineKeyboardMarkup(inline_keyboard=
                                    [[InlineKeyboardButton(text='Купить', callback_data='sold_sh15')]])
    elif n == 'sh16':
        return InlineKeyboardMarkup(inline_keyboard=
                                    [[InlineKeyboardButton(text='Купить', callback_data='sold_sh16')]])
    elif n == 'sh17':
        return InlineKeyboardMarkup(inline_keyboard=
                                    [[InlineKeyboardButton(text='Купить', callback_data='sold_sh17')]])
    elif n == 'sh18':
        return InlineKeyboardMarkup(inline_keyboard=
                                    [[InlineKeyboardButton(text='Купить', callback_data='sold_sh18')]])
    elif n == 'sh19':
        return InlineKeyboardMarkup(inline_keyboard=
                                    [[InlineKeyboardButton(text='Купить', callback_data='sold_sh19')]])
    elif n == 'sh20':
        return InlineKeyboardMarkup(inline_keyboard=
                                    [[InlineKeyboardButton(text='Купить', callback_data='sold_sh20')]])
    elif n == 'sh21':
        return InlineKeyboardMarkup(inline_keyboard=
                                    [[InlineKeyboardButton(text='Купить', callback_data='sold_sh21')]])
    elif n == 'sh22':
        return InlineKeyboardMarkup(inline_keyboard=
                                    [[InlineKeyboardButton(text='Купить', callback_data='sold_sh22')]])
    elif n == 'sh23':
        return InlineKeyboardMarkup(inline_keyboard=
                                    [[InlineKeyboardButton(text='Купить', callback_data='sold_sh23')]])
    elif n == 'sh24':
        return InlineKeyboardMarkup(inline_keyboard=
                                    [[InlineKeyboardButton(text='Купить', callback_data='sold_sh24')]])
    elif n == 'sh25':
        return InlineKeyboardMarkup(inline_keyboard=
                                    [[InlineKeyboardButton(text='Купить', callback_data='sold_sh25')]])


def done(user_id, quiz) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅", callback_data=f"done_{user_id}_{quiz}"),
         InlineKeyboardButton(text="❌", callback_data=f"not_done_{user_id}_{quiz}")]
         ])

def verify(user_id) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅", callback_data=f"verify_done_{user_id}"),
         InlineKeyboardButton(text="❌", callback_data=f"verify_failed_{user_id}")]
    ])

def videolink1() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Посмотреть видео", url="https://vk.com/video-216336347_456239050")]])

def videolink2() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Посмотреть видео", url="https://vk.com/video-30684004_456239841")]])

def videolink3() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Посмотреть видео", url="https://vk.com/video-219159801_456239042")]])

def videolink4() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Посмотреть видео", url="https://vk.com/video-30684004_456239824")]])

def videolink5() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Посмотреть видео", url="https://vk.com/video-30684004_456239846")]])

def videolink6() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Посмотреть видео", url="https://vk.com/video-30684004_456239845")]])

def videolink7() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Посмотреть видео", url="https://vk.com/video-216045400_456239018")]])

def videolink8() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Посмотреть видео", url="https://vk.com/clip-216336347_456239017?c=1")]])

def videolink9() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Посмотреть видео", url="https://vk.com/clip-216336347_456239105?c=1")]])

def videolink10() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Посмотреть видео", url="https://vk.com/clip-216336347_456239041?c=1")]])

