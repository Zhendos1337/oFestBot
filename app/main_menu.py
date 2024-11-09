import datetime

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import aiosqlite
from aiogram.types import FSInputFile


from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Bot
from app.db_requests import (wallet_value, wallet_db, quest_db, shop_db,
                             verify_exist, verify_db, referal_db,
                             referal_exist, referal_delete, where_from_user, add_friend, add_social, add_other, add_qr, get_money, shop_balance, purchase, friend_reward)
from config import TOKEN
from app.keyboards import get_type_of_quest_inout, main_menu, squads_menu, where_from, anketa, shop_menu, buy, verify


router = Router()
bot = Bot(token=TOKEN)


about = ('Здесь ты сможешь найти работу, а ещё своих друзей, любовь и путешествия! \n\n'
         'В СПбГУТ отряды действуют с 2018 года по 5 направлениям: вожатые, '
         'строители, проводники поезда, сборщики урожая и медиа-специалисты. '
         'Чтобы узнать больше, подписывайся на группу штаба студенческих отрядов '
         'СПбГУТ в ВК: https://vk.com/so_spbsut')

greetins = ('Что умеет этот бот?\n\n'
            'Изучай направления студенческих отрядов, выполняй задания, '
            'зарабатывай БончКоины и обменивай их на сувениры и крутой мерч!\n\n'
            'А пока отправляй фото своего пропуска, чтобы заработать свои первые 50 БончКоинов и пройти верификацию.\n\n'
            'Бот проснётся 11 ноября и будет работать до 15 ноября с 9:00 до 21:00.')



class Form(StatesGroup):
    photo = State()
    friend_name = State()
    question = State()





@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        tg_id = message.from_user.id
        v = 0
        user_name = message.from_user.username.lower()
        await verify_db(tg_id, v, user_name)
        referal = 1
        qr = 0
        friend = 0
        social = 0
        other = 0
        await referal_db(tg_id, referal, qr, friend, social, other)
        if (str(await verify_exist(message.from_user.id)))[1:-2] == '0':
            await message.answer(f'Привет, {message.from_user.first_name}!\n{greetins}')
            await state.set_state(Form.photo)
        else:
            await message.answer('Теперь мы можем начинать!', reply_markup=main_menu())
            if (str(await referal_exist(message.from_user.id)))[1:-2] == '1':
                await message.answer(f'Откуда ты узнал про бота?',
                                 reply_markup=where_from())
            tg_id = message.from_user.id
            wallet = 50
            user_name = (message.from_user.username).lower()
            await wallet_db(tg_id,wallet, user_name)
            q1 = 1
            q2 = 1
            q3 = 1
            q4 = 1
            q5 = 1
            q6 = 1
            q7 = 1
            q8 = 1
            q9 = 1
            q10 = 1
            q11 = 1
            q12 = 1
            q13 = 1
            q14 = 1
            q15 = 1
            q16 = 1
            q17 = 1
            q18 = 1
            q19 = 1
            q20 = 1
            q21 = 1
            d1 = 1
            d2 = 1
            d3 = 1
            d4 = 1
            d5 = 1
            d6 = 1
            d7 = 1
            d8 = 1
            d9 = 1
            d10 = 1
            d11 = 1
            d12 = 1
            d13 = 1
            d14 = 1
            d15 = 1
            d16 = 1
            d17 = 1
            d18 = 1
            d19 = 1
            d20 = 1
            l1 = 1
            l2 = 1
            l3 = 1
            l4 = 1
            l5 = 1
            l6 = 1
            l7 = 1
            l8 = 1
            l9 = 1
            l10 = 1
            irl1 = 1
            irl2 = 1
            irl3 = 1
            irl4 = 1
            irl5 = 1
            irl6 = 1
            irl7 = 1
            irl8 = 1
            irl9 = 1
            oirl1 = 1
            oirl2 = 1
            oirl3 = 1
            oirl4 = 1
            oirl5 = 1
            oirl6 = 1
            ol1 = 1
            ol2 = 1
            od1 = 1
            od2 = 1
            od3 = 1
            oq1 = 1
            oq2 = 1
            oq3 = 1
            oq4 = 1
            oq5 = 1
            oq6 = 1
            oq7 = 1
            oq8 = 1
            oq9 = 1
            oq10 = 1
            lirl1 = 1
            lirl2 = 1
            lirl3 = 1
            lirl4 = 1
            lirl5 = 1
            lirl6 = 1
            ll1 = 1
            ll2 = 1
            ld1 = 1
            ld2 = 1
            ld3 = 1
            lq1 = 1
            lq2 = 1
            lq3 = 1
            lq4 = 1
            lq5 = 1
            lq6 = 1
            lq7 = 1
            lq8 = 1
            lq9 = 1
            lq10 = 1
            kirl1 = 1
            kirl2 = 1
            kirl3 = 1
            kirl4 = 1
            kirl5 = 1
            kirl6 = 1
            kl1 = 1
            kl2 = 1
            kd1 = 1
            kd2 = 1
            kd3 = 1
            kq1 = 1
            kq2 = 1
            kq3 = 1
            kq4 = 1
            kq5 = 1
            kq6 = 1
            kq7 = 1
            kq8 = 1
            kq9 = 1
            kq10 = 1
            svirl1 = 1
            svirl2 = 1
            svirl3 = 1
            svirl4 = 1
            svirl5 = 1
            svirl6 = 1
            svl1 = 1
            svl2 = 1
            svd1 = 1
            svd2 = 1
            svd3 = 1
            svq1 = 1
            svq2 = 1
            svq3 = 1
            svq4 = 1
            svq5 = 1
            svq6 = 1
            svq7 = 1
            svq8 = 1
            svq9 = 1
            svq10 = 1
            eirl1 = 1
            eirl2 = 1
            eirl3 = 1
            eirl4 = 1
            eirl5 = 1
            eirl6 = 1
            el1 = 1
            el2 = 1
            ed1 = 1
            ed2 = 1
            ed3 = 1
            eq1 = 1
            eq2 = 1
            eq3 = 1
            eq4 = 1
            eq5 = 1
            eq6 = 1
            eq7 = 1
            eq8 = 1
            eq9 = 1
            eq10 = 1
            airl1 = 1
            airl2 = 1
            airl3 = 1
            airl4 = 1
            airl5 = 1
            airl6 = 1
            al1 = 1
            al2 = 1
            ad1 = 1
            ad2 = 1
            ad3 = 1
            aq1 = 1
            aq2 = 1
            aq3 = 1
            aq4 = 1
            aq5 = 1
            aq6 = 1
            aq7 = 1
            aq8 = 1
            aq9 = 1
            aq10 = 1
            dq1 = 1
            dq2 = 1
            dq3 = 1
            dq4 = 1
            dq5 = 1
            s1 = 1
            s2 = 1
            s3 = 1
            s4 = 1
            s5 = 1
            s6 = 1
            s7 = 1
            s8 = 1
            s9 = 1
            s10 = 1
            await quest_db(tg_id, user_name, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, irl1, irl2, irl3, irl4, irl5, irl6, irl7, irl8, irl9, oirl1, oirl2, oirl3, oirl4, oirl5, oirl6, ol1, ol2, od1, od2, od3, oq1, oq2, oq3, oq4, oq5, oq6, oq7, oq8, oq9, oq10, lirl1, lirl2, lirl3, lirl4, lirl5, lirl6, ll1, ll2, ld1, ld2, ld3, lq1, lq2, lq3, lq4, lq5, lq6, lq7, lq8, lq9, lq10, kirl1, kirl2, kirl3, kirl4, kirl5, kirl6, kl1, kl2, kd1, kd2, kd3, kq1, kq2, kq3, kq4, kq5, kq6, kq7, kq8, kq9, kq10, svirl1, svirl2, svirl3, svirl4, svirl5, svirl6, svl1, svl2, svd1, svd2, svd3, svq1, svq2, svq3, svq4, svq5, svq6, svq7, svq8, svq9, svq10, eirl1, eirl2, eirl3, eirl4, eirl5, eirl6, el1, el2, ed1, ed2, ed3, eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9, eq10, airl1, airl2, airl3, airl4, airl5, airl6, al1, al2, ad1, ad2, ad3, aq1, aq2, aq3, aq4, aq5, aq6, aq7, aq8, aq9, aq10, dq1, dq2, dq3, dq4, dq5, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10)
            num = 1
            sh1 = 0
            sh2 = 0
            sh3 = 0
            sh4 = 0
            sh5 = 0
            sh6 = 0
            sh7 = 0
            sh8 = 0
            sh9 = 0
            sh10 = 0
            sh11 = 0
            sh12 = 0
            sh13 = 0
            sh14 = 0
            sh15 = 0
            sh16 = 0
            sh17 = 0
            sh18 = 0
            sh19 = 0
            sh20 = 0
            sh21 = 0
            sh22 = 0
            sh23 = 0
            sh24 = 0
            sh25 = 0
            qr = 0
            social = 0
            friend = 0
            other = 0
            await shop_db(num, friend, social, qr, other, sh1, sh2, sh3, sh4, sh5, sh6, sh7, sh8, sh9, sh10, sh11, sh12, sh13, sh14, sh15, sh16, sh17, sh18, sh19, sh20, sh21, sh22, sh23, sh24, sh25)
    else:
        await bot.send_message(message.from_user.id, 'Бот спит, приходи с 9:00 до 21:00, в его рабочее время')

@router.message(Form.photo, F.photo)
async def reg_photo(message: Message, state: FSMContext):
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await state.update_data(photo=message.photo[-1].file_id)
        data = await state.get_data()
        await bot.send_photo(chat_id=-1002250236179, photo=data['photo'], caption=f'@{message.from_user.username} просит доступ к боту', reply_markup=verify(message.from_user.id))
        await bot.send_message(chat_id=message.from_user.id,
                                    text ='Отлично!\nМодераторы очень скоро внесут тебя в список участников.')
        await state.clear()
    else:
        await bot.send_message(message.from_user.id, 'Бот спит, приходи с 9:00 до 21:00, в его рабочее время')

@router.callback_query(F.data == 'friend')
async def friend(callback_query: types.CallbackQuery, bot: Bot, state: FSMContext) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await bot.send_message(callback_query.from_user.id, 'Класс! Введи его username, мы начислим ему 10 БончКоинов!')
        await state.set_state(Form.friend_name)
        await callback_query.message.delete()
        await referal_delete(callback_query.from_user.id)
        await where_from_user(callback_query.from_user.id, callback_query.data)
        await add_friend()
        await callback_query.answer('')
    else:
        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')



@router.message(Form.friend_name)
async def friend_name(message: Message, state: FSMContext):
    if datetime.datetime(2024, 11, 10) < datetime.datetime.now():
        greetins_social = ('Отлично! Спасибо за ответы. Задания уже доступны, а ещё ты можешь изучить '
                           'информацию об отрядах и приглядеть себе покупки в магазине. Переходи скорее в '
                           'меню.')
    else:
        greetins_social = ('Отлично! Спасибо за ответы. Задания будут доступны с 11 ноября с 9:00, '
                           'но ты пока можешь изучить информацию об отрядах и приглядеть себе покупки в '
                           'магазине. Переходи скорее в меню.')
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await state.update_data(friend_name=((message.text).split('@')[-1]).lower())
        data = await state.get_data()
        friend = data['friend_name']
        if friend != ((message.from_user.username).lower()).split('@')[-1]:
            await friend_reward(friend)
            await bot.send_message(message.from_user.id, f'{greetins_social}')
        else:
            await message.answer('Жулик, не воруй')
            await bot.send_message(message.from_user.id, f'{greetins_social}')
        await state.clear()
    else:
        await bot.send_message(message.from_user.id, 'Бот спит, приходи с 9:00 до 21:00, в его рабочее время')


@router.callback_query(F.data == 'other')
async def friend(callback_query: types.CallbackQuery, bot: Bot) -> None:
    if datetime.datetime(2024, 11, 10) < datetime.datetime.now():
        greetins_social = ('Отлично! Спасибо за ответы. Задания уже доступны, а ещё ты можешь изучить '
                           'информацию об отрядах и приглядеть себе покупки в магазине. Переходи скорее в '
                           'меню.')
    else:
        greetins_social = ('Отлично! Спасибо за ответы. Задания будут доступны с 11 ноября с 9:00, '
                           'но ты пока можешь изучить информацию об отрядах и приглядеть себе покупки в '
                           'магазине. Переходи скорее в меню.')
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await bot.send_message(callback_query.from_user.id, f'{greetins_social}')
        await callback_query.message.delete()
        await referal_delete(callback_query.from_user.id)
        await where_from_user(callback_query.from_user.id, callback_query.data)
        await add_other()
        await callback_query.answer('')
    else:
        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')



@router.callback_query(F.data == 'qr')
async def friend(callback_query: types.CallbackQuery, bot: Bot) -> None:
    if datetime.datetime(2024, 11, 10) < datetime.datetime.now():
        greetins_social = ('Отлично! Спасибо за ответы. Задания уже доступны, а ещё ты можешь изучить '
                           'информацию об отрядах и приглядеть себе покупки в магазине. Переходи скорее в '
                           'меню.')
    else:
        greetins_social = ('Отлично! Спасибо за ответы. Задания будут доступны с 11 ноября с 9:00, '
                           'но ты пока можешь изучить информацию об отрядах и приглядеть себе покупки в '
                           'магазине. Переходи скорее в меню.')
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await bot.send_message(callback_query.from_user.id, f'{greetins_social}')
        await callback_query.message.delete()
        await referal_delete(callback_query.from_user.id)
        await where_from_user(callback_query.from_user.id, callback_query.data)
        await add_qr()
        await callback_query.answer('')
    else:
        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')



@router.callback_query(F.data == 'social')
async def friend(callback_query: types.CallbackQuery, bot: Bot) -> None:
    if datetime.datetime(2024, 11, 10) < datetime.datetime.now():
        greetins_social = ('Отлично! Спасибо за ответы. Задания уже доступны, а ещё ты можешь изучить '
                           'информацию об отрядах и приглядеть себе покупки в магазине. Переходи скорее в '
                           'меню.')
    else:
        greetins_social = ('Отлично! Спасибо за ответы. Задания будут доступны с 11 ноября с 9:00, '
                           'но ты пока можешь изучить информацию об отрядах и приглядеть себе покупки в '
                           'магазине. Переходи скорее в меню.')
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await bot.send_message(callback_query.from_user.id, f'{greetins_social}')
        await callback_query.message.delete()
        await referal_delete(callback_query.from_user.id)
        await where_from_user(callback_query.from_user.id, callback_query.data)
        await add_social()
        await callback_query.answer('')
    else:
         await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')



@router.message(F.text=="Об отрядах")
async def faq_main(callback_query: types.CallbackQuery, bot: Bot) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await bot.send_message(callback_query.from_user.id,f'{about}',
                               reply_markup=squads_menu())
    else:
        await bot.send_message(message.from_user.id, 'Бот спит, приходи с 9:00 до 21:00, в его рабочее время')


@router.message(F.text=="Магазин")
async def shop_main(message: Message, bot: Bot) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if datetime.datetime(2024, 11, 14) < datetime.datetime.today() < datetime.datetime(2024, 11, 16) or datetime.datetime(2024, 11, 8) < datetime.datetime.today() < datetime.datetime(2024, 11, 10):
            shop = ('Здесь ты можешь посмотреть, что есть в нашем магазине. Изучай общую картинку и нажимай код товара, чтобы посмотреть его поближе или купить.\n'
                    f'\n1000 БончКоинов:'
                    f'\n1. Секретный подарок от ССхО Космея'
                    f'\n2. Секретный подарок от СОП Лотос'
                    f'\n3. Секретный подарок от ССО Эдем'
                    f'\n4. Секретный подарок от СМедО АТОМ'
                    f'\n5. Секретный подарок от СПО Орбита'
                    f'\n6. Секретный подарок от СПО Северная Венеция\n'
                    f'\n2500 БончКоинов:'
                    f'\n7. Свитшот\n'
                    f'\n2000 БончКоинов:'
                    f'\n8. Футболка \n'
                    f'\n1500 БончКоинов:'
                    f'\n9. Шоппер'
                    f'\n10. Барсетка'
                    f'\n11. Носки'
                    f'\n12. Дождевик'
                    f'\n13. Термокружка\n'
                    f'\n1000 БончКоинов:'
                    f'\n14. Обложка для студака'
                    f'\n15. Обложка для паспорта'
                    f'\n16. Картхолдер'
                    f'\n17. Ежедневник'
                    f'\n700 БончКоинов:'
                    f'\n18. Металлический значок\n'
                    f'\n500 БончКоинов:'
                    f'\n19. Календарь'
                    f'\n20. Постер А2'
                    f'\n21. Стикерпак\n'
                    f'\n300 БончКоинов:'
                    f'\n22. Закатной значок'
                    f'\n23. Силиконовый браслет'
                    f'\n24. Стартер от Додо-Пицца'
                    f'\n25. Сертификат на кофе')
            photo = FSInputFile('sh_general.png', filename='sh_general.png')
            await bot.send_photo(message.from_user.id, photo=photo, caption=f'{shop}', reply_markup=shop_menu())
        else:
            await bot.send_message(message.from_user.id, 'Магазин будет открыт в пятницу')
    else:
            await bot.send_message(message.from_user.id, 'Бот спит, приходи с 9:00 до 21:00, в его рабочее время')


@router.callback_query(F.data.startswith('shopping'))
async def shopper(callback_query: types.CallbackQuery, bot: Bot) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        bal1 = (str(await shop_balance('sh1')))[1:-2]
        bal2 = (str(await shop_balance('sh2')))[1:-2]
        bal3 = (str(await shop_balance('sh3')))[1:-2]
        bal4 = (str(await shop_balance('sh4')))[1:-2]
        bal5 = (str(await shop_balance('sh5')))[1:-2]
        bal6 = (str(await shop_balance('sh6')))[1:-2]
        bal7 = (str(await shop_balance('sh7')))[1:-2]
        bal8 = (str(await shop_balance('sh8')))[1:-2]
        bal9 = (str(await shop_balance('sh9')))[1:-2]
        bal10 = (str(await shop_balance('sh10')))[1:-2]
        bal11 = (str(await shop_balance('sh11')))[1:-2]
        bal12 = (str(await shop_balance('sh12')))[1:-2]
        bal13 = (str(await shop_balance('sh13')))[1:-2]
        bal14 = (str(await shop_balance('sh14')))[1:-2]
        bal15 = (str(await shop_balance('sh15')))[1:-2]
        bal16 = (str(await shop_balance('sh16')))[1:-2]
        bal17 = (str(await shop_balance('sh17')))[1:-2]
        bal18 = (str(await shop_balance('sh18')))[1:-2]
        bal19 = (str(await shop_balance('sh19')))[1:-2]
        bal20 = (str(await shop_balance('sh20')))[1:-2]
        bal21 = (str(await shop_balance('sh21')))[1:-2]
        bal22 = (str(await shop_balance('sh22')))[1:-2]
        bal23 = (str(await shop_balance('sh23')))[1:-2]
        bal24 = (str(await shop_balance('sh24')))[1:-2]
        bal25 = (str(await shop_balance('sh25')))[1:-2]
        if callback_query.data.split('_')[-1] == 'sh1':
            photo = FSInputFile('sh1.png', 'sh1.png')
            text = (f'Осталось {bal1} шт.')
        elif callback_query.data.split('_')[-1] == 'sh2':
            photo = FSInputFile('sh2.png', 'sh2.png')
            text = (f'Осталось {bal2} шт.')
        elif callback_query.data.split('_')[-1] == 'sh3':
            photo = FSInputFile('sh3.png', 'sh3.png')
            text = (f'Осталось {bal3} шт.')
        elif callback_query.data.split('_')[-1] == 'sh4':
            photo = FSInputFile('sh4.png', 'sh4.png')
            text = (f'Осталось {bal4} шт.')
        elif callback_query.data.split('_')[-1] == 'sh5':
            photo = FSInputFile('sh5.png', 'sh5.png')
            text = (f'Осталось {bal5} шт.')
        elif callback_query.data.split('_')[-1] == 'sh6':
            photo = FSInputFile('sh6.png', 'sh6.png')
            text = (f'Осталось {bal6} шт.')
        elif callback_query.data.split('_')[-1] == 'sh7':
            photo = FSInputFile('sh7.png', 'sh7.png')
            text = (f'Осталось {bal7} шт.')
        elif callback_query.data.split('_')[-1] == 'sh8':
            photo = FSInputFile('sh8.png', 'sh8.png')
            text = (f'Осталось {bal8} шт.')
        elif callback_query.data.split('_')[-1] == 'sh9':
            photo = FSInputFile('sh9.png', 'sh9.png')
            text = (f'Осталось {bal9} шт.')
        elif callback_query.data.split('_')[-1] == 'sh10':
            photo = FSInputFile('sh10.png', 'sh10.png')
            text = (f'Осталось {bal10} шт.')
        elif callback_query.data.split('_')[-1] == 'sh11':
            photo = FSInputFile('sh11.png', 'sh11.png')
            text = (f'Осталось {bal11} шт.')
        elif callback_query.data.split('_')[-1] == 'sh12':
            photo = FSInputFile('sh12.png', 'sh12.png')
            text = (f'Осталось {bal12} шт.')
        elif callback_query.data.split('_')[-1] == 'sh13':
            photo = FSInputFile('sh13.png', 'sh13.png')
            text = (f'Осталось {bal13} шт.')
        elif callback_query.data.split('_')[-1] == 'sh14':
            photo = FSInputFile('sh14.png', 'sh14.png')
            text = (f'Осталось {bal14} шт.')
        elif callback_query.data.split('_')[-1] == 'sh15':
            photo = FSInputFile('sh15.png', 'sh15.png')
            text = (f'Осталось {bal15} шт.')
        elif callback_query.data.split('_')[-1] == 'sh16':
            photo = FSInputFile('sh16.png', 'sh16.png')
            text = (f'Осталось {bal16} шт.')
        elif callback_query.data.split('_')[-1] == 'sh17':
            photo = FSInputFile('sh17.png', 'sh17.png')
            text = (f'Осталось {bal17} шт.')
        elif callback_query.data.split('_')[-1] == 'sh18':
            photo = FSInputFile('sh18.png', 'sh18.png')
            text = (f'Осталось {bal18} шт.')
        elif callback_query.data.split('_')[-1] == 'sh19':
            photo = FSInputFile('sh19.png', 'sh19.png')
            text = (f'Осталось {bal19} шт.')
        elif callback_query.data.split('_')[-1] == 'sh20':
            photo = FSInputFile('sh20.png', 'sh20.png')
            text = (f'Осталось {bal20} шт.')
        elif callback_query.data.split('_')[-1] == 'sh21':
            photo = FSInputFile('sh21.png', 'sh21.png')
            text = (f'Осталось {bal21} шт.')
        elif callback_query.data.split('_')[-1] == 'sh22':
            photo = FSInputFile('sh22.png', 'sh22.png')
            text = (f'Осталось {bal22} шт.')
        elif callback_query.data.split('_')[-1] == 'sh23':
            photo = FSInputFile('sh23.png', 'sh23.png')
            text = (f'Осталось {bal23} шт.')
        elif callback_query.data.split('_')[-1] == 'sh24':
            photo = FSInputFile('sh24.png', 'sh24.png')
            text = (f'Осталось {bal24} шт.')
        elif callback_query.data.split('_')[-1] == 'sh25':
            photo = FSInputFile('sh25.png', 'sh25.png')
            text = (f'Осталось {bal25} шт.')
        await  callback_query.answer('')
        await bot.send_photo(callback_query.from_user.id, photo=photo, caption=f'{text}', reply_markup=buy(callback_query.data.split('_')[-1]))
    else:
            await bot.send_message(message.from_user.id, 'Бот спит, приходи с 9:00 до 21:00, в его рабочее время')



@router.callback_query(F.data.startswith('sold'))
async def selling(callback_query: types.CallbackQuery, bot: Bot) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        buyer = callback_query.from_user.username
        if (str(await shop_balance(callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Извини, товар закончился 🙁')
        else:
            if callback_query.data.split('_')[-1] == 'sh1':
                cost = 1000
                item = 'Секретный подарок от ССхО Космея'
            elif callback_query.data.split('_')[-1] == 'sh2':
                item = 'Секретный подарок от СОП Лотос'
                cost = 1000
            elif callback_query.data.split('_')[-1] == 'sh3':
                item = 'Секретный подарок от ССО Эдем'
                cost = 1000
            elif callback_query.data.split('_')[-1] == 'sh4':
                item = 'Секретный подарок от СМедО АТОМ'
                cost = 1000
            elif callback_query.data.split('_')[-1] == 'sh5':
                item = 'Секретный подарок от СПО Орбита'
                cost = 1000
            elif callback_query.data.split('_')[-1] == 'sh6':
                item = 'Секретный подарок от СПО Северная Венеция'
                cost = 1000
            elif callback_query.data.split('_')[-1] == 'sh7':
                item = 'свитшот'
                cost = 2500
            elif callback_query.data.split('_')[-1] == 'sh8':
                item = 'Футболка'
                cost = 2000
            elif callback_query.data.split('_')[-1] == 'sh9':
                item = 'Шоппер'
                cost = 1500
            elif callback_query.data.split('_')[-1] == 'sh10':
                item = 'Барсетка'
                cost = 1500
            elif callback_query.data.split('_')[-1] == 'sh11':
                item = 'Носки'
                cost = 1500
            elif callback_query.data.split('_')[-1] == 'sh12':
                item = 'Дождевик'
                cost = 1500
            elif callback_query.data.split('_')[-1] == 'sh13':
                item = 'Термокружка'
                cost = 1500
            elif callback_query.data.split('_')[-1] == 'sh14':
                item = 'Обложка для студака'
                cost = 1000
            elif callback_query.data.split('_')[-1] == 'sh15':
                item = 'Обложка для паспорта'
                cost = 1000
            elif callback_query.data.split('_')[-1] == 'sh16':
                item = 'Картхолдер'
                cost = 1000
            elif callback_query.data.split('_')[-1] == 'sh17':
                item = 'Ежедневник'
                cost = 1000
            elif callback_query.data.split('_')[-1] == 'sh18':
                item = 'Металлический значок'
                cost = 700
            elif callback_query.data.split('_')[-1] == 'sh19':
                item = 'Календарь'
                cost = 700
            elif callback_query.data.split('_')[-1] == 'sh20':
                item = 'Постер А2'
                cost = 500
            elif callback_query.data.split('_')[-1] == 'sh21':
                item = 'Стикерпак'
                cost = 500
            elif callback_query.data.split('_')[-1] == 'sh22':
                item = 'Закатной значок'
                cost = 300
            elif callback_query.data.split('_')[-1] == 'sh23':
                item = 'Силиконовый браслет'
                cost = 300
            elif callback_query.data.split('_')[-1] == 'sh24':
                item = 'Стартер от Додо-пицца'
                cost = 300
            elif callback_query.data.split('_')[-1] == 'sh25':
                item = 'Сертификат на кофе'
                cost = 300
            user_name = callback_query.from_user.username
            db = await aiosqlite.connect('tg_users_wallet.db')
            cursor = await db.execute(f'SELECT wallet FROM users_wallet WHERE user_name == "{user_name}"')
            wallet = await cursor.fetchone()
            await db.commit()
            await db.close()
            if int((str(wallet))[1:-2]) >= cost :
                await callback_query.message.answer(text=f'Подздавляю с покупкой!\nПокажи это сообщение в магазине и тебе выдадут {item}')
                await bot.send_message(chat_id=-1002250236179, text=f'@{user_name} купил {item}')
                await get_money(callback_query.from_user.id, cost)
                await purchase(callback_query.data.split('_')[-1])
            else:
                diff = cost - int((str(wallet))[1:-2])
                await callback_query.message.answer(text=f'Тебе не хватает {diff} на {item} БончКоинов')
        await callback_query.message.delete()
    else:
        await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')



@router.message(F.text=="Задания")
async def quests_main(message: Message, callback_query: types.CallbackQuery, bot: Bot) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if datetime.datetime.now() > datetime.datetime(2024, 11, 10) or datetime.datetime(2024, 11, 9) > datetime.datetime.today() > datetime.datetime(2024, 11, 4):
            await bot.send_message(callback_query.from_user.id, 'Ты можешь выполнить общие и профильные задания.\nКакие выбираешь?',
                                   reply_markup=get_type_of_quest_inout())
        else:
            await bot.send_message(callback_query.from_user.id, 'Задания будут доступны с 11 ноября')
    else:
        await bot.send_message(message.from_user.id, 'Бот спит, приходи с 9:00 до 21:00, в его рабочее время')

@router.message(F.text=="Кошелек")
async def wallet_main(message: Message, bot: Bot) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await bot.send_message(message.from_user.id, text=f'У тебя на балансе 'f'{(str(await wallet_value(message.from_user.id)))[1:-2]} БончКоинов')
    else:
        await bot.send_message(message.from_user.id, 'Бот спит, приходи с 9:00 до 21:00, в его рабочее время')


@router.message(F.text=="Анкета")
async def shop_main(callback_query: types.CallbackQuery, bot: Bot) -> None:
    anketat = ('Надеемся, что ты ознакомился с профилями отрядов перед заполнением анкеты. Скорее заполняй заявку!'
               '\nНе упустите свой шанс стать частью нашего большого сообщества!')
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await bot.send_message(callback_query.from_user.id,f'{anketat}', reply_markup=anketa())
    else:
        await bot.send_message(message.from_user.id, 'Бот спит, приходи с 9:00 до 21:00, в его рабочее время')


rasp = ('Задания можно выполнять не только онлайн, но и очно, а чтобы полностью погрузиться в атмосферу и получить больше БончКоинов, мы ждем тебя с понедельника по пятницу на 1 этаже 1 корпуса.'

            '\n\nПонедельник — знакомство со штабом студенчиским отрядов и выполнение общих заданий.'
            '\n\nВторник — знакомство со студенчискими отрядами СПО Северная Венеция и ССО Эдем, выполнение общих и профильных заданий отярдов.'
            '\n\nСреда — знакомство со студенчискими отрядами ССхО Космея и СОП Лотос, выполнение общих и профильных заданий отярдов.'
            '\n\nЧетверг — знакомство со студенчискими отрядами СПО Орбита и СМедО АТОМ, выполнение общих и профильных заданий отярдов.'
            '\n\nПятница  — открытие магазина, концерт и розыгрыш подарков.')
@router.message(F.text=="Расписание")
async def shop_main(callback_query: types.CallbackQuery, bot: Bot) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await bot.send_message(callback_query.from_user.id,f'{rasp}')
    else:
        await bot.send_message(message.from_user.id, 'Бот спит, приходи с 9:00 до 21:00, в его рабочее время')


@router.message(F.text=="Задать вопрос")
async def shop_main(message: Message, bot: Bot, state: FSMContext) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await bot.send_message(message.from_user.id,f'Задай свой вопрос, тебе поможет первый освободившийся модератор!')
        await state.set_state(Form.question)
    else:
        await bot.send_message(message.from_user.id, 'Бот спит, приходи с 9:00 до 21:00, в его рабочее время')


@router.message(Form.question)
async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.update_data(question=message.from_user)
    await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
    await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал вопрос, помогите ему!')
    await state.clear()
# @router.message(F.text=='friend')
# async def friend(message: Message, bot: Bot, state: FSMContext) -> None:
#     if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
#         await bot.send_message(message.from_user.id, 'Класс! Введи его username, мы начислим ему 10 БончКоинов!')
#         await state.set_state(Form.friend_name1)
#     else:
#         await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')
#
#
#
# @router.message(Form.friend_name1)
# async def friend_name(message: Message, state: FSMContext):
#     if datetime.datetime(2024, 11, 10) < datetime.datetime.now():
#         greetins_social = ('Отлично! Спасибо за ответы. Задания уже доступны, а ещё ты можешь изучить '
#                            'информацию об отрядах и приглядеть себе покупки в магазине. Переходи скорее в '
#                            'меню.')
#     else:
#         greetins_social = ('Отлично! Спасибо за ответы. Задания будут доступны с 11 ноября с 9:00, '
#                            'но ты пока можешь изучить информацию об отрядах и приглядеть себе покупки в '
#                            'магазине. Переходи скорее в меню.')
#     if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
#         await state.update_data(friend_name1=((message.text).split('@')[-1]).lower())
#         data = await state.get_data()
#         friend = data['friend_name1']
#         if friend != ((message.from_user.username).lower()).split('@')[-1]:
#             await friend_reward(friend)
#             await bot.send_message(message.from_user.id, f'{greetins_social}')
#             await bot.send_message(message.from_user.id, f'{friend}')
#         else:
#             await message.answer('Жулик, не воруй')
#             await bot.send_message(message.from_user.id, f'{greetins_social}')
#         await state.clear()
#     else:
#         await bot.send_message(message.from_user.id, 'Бот спит, приходи с 9:00 до 21:00, в его рабочее время')