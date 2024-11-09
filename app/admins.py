from aiogram import Router, F, types
from aiogram import Bot
from aiogram.filters import state
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
import aiosqlite
from app.db_requests import quiz_exist_admin, how_many_qr, how_many_friends, how_many_social, how_many_other, verifying, shop_balance

ADMIN = [1513996525, 1954831647, 639051015, 670194361]
router = Router()

class Test(StatesGroup):
    hlp = State()


admin_menu = ('''
Сейчас я тебе расскажу об основных командах бота.\n
1. добавить товар x y (x - номер товара в магазине, y - количество добавляемого товара)
пример: добавить товар 1 2 (товара 1(Секретный подарок от ССхО Космея) стало на 2 больше)\n
2. убрать товар x y (x - номер товара в магазине, y - количество  товара, которое мы убираем)
пример: убрать товар 3 1 (товара 3(Секретный подарок от ССО Эдем) стало на 1 меньше)\n
3. пополнить x y (x - имя пользователя(можно писать с @ и без), y - количество BonchCoins, которое мы добавляем в кошелек)
пример: пополнить @user 100 / списать username 100 (пользователю @user добавили 100 BonchCoins)\n
4. списать x y (x - имя пользователя, y - количество BonchCoins, которое мы списываем из кошелька)
пример: списать @username 100 / списать username 100 (пользователю @user списывают 100 BonchCoins)\n
5. кошелек x (x - имя пользователя, выводит баланс пользователя\n
6. остаток (показывает остатки в магазине)\n
7. откуда узнал (показывает статистику откуда пользователи узнали про бота
8. рассылка x (x - сообщение для всех пользователей бота. Пример - рассылка Это текст для рассылки(бот отправит всем пользователям "Это текст для рассылки")
Все команды можно писать с большой и маленькой буквы, но тест команды должен быть именно в том порядке, в каком они написаны тут:)

Команды 1,2,3,4 добавлены на всякий случай, если что-то пойдет не так, надобности их использования нет, вся их работа делается автоматически
''')


@router.message(F.text.lower() == 'меню админа')
async def hlp(message: Message, bot: Bot) -> None:
    if message.from_user.id in ADMIN:
        await message.answer(f'Привет, {message.from_user.full_name}! {admin_menu}')

@router.message(F.text.lower().contains('пополнить'))
async def wallet_change(message: Message, bot: Bot) -> None:
        if message.from_user.id in ADMIN:
            change = message.text.split(' ')[2]
            user_name = (message.text.split(' ')[1]).split('@')[-1]
            db = await aiosqlite.connect('tg_users_wallet.db')
            await db.execute(f'UPDATE users_wallet SET wallet = wallet + {change} WHERE user_name == "{user_name}"')
            cursor = await db.execute(f'SELECT wallet FROM users_wallet WHERE user_name == "{user_name}"')
            wallet = await cursor.fetchone()
            await db.commit()
            await db.close()
            await bot.send_message(message.chat.id, f'Пополнение прошло успешно \nУ @{user_name} в кошельке {(str(wallet))[1:-2]} BonchCoins')
        else:
            await bot.send_message(message.chat.id, 'Жулик, не воруй!')


@router.message(F.text.lower().contains('списать'))
async def wallet_change(message: Message, bot: Bot) -> None:
    if message.from_user.id in ADMIN:
        change = message.text.split(' ')[2]
        user_name = (message.text.split(' ')[1]).split('@')[-1]
        db = await aiosqlite.connect('tg_users_wallet.db')
        await db.execute(f'UPDATE users_wallet SET wallet = wallet - {change} WHERE user_name == "{user_name}"')
        cursor = await db.execute(f'SELECT wallet FROM users_wallet WHERE user_name == "{user_name}"')
        wallet = await cursor.fetchone()
        await db.commit()
        await db.close()
        await bot.send_message(message.chat.id, f'Списание прошло успешно \nУ @{user_name} в кошельке {(str(wallet))[1:-2]} BonchCoins')
    else:await bot.send_message(message.chat.id, 'Жулик, не воруй!')


@router.message(F.text.lower().contains('кошелек'))
async def wallet_change(message: Message, bot: Bot) -> None:
    if message.from_user.id in ADMIN:
        user_name = (message.text.split(' ')[1]).split('@')[-1]
        db = await aiosqlite.connect('tg_users_wallet.db')
        cursor = await db.execute(f'SELECT wallet FROM users_wallet WHERE user_name == "{user_name}"')
        wallet = await cursor.fetchone()
        await db.commit()
        await db.close()
        await bot.send_message(message.chat.id, f'У @{user_name} в кошельке {(str(wallet))[1:-2]} BonchCoins')
    else:await bot.send_message(message.chat.id, 'Жулик, не воруй!')


@router.message(F.text.lower().contains('добавить товар'))
async def wallet_change(message: Message, bot: Bot) -> None:
    if message.from_user.id in ADMIN:
        count = message.text.split(' ')[3]
        num = (message.text.split(' ')[2])
        db = await aiosqlite.connect('shop.db')
        await db.execute(f'UPDATE shop_db  SET sh{num} = sh{num} + {count} WHERE num == 1')
        cursor = await db.execute(f'SELECT sh{num} FROM shop_db WHERE num == 1')
        sh = await cursor.fetchone()
        await db.commit()
        await db.close()
        await bot.send_message(message.chat.id, f'В магазине {(str(sh))[1:-2]} шт. товара номер {num}')


@router.message(F.text.lower().contains('убрать товар'))
async def wallet_change(message: Message, bot: Bot) -> None:
    if message.from_user.id in ADMIN:
        count = message.text.split(' ')[3]
        num = message.text.split(' ')[2]
        db = await aiosqlite.connect('shop.db')
        await db.execute(f'UPDATE shop_db  SET sh{num} = sh{num} - {count} WHERE num == 1')
        cursor = await db.execute(f'SELECT sh{num} FROM shop_db WHERE num == 1')
        sh = await cursor.fetchone()
        await db.commit()
        await db.close()
        # if 4 < int((str(sh))[1:-2]) < 21:
        #     item = 'товаров'
        # elif int((str(sh))[1:-2])%10 == 1:
        #     item = 'товар'
        # elif 1 < int((str(sh))[1:-2])%10 < 5:
        #     item = 'товара'
        # elif int((str(sh))[1:-2]) == 0:
        #     item = 'товара'
        await bot.send_message(message.chat.id, f'В магазине {(str(sh))[1:-2]} шт. товара номер {num}')



@router.callback_query(F.data.startswith('verify_done'))
async def verify (callback_query: types.CallbackQuery, bot: Bot) -> None:
    tg_id = callback_query.data.split('_')[-1]
    await verifying(tg_id)
    db = await aiosqlite.connect('verify.db')
    cursor = await db.execute(f'SELECT user_name FROM users_verify WHERE tg_id == {tg_id}')
    data = await cursor.fetchone()
    await db.commit()
    await db.close()
    await callback_query.message.answer(f'{(str(data))[2:-3]} успешно добавлен в список участников!')
    await bot.send_message(chat_id=tg_id, text=f'Тебя одобрили! Теперь еще раз пропиши команду /start и приступай к заданиям!')
    await callback_query.message.delete()

@router.callback_query(F.data.startswith('verify_failed'))
async def verify (callback_query: types.CallbackQuery, bot: Bot) -> None:
    failed_text = ('К сожалению, вы не сможете принять участие, наше мероприятие только для студентов СПбГУТ им. проф. М.А. Бонч-Бруевича. Если ты студент СПбГУТ отправь фото своего пропуска, перед этим заново написав /start.')
    tg_id = callback_query.data.split('_')[-1]
    await bot.send_message(chat_id=tg_id, text=f'{failed_text}')
    await callback_query.message.delete()

@router.callback_query(F.data.startswith('done'))
async def wallet_change1(callback_query: types.CallbackQuery, bot: Bot) -> None:
        tg_id = callback_query.data.split('_')[1]
        quest = callback_query.data.split('_')[-1]
        if quest == 'd2':
            reward = 10
            ans_to_user = 'Задание 2 из Сделай это'
        elif quest == 'd3':
            reward = 10
            ans_to_user = 'Задание 3 из Сделай это'
        elif quest == 'd4':
            reward = 10
            ans_to_user = 'Задание 4 из Сделай это'
        elif quest == 'd5':
            reward = 10
            ans_to_user = 'Задание 5 из Сделай это'
        elif quest == 'd6':
            reward = 10
            ans_to_user = 'Задание 6 из Сделай это'
        elif quest == 'd7':
            reward = 10
            ans_to_user = 'Задание 7 из Сделай это'
        elif quest == 'd8':
            reward = 10
            ans_to_user = 'Задание 8 из Сделай это'
        elif quest == 'd9':
            reward = 20
            ans_to_user = 'Задание 9 из Сделай это'
        elif quest == 'd10':
            reward = 20
            ans_to_user = 'Задание 10 из Сделай это'
        elif quest == 'd11':
            reward = 20
            ans_to_user = 'Задание 11 из Сделай это'
        elif quest == 'd12':
            reward = 20
            ans_to_user = 'Задание 12 из Сделай это'
        elif quest == 'd13':
            reward = 20
            ans_to_user = 'Задание 13 из Сделай это'
        elif quest == 'd14':
            reward = 20
            ans_to_user = 'Задание 14 из Сделай это'
        elif quest == 'd15':
            reward = 30
            ans_to_user = 'Задание 15 из Сделай это'
        elif quest == 'd16':
            reward = 30
            ans_to_user = 'Задание 16 из Сделай это'
        elif quest == 'd17':
            reward = 30
            ans_to_user = 'Задание 17 из Сделай это'
        elif quest == 'd18':
            reward = 30
            ans_to_user = 'Задание 18 из Сделай это'
        elif quest == 'd19':
            reward = 30
            ans_to_user = 'Задание 19 из Сделай это'
        elif quest == 'd20':
            reward = 30
            ans_to_user = 'Задание 20 из Сделай это'
        elif quest == 'l2':
            reward = 15
            ans_to_user = 'Задание 2 из Изучи это'
        elif quest == 'l3':
            reward = 15
            ans_to_user = 'Задание 3 из Изучи это'
        elif quest == 'l4':
            reward = 15
            ans_to_user = 'Задание 4 из Изучи это'
        elif quest == 'l5':
            reward = 15
            ans_to_user = 'Задание 5 из Изучи это'
        elif quest == 'l6':
            reward = 15
            ans_to_user = 'Задание 6 из Изучи это'
        elif quest == 'l7':
            reward = 15
            ans_to_user = 'Задание 7 из Изучи это'
        elif quest == 'l8':
            reward = 15
            ans_to_user = 'Задание 8 из Изучи это'
        elif quest == 'l9':
            reward = 15
            ans_to_user = 'Задание 9 из Изучи это'
        elif quest == 'l10':
            reward = 15
            ans_to_user = 'Задание 10 из Изучи это'
        elif quest == 'l1':
            reward = 15
            ans_to_user = 'Задание 1 из Изучи это'
        elif quest == 'irl2':
            reward = 50
            ans_to_user = '2 очное общее  задание'
        elif quest == 'irl3':
            reward = 50
            ans_to_user = '3 очное общее  задание'
        elif quest == 'irl4':
            reward = 40
            ans_to_user = '4 очное общее задание'
        elif quest == 'irl5':
            reward = 40
            ans_to_user = '5 очное общее задание'
        elif quest == 'irl6':
            reward = 40
            ans_to_user = '6 очное общее задание'
        elif quest == 'irl7':
            reward = 30
            ans_to_user = '7 очное общее задание'
        elif quest == 'irl8':
            reward = 30
            ans_to_user = '8 очное общее задание'
        elif quest == 'irl9':
            reward = 30
            ans_to_user = '9 очное общее задание'
        elif quest == 'irl1':
            reward = 50
            ans_to_user = '1 очное общее задание'
        elif quest == 'oirl1':
            reward = 50
            ans_to_user = '1 очное задание СПО Орбита'
        elif quest == 'oirl2':
            reward = 50
            ans_to_user = '2 очное задание СПО Орбита'
        elif quest == 'oirl3':
            reward = 40
            ans_to_user = '3 очное задание СПО Орбита'
        elif quest == 'oirl4':
            reward = 40
            ans_to_user = '4 очное задание СПО Орбита'
        elif quest == 'oirl5':
            reward = 30
            ans_to_user = '5 очное задание СПО Орбита'
        elif quest == 'oirl6':
            reward = 30
            ans_to_user = '6 очное задание СПО Орбита'
        elif quest == 'ol2':
            reward = 15
            ans_to_user = '2 задание СПО Орбита из Изучи это'
        elif quest == 'ol1':
            reward = 15
            ans_to_user = '1 задание СПО Орбита из Изучи это'
        elif quest == 'od1':
            reward = 20
            ans_to_user = '1 задание СПО Орбита из Сделай это'
        elif quest == 'od2':
            reward = 20
            ans_to_user = '2 задание СПО Орбита из Сделай это'
        elif quest == 'od3':
            reward = 20
            ans_to_user = '3 задание СПО Орбита из Сделай это'
        elif quest == 'lirl1':
            reward = 50
            ans_to_user = '1 очное задание СОП Лотос'
        elif quest == 'lirl2':
            reward = 50
            ans_to_user = '2 очное задание СОП Лотос'
        elif quest == 'lirl3':
            reward = 40
            ans_to_user = '3 очное задание СОП Лотос'
        elif quest == 'lirl4':
            reward = 40
            ans_to_user = '4 очное задание СОП Лотос'
        elif quest == 'lirl5':
            reward = 30
            ans_to_user = '5 очное задание СОП Лотос'
        elif quest == 'lirl6':
            reward = 30
            ans_to_user = '6 очное задание СОП Лотос'
        elif quest == 'll2':
            reward = 15
            ans_to_user = '2 задание СОП Лотос из Изучи это'
        elif quest == 'll1':
            reward = 15
            ans_to_user = '1 задание СОП Лотос из Изучи это'
        elif quest == 'ld1':
            reward = 20
            ans_to_user = '1 задание СОП Лотос из Сделай это'
        elif quest == 'ld2':
            reward = 20
            ans_to_user = '2 задание СОП Лотос из Сделай это'
        elif quest == 'ld3':
            reward = 20
            ans_to_user = '3 задание СОП Лотос из Сделай это'
        elif quest == 'kirl1':
            reward = 50
            ans_to_user = '1 очное задание ССхО Космея'
        elif quest == 'kirl2':
            reward = 50
            ans_to_user = '2 очное задание ССхО Космея'
        elif quest == 'kirl3':
            reward = 40
            ans_to_user = '3 очное задание ССхО Космея'
        elif quest == 'kirl4':
            reward = 40
            ans_to_user = '4 очное задание ССхО Космея'
        elif quest == 'kirl5':
            reward = 30
            ans_to_user = '5 очное задание ССхО Космея'
        elif quest == 'kirl6':
            reward = 30
            ans_to_user = '6 очное задание ССхО Космея'
        elif quest == 'kl2':
            reward = 15
            ans_to_user = '2 задание ССхО Космея из Изучи это'
        elif quest == 'kl1':
            reward = 15
            ans_to_user = '1 задание ССхО Космея из Изучи это'
        elif quest == 'kd1':
            reward = 20
            ans_to_user = '1 задание ССхО Космея из Сделай это'
        elif quest == 'kd2':
            reward = 20
            ans_to_user = '2 задание ССхО Космея из Сделай это'
        elif quest == 'kd3':
            reward = 20
            ans_to_user = '3 задание ССхО Космея из Сделай это'
        elif quest == 'svirl1':
            reward = 50
            ans_to_user = '1 очное задание СПО Северная Венеция'
        elif quest == 'svirl2':
            reward = 50
            ans_to_user = '2 очное задание СПО Северная Венеция'
        elif quest == 'svirl3':
            reward = 40
            ans_to_user = '3 очное задание СПО Северная Венеция'
        elif quest == 'svirl4':
            reward = 40
            ans_to_user = '4 очное задание СПО Северная Венеция'
        elif quest == 'svirl5':
            reward = 30
            ans_to_user = '5 очное задание СПО Северная Венеция'
        elif quest == 'svirl6':
            reward = 30
            ans_to_user = '6 очное задание СПО Северная Венеция'
        elif quest == 'svl2':
            reward = 15
            ans_to_user = '2 задание СПО Северная Венеция из Изучи это'
        elif quest == 'svl1':
            reward = 15
            ans_to_user = '1 задание СПО Северная Венеция из Изучи это'
        elif quest == 'svd1':
            reward = 20
            ans_to_user = '1 задание СПО Северная Венеция из Сделай это'
        elif quest == 'svd2':
            reward = 20
            ans_to_user = '2 задание СПО Северная Венеция из Сделай это'
        elif quest == 'svd3':
            reward = 20
            ans_to_user = '3 задание СПО Северная Венеция из Сделай это'
        elif quest == 'airl1':
            reward = 50
            ans_to_user = '1 очное задание СМедО АТОМ'
        elif quest == 'airl2':
            reward = 50
            ans_to_user = '2 очное задание СМедО АТОМ'
        elif quest == 'airl3':
            reward = 40
            ans_to_user = '3 очное задание СМедО АТОМ'
        elif quest == 'airl4':
            reward = 40
            ans_to_user = '4 очное задание СМедО АТОМ'
        elif quest == 'airl5':
            reward = 30
            ans_to_user = '5 очное задание СМедО АТОМ'
        elif quest == 'airl6':
            reward = 30
            ans_to_user = '6 очное задание СМедО АТОМ'
        elif quest == 'al2':
            reward = 15
            ans_to_user = '2 задание СМедО АТОМ из Изучи это'
        elif quest == 'al1':
            reward = 15
            ans_to_user = '1 задание СМедО АТОМ из Изучи это'
        elif quest == 'ad1':
            reward = 20
            ans_to_user = '1 задание СМедО АТОМ из Сделай это'
        elif quest == 'ad2':
            reward = 20
            ans_to_user = '2 задание СМедО АТОМ из Сделай это'
        elif quest == 'ad3':
            reward = 20
            ans_to_user = '3 задание СМедО АТОМ из Сделай это'
        elif quest == 'eirl1':
            reward = 50
            ans_to_user = '1 очное задание ССО Эдем'
        elif quest == 'eirl2':
            reward = 50
            ans_to_user = '2 очное задание ССО Эдем'
        elif quest == 'eirl3':
            reward = 40
            ans_to_user = '3 очное задание ССО Эдем'
        elif quest == 'eirl4':
            reward = 40
            ans_to_user = '4 очное задание ССО Эдем'
        elif quest == 'eirl5':
            reward = 30
            ans_to_user = '5 очное задание ССО Эдем'
        elif quest == 'eirl6':
            reward = 30
            ans_to_user = '6 очное задание ССО Эдем'
        elif quest == 'el2':
            reward = 15
            ans_to_user = '2 задание ССО Эдем из Изучи это'
        elif quest == 'el1':
            reward = 15
            ans_to_user = '1 задание ССО Эдем из Изучи это'
        elif quest == 'ed1':
            reward = 20
            ans_to_user = '1 задание ССО Эдем из Сделай это'
        elif quest == 'ed2':
            reward = 20
            ans_to_user = '2 задание ССО Эдем из Сделай это'
        elif quest == 'ed3':
            reward = 20
            ans_to_user = '3 задание ССО Эдем из Сделай это'
        elif quest == 'dq1':
            reward = 100
            ans_to_user = 'Ежедневное задание'
        elif quest == 'dq2':
            reward = 100
            ans_to_user = 'Ежедневное задание'
        elif quest == 'dq3':
            reward = 100
            ans_to_user = 'Ежедневное задание'
        elif quest == 'dq4':
            reward = 100
            ans_to_user = 'Ежедневное задание'
        elif quest == 'dq5':
            reward = 100
            ans_to_user = 'Ежедневное задание'
        elif quest == 's2':
            reward = 5
            ans_to_user = '2 задание из "Подпишись"'
        elif quest == 's3':
            reward = 5
            ans_to_user = '3 задание из "Подпишись"'
        elif quest == 's4':
            reward = 5
            ans_to_user = '4 задание из "Подпишись"'
        elif quest == 's5':
            reward = 5
            ans_to_user = '5 задание из "Подпишись"'
        elif quest == 's6':
            reward = 5
            ans_to_user = '6 задание из "Подпишись"'
        elif quest == 's7':
            reward = 5
            ans_to_user = '7 задание из "Подпишись"'
        elif quest == 's8':
            reward = 5
            ans_to_user = '8 задание из "Подпишись"'
        elif quest == 's9':
            reward = 5
            ans_to_user = '9 задание из "Подпишись"'
        elif quest == 's1':
            reward = 15
            ans_to_user = '1 задание из "Подпишись"'

        db = await aiosqlite.connect('quest_list.db')
        await db.execute(f'UPDATE quest_list SET {quest} = 0 WHERE tg_id == "{tg_id}"')
        cursor = await db.execute(f'SELECT user_name FROM quest_list WHERE tg_id == "{tg_id}"')
        data = await cursor.fetchone()
        await db.commit()
        await db.close()
        dbd = await aiosqlite.connect('tg_users_wallet.db')
        await dbd.execute(f'UPDATE users_wallet SET wallet = wallet + {reward} WHERE tg_id == "{tg_id}"')
        await dbd.commit()
        await dbd.close()
        await callback_query.message.answer(f'Операция прошла успешно!{(str(data))[2:-3]} получил свои BonchCoins за {ans_to_user}')

        await bot.send_message(chat_id=tg_id,text= f'{ans_to_user} выполнено! Ты получил {reward} BonchCoins!')
        await callback_query.message.delete()
        await callback_query.answer('Операция выполнена')


@router.callback_query(F.data.startswith('not_done'))
async def wallet_change1(callback_query: types.CallbackQuery, bot: Bot) -> None:
    tg_id = callback_query.data.split('_')[2]
    quest = callback_query.data.split('_')[-1]
    if quest == 'd2':
        ans_to_user = 'Задание 2 из Сделай это'
    elif quest == 'd3':
        ans_to_user = 'Задание 3 из Сделай это'
    elif quest == 'd4':
        ans_to_user = 'Задание 4 из Сделай это'
    elif quest == 'd5':
        ans_to_user = 'Задание 5 из Сделай это'
    elif quest == 'd6':
        ans_to_user = 'Задание 6 из Сделай это'
    elif quest == 'd7':
        ans_to_user = 'Задание 7 из Сделай это'
    elif quest == 'd8':
        ans_to_user = 'Задание 8 из Сделай это'
    elif quest == 'd9':
        ans_to_user = 'Задание 9 из Сделай это'
    elif quest == 'd10':
        ans_to_user = 'Задание 10 из Сделай это'
    elif quest == 'd11':
        ans_to_user = 'Задание 11 из Сделай это'
    elif quest == 'd12':
        ans_to_user = 'Задание 12 из Сделай это'
    elif quest == 'd13':
        ans_to_user = 'Задание 13 из Сделай это'
    elif quest == 'd14':
        ans_to_user = 'Задание 14 из Сделай это'
    elif quest == 'l2':
        ans_to_user = 'Задание 2 из Изучи это'
    elif quest == 'l3':
        ans_to_user = 'Задание 3 из Изучи это'
    elif quest == 'l4':
        ans_to_user = 'Задание 4 из Изучи это'
    elif quest == 'l5':
        ans_to_user = 'Задание 5 из Изучи это'
    elif quest == 'l6':
        ans_to_user = 'Задание 6 из Изучи это'
    elif quest == 'l7':
        ans_to_user = 'Задание 7 из Изучи это'
    elif quest == 'l8':
        ans_to_user = 'Задание 8 из Изучи это'
    elif quest == 'l9':
        ans_to_user = 'Задание 9 из Изучи это'
    elif quest == 'l10':
        ans_to_user = 'Задание 10 из Изучи это'
    elif quest == 'l1':
        ans_to_user = 'Задание 1 из Изучи это'
    elif quest == 'irl2':
        ans_to_user = '2 очное общее  задание'
    elif quest == 'irl3':
        ans_to_user = '3 очное общее  задание'
    elif quest == 'irl4':
        ans_to_user = '4 очное общее задание'
    elif quest == 'irl5':
        ans_to_user = '5 очное общее задание'
    elif quest == 'irl6':
        ans_to_user = '6 очное общее задание'
    elif quest == 'irl7':
        ans_to_user = '7 очное общее задание'
    elif quest == 'irl8':
        ans_to_user = '8 очное общее задание'
    elif quest == 'irl9':
        ans_to_user = '9 очное общее задание'
    elif quest == 'irl1':
        ans_to_user = '1 очное общее задание'
    elif quest == 'oirl1':
        ans_to_user = '1 очное задание СПО Орбита'
    elif quest == 'oirl2':
        ans_to_user = '2 очное задание СПО Орбита'
    elif quest == 'oirl3':
        ans_to_user = '3 очное задание СПО Орбита'
    elif quest == 'oirl4':
        ans_to_user = '4 очное задание СПО Орбита'
    elif quest == 'oirl5':
        ans_to_user = '5 очное задание СПО Орбита'
    elif quest == 'oirl6':
        ans_to_user = '6 очное задание СПО Орбита'
    elif quest == 'ol2':
        ans_to_user = '2 задание СПО Орбита из Изучи это'
    elif quest == 'ol1':
        ans_to_user = '1 задание СПО Орбита из Изучи это'
    elif quest == 'od1':
        ans_to_user = '1 задание СПО Орбита из Сделай это'
    elif quest == 'od2':
        ans_to_user = '2 задание СПО Орбита из Сделай это'
    elif quest == 'od3':
        ans_to_user = '3 задание СПО Орбита из Сделай это'
    elif quest == 'lirl1':
        ans_to_user = '1 очное задание СОП Лотос'
    elif quest == 'lirl2':
        ans_to_user = '2 очное задание СОП Лотос'
    elif quest == 'lirl3':
        ans_to_user = '3 очное задание СОП Лотос'
    elif quest == 'lirl4':
        ans_to_user = '4 очное задание СОП Лотос'
    elif quest == 'lirl5':
        ans_to_user = '5 очное задание СОП Лотос'
    elif quest == 'lirl6':
        ans_to_user = '6 очное задание СОП Лотос'
    elif quest == 'll2':
        ans_to_user = '2 задание СОП Лотос из Изучи это'
    elif quest == 'll1':
        ans_to_user = '1 задание СОП Лотос из Изучи это'
    elif quest == 'ld1':
        ans_to_user = '1 задание СОП Лотос из Сделай это'
    elif quest == 'ld2':
        ans_to_user = '2 задание СОП Лотос из Сделай это'
    elif quest == 'ld3':
        ans_to_user = '3 задание СОП Лотос из Сделай это'
    elif quest == 'kirl1':
        ans_to_user = '1 очное задание ССхО Космея'
    elif quest == 'kirl2':
        ans_to_user = '2 очное задание ССхО Космея'
    elif quest == 'kirl3':
        ans_to_user = '3 очное задание ССхО Космея'
    elif quest == 'kirl4':
        ans_to_user = '4 очное задание ССхО Космея'
    elif quest == 'kirl5':
        ans_to_user = '5 очное задание ССхО Космея'
    elif quest == 'kirl6':
        ans_to_user = '6 очное задание ССхО Космея'
    elif quest == 'kl2':
        ans_to_user = '2 задание ССхО Космея из Изучи это'
    elif quest == 'kl1':
        ans_to_user = '1 задание ССхО Космея из Изучи это'
    elif quest == 'kd1':
        ans_to_user = '1 задание ССхО Космея из Сделай это'
    elif quest == 'kd2':
        ans_to_user = '2 задание ССхО Космея из Сделай это'
    elif quest == 'kd3':
        ans_to_user = '3 задание ССхО Космея из Сделай это'
    elif quest == 'svirl1':
        ans_to_user = '1 очное задание СПО Северная Венеция'
    elif quest == 'svirl2':
        ans_to_user = '2 очное задание СПО Северная Венеция'
    elif quest == 'svirl3':
        ans_to_user = '3 очное задание СПО Северная Венеция'
    elif quest == 'svirl4':
        ans_to_user = '4 очное задание СПО Северная Венеция'
    elif quest == 'svirl5':
        ans_to_user = '5 очное задание СПО Северная Венеция'
    elif quest == 'svirl6':
        ans_to_user = '6 очное задание СПО Северная Венеция'
    elif quest == 'svl2':
        ans_to_user = '2 задание СПО Северная Венеция из Изучи это'
    elif quest == 'svl1':
        ans_to_user = '1 задание СПО Северная Венеция из Изучи это'
    elif quest == 'svd1':
        ans_to_user = '1 задание СПО Северная Венеция из Сделай это'
    elif quest == 'svd2':
        ans_to_user = '2 задание СПО Северная Венеция из Сделай это'
    elif quest == 'svd3':
        ans_to_user = '3 задание СПО Северная Венеция из Сделай это'
    elif quest == 'airl1':
        ans_to_user = '1 очное задание СМедО АТОМ'
    elif quest == 'airl2':
        ans_to_user = '2 очное задание СМедО АТОМ'
    elif quest == 'airl3':
        ans_to_user = '3 очное задание СМедО АТОМ'
    elif quest == 'airl4':
        ans_to_user = '4 очное задание СМедО АТОМ'
    elif quest == 'airl5':
        ans_to_user = '5 очное задание СМедО АТОМ'
    elif quest == 'airl6':
        ans_to_user = '6 очное задание СМедО АТОМ'
    elif quest == 'al2':
        ans_to_user = '2 задание СМедО АТОМ из Изучи это'
    elif quest == 'al1':
        ans_to_user = '1 задание СМедО АТОМ из Изучи это'
    elif quest == 'ad1':
        ans_to_user = '1 задание СМедО АТОМ из Сделай это'
    elif quest == 'ad2':
        ans_to_user = '2 задание СМедО АТОМ из Сделай это'
    elif quest == 'ad3':
        ans_to_user = '3 задание СМедО АТОМ из Сделай это'
    elif quest == 'eirl1':
        ans_to_user = '1 очное задание ССО Эдем'
    elif quest == 'eirl2':
        ans_to_user = '2 очное задание ССО Эдем'
    elif quest == 'eirl3':
        ans_to_user = '3 очное задание ССО Эдем'
    elif quest == 'eirl4':
        ans_to_user = '4 очное задание ССО Эдем'
    elif quest == 'eirl5':
        ans_to_user = '5 очное задание ССО Эдем'
    elif quest == 'eirl6':
        ans_to_user = '6 очное задание ССО Эдем'
    elif quest == 'el2':
        ans_to_user = '2 задание ССО Эдем из Изучи это'
    elif quest == 'el1':
        ans_to_user = '1 задание ССО Эдем из Изучи это'
    elif quest == 'ed1':
        ans_to_user = '1 задание ССО Эдем из Сделай это'
    elif quest == 'ed2':
        ans_to_user = '2 задание ССО Эдем из Сделай это'
    elif quest == 'ed3':
        ans_to_user = '3 задание ССО Эдем из Сделай это'
    elif quest == 'dq1':
        ans_to_user = 'Ежедневное задание'
    elif quest == 'dq2':
        ans_to_user = 'Ежедневное задание'
    elif quest == 'dq3':
        ans_to_user = 'Ежедневное задание'
    elif quest == 'dq4':
        ans_to_user = 'Ежедневное задание'
    elif quest == 'dq5':
        ans_to_user = 'Ежедневное задание'
    await bot.send_message(chat_id=tg_id,text= f'{ans_to_user} выполнено неправильно, попробуй еще раз.')
    await callback_query.message.delete()
    await callback_query.answer('')


@router.message(F.text.lower().contains('откуда узнал'))
async def wallet_change(message: Message, bot: Bot) -> None:
    if message.from_user.id in ADMIN:
        qr = (str(await how_many_qr()))[1:-2]
        friend = (str(await how_many_friends()))[1:-2]
        other = (str(await how_many_other()))[1:-2]
        social = (str(await how_many_social()))[1:-2]
        await bot.send_message(message.chat.id, f'Рассказал друг: {friend}\nQR: {qr}\nСоцсети: {social}\nДругое: {other}')
    else:await bot.send_message(message.chat.id, 'Жулик, не воруй!')

@router.message(F.text.lower().contains('остаток'))
async def balance(message: Message, bot: Bot) -> None:
    if message.from_user.id in ADMIN:
        sh1 = (str(await shop_balance('sh1')))[1:-2]
        sh2 = (str(await shop_balance('sh2')))[1:-2]
        sh3 = (str(await shop_balance('sh3')))[1:-2]
        sh4 = (str(await shop_balance('sh4')))[1:-2]
        sh5 = (str(await shop_balance('sh5')))[1:-2]
        sh6 = (str(await shop_balance('sh6')))[1:-2]
        sh7 = (str(await shop_balance('sh7')))[1:-2]
        sh8 = (str(await shop_balance('sh8')))[1:-2]
        sh9 = (str(await shop_balance('sh9')))[1:-2]
        sh10 = (str(await shop_balance('sh10')))[1:-2]
        sh11 = (str(await shop_balance('sh11')))[1:-2]
        sh12 = (str(await shop_balance('sh12')))[1:-2]
        sh13 = (str(await shop_balance('sh13')))[1:-2]
        sh14 = (str(await shop_balance('sh14')))[1:-2]
        sh15 = (str(await shop_balance('sh15')))[1:-2]
        sh16 = (str(await shop_balance('sh16')))[1:-2]
        sh17 = (str(await shop_balance('sh17')))[1:-2]
        sh18 = (str(await shop_balance('sh18')))[1:-2]
        sh19 = (str(await shop_balance('sh19')))[1:-2]
        sh20 = (str(await shop_balance('sh20')))[1:-2]
        sh21 = (str(await shop_balance('sh21')))[1:-2]
        sh22 = (str(await shop_balance('sh22')))[1:-2]
        sh23 = (str(await shop_balance('sh23')))[1:-2]
        sh24 = (str(await shop_balance('sh24')))[1:-2]
        sh25 = (str(await shop_balance('sh25')))[1:-2]
        await bot.send_message(message.chat.id, f'Секретный подарок от ССхО Космея: {sh1}'
                                                f'\nСекретный подарок от СОП Лотос: {sh2}'
                                                f'\nСекретный подарок от ССО Эдем: {sh3}'
                                                f'\nСекретный подарок от СМедО АТОМ: {sh4}'
                                                f'\nСекретный подарок от СПО Орбита: {sh5}'
                                                f'\nСекретный подарок от СПО Северная Венеция: {sh6}'
                                                f'\nСвитшот: {sh7}'
                                                f'\nФутболка: {sh8}'
                                                f'\nШоппер: {sh9}'
                                                f'\nБарсетка: {sh10}'
                                                f'\nНоски: {sh11}'
                                                f'\nДождевик: {sh12}'
                                                f'\nТермокружка: {sh13}'
                                                f'\nОбложка для студака: {sh14}'
                                                f'\nОбложка для паспорта: {sh15}'
                                                f'\nКартхолдер: {sh16}'
                                                f'\nЕжедневник: {sh17}'
                                                f'\nМеталлический значок: {sh18}'
                                                f'\nКалендарь : {sh19}'
                                                f'\nПостер А2: {sh20}'
                                                f'\nСтикерпак: {sh21}'
                                                f'\nЗакатной значок: {sh22}'
                                                f'\nСиликоновый браслет: {sh23}'
                                                f'\nСтартер от Додо-Пицца: {sh24}'
                                                f'\nСертификат на кофе: {sh25}')
    else:await bot.send_message(message.chat.id, 'Жулик, не воруй!')


@router.message(F.text.lower().contains('рассылка'))
async def news(message: Message, bot: Bot) -> None:
    if message.from_user.id in ADMIN:
        text = message.text[9:]
        db = await aiosqlite.connect('verify.db')
        cursor = await db.execute(f'SELECT tg_id FROM users_verify')
        users = await cursor.fetchall()
        for id in users:
            try:
                await bot.send_message(id[0], f'{text}')
            except:
                pass
    else:await bot.send_message(message.chat.id, 'Жулик, не воруй!')
