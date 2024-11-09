import asyncio
import datetime
from typing import Union, Callable, Any, Awaitable

from aiogram import Router, types, F, BaseMiddleware
from app.keyboards import (type_quests_list_online_special_l, type_quests_list_online_special_r,
                           oquiz1_4_, orbita_quiz1, orbita_quiz2, orbita_quiz3, orbita_quiz4, orbita_quiz5, orbita_quiz6, orbita_quiz7,
                           orbita_quiz8, orbita_quiz9, orbita_quiz10, oquiz5_8_, oquiz9_12_, odoit1_4_, ldoit1_4_, irl_orbita_ready, get_type_of_quest_special, orblearn1_4_, lotus_quiz1, lotus_quiz2, lotus_quiz3, lotus_quiz4, lotus_quiz5, lotus_quiz6, lotus_quiz7, lotus_quiz8, lotus_quiz9, lotus_quiz10, lquiz9_12_, lquiz1_4_, lquiz5_8_, llearn1_4_, irl_lotos_ready, klearn1_4_, kosmeya_quiz10, kosmeya_quiz1, irl_kosmeya_ready, kosmeya_quiz2, kosmeya_quiz3, kosmeya_quiz4, kosmeya_quiz5, kosmeya_quiz6, kosmeya_quiz7, kosmeya_quiz8, kosmeya_quiz9, kquiz1_4_, kquiz5_8_, kquiz9_12_, kdoit1_4_, sv_quiz1, sv_quiz2, sv_quiz3,sv_quiz4,sv_quiz5,sv_quiz6,sv_quiz7,sv_quiz8,sv_quiz9,sv_quiz10,svquiz1_4_,svquiz5_8_,svquiz9_12_,svlearn1_4_,svdoit1_4_,irl_sv_ready, a_quiz1, a_quiz2, a_quiz3, a_quiz4, a_quiz5, a_quiz6, a_quiz7, a_quiz8, a_quiz9, a_quiz10, aquiz1_4_, aquiz9_12_, aquiz5_8_, alearn1_4_, adoit1_4_, irl_e_ready, irl_a_ready, e_quiz1, e_quiz2, e_quiz3, e_quiz4, e_quiz5, e_quiz6, e_quiz7, e_quiz8, e_quiz9, e_quiz10, equiz1_4_, equiz9_12_, equiz5_8_, elearn1_4_, edoit1_4_, done)
from app.db_requests import (quiz_exist )
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from aiogram.types import Message, InputMediaPhoto, InputMedia

router = Router()


class Test(StatesGroup):
    answersubs = State()
    od2 = State()
    od3 = State()
    od1 = State()
    ol1 = State()
    ol2 = State()
    ld2 = State()
    ld3 = State()
    ld1 = State()
    ll1 = State()
    ll2 = State()
    kd2 = State()
    kd3 = State()
    kd1 = State()
    kl1 = State()
    kl2 = State()
    svd2 = State()
    svd3 = State()
    svd1 = State()
    svl1 = State()
    svl2 = State()
    ed2 = State()
    ed3 = State()
    ed1 = State()
    el1 = State()
    el2 = State()
    ad2 = State()
    ad3 = State()
    ad1 = State()
    al1 = State()
    al2 = State()
    dq1 = State()
    dq2 = State()
    dq3 = State()
    dq4 = State()
    dq5 = State()


lquiz1_4 = ('1.Что изображено на логотипе отряда СОП "Лотос"?'
            '\n2. Сколько нужно отработать часов, чтобы сезон считался успешно отработанным и зачтенным?'
            '\n3. В честь чего назван отряд СОП "Лотос"?'
            '\n4. Когда был основан СОП "Лотос"?')


lquiz5_8 = ('5. На каких жд направлениях бойцы отряда работали в 2023 году?'
            '\n6. Какой из командиров СОП "Лотос" был в командном составе отряда дольше остальных?'
            '\n7. Сколько лет исполнится Лотосу в следующем году?'
            '\n8. Откуда взяты цвета СОП "Лотос"?')


lquiz9_12 = ('9. В каких компаниях работал отряд? '
             '\n10. Какая традиция есть у отряда на 1 апреля в группе ВКонтакте? ')


oquiz1_4 = ('Для заданий из викторины - одна попытка, будь внимателен!'
            '\n\n1. Расшифруй что значит для Орбиты "ККК"?'
            '\n2. Когда день рождения отряда Орбиты?'
            '\n3. Какие отряды созданы бойцами Орбиты?'
            '\n4. Сколько лет отряду Орбита иполнилось в 2023 году?')


oquiz5_8 = ('5. В каком лагере работала Орбита в 2024 году?'
           '\n6. Что НЕ является традицией Орбиты?'
           '\n7. Кому принадлежит черепашка Орбитяночка?'
           '\n8. Кто был флагоносцем СПО Орбита 2023 году?')


oquiz9_12 = ('9. Какая тема на творческом конкурсе была у Орбиты в 2022 году?'
            '\n10. Какой рукой "орбитятся"?')


orblearn1_4 = ('1. Изучи группу СПО "Орбита" и скажи, сколько новых бойцов появилось в 2024 году?'
               '\n2. Перечислите 3 рубрики, которые есть в группе СПО "Орбита"?')




irl_orbita = ('Приходи на 1 этаж 1 корпуса и выполняй задания:'
        '\n\n1. Сфотографируйся с Орбиткой и выложи фото в комментарий под постом в группе СПО "Орбита".'
       '\n2. Напиши свои пожелания на "заборчике".'
       '\n3. Покрути колесо фортуны.'
       '\n4. Найди лишнее на фото.'
       '\n5. Пройди мастер-класс (3д модель).'
       '\n6. Угадай, ставили ли под этот трек флешмоб?')


otodo1_4 = ('1. Сделай селфи, где ты орбитишься и прикрепи фото к ответу.'
            '\n2. Опиши идеальный день в лагере для вожатого.'
            '\n3. Напиши название песни, которая ассоциируется у тебя с лагерем '
            'и расскажи почему ты выбрал именно ее.')


ltodo1_4 = ('1.Запиши видео-рецепт самого вкусного чая, который ты себе делаешь.'
            '\n2. Расскажи, что для тебя поездная романтика? Опиши это запахами, цветами и песней.'
            '\n3. Запиши в голосовом сообщении сигнал отправления поезда.')


llearn1_4 = ('1. Изучи группу СОП "Лотос" и назови города, которые бойцы посетили на сезоне.'
             '\n2. Изучи группу СОП "Лотос" и назови главные атрибуты проводника на сезоне.')


lirl = ('Приходи на 1 этаж 1 корпуса и выполняй задания:'
        '\n\n1. Проведи повторную проверку документов. Расскажи про вагон, как настоящий проводник.'
        '\n2. Вытяни из мешочка обычный предмет и объясни, как это можно использовать необычно.'
        '\n3. Нарисуй логотип Лотоса.'
        '\n4. Сделай фотографию с бойцами изображая цветок лотоса.'
        '\n5. Кидай красный! (закинуть флажок в ведро) '
        '\n6. Узнай, что ждет тебя с нами на сезоне, и помни, карты Таро не врут!')


@router.callback_query(F.data == 'lchoose_quiz')
async def quests_quiz_p1(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{lquiz1_4}", reply_markup=lquiz1_4_())
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('lquiz'))
async def quests_quiz1_4(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
                await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='lq1':
                await callback_query.message.answer(f'Что изображено на логотипе отряда СОП "Лотос"?\nа) поезд и цветок\nб) кружка и цветок\nв) вокзал и лепесток.', reply_markup=lotus_quiz1())
            elif callback_query.data.split('_')[-1] =='lq2':
                await callback_query.message.answer(f"Сколько нужно отработать часов, чтобы сезон считался зачтенным?\nа)350\nб)400\nв)450\nг)500", reply_markup=lotus_quiz2())
            elif callback_query.data.split('_')[-1] =='lq3':
                await callback_query.message.answer(f"В честь чего назван отряд СОП 'Лотос'?\nа)цветок\nб)поезд\nв)сеть химчисток\nг)легенда о цветке", reply_markup=lotus_quiz3())
            elif callback_query.data.split('_')[-1] =='lq4':
                await callback_query.message.answer(f"Когда был основан СОП 'Лотос'?\nа) 1 апреля\nб) 1 октября\nв) 1 февраля\nг) 1 марта;", reply_markup=lotus_quiz4())
            elif callback_query.data.split('_')[-1] =='lq5':
                await callback_query.message.answer(f"На каких направлениях бойцы отряда работали в 2023 году?\nа) Мурманск, Москва\nб)Симферополь,Адлер\nв)Симферополь, Евпатория\nг)Севастополь, Евпатория;", reply_markup=lotus_quiz5())
            elif callback_query.data.split('_')[-1] =='lq6':
                await callback_query.message.answer(f"Какой из командиров СОП 'Лотос' был в командном составе отряда дольше остальных?\nа)Часов Дмитрий\nб)Разенков Даниил\nв)Трофимушкин Максим; ", reply_markup=lotus_quiz6())
            elif callback_query.data.split('_')[-1] =='lq7':
                await callback_query.message.answer(f"Сколько лет исполнится Лотосу в следующем году?\nа)3 года\nб)5 лет\nв)4 года;", reply_markup=lotus_quiz7())
            elif callback_query.data.split('_')[-1] =='lq8':
                await callback_query.message.answer(f"Откуда взяты цвета СОП 'Лотос'?\nа)цвета поездов 'Таврия'\n б)цвета поезда 'Лотос'\n в) любимые цвета первого командира;", reply_markup=lotus_quiz8())
            elif callback_query.data.split('_')[-1] =='lq9':
                await callback_query.message.answer(f"В каких компаниях работал отряд? \nа)ФПК, ГСЭ, РБЕ\nб)ФПК, ГСЭ\nв)ГСЭ", reply_markup=lotus_quiz9())
            elif callback_query.data.split('_')[-1] =='lq10':
                await callback_query.message.answer(f"Какая традиция есть у отряда на 1 апреля в группе? \nа)становимся сетью химчисток\nб)становимся СПО вместо СОП\nв)меняем сферу деятельности", reply_markup=lotus_quiz10())
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('next_to_lquiz_p'))
async def quests_quiz_next(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if callback_query.data.split('_')[-1] =='p2':
            await callback_query.message.answer(f'{lquiz5_8}', reply_markup=lquiz5_8_())
            await callback_query.message.delete()
        if callback_query.data.split('_')[-1] =='p3':
            await callback_query.message.answer(f'{lquiz9_12}', reply_markup=lquiz9_12_())
            await callback_query.message.delete()
        await callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('back_to_lquiz_p'))
async def quests_quiz_back(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if callback_query.data.split('_')[-1] =='p1':
            await callback_query.message.answer(f'{lquiz1_4}', reply_markup=lquiz1_4_())
            await callback_query.message.delete()
        if callback_query.data.split('_')[-1] =='p2':
            await callback_query.message.answer(f'{lquiz5_8}', reply_markup=lquiz5_8_())
            await callback_query.message.delete()
        await callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data == 'orbDO_IT')
async def quests_quiz_p1(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{otodo1_4}", reply_markup=odoit1_4_())
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')



@router.callback_query(F.data.startswith('odoit'))
async def quests_quiz1_4(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='od1':
                await callback_query.message.answer(f"Сделай селфи, где ты орбитишься и прикрепи фото к ответу.")
                await state.set_state(Test.od1)
            elif callback_query.data.split('_')[-1] =='od2':
                await callback_query.message.answer(f"Опиши идеальный день в лагере для вожатого.")
                await state.set_state(Test.od2)
            elif callback_query.data.split('_')[-1] =='od3':
                await callback_query.message.answer(f"Напиши название песни, которая ассоциируется у тебя с лагерем и расскажи почему ты выбрал именно ее.")
                await state.set_state(Test.od3)
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.message(Test.od3)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(od3=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 3 задания орбиты из "Сделай это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'od3'))
    await state.clear()


@router.message(Test.od2)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(od2=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 2 задания орбиты из "Сделай это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'od2'))
    await state.clear()


@router.message(Test.od1)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(od1=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 1 задания орбиты из "Сделай это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'od1'))
    await state.clear()


@router.callback_query(F.data == 'oonline')
async def quests_online(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"Сегодня день Орбиты! Выбери тип задания",
                                                reply_markup=type_quests_list_online_special_l())
        await callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data == 'orblearn_it')
async def quests_quiz_p1(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{orblearn1_4}", reply_markup=orblearn1_4_())
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('orblearn'))
async def quests_quiz1_4(callback_query: types.CallbackQuery, state: FSMContext, bot: Bot) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='ol1':
                await callback_query.message.answer(f'Изучи группу СПО "Орбита" и скажи, сколько новых бойцов появилось в 2024 году.')
                await state.set_state(Test.ol1)
            elif callback_query.data.split('_')[-1] =='ol2':
                await callback_query.message.answer('Перечислите 3 рубрики, которые есть в группе СПО "Орбита".')
                await state.set_state(Test.ol2)
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')

@router.message(Test.ol2)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(l2=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 2 задания орбиты из "Изучи это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'ol2'))
    await state.clear()


@router.message(Test.ol1)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(l3=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 1 задания орбиты из "Изучи это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'ol1'))
    await state.clear()




@router.callback_query(F.data == 'lonline')
async def quests_online(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"Выбери тип задания", reply_markup=type_quests_list_online_special_r())
        await callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')



@router.callback_query(F.data == 'llearn_it')
async def quests_quiz_p1(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{llearn1_4}", reply_markup=llearn1_4_())
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')

@router.callback_query(F.data.startswith('llearn'))
async def quests_quiz1_4(callback_query: types.CallbackQuery, state: FSMContext, bot: Bot) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='ll1':
                await callback_query.message.answer(f'Изучи группу СОП "Лотос" и назови города, которые бойцы посетили на сезоне.')
                await state.set_state(Test.ll1)
            elif callback_query.data.split('_')[-1] =='ll2':
                await callback_query.message.answer('Изучи группу СОП "Лотос" и назови главные атрибуты проводника на сезоне.')
                await state.set_state(Test.ll2)
        await  callback_query.answer('')
    else:
        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


    @router.message(Test.ll2)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(l2=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 2 задания лотоса из "Изучи это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'll2'))
        await state.clear()


    @router.message(Test.ll1)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(l1=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 1 задания лотоса из "Изучи это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'll1'))
        await state.clear()


@router.callback_query(F.data == 'lDO_IT')
async def quests_quiz_p1(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{ltodo1_4}", reply_markup=ldoit1_4_())
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')
@router.callback_query(F.data.startswith('ldoit'))
async def quests_quiz1_4(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='ld1':
                await callback_query.message.answer(f"Запиши видео-рецепт самого вкусного чая, который ты себе делаешь.")
                await state.set_state(Test.ld1)
            elif callback_query.data.split('_')[-1] =='ld2':
                await callback_query.message.answer(f"Расскажи, что для тебя поездная романтика? Опиши это запахами, цветами и песней.")
                await state.set_state(Test.ld2)
            elif callback_query.data.split('_')[-1] =='ld3':
                await callback_query.message.answer(f"Запиши в голосовом сообщении сигнал отправления поезда.")
                await state.set_state(Test.ld3)
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.message(Test.ld3)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(ld3=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 3 задания лотоса из "Сделай это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'ld3'))
    await state.clear()


@router.message(Test.ld2)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(ld2=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 2 задания лотоса из "Сделай это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'ld2'))
    await state.clear()


@router.message(Test.ld1)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(ld1=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 1 задания лотоса из "Сделай это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'ld1'))
    await state.clear()



@router.callback_query(F.data == 'special')
async def quests_irl(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if datetime.datetime (2024, 11, 12) > datetime.datetime.today() > datetime.datetime (2024, 11, 10):
            await callback_query.message.answer('Задания отрядов будут доступны с завтрашнего дня!')
        if datetime.datetime (2024, 11, 13) > datetime.datetime.today() > datetime.datetime (2024, 11, 11) or datetime.datetime(2024, 11, 7) > datetime.datetime.today() > datetime.datetime(2024, 11, 5):
            await callback_query.message.answer('Сегодня день СПО Северная Венеция и ССО Эдем!', reply_markup=get_type_of_quest_special())
        elif datetime.datetime (2024, 11, 14) > datetime.datetime.now().today() > datetime.datetime (2024, 11, 12) or datetime.datetime(2024, 11, 8) > datetime.datetime.today() > datetime.datetime(2024, 11, 6):
            await callback_query.message.answer('Сегодня день ССхО Космея и СОП Лотос!', reply_markup=get_type_of_quest_special())
        elif datetime.datetime (2024, 11, 15) > datetime.datetime.now().today() > datetime.datetime (2024, 11, 13) or datetime.datetime(2024, 11, 9) > datetime.datetime.today() > datetime.datetime(2024, 11, 7):
            await callback_query.message.answer('Сегодня день СПО Орбита и СМедО АТОМ!', reply_markup=get_type_of_quest_special())
        await callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('lirl'))
async def quests_irl(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{lirl}\nНажми на кнопочку ниже, если выполнил задание, тогда модератор сможет подтвердить его выполнение.", reply_markup=irl_lotos_ready())
        await callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')

@router.callback_query(F.data.startswith('lotosirl_'))
async def quests_quiz1_4(callback_query: types.CallbackQuery, state: FSMContext, bot: Bot) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='lirl1':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание лотоса 1 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'lirl1'))
            elif callback_query.data.split('_')[-1] =='lirl2':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание лотоса 2 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'lirl2'))
            elif callback_query.data.split('_')[-1] =='lirl3':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание лотоса 3 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'lirl3'))
            elif callback_query.data.split('_')[-1] =='lirl4':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание лотоса 4 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'lirl4'))
            elif callback_query.data.split('_')[-1] =='lirl5':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание лотоса 5 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'lirl5'))
            elif callback_query.data.split('_')[-1] =='lirl6':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание лотоса 6 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'lirl6'))
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('oirl'))
async def quests_irl(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{irl_orbita}\nНажми на кнопочку ниже, если выполнил задание, тогда модератор сможет подтвердить его выполнение.", reply_markup=irl_orbita_ready())
        await callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('orbitairl_'))
async def quests_quiz1_4(callback_query: types.CallbackQuery, state: FSMContext, bot: Bot) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='oirl1':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание орбиты 1 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'oirl1'))
            elif callback_query.data.split('_')[-1] =='oirl2':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание орбиты 2 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'oirl2'))
            elif callback_query.data.split('_')[-1] =='oirl3':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание орбиты 3 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'oirl3'))
            elif callback_query.data.split('_')[-1] =='oirl4':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание орбиты 4 \n Проверьте его и зачислите ему BonchCoins!\n', reply_markup=done(callback_query.from_user.id, 'oirl4'))
            elif callback_query.data.split('_')[-1] =='oirl5':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание орбиты 5 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'oirl5'))
            elif callback_query.data.split('_')[-1] =='oirl6':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание орбиты 6 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'oirl6'))
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('lirl_'))
async def quests_quiz1_4(callback_query: types.CallbackQuery, state: FSMContext, bot: Bot) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='lirl1':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание лотоса 1 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'lirl1'))
            elif callback_query.data.split('_')[-1] =='lirl2':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание лотоса 2 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'lirl2'))
            elif callback_query.data.split('_')[-1] =='lirl3':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание лотоса 3 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'lirk3'))
            elif callback_query.data.split('_')[-1] =='lirl4':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание лотоса 4 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'lirl4'))
            elif callback_query.data.split('_')[-1] =='lirl5':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание лотоса 5 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'lirl5'))
            elif callback_query.data.split('_')[-1] =='lirl6':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание лотоса 6 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'lirl6'))
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data == 'orbchoose_quiz')
async def quests_quiz_p1(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{oquiz1_4}", reply_markup=oquiz1_4_())
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('oquiz'))
async def quests_quiz1_4(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='oq1':
                await callback_query.message.answer(f'Расшифруй что значит для Орбиты "ККК"?\nа) команда, качество, креатив\nб) крутые, классные, кайфовые\nв) Казанский, Колесников, Крицкий.', reply_markup=orbita_quiz1())
            elif callback_query.data.split('_')[-1] =='oq2':
                await callback_query.message.answer(f"Когда день рождения отряда Орбиты?\nа) 14 февраля\nб) 25 декабря\nв) 3 июня.", reply_markup=orbita_quiz2())
            elif callback_query.data.split('_')[-1] =='oq3':
                await callback_query.message.answer(f"Какие отряды созданы бойцами Орбиты?\nа) Космея, Атом\nб) Лотос, Северная Венецеия\nв) Эдем, Космея", reply_markup=orbita_quiz3())
            elif callback_query.data.split('_')[-1] =='oq4':
                await callback_query.message.answer(f"Сколько лет отряду Орбита иполнилось в 2023 году?\nа) 25 лет\nб) 4 года \nв) 9 лет", reply_markup=orbita_quiz4())
            elif callback_query.data.split('_')[-1] =='oq5':
                await callback_query.message.answer(f"В каком лагере работала Орбита в 2024 году?\nа) Ракета\nб) Голубая стрела\nв) Северная Зорька.", reply_markup=orbita_quiz5())
            elif callback_query.data.split('_')[-1] =='oq6':
                await callback_query.message.answer(f"Что НЕ является традицией Орбиты?\nа) петь отрядную песню в значимые моменты\nб) орбититься на фотографиях\nв) цвет кандидатского галстука - фиолетовый", reply_markup=orbita_quiz6())
            elif callback_query.data.split('_')[-1] =='oq7':
                await callback_query.message.answer(f"Кому принадлежит черепашка Орбитяночка?\nа) Оле Кузьминой\nб) Владе Томиловой\nв) Дане Труфанову", reply_markup=orbita_quiz7())
            elif callback_query.data.split('_')[-1] =='oq8':
                await callback_query.message.answer(f"Кто был флагоносцем СПО Орбита 2023 году?\nа) Егор Проскуров\nб) Наташа Жукова\nв) Никита Фирсов", reply_markup=orbita_quiz8())
            elif callback_query.data.split('_')[-1] =='oq9':
                await callback_query.message.answer(f"Какая тема на творческом конкурсе была у Орбиты в 2022 году?\nа) Коралина в стране кошмаров\nб) Симпсоны\nв) Смурфики  ", reply_markup=orbita_quiz9())
            elif callback_query.data.split('_')[-1] =='oq10':
                await callback_query.message.answer(f"Какой рукой орбитятся?\nа) правой\nб) левой\nв) без разницы.", reply_markup=orbita_quiz10())
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('next_to_oquiz_p'))
async def quests_quiz_next(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if callback_query.data.split('_')[-1] =='p2':
            await callback_query.message.answer(f'{oquiz5_8}', reply_markup=oquiz5_8_())
            await callback_query.message.delete()
        if callback_query.data.split('_')[-1] =='p3':
            await callback_query.message.answer(f'{oquiz9_12}', reply_markup=oquiz9_12_())
            await callback_query.message.delete()
        await callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')


@router.callback_query(F.data.startswith('back_to_oquiz_p'))
async def quests_quiz_back(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if callback_query.data.split('_')[-1] =='p1':
            await callback_query.message.answer(f'{oquiz1_4}', reply_markup=oquiz1_4_())
            await callback_query.message.delete()
        if callback_query.data.split('_')[-1] =='p2':
            await callback_query.message.answer(f'{oquiz5_8}', reply_markup=oquiz5_8_())
            await callback_query.message.delete()
        await callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')


kirl = ('Приходи на 1 этаж 1 корпуса и выполняй задания:'
        '\n\n1. Сыграй в бирпонг.'
        '\n2. Поиграй в настольную игру.'
        '\n3. Сыграй в крестики нолики.'
        '\n4. Скажи комплимент.'
        '\n5. Найди отличия на фотографиях.'
        '\n6. Опиши сельскохозяйственные термины.')


@router.callback_query(F.data.startswith('kirl'))
async def quests_irl(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{kirl}\nНажми на кнопочку ниже, если выполнил задание, тогда модератор сможет подтвердить его выполнение.", reply_markup=irl_kosmeya_ready())
        await callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('kosmeyairl_'))
async def quests_quiz1_4(callback_query: types.CallbackQuery, state: FSMContext, bot: Bot) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='kirl1':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание космеи 1 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'kirl1'))
            elif callback_query.data.split('_')[-1] =='kirl2':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание космеи 2 \n Проверьте его и зачислите ему BonchCoins!\n', reply_markup=done(callback_query.from_user.id, 'kirl2'))
            elif callback_query.data.split('_')[-1] =='kirl3':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание космеи 3 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'kirl3'))
            elif callback_query.data.split('_')[-1] =='kirl4':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание космеи 4 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'kirl4'))
            elif callback_query.data.split('_')[-1] =='kirl5':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание космеи 5 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'kirl5'))
            elif callback_query.data.split('_')[-1] =='kirl6':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание космеи 6 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'kirl6'))
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')


kquiz1_4 = ('Для заданий из викторины - одна попытка, будь внимателен!'
            '\n\n1. Продолжи фразу: "Хочу на море и ...'
            '\n2. Какого числа день рождение ССхО "Космея"?'
            '\n3. Что являеться талисманом ССхО "Космея"?'
            '\n4. Какое было последнее место работы ССхО "Космея"?')

kquiz5_8 = ('5. Что из этого не является традицией ССхО "Космея"?'
            '\n6. С чем на сезоне работает ССхО "Космея"?'
            '\n7. Сколько полных лет ССхО "Космея"?'
            '\n8. Кто является первым командиром ССхО "Космея"?')


kquiz9_12 = ('9. Что такое Комисарка?'
             '\n10. Кем бойцы ССхО "Космеи" являются друг для друга?')


@router.callback_query(F.data == 'kchoose_quiz')
async def quests_quiz_p1(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{kquiz1_4}", reply_markup=kquiz1_4_())
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('kquiz'))
async def quests_quiz1_4(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='kq1':
                await callback_query.message.answer(f'Продолжи фразу: "Хочу на море и ..."?\nа) арбуз\nб) в горы\nв) денег.', reply_markup=kosmeya_quiz1())
            elif callback_query.data.split('_')[-1] =='kq2':
                await callback_query.message.answer(f"Какого числа день рождение ССхО 'Космея'?\na) 14 февраля\nб) 1 сентября\nв) 11 сентября", reply_markup=kosmeya_quiz2())
            elif callback_query.data.split('_')[-1] =='kq3':
                await callback_query.message.answer(f"Какое было последнее место работы ССхО 'Космея''?\na) Абрау-Дюрсо\nб) Виноградное\nв) Золотая Балка;", reply_markup=kosmeya_quiz3())
            elif callback_query.data.split('_')[-1] =='kq4':
                await callback_query.message.answer(f"Что из этого не является традицией ССхО 'Космея'?\nа) Варить варенье на сезоне\nб) Дневник сезона\nв) Рефлексия по дню;", reply_markup=kosmeya_quiz4())
            elif callback_query.data.split('_')[-1] =='kq5':
                await callback_query.message.answer(f"С чем на сезоне работает ССхО 'Космея'?\nа) Виноград\nб)Морошка\nв)Помидоры;", reply_markup=kosmeya_quiz5())
            elif callback_query.data.split('_')[-1] =='kq6':
                await callback_query.message.answer(f"Что являеться талисманом ССхО 'Космея'?\na) Звёздочка Маруся\nб) Виноград Олег\nг) Цветочек Космо;", reply_markup=kosmeya_quiz6())
            elif callback_query.data.split('_')[-1] =='kq7':
                await callback_query.message.answer(f"Сколько полных лет ССхО 'Космея'?\na)2 года\nб) 3 года\nв) 4 года;", reply_markup=kosmeya_quiz7())
            elif callback_query.data.split('_')[-1] =='kq8':
                await callback_query.message.answer(f"Кто является первым командиром ССхО 'Космея'?\nа) Кирил Кридский\nб) Дарья Манушина\nв)Артём Николаев;", reply_markup=kosmeya_quiz8())
            elif callback_query.data.split('_')[-1] =='kq9':
                await callback_query.message.answer(f"Что такое Комисарка?\nа) Время, когда отряд объеденяется\nб) Тихий час\nв) чаепитие;", reply_markup=kosmeya_quiz9())
            elif callback_query.data.split('_')[-1] =='kq10':
                await callback_query.message.answer(f"Кем бойцы ССхО Космеи являються друг для друга?\nа) Семьёй\nб)Знакомыми\nв) Врагами;", reply_markup=kosmeya_quiz10())
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('next_to_kquiz_p'))
async def quests_quiz_next(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if callback_query.data.split('_')[-1] =='p2':
            await callback_query.message.answer(f'{kquiz5_8}', reply_markup=kquiz5_8_())
            await callback_query.message.delete()
        if callback_query.data.split('_')[-1] =='p3':
            await callback_query.message.answer(f'{kquiz9_12}', reply_markup=kquiz9_12_())
            await callback_query.message.delete()
        await callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('back_to_kquiz_p'))
async def quests_quiz_back(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if callback_query.data.split('_')[-1] =='p1':
            await callback_query.message.answer(f'{kquiz1_4}', reply_markup=kquiz1_4_())
            await callback_query.message.delete()
        if callback_query.data.split('_')[-1] =='p2':
            await callback_query.message.answer(f'{kquiz5_8}', reply_markup=kquiz5_8_())
            await callback_query.message.delete()
        await callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')

klearn1_4 = ('1. Изучи группу ССхО "Космея" и напиши сколько человек выехало на сезон 2023?'
             '\n2. Напишите название песни, записанной ССхО "Космея"?')


@router.callback_query(F.data == 'klearn_it')
async def quests_quiz_p1(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{klearn1_4}", reply_markup=klearn1_4_())
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('klearn'))
async def quests_quiz1_4(callback_query: types.CallbackQuery, state: FSMContext, bot: Bot) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='kl1':
                await callback_query.message.answer(f'Изучи группу ССхО "Космея" и напиши сколько человек выехало на сезон 2023? ')
                await state.set_state(Test.kl1)
            elif callback_query.data.split('_')[-1] =='kl2':
                await callback_query.message.answer('Напишите название песни, записанной ССхО "Космея"?')
                await state.set_state(Test.kl2)
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.message(Test.kl2)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(l2=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 2 задания космеи из "Изучи это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'kl2'))
    await state.clear()


@router.message(Test.kl1)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(l1=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 1 задания космеи из "Изучи это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'kl1'))
    await state.clear()


ktodo1_4 = ('1. Рефлексия: опиши как прошёл твой день, какие эмоции испытал и оцени свой день по 10-бальной шкале.'
         '\n2. Закосмейся и отправь фото.'
         '\n3. Нарисуй и отправь мне своё представление о сезоне ССхО "Космея".')


@router.callback_query(F.data == 'kDO_IT')
async def quests_quiz_p1(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{ktodo1_4}", reply_markup=kdoit1_4_())
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('kdoit'))
async def quests_quiz1_4(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='kd1':
                await callback_query.message.answer(f"Запиши видео-рецепт самого вкусного чая, который ты себе делаешь.")
                await state.set_state(Test.kd1)
            elif callback_query.data.split('_')[-1] =='kd2':
                await callback_query.message.answer(f"Расскажи, что для тебя поездная романтика? Опиши это запахами, цветами и песней.")
                await state.set_state(Test.kd2)
            elif callback_query.data.split('_')[-1] =='kd3':
                await callback_query.message.answer(f"Запиши в голосовом сообщении сигнал отправления поезда")
                await state.set_state(Test.kd3)
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


    @router.message(Test.kd3)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(ld3=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 3 задания космеи из "Сделай это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'kd3'))
        await state.clear()


    @router.message(Test.kd2)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(ld2=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 2 задания космеи из "Сделай это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'kd2'))
        await state.clear()


    @router.message(Test.kd1)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(ld1=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 1 задания космеи из "Сделай это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'kd1'))
        await state.clear()


@router.callback_query(F.data == 'konline')
async def quests_online(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"Выбери тип задания", reply_markup=type_quests_list_online_special_l())
        await callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')



svirl = ('Приходи на 1 этаж 1 корпуса и выполняй задания:'
        '\n\n1. Сними Reels/Clip на фотозоне. '
        '\n2. Покажи мини-танец с фонариком СПО «Северная Венеция».'
        '\n3. Поучавствуй в «Громком разговоре».'
        '\n4. Испытай судьбу и кинь кубики. '
        '\n5. Поиграй в игру «найди пару».'
        '\n6. Собери пазл.')


@router.callback_query(F.data.startswith('svirl'))
async def quests_irl(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{svirl}\nНажми на кнопочку ниже, если выполнил задание, тогда модератор сможет подтвердить его выполнение.", reply_markup=irl_sv_ready())
        await callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('sevvenirl_'))
async def quests_quiz1_4(callback_query: types.CallbackQuery, state: FSMContext, bot: Bot) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='svirl1':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание северной венеции 1 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'svirl1'))
            elif callback_query.data.split('_')[-1] =='svirl2':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание северной венеции 2 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'svirl2'))
            elif callback_query.data.split('_')[-1] =='svirl3':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание северной венеции 3 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'svirl3'))
            elif callback_query.data.split('_')[-1] =='svirl4':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание северной венеции 4 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'svirl4'))
            elif callback_query.data.split('_')[-1] =='svirl5':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание северной венеции 5 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'svirl5'))
            elif callback_query.data.split('_')[-1] =='svirl6':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание северной венеции 6 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'svirl6'))
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


svquiz1_4 = ('Для заданий из викторины - одна попытка, будь внимателен!'
            '\n\n1. Продолжи фразу "Зажигаем свет...'
            '\n2. Куда можно попасть с СПО «Северная Венеция»?'
            '\n3. В каком лагере СПО «Северная Венеция» работала летом 2024 года?'
            '\n4. В каком году создался СПО «Северная Венеция»?')


svquiz5_8 = ('5. Что изображено на флаге СПО «Северная Венеция»?'
            '\n6. На каком мероприятии бойцы СПО «Северная Венеция» точно были в сентябре?'
            '\n7. Какой рубрики НЕТ в группе СПО «Северная Венеция»?'
            '\n8. Сколько мальчиков в СПО «Северная Венеция»?')


svquiz9_12 = ('9. Самый "старый" боец СПО «Северная Венеция»?'
             '\n10. Сколько котиков в группе СПО «Северная Венеция»?')


@router.callback_query(F.data == 'svchoose_quiz')
async def quests_quiz_p1(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{svquiz1_4}", reply_markup=svquiz1_4_())
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')



@router.callback_query(F.data.startswith('svquiz'))
async def quests_quiz1_4(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='svq1':
                await callback_query.message.answer(f'Продолжи фразу "Зажигаем свет...\nа) в комнате\nб) на улице\nв)внутри', reply_markup=sv_quiz1())
            elif callback_query.data.split('_')[-1] =='svq2':
                await callback_query.message.answer(f"Куда можно попасть с СПО «Северная Венеция»?\nа) в детский лагерь\nб) в сказку\nв) в СПбГУТ ", reply_markup=sv_quiz2())
            elif callback_query.data.split('_')[-1] =='svq3':
                await callback_query.message.answer(f"В каком лагере СПО «Северная Венеция» работала летом 2024 года?\nа) ДОЛ «Зарница»\nб) ДОЛ «Молодежный»\nв) ДОЛ «Восход»", reply_markup=sv_quiz3())
            elif callback_query.data.split('_')[-1] =='svq4':
                await callback_query.message.answer(f"В каком году создался СПО «Северная Венеция»?\nа) 2017\nб)2023\nв) 2019", reply_markup=sv_quiz4())
            elif callback_query.data.split('_')[-1] =='svq5':
                await callback_query.message.answer(f"Что изображено на флаге СПО «Северная Венеция»?\nа) мосты\nб) Петропавловская крепость\nв) лодка и фонарик", reply_markup=sv_quiz5())
            elif callback_query.data.split('_')[-1] =='svq6':
                await callback_query.message.answer(f"На каком мероприятии бойцы СПО «Северная Венеция» точно были в сентябре?\nа) Вахта СПбГУТ\nб)Медиашкола\nв) день Донора", reply_markup=sv_quiz6())
            elif callback_query.data.split('_')[-1] =='svq7':
                await callback_query.message.answer(f"Какой рубрики НЕТ в группе СПО «Северная Венеция»?\nа) Методичка в кармане\nб) Отгадай бойца\nв) Северная Венеция рекомендует ", reply_markup=sv_quiz7())
            elif callback_query.data.split('_')[-1] =='svq8':
                await callback_query.message.answer(f"Сколько мальчиков в СПО «Северная Венеция»?\nа) 4\nб) 1\nв) 0", reply_markup=sv_quiz8())
            elif callback_query.data.split('_')[-1] =='svq9':
                await callback_query.message.answer(f'Самый "старый" боец СПО «Северная Венеция»?\nа) Ася Петрова\nб) Таша Крылова\nв) Ксюша Авласенко;', reply_markup=sv_quiz9())
            elif callback_query.data.split('_')[-1] =='svq10':
                await callback_query.message.answer(f"Сколько котиков в группе СПО «Северная Венеция»?\nа) 12\nб) 8\nв) 5", reply_markup=sv_quiz10())
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('next_to_svquiz_p'))
async def quests_quiz_next(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if callback_query.data.split('_')[-1] =='p2':
            await callback_query.message.answer(f'{svquiz5_8}', reply_markup=svquiz5_8_())
            await callback_query.message.delete()
        if callback_query.data.split('_')[-1] =='p3':
            await callback_query.message.answer(f'{svquiz9_12}', reply_markup=svquiz9_12_())
            await callback_query.message.delete()
        await callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('back_to_svquiz_p'))
async def quests_quiz_back(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if callback_query.data.split('_')[-1] =='p1':
            await callback_query.message.answer(f'{svquiz1_4}', reply_markup=svquiz1_4_())
            await callback_query.message.delete()
        if callback_query.data.split('_')[-1] =='p2':
            await callback_query.message.answer(f'{svquiz5_8}', reply_markup=svquiz5_8_())
            await callback_query.message.delete()
        await callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


svlearn1_4 = ('1. Изучи видеозаписи в группе СПО «Северная Венеция» и напиши название песни, которая зазвучала у Вики в наушниках'
             '\n2. Изучи клипы в группе СПО «Северная Венеция» и ответь, какой подарок от ВКонтакте выиграла Ася')


@router.callback_query(F.data == 'svlearn_it')
async def quests_quiz_p1(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{svlearn1_4}", reply_markup=svlearn1_4_())
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('svlearn'))
async def quests_quiz1_4(callback_query: types.CallbackQuery, state: FSMContext, bot: Bot) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='svl1':
                await callback_query.message.answer(f'Изучи видеозаписи в группе СПО «Северная Венеция» и напиши название песни, которая зазвучала у Вики в наушниках')
                await state.set_state(Test.svl1)
            elif callback_query.data.split('_')[-1] =='svl2':
                await callback_query.message.answer('Изучи клипы в группе СПО «Северная Венеция» и ответь, какой подарок от ВКонтакте выиграла Ася')
                await state.set_state(Test.svl2)
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.message(Test.svl2)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(svl2=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 2 задания северной венеции из "Изучи это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'svl2'))
    await state.clear()


@router.message(Test.svl1)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(sv1=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 1 задания северной венеции из "Изучи это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'svl1'))
    await state.clear()


svtodo1_4 =('1. Напиши историю на 10 предложений с 5 выдуманными персонажами, которые помогают детям преодолеть страхи.'
            '\n2. Выбери тематику смены, которая идеально подошла бы тебе и объясни почему.'
            '\n3. Сфотографируйся с кубиком в фотозоне СПО «Северная Венеция».')


@router.callback_query(F.data == 'svDO_IT')
async def quests_quiz_p1(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{svtodo1_4}", reply_markup=svdoit1_4_())
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('svdoit'))
async def quests_quiz1_4(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='svd1':
                await callback_query.message.answer(f"Напиши историю на 10 предложений с 5 выдуманными персонажами, которые помогают детям преодолеть страхи.")
                await state.set_state(Test.svd1)
            elif callback_query.data.split('_')[-1] =='svd2':
                await callback_query.message.answer(f"Выбери тематику смены, которая идеально подошла бы тебе и объясни почему.")
                await state.set_state(Test.svd2)
            elif callback_query.data.split('_')[-1] =='svd3':
                await callback_query.message.answer(f"Сфотографируйся с кубиком в фотозоне СПО «Северная Венеция».")
                await state.set_state(Test.svd3)
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.message(Test.svd3)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(svd3=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 3 задания северной венеции из "Сделай это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'svd3'))
    await state.clear()


@router.message(Test.svd2)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(svd2=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 2 задания северной венеции из "Сделай это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'svd2'))
    await state.clear()


@router.message(Test.svd1)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(svd1=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 1 задания северной венеции из "Сделай это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'svd1'))
    await state.clear()


@router.callback_query(F.data == 'svonline')
async def quests_online(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"Выбери тип задания", reply_markup=type_quests_list_online_special_l())
        await callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


eirl = ('Приходи на 1 этаж 1 корпуса и выполняй задания:'
        '\n\n1. Приходишь и звонишь родственнику и говоришь что едешь в строй отряд.'
        '\n2. Сделать башню из людей.'
        '\n3. Найди аномалии в альбоме сезона.'
        '\n4. Устроить битву на касках и залить в историю.'
        '\n5. Прийти и написать 5 людям: я поеду с ССО "Эдем" летом.'
        '\n6. Сфоткаться с флагом ССО "Эдема".')
@router.callback_query(F.data.startswith('eirl'))
async def quests_irl(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{eirl}\nНажми на кнопочку ниже, если выполнил задание, тогда модератор сможет подтвердить его выполнение.", reply_markup=irl_e_ready())
        await callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('edemirl_'))
async def quests_quiz1_4(callback_query: types.CallbackQuery, state: FSMContext, bot: Bot) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='eirl1':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание Эдема 1', reply_markup=done(callback_query.from_user.id, 'eirl1'))
            elif callback_query.data.split('_')[-1] =='eirl2':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание Эдема 2', reply_markup=done(callback_query.from_user.id, 'eirl2'))
            elif callback_query.data.split('_')[-1] =='eirl3':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание Эдема 3', reply_markup=done(callback_query.from_user.id, 'eirl3'))
            elif callback_query.data.split('_')[-1] =='eirl4':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание Эдема 4', reply_markup=done(callback_query.from_user.id, 'eirl4'))
            elif callback_query.data.split('_')[-1] =='eirl5':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание Эдема 5', reply_markup=done(callback_query.from_user.id, 'eirl5'))
            elif callback_query.data.split('_')[-1] =='eirl6':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание Эдема 6', reply_markup=done(callback_query.from_user.id, 'eirl6'))
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


equiz1_4 = ('Для заданий из викторины - одна попытка, будь внимателен!'
            '\n\n1. Сколько лет ССО «Эдем»?'
            '\n2. Какой язык используется в качестве заголовков в ССО «Эдем»?'
            '\n3. Какой фрукт-символ используется в атрибутике ССО «Эдем»?'
            '\n4. Где проходил сезон 2024 года?')


equiz5_8 = ('5. В какой компании работал ССО «Эдем» этим летом?'
            '\n6. Что означает Эдем?'
            '\n7. Кто был основателем ССО «Эдем»?'
            '\n8. С каким животным ассоциируется комиссар ССО «Эдем»?')


equiz9_12 = ('9. ССО это?'
             '\n10. Какая должность отвечает за ТБ на стройке?')


@router.callback_query(F.data == 'echoose_quiz')
async def quests_quiz_p1(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{equiz1_4}", reply_markup=equiz1_4_())
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('equiz'))
async def quests_quiz1_4(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='eq1':
                await callback_query.message.answer(f'Сколько лет ССО «Эдем»\nа) 1 год\nб) 2 года\nв) 4 года', reply_markup=e_quiz1())
            elif callback_query.data.split('_')[-1] =='eq2':
                await callback_query.message.answer(f"Какой язык используется в качестве заголовков в ССО «Эдем»\nа) Испанский\nб) Греческий\nв) Латынь", reply_markup=e_quiz2())
            elif callback_query.data.split('_')[-1] =='eq3':
                await callback_query.message.answer(f"Какой фрукт-символ используется в атрибутике ССО «Эдем»?\nа) Банан\nб) Яблоко\nв) Дракон-фрукт;", reply_markup=e_quiz3())
            elif callback_query.data.split('_')[-1] =='eq4':
                await callback_query.message.answer(f"Где проходил сезон 2024 года?\nа) Мурманск\nб) Норильск\nв) Губкинский", reply_markup=e_quiz4())
            elif callback_query.data.split('_')[-1] =='eq5':
                await callback_query.message.answer(f"В какой компании работал ССО «Эдем» этим летом?\nа) ССК\nб) СРК\nв) ЯМАЛ-СТРОЙ", reply_markup=e_quiz5())
            elif callback_query.data.split('_')[-1] =='eq6':
                await callback_query.message.answer(f"Что означает Эдем?\nа) Вознесение\nб) Дерево\nв) Райский сад", reply_markup=e_quiz6())
            elif callback_query.data.split('_')[-1] =='eq7':
                await callback_query.message.answer(f"Кто был основателем ССО «Эдем»?\nа) Никита, Миша, Оля\nб) Даня, Кирилл, Дарина\nв) Тамир, Оля, Соломон;", reply_markup=e_quiz7())
            elif callback_query.data.split('_')[-1] =='eq8':
                await callback_query.message.answer(f"С каким животным ассоциируется комиссар отряда ССО «Эдем»?\nа) Лягушка\nб) Кабан\nв) Утконос;", reply_markup=e_quiz8())
            elif callback_query.data.split('_')[-1] =='eq9':
                await callback_query.message.answer(f'ССО это?\nа) Союзное строительное общество\nб) Студенческий строительный отряд\nв) Силы специальных операций', reply_markup=e_quiz9())
            elif callback_query.data.split('_')[-1] =='eq10':
                await callback_query.message.answer(f"Какая должность отвечает за ТБ на стройке?\nа) Боец\nб) Мастер\nв) Казначей;", reply_markup=e_quiz10())
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('next_to_equiz_p'))
async def quests_quiz_next(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if callback_query.data.split('_')[-1] =='p2':
            await callback_query.message.answer(f'{equiz5_8}', reply_markup=equiz5_8_())
            await callback_query.message.delete()
        if callback_query.data.split('_')[-1] =='p3':
            await callback_query.message.answer(f'{equiz9_12}', reply_markup=equiz9_12_())
            await callback_query.message.delete()
        await callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')

@router.callback_query(F.data.startswith('back_to_equiz_p'))
async def quests_quiz_back(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if callback_query.data.split('_')[-1] =='p1':
            await callback_query.message.answer(f'{equiz1_4}', reply_markup=equiz1_4_())
            await callback_query.message.delete()
        if callback_query.data.split('_')[-1] =='p2':
            await callback_query.message.answer(f'{equiz5_8}', reply_markup=equiz5_8_())
            await callback_query.message.delete()
        await callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


elearn1_4 = ('1. Какое второе блюдо приготовил поваренок Артём?'
              '\n2. Что такое кофемолка?')


@router.callback_query(F.data == 'elearn_it')
async def quests_quiz_p1(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{elearn1_4}", reply_markup=elearn1_4_())
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('elearn'))
async def quests_quiz1_4(callback_query: types.CallbackQuery, state: FSMContext, bot: Bot) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='el1':
                await callback_query.message.answer(f'Изучи видеозаписи в группе СПО «Северная Венеция» и напиши название песни, которая зазвучала у Вики в наушниках')
                await state.set_state(Test.el1)
            elif callback_query.data.split('_')[-1] =='el2':
                await callback_query.message.answer('Изучи клипы в группе СПО «Северная Венеция» и ответь, какой подарок от ВКонтакте выиграла Ася')
                await state.set_state(Test.el2)
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.message(Test.el2)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(el2=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 2 задания Эдема из "Изучи это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'el2'))
    await state.clear()


@router.message(Test.el1)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(e1=message.from_user)
    user_name = message.from_user.username
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 1 задания Эдема из "Изучи это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'el1'))
    await state.clear()


etodo1_4 =('1. Сделать макет памятника ССО «Эдем» и отправить фото мне.'
            '\n2. Нарисовать гигантское удостоверение сварщика. (Фотография(можно нарисовать), серийный номер, подпись, компания и тд).'
            '\n3. Селфи с тотемным фруктом ССО «Эдем».')


@router.callback_query(F.data == 'eDO_IT')
async def quests_quiz_p1(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{etodo1_4}", reply_markup=edoit1_4_())
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('edoit'))
async def quests_quiz1_4(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='ed1':
                await callback_query.message.answer(f"Напиши историю на 10 предложений с 5 выдуманными персонажами, которые помогают детям преодолеть страхи.")
                await state.set_state(Test.ed1)
            elif callback_query.data.split('_')[-1] =='ed2':
                await callback_query.message.answer(f"Выбери тематику смены, которая идеально подошла бы тебе и объясни почему")
                await state.set_state(Test.ed2)
            elif callback_query.data.split('_')[-1] =='ed3':
                await callback_query.message.answer(f"Сфотографируйся с кубиком в фотозоне СПО «Северная Венеция»")
                await state.set_state(Test.ed3)
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.message(Test.ed3)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(ed3=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 3 задания Эдема из "Сделай это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'ed3'))
    await state.clear()


@router.message(Test.ed2)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(ed2=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 2 задания Эдема из "Сделай это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'ed2'))
    await state.clear()


@router.message(Test.ed1)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(ed1=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 1 задания Эдема из "Сделай это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'ed1'))
    await state.clear()


@router.callback_query(F.data == 'eonline')
async def quests_online(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"У нас есть для тебя очные и онлайн задания\nКакие выбирешь?", reply_markup=type_quests_list_online_special_r())
        await callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


airl = ('Приходи на 1 этаж 1 корпуса и выполняй задания:'
        '\n\n1. Озвучь видеоролик.'
        '\n2. Сфотографироваться с командиром АТОМа.'
        '\n3. Оставить свой след на фотозоне. '
        '\n4. Сняться в клипе и ответить на вопросы. '
        '\n5. Почувствуй себя главным редактором журнала.'
        '\n6. Нарисовать эмблему медианаправления.')


@router.callback_query(F.data.startswith('airl'))
async def quests_irl(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{airl}\nНажми на кнопочку ниже, если выполнил задание, тогда модератор сможет подтвердить его выполнение.", reply_markup=irl_a_ready())
        await callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('atomirl_'))
async def quests_quiz1_4(callback_query: types.CallbackQuery, state: FSMContext, bot: Bot) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='airl1':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание атома 1 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'airl1'))
            elif callback_query.data.split('_')[-1] =='airl2':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание атома 2 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'airl2'))
            elif callback_query.data.split('_')[-1] =='airl3':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание атома 3 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'airl3'))
            elif callback_query.data.split('_')[-1] =='airl4':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание атома 4 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'airl4'))
            elif callback_query.data.split('_')[-1] =='airl5':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание атома 5 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'airl5'))
            elif callback_query.data.split('_')[-1] =='airl6':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание атома 6 \n Проверьте его и зачислите ему BonchCoins!', reply_markup=done(callback_query.from_user.id, 'airl6'))
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


aquiz1_4 = ('Для заданий из викторины - одна попытка, будь внимателен!'
            '\n\n1. Сколько направлений обучения есть в отряде?'
            '\n2. Что такое выдержка при фотосъемке?'
            '\n3. СМедО – это'
            '\n4. Кто пользуется приложением Figma?')


aquiz5_8 = ('5. Чем занимается бильдредактор?'
            '\n6. Сколько медиа отрядов в Санкт-Петербурге?'
            '\n7. АТОМ -'
            '\n8. Что мы называем медиамастерскими? ')


aquiz9_12 = ('9. Сотворчество – это'
             '\n10. Для чего используют эмоди в тексте?')


@router.callback_query(F.data == 'achoose_quiz')
async def quests_quiz_p1(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{aquiz1_4}", reply_markup=aquiz1_4_())
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')


@router.callback_query(F.data.startswith('aquiz'))
async def quests_quiz1_4(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='aq1':
                await callback_query.message.answer(f'Сколько направлений обучения есть в отряде?\nа) 2\nб) 5\nв) 10.', reply_markup=a_quiz1())
            elif callback_query.data.split('_')[-1] =='aq2': #доделать начиная здесь!
                await callback_query.message.answer(f"Что такое выдержка при фотосъемке?\nа) стрессоустойчивость\nб) вырезка\nв) время, в течение которого открыт затвор камеры.", reply_markup=a_quiz2())
            elif callback_query.data.split('_')[-1] =='aq3':
                await callback_query.message.answer(f"СМедО – это\nа) студенческий медицинский отряд\nб) студенческий медиаотряд\nв) студенческий отряд пасечников.", reply_markup=a_quiz3())
            elif callback_query.data.split('_')[-1] =='aq4':
                await callback_query.message.answer(f"Кто пользуется приложением Figma?\nа) дизайнер\nб) видеооператор\nв) копирайтер.", reply_markup=a_quiz4())
            elif callback_query.data.split('_')[-1] =='aq5':
                await callback_query.message.answer(f"Чем занимается бильдредактор?\nа) редактурой текса\nб) созданим графического изображения\nв) отбором и редактированием фото.", reply_markup=a_quiz5())
            elif callback_query.data.split('_')[-1] =='aq6':
                await callback_query.message.answer(f"Сколько медиа отрядов в Санкт-Петербурге?\nа) 5\nб) 3\nв) 1.", reply_markup=a_quiz6())
            elif callback_query.data.split('_')[-1] =='aq7':
                await callback_query.message.answer(f"АТОМ –\nа) Методичка в кармане\nа) я и ты\nб) мы\nв) творчество.", reply_markup=a_quiz7())
            elif callback_query.data.split('_')[-1] =='aq8':
                await callback_query.message.answer(f"Что мы называем медиамастерскими? \nа) профильные занятия отряда\nб) фотосъемки\nв) комиссарки.", reply_markup=a_quiz8())
            elif callback_query.data.split('_')[-1] =='aq9':
                await callback_query.message.answer(f'Сотворчество – это\nа) совместное творчество\nб) творчество в студенческих отрядах\nв) событийное творчество.', reply_markup=a_quiz9())
            elif callback_query.data.split('_')[-1] =='aq10':
                await callback_query.message.answer(f"Для чего используют эмоди в тексте?\nа) разбавляют полотно текста\nб) снижение формальность текста\nв) добавляют эмоциональную окраску.", reply_markup=a_quiz10())
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('next_to_aquiz_p'))
async def quests_quiz_next(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if callback_query.data.split('_')[-1] =='p2':
            await callback_query.message.answer(f'{aquiz5_8}', reply_markup=aquiz5_8_())
            await callback_query.message.delete()
        if callback_query.data.split('_')[-1] =='p3':
            await callback_query.message.answer(f'{aquiz9_12}', reply_markup=aquiz9_12_())
            await callback_query.message.delete()
        await callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('back_to_aquiz_p'))
async def quests_quiz_back(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if callback_query.data.split('_')[-1] =='p1':
            await callback_query.message.answer(f'{aquiz1_4}', reply_markup=aquiz1_4_())
            await callback_query.message.delete()
        if callback_query.data.split('_')[-1] =='p2':
            await callback_query.message.answer(f'{aquiz5_8}', reply_markup=aquiz5_8_())
            await callback_query.message.delete()
        await callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


alearn1_4 = ('1. Узнай в нашей группе ВКонтакте, кто стал лучшим бойцом трудового сезона. '
             '\n2. Изучи группу и напиши мне какой девиз меиаотряда?')


@router.callback_query(F.data == 'alearn_it')
async def quests_quiz_p1(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{alearn1_4}", reply_markup=alearn1_4_())
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('alearn'))
async def quests_quiz1_4(callback_query: types.CallbackQuery, state: FSMContext, bot: Bot) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='al1':
                await callback_query.message.answer(f'Узнай в нашей группе ВКонтакте, кто стал лучшим бойцом трудового сезона')
                await state.set_state(Test.al1)
            elif callback_query.data.split('_')[-1] =='al2':
                await callback_query.message.answer('Изучи группу и скажи, какой девиз меиаотряда?')
                await state.set_state(Test.al2)
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.message(Test.al2)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(al2=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 2 задания атома из "Изучи это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'al2'))
    await state.clear()


@router.message(Test.al1)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(a1=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 1 задания атома из "Изучи это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'al1'))
    await state.clear()


atodo1_4 =('1. Снять клип для ВК на любой популярный тренд, видео приложить в ответ.'
           '\n2. Подбери 5 треков для дискотеки.'
           '\n3. Сделай фото с командиром АТОМа.')


@router.callback_query(F.data == 'aDO_IT')
async def quests_quiz_p1(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{atodo1_4}", reply_markup=adoit1_4_())
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.callback_query(F.data.startswith('adoit'))
async def quests_quiz1_4(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='ad1':
                await callback_query.message.answer(f"Снять клип для ВК на любой популярный тренд, видео приложить в ответ.")
                await state.set_state(Test.ad1)
            elif callback_query.data.split('_')[-1] =='ad2':
                await callback_query.message.answer(f"Подбери 5 треков для дискотеки.")
                await state.set_state(Test.ad2)
            elif callback_query.data.split('_')[-1] =='ad3':
                await callback_query.message.answer(f"Сделай фото с командиром АТОМа.")
                await state.set_state(Test.ad3)
        await  callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


@router.message(Test.ad3)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(ad3=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 3 задания атома из "Сделай это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'ad3'))
    await state.clear()


@router.message(Test.ad2)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(ad2=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 2 задания атома из "Сделай это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'ad2'))
    await state.clear()


@router.message(Test.ad1)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(ad1=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 1 задания атома из "Сделай это", проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'ad1'))
    await state.clear()


@router.callback_query(F.data == 'aonline')
async def quests_online(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"Выбери тип задания", reply_markup=type_quests_list_online_special_r())
        await callback_query.answer('')
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')


daily1 = ('Найди 10 таких плакатов на территории университета и сделай на фоне плакатов селфи. '
          '10 фотографий прикрепи в ответ, чтобы получить 100 БончКоинов!')
daily2 = ('Внимательно изучи фотовыставку, посвященную студенческим отрядам, которая находится на '
          '1 этаже 1 корпуса и напиши в ответ точно такое же описание терминов, как на выставке '
          '(боец, комиссарка, дорога на сезон, агитбригада, вклсм, друзья, целина). Изучай и '
          'резюмируй нашу выставку, чтобы получить свои 100 БончКоинов!')
daily3 = ('Напиши рассказ о своём лучшем лете! Подробно расскажи, что произошло тем летом и '
          'какие воспоминания у тебя остались. Минимальное количество слов — 150. К рассказу '
          'обязательно прикрепи 2-3 фото, которые послужат дополнительной иллюстрацией, а ты '
          'получишь свои 100 БончКоинов!')
daily4 = ('Приходи на Форсайт-сессию «Студенческие отряды: сквозь года» в 16:30 в кабинет *тут '
          'будет номер кабинета*. Проводить сессию будет Антон Борисович Гехт, заведующий кафедрой '
          'истории и регионоведения. На месте будет регистрация, как пройдешь её — получишь 100 '
          'БончКоинов на счёт!')
daily5 = ('Приходи на концертно-конкурсную программу на 1 этаж 1 го корпуса в 12:30. '
          'Сделай фотку возле сцены и скидывай её в ответ, чтобы получить 100 БончКоинов!')

@router.callback_query(F.data.startswith('dailyq'))
async def daily(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if datetime.datetime(2024, 11, 12) > datetime.datetime.today() > datetime.datetime(2024, 11, 10):
            if str(await quiz_exist(callback_query.from_user.id, 'dq1'))[1:-2] == '0':
                await callback_query.message.answer('Ты уже выполнил это задание!')
            else:
                await callback_query.message.answer(f'{daily1}')
                await state.set_state(Test.dq1)
        elif datetime.datetime(2024, 11, 13) > datetime.datetime.today() > datetime.datetime(2024, 11, 11):
            if str(await quiz_exist(callback_query.from_user.id, 'dq2'))[1:-2] == '0':
                await callback_query.message.answer('Ты уже выполнил это задание!')
            else:
                await callback_query.message.answer(f'{daily2}')
                await state.set_state(Test.dq2)
        elif datetime.datetime(2024, 11, 14) > datetime.datetime.today() > datetime.datetime(2024, 11, 12):
            if str(await quiz_exist(callback_query.from_user.id, 'dq3'))[1:-2] == '0':
                await callback_query.message.answer('Ты уже выполнил это задание!')
            else:
                await callback_query.message.answer(f'{daily3}')
                await state.set_state(Test.dq3)
        elif datetime.datetime(2024, 11, 15) > datetime.datetime.today() > datetime.datetime(2024, 11, 13):
            if str(await quiz_exist(callback_query.from_user.id, 'dq4'))[1:-2] == '0':
                await callback_query.message.answer('Ты уже выполнил это задание!')
            else:
                await callback_query.message.answer(f'{daily4}')
                await state.set_state(Test.dq4)
        elif datetime.datetime(2024, 11, 16) > datetime.datetime.today() > datetime.datetime(2024, 11, 14):
            if str(await quiz_exist(callback_query.from_user.id, 'dq5'))[1:-2] == '0':
                await callback_query.message.answer('Ты уже выполнил это задание!')
            else:
                await callback_query.message.answer(f'{daily5}')
                await state.set_state(Test.dq5)
    else:

        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')



class AlbumMiddleware(BaseMiddleware):
    album_data: dict = {}

    def __init__(self, latency: Union[int, float] = 0.01):
        self.latency = latency

    async def __call__(
            self,
            handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
            message: Message,
            data: dict[str, Any]
    ) -> Any:
        if not message.media_group_id:
            await handler(message, data)
            return
        try:
            self.album_data[message.media_group_id].append(message)
        except KeyError:
            self.album_data[message.media_group_id] = [message]
            await asyncio.sleep(self.latency)

            data['_is_last'] = True
            data["album"] = self.album_data[message.media_group_id]
            await handler(message, data)

        if message.media_group_id and data.get("_is_last"):
            del self.album_data[message.media_group_id]
            del data['_is_last']

router.message.middleware(AlbumMiddleware())
@router.message(Test.dq1)
async def subs_res(message: Message, bot: Bot, state: FSMContext, album: list[Message]) -> None:
    media_group = []
    for msg in album:
        if msg.photo:
            file_id = msg.photo[-1].file_id
            media_group.append(InputMediaPhoto(media=file_id))
        else:
            obj_dict = msg.dict()
            file_id = obj_dict[msg.content_type]['file_id']
            media_group.append(InputMedia(media=file_id))
    await state.update_data(dq1=message.from_user)
    await bot.send_media_group(media=media_group, chat_id=-1002250236179)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение ежедневного, проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'dq1'))
    await state.clear()

@router.message(Test.dq2)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(dq2=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение ежедневного, проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'dq2'))
    await state.clear()

@router.message(Test.dq3)
async def subs_res(message: Message, bot: Bot, state: FSMContext, album: list[Message]) -> None:
    media_group = []
    for msg in album:
        if msg.photo:
            file_id = msg.photo[-1].file_id
            media_group.append(InputMediaPhoto(media=file_id))
        else:
            obj_dict = msg.dict()
            file_id = obj_dict[msg.content_type]['file_id']
            media_group.append(InputMedia(media=file_id))
    await state.update_data(dq3=message.from_user)
    await bot.send_media_group(chat_id=-1002250236179, media=media_group)
    await bot.send_message (chat_id=-1002250236179, text=f'{message.caption}')
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение ежедневного, проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'dq3'))
    await state.clear()

@router.message(Test.dq4)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(dq4=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение ежедневного, проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'dq4'))
    await state.clear()

@router.message(Test.dq5)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(dq5=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение ежедневного, проверьте его и зачислите ему BonchCoins!', reply_markup=done(message.from_user.id, 'dq5'))
    await state.clear()


