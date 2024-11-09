import asyncio
import datetime
from typing import Any, Awaitable, Callable, Union

from aiogram import Router, types, F, BaseMiddleware
from app.keyboards import (type_quests_list_online,
                           quiz1_4_, quiz1, quiz2, quiz3, quiz4, quiz5, quiz6, quiz7,
                           quiz8, quiz9, quiz10, quiz5_8_, quiz9_12_, doit1_4_, doit5_8_, doit9_12_, doit13_16_, doit17_20_, learn5_8_, learn9_12_, learn1_4_, irl_ready, get_type_of_quest, done, subs1_4_, subs5_8_, subs9_12_, orblink, svlink, edemlink, lotoslink, kosmeyalink, atomlink, shtablink, link1, link2, link3, videolink1, videolink2, videolink3, videolink4, videolink5, videolink6, videolink7, videolink8, videolink9, videolink10)
from app.db_requests import (quiz_exist, quiz_reward, delete_quiz)
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from aiogram.types import Message, InputMediaPhoto, InputMedia



router = Router()


class Test(StatesGroup):
    answersubs = State()
    d2 = State()
    d3 = State()
    d4 = State()
    d5 = State()
    d6 = State()
    d7 = State()
    d8 = State()
    d9 = State()
    d10 = State()
    d11 = State()
    d12 = State()
    d13 = State()
    d14 = State()
    d15 = State()
    d16 = State()
    d17 = State()
    d18 = State()
    d19 = State()
    d20 = State()
    l1 = State()
    l2 = State()
    l3 = State()
    l4 = State()
    l5 = State()
    l6 = State()
    l7 = State()
    l8 = State()
    l9 = State()
    l10 = State()
    s1 = State()
    s2 = State()
    s3 = State()
    s4 = State()
    s5 = State()
    s6 = State()
    s7 = State()
    s8 = State()
    s9 = State()
    s10 = State()

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

quiz1_4 = ('1. В каком году зародилось движение студенческих отрядов?'
          '\n2. Сколько направлений студенческих отрядов есть в СПбГУТ?'
          '\n3. Первый отряд из ныне действующих, который появился в СПбГУТ?'
          '\n4. Как называется фирменная одежда бойца студенческих отрядов СПбГУТ?')

quiz5_8 = ('5. Какой студенческий отряд самый молодой в СПбГУТ?'
             '\n6. Какой должности нет в студенческом отряде?'
             '\n7. Сколько бойцов студенческих отрядов числится в отрядах СПбГУТ?'
             '\n8. Как называют участника студенческих отрядов, который выехал на сезон, '
             'но еще не стал бойцом?')

quiz9_12 = ('9. Что изображено помимо скобочек на логотипе штаба студенческих отрядов СПбГУТ?'
             '\n10. Сколько действующих студенческих отрядов в Санкт-Петербурге?')


todo1_4 = ('1. Пригласи своих друзей из Бонча в телеграм-бот, чтобы они также выполняли задания! За каждого друга получишь 10 БончКоинов. Друг при регистрации в боте должен указать твой ник в телеграме.'
           '\n2. Пройди тест, какое направление тебе подходит, оставь результат в комментариях к посту, а сюда отправляй скриншот.'
           '\n3. Напиши, топ-5 вещей, которые важны для тебя в твоём первом опыте работы.'
           '\n4. Нарисуй на листочке логотип штаба СПбГУТ. Фото рисунка отправляй сюда.')


todo5_8 = ('5. Напиши 5 городов России, где ни разу не был, но хотелось бы посетить.'
           '\n6. Напиши минимум 5 действующих штабов студенческих отрядов в Санкт-Петербурге.'
           '\n7. Почему 17 февраля особенный день для студенческих отрядов? Напиши свой ответ.'
           '\n8 Напиши название любого художественного фильма про студенческие отряды.')


todo9_12 = ('9. Сделай коллаж, который будет посвящен студенческим отрядам СПбГУТ в любом графическом редакторе и поделись со мной.'
            '\n10 Сделай фото в фотобудке в зоне Отряд Festa с 12 до 13 часов и прикрепи фото своей фотокарточки в ответ мне.'
            '\n11 Изучи биографию известного человека, который состоял в студенческих отрядах. Напиши об этом человеке минимум 5 предложений.'
            '\n12 Приведи цитату из своей любимой книги, расскажи, что она значит для тебя, а также поделись автором и названием книги.')


todo13_16 = ('13. Придумай свой отряд. Напиши его направление, название и приложи рисунок с логотипом этого отряда.'
             '\n14. Найди фото-выставку «Сезон в объективе» в Бонче, сфотографируй топ-3 работы по твоему мнению и отправляй мне.'
             '\n15. Сделай своё резюме, можешь исспользовать шаблон, отправь мне файл, который получится.'
             '\n16. Сделай своё портфолио, можешь исспользовать шаблон, отправь мне файл, который получится.')


todo17_20 = ('17. Напиши сопроводительное письмо, если бы ты выбрал один из отрядов СПбГУТ для вступления.'
             '\n18. Запиши и отправь мне видеовизитку о себе, используя шаблон: имя, возраст, группу и курс, хобби/увлечения, чем гордишься. '
             '\n19. Придумай себе любую цель на ближайшие 3 года, распиши её по системе SMART и пришли мне.'
             '\n20. Сделай своё примерное расписание дня и оформи его красиво в любом графическом редакторе. Пришли мне изображение.')


subs = ('После выполнения присылай скриншот. Как только модераторы проверят, тебе зачислят БончКоины;)'
        '\n\n 1. Подписаться на группу в ВК Штаба студенческих отрядов СПбГУТ https://vk.com/so_spbsut'
        '\n2. Подписаться на группу в ВК СПО Северная Венеция https://vk.com/venice_of_the_north'
        '\n3. Подписаться на группу в ВК СПО Орбита https://vk.com/spo_orbita '
        '\n4. Подписаться на группу в ВК СОП Лотос https://vk.com/soplotos'
        '\n5. Подписаться на группу в ВК ССхО Космея https://vk.com/ssho_kosmeya'
        '\n6. Подписаться на группу в ВК ССО Эдем https://vk.com/sso_eden'
        '\n7. Подписаться на группу в ВК СМедО АТОМ https://vk.com/smedo_atom'
        '\n8. Подписаться на группу в ВК Санкт-Петербургских студенческих отрядов https://vk.com/spbso'
        '\n9. Подписаться на группу в ВК Российскийх студенческих отрядов https://vk.com/rso_official'
        '\n10. Подписаться на канал в ТГ Российскийх студенческих отрядов https://t.me/rso_official')


learn1_4 = ('Ответы на эти вопросы есть в видео, для просмотра нажимай на нужное задание!'
            '\n\n 1. Зачем Сергей Майоров, ветеран отрядного движения и экс-командир студенческих отрядов ЛЭИС им. проф. М.А. Бонч-Бруевича поехал в первый раз в стройотряд?'
            '\n2. Что написано на подарочных пакетах?'
            '\n3. Какую кричалку кричат ребята, в конце видео?'
            '\n4. На какой минуте и секунде награждают Мистера выпускного бала СПбСО?')


learn5_8 = (' 5. Как называется книга, которая объединяет увлечения Максима и Кати, где она хранится?'
          '\n6. В каком году Полякова Елена Валерьевна, старший преподаватель кафедры ФиЛС, вступила в студенческие отряды?'
          '\n7. На какую жд станцию прибыли участники видео?'
          '\n8. Сколько человек в клипе?')


learn9_12 = (' 9. Какое чувство любит автор этого клипа?'
             '\n10. Что написано на фотозоне справа сверху от буквы «h», слова Bonch ')


irl = ('Приходи на 1 этаж 1 корпуса и выполняй задания:'
        '\n\n1. Угадай 5 мероприятий по значкам.'
       '\n2. Пройди до конца напольную игру.'
       '\n3. Продолжи строчки из отрядных песен.'
       '\n4. Разгадай отрядные ребусы.'
       '\n5. Придумай и расскажи четверостишие про студенческие отряды.'
       '\n6. Получи послание из почты и оставь послание следующему человеку!'
       '\n7. Сыграй в игру "Что в чёрном ящике?"'
       '\n8. Напиши расшифровки аббревиатур в назвнаниях студенческих отрядов.'
       '\n9. Обними любого человека в строевке (зелёная куртка).')


@router.callback_query(F.data == 'general')
async def quests_irl(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer('Выбери тип задания', reply_markup=get_type_of_quest())
        await callback_query.answer('')
    else:

          await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')


@router.callback_query(F.data == 'irl')
async def quests_irl(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{irl}\nНажми на кнопочку ниже, если выполнил задание, тогда модератор сможет подтвердить выполнение задания.",reply_markup=irl_ready())
        await callback_query.answer('')
    else:
      await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')



@router.callback_query(F.data.startswith('irl'))
async def quests_quiz1_4(callback_query: types.CallbackQuery, state: FSMContext, bot: Bot) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='irl1':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание 1 \n Проверьте его и зачислите ему БончКоинов!', reply_markup=done(callback_query.from_user.id, 'irl1'))
            elif callback_query.data.split('_')[-1] =='irl2':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание 2 \n Проверьте его и зачислите ему БончКоинов!', reply_markup=done(callback_query.from_user.id, 'irl2'))
            elif callback_query.data.split('_')[-1] =='irl3':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание 3 \n Проверьте его и зачислите ему БончКоинов!', reply_markup=done(callback_query.from_user.id, 'irl3'))
            elif callback_query.data.split('_')[-1] =='irl4':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание 4 \n Проверьте его и зачислите ему БончКоинов!', reply_markup=done(callback_query.from_user.id, 'irl4'))
            elif callback_query.data.split('_')[-1] =='irl5':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание 5 \n Проверьте его и зачислите ему БончКоинов!', reply_markup=done(callback_query.from_user.id, 'irl5'))
            elif callback_query.data.split('_')[-1] =='irl6':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание 6 \n Проверьте его и зачислите ему БончКоинов!', reply_markup=done(callback_query.from_user.id, 'irl6'))
            elif callback_query.data.split('_')[-1] =='irl7':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание 7 \n Проверьте его и зачислите ему БончКоинов!', reply_markup=done(callback_query.from_user.id, 'irl7'))
            elif callback_query.data.split('_')[-1] =='irl8':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание 8 \n Проверьте его и зачислите ему БончКоинов!' , reply_markup=done(callback_query.from_user.id, 'irl8'))
            elif callback_query.data.split('_')[-1] =='irl9':
                await bot.send_message(chat_id=-1002250236179, text=f'@{callback_query.from_user.username} выполнил очное задание 9 \n Проверьте его и зачислите ему БончКоинов!' , reply_markup=done(callback_query.from_user.id, 'irl9'))
        await  callback_query.answer('')
    else:
      await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')




@router.callback_query(F.data == 'online')
async def quests_online(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"Выбери тип задания!",
                                            reply_markup=type_quests_list_online())
        await callback_query.answer('')
    else:
      await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')



@router.callback_query(F.data == 'learn_it')
async def quests_quiz_p1(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{learn1_4}", reply_markup=learn1_4_())
        await  callback_query.answer('')
    else:
      await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')


@router.callback_query(F.data.startswith('next_to_learn_p'))
async def quests_quiz_next(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if callback_query.data.split('_')[-1] =='p2':
            await callback_query.message.answer(f'{learn5_8}', reply_markup=learn5_8_())
            await callback_query.message.delete()
        if callback_query.data.split('_')[-1] =='p3':
            await callback_query.message.answer(f'{learn9_12}', reply_markup=learn9_12_())
            await callback_query.message.delete()
        await callback_query.answer('')
    else:
      await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')



@router.callback_query(F.data.startswith('back_to_learn_p'))
async def quests_quiz_back(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if callback_query.data.split('_')[-1] =='p1':
            await callback_query.message.answer(f'{learn1_4}', reply_markup=learn1_4_())
            await callback_query.message.delete()
        if callback_query.data.split('_')[-1] =='p2':
            await callback_query.message.answer(f'{learn5_8}', reply_markup=learn5_8_())
            await callback_query.message.delete()
        if callback_query.data.split('_')[-1] =='p3':
            await callback_query.message.answer(f'{learn9_12}', reply_markup=learn9_12_())
            await callback_query.message.delete()
        await callback_query.answer('')
    else:
      await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')



@router.callback_query(F.data.startswith('learn'))
async def quests_quiz1_4(callback_query: types.CallbackQuery, state: FSMContext, bot: Bot) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='l1':
                await callback_query.message.answer(f'Зачем Сергей Майоров, ветеран отрядного движения и экс-командир студенческих отрядов ЛЭИС им. проф. М.А. Бонч-Бруевича поехал в первый раз в стройотряд?\nhttps://vk.com/video-216336347_456239050', reply_markup=videolink1())
                await state.set_state(Test.l1)
            elif callback_query.data.split('_')[-1] =='l2':
                await callback_query.message.answer('Что написано на подарочных пакетах?\nhttps://vk.com/video-30684004_456239841', reply_markup=videolink2())
                await state.set_state(Test.l2)
            elif callback_query.data.split('_')[-1] =='l3':
                await callback_query.message.answer('Какую кричалку кричат ребята, в конце видео?\nhttps://vk.com/video-219159801_456239042', reply_markup=videolink3())
                await state.set_state(Test.l3)
            elif callback_query.data.split('_')[-1] =='l4':
                await callback_query.message.answer('На какой минуте и секунде награждают Мистера выпускного бала СПбСО?\nhttps://vk.com/video-30684004_456239824', reply_markup=videolink4())
                await state.set_state(Test.l4)
            elif callback_query.data.split('_')[-1] =='l5':
                await callback_query.message.answer('Как называется книга, которая объединяет увлечения Максима и Кати, где она хранится?\nhttps://vk.com/video-30684004_456239846', reply_markup=videolink5())
                await state.set_state(Test.l5)
            elif callback_query.data.split('_')[-1] =='l6':
                await callback_query.message.answer('В каком году Полякова Елена Валерьевна, старший преподаватель кафедры ФиЛС, вступила в студенческие отряды?\nhttps://vk.com/video-30684004_456239845', reply_markup=videolink6())
                await state.set_state(Test.l6)
            elif callback_query.data.split('_')[-1] =='l7':
                await callback_query.message.answer('На какую жд станцию прибыли участники видео?\nhttps://vk.com/video-216045400_456239018', reply_markup=videolink7())
                await state.set_state(Test.l7)
            elif callback_query.data.split('_')[-1] =='l8':
                await callback_query.message.answer('Сколько человек в клипе?\nhttps://vk.com/clip-216336347_456239017?c=1', reply_markup=videolink8())
                await state.set_state(Test.l8)
            elif callback_query.data.split('_')[-1] =='l9':
                await callback_query.message.answer('Какое чувство любит автор этого клипа?\nhttps://vk.com/clip-216336347_456239105?c=1', reply_markup=videolink9())
                await state.set_state(Test.l9)
            elif callback_query.data.split('_')[-1] =='l10':
                await callback_query.message.answer('Что написано на фотозоне справа сверху от буквы «h», слова Bonch?\nhttps://vk.com/clip-216336347_456239041?c=1', reply_markup=videolink())
                await state.set_state(Test.l10)
        await  callback_query.answer('')
    else:
      await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')


    @router.message(Test.l2)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(l2=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение второго задания из "Изучи это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'l2'))
        await state.clear()


    @router.message(Test.l3)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(l3=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение третьего задания из "Изучи это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'l3'))
        await state.clear()


    @router.message(Test.l4)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(l4=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение четвертого задания из "Изучи это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'l4'))
        await state.clear()


    @router.message(Test.l5)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(l5=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение пятого задания из "Изучи это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'l5'))
        await state.clear()


    @router.message(Test.l6)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(l6=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение шестого задания из "Изучи это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'l6'))
        await state.clear()


    @router.message(Test.l7)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(l7=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение седьмого задания из "Изучи это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'l7'))
        await state.clear()


    @router.message(Test.l8)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(l8=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение восьмого задания из "Изучи это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'l8'))
        await state.clear()


    @router.message(Test.l9)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(l9=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 9 задания из "Изучи это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'l9'))
        await state.clear()


    @router.message(Test.l10)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(l10=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 10 задания из "Изучи это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'l10'))
        await state.clear()


    @router.message(Test.l1)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(l1=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 1 задания из "Изучи это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'l1'))
        await state.clear()


@router.callback_query(F.data == 'DO_IT')
async def quests_quiz_p1(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{todo1_4}", reply_markup=doit1_4_())
        await  callback_query.answer('')
    else:
      await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')


@router.callback_query(F.data.startswith('next_to_doit_p'))
async def quests_quiz_next(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if callback_query.data.split('_')[-1] =='p2':
            await callback_query.message.answer(f'{todo5_8}', reply_markup=doit5_8_())
            await callback_query.message.delete()
        if callback_query.data.split('_')[-1] =='p3':
            await callback_query.message.answer(f'{todo9_12}', reply_markup=doit9_12_())
            await callback_query.message.delete()
        await callback_query.answer('')
        if callback_query.data.split('_')[-1] =='p4':
            await callback_query.message.answer(f'{todo13_16}', reply_markup=doit13_16_())
            await callback_query.message.delete()
        if callback_query.data.split('_')[-1] =='p5':
            await callback_query.message.answer(f'{todo17_20}', reply_markup=doit17_20_())
            await callback_query.message.delete()
        await callback_query.answer('')
    else:
      await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')



@router.callback_query(F.data.startswith('back_to_doit_p'))
async def quests_quiz_back(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if callback_query.data.split('_')[-1] =='p1':
            await callback_query.message.answer(f'{todo1_4}', reply_markup=doit1_4_())
            await callback_query.message.delete()
        if callback_query.data.split('_')[-1] =='p2':
            await callback_query.message.answer(f'{todo5_8}', reply_markup=doit5_8_())
            await callback_query.message.delete()
        if callback_query.data.split('_')[-1] =='p3':
            await callback_query.message.answer(f'{todo9_12}', reply_markup=doit9_12_())
            await callback_query.message.delete()
        if callback_query.data.split('_')[-1] =='p4':
            await callback_query.message.answer(f'{todo13_16}', reply_markup=doit13_16_())
            await callback_query.message.delete()
        await callback_query.answer('')
    else:
      await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')



@router.callback_query(F.data.startswith('doit'))
async def quests_quiz1_4(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='d1':
                await callback_query.message.answer(f"Пригласи своих друзей из Бонча в телеграмм-бот, чтобы они также выполняли задания! За каждого друга получишь 10 БончКоинов. Друг при регистрации в боте должен указать твой ник в тг.")
            elif callback_query.data.split('_')[-1] =='d2':
                await callback_query.message.answer(f"Пройди тест, какое направление тебе подходит, оставь результат в комментариях и прикрепи скриншот.")
                await state.set_state(Test.d2)
            elif callback_query.data.split('_')[-1] =='d3':
                await callback_query.message.answer(f"Напиши, топ-5 вещей, что для тебя важно в твоём первом опыте работы.")
                await state.set_state(Test.d3)
            elif callback_query.data.split('_')[-1] =='d4':
                await callback_query.message.answer(f"Нарисуй на листочке логотип штаба СПбГУТ. Фото рисунка отправь в ответе.")
                await state.set_state(Test.d4)
            elif callback_query.data.split('_')[-1] =='d5':
                await callback_query.message.answer(f"Напиши 5 городов России, где ни разу не был, но хотел бы посетить.")
                await state.set_state(Test.d5)
            elif callback_query.data.split('_')[-1] =='d6':
                await callback_query.message.answer(f"Напиши минимум 5 действующих штабов студенческих отрядов в Санкт-Петербурге.?")
                await state.set_state(Test.d6)
            elif callback_query.data.split('_')[-1] =='d7':
                await callback_query.message.answer(f"Почему 17 февраля особенный день для студенческих отрядов? Напиши свой ответ.")
                await state.set_state(Test.d7)
            elif callback_query.data.split('_')[-1] =='d8':
                await callback_query.message.answer(f"Напиши название любого художественного фильма про студенческие отряды.")
                await state.set_state(Test.d8)
            elif callback_query.data.split('_')[-1] =='d9':
                await callback_query.message.answer(f"Сделай коллаж, который будет посвящен студенческим отрядам СПбГУТ в любом графическом редактора.")
                await state.set_state(Test.d9)
            elif callback_query.data.split('_')[-1] =='d10':
                await callback_query.message.answer(f"Сделай фото в фотобудке в зоне Отряд Festa с 12 до 13, прикрепи фото фотокарточки в ответ.")
                await state.set_state(Test.d10)
            elif callback_query.data.split('_')[-1] =='d11':
                await callback_query.message.answer(f"Исследуйте биографию известного человека, который состоял в студенческих отрядах. Напиши об этом человеке минимум 5 предложений. ")
                await state.set_state(Test.d11)
            elif callback_query.data.split('_')[-1] =='d12':
                await callback_query.message.answer(f"Приведи цитату из своей любимой книги, опиши, что она значит для тебя, автора и название книги.")
                await state.set_state(Test.d12)
            elif callback_query.data.split('_')[-1] =='d13':
                await callback_query.message.answer(f"Придумай свой отряд. Напиши его аббревиатуру, расшифровку, название и приложи рисунок с логотипом этого отряда.")
                await state.set_state(Test.d13)
            elif callback_query.data.split('_')[-1] =='d14':
                await callback_query.message.answer(f"Найди фото-выставку «Сезон в объективе» в Бонче и сфотографируй топ-3 работы по твоему мнению.")
                await state.set_state(Test.d14)
            elif callback_query.data.split('_')[-1] =='d15':
                await callback_query.message.answer(f"Сделай своё резюме, можешь исспользовать шаблон, оставь файл в подтверждении.")
                await state.set_state(Test.d15)
            elif callback_query.data.split('_')[-1] =='d16':
                await callback_query.message.answer(f"Сделай своё портфолио, можешь исспользовать шаблон, оставь файл в подтверждении.")
                await state.set_state(Test.d16)
            elif callback_query.data.split('_')[-1] =='d17':
                await callback_query.message.answer(f"Напиши сопроводительное письмо, если бы ты выбрал один из отрядов СПбГУТ для вступления.")
                await state.set_state(Test.d17)
            elif callback_query.data.split('_')[-1] =='d18':
                await callback_query.message.answer(f"Запиши видеовизитку о себе, используя шаблон: имя, возраст, группу и курс, хобби/увлечения, чем гордишься.")
                await state.set_state(Test.d18)
            elif callback_query.data.split('_')[-1] =='d19':
                await callback_query.message.answer(f"Придумай себе любую цель на ближайшие 3 года и распиши её по системе SMART.")
                await state.set_state(Test.d19)
            elif callback_query.data.split('_')[-1] =='d20':
                await callback_query.message.answer(f"Сделай своё примерное расписание дня и оформи его красиво в любом графическом редакторе. В ответ пришли изображение.")
                await state.set_state(Test.d20)
        await  callback_query.answer('')
    else:
      await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')


    @router.message(Test.d2)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(d2=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение второго задания из "Сделай это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'd2'))
        await state.clear()


    @router.message(Test.d3)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(d3=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение третьего задания из "Сделай это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'd3'))
        await state.clear()


    @router.message(Test.d4)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(d4=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение четвертого задания из "Сделай это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'd4'))
        await state.clear()


    @router.message(Test.d5)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(d5=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение пятого задания из "Сделай это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'd5'))
        await state.clear()


    @router.message(Test.d6)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(d6=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение шестого задания из "Сделай это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'd6'))
        await state.clear()


    @router.message(Test.d7)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(d7=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение седьмого задания из "Сделай это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'd7'))
        await state.clear()


    @router.message(Test.d8)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(d8=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение восьмого задания из "Сделай это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'd8'))
        await state.clear()


    @router.message(Test.d9)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(d9=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 9 задания из "Сделай это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'd9'))
        await state.clear()

    @router.message(Test.d10)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(d10=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 10 задания из "Сделай это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'd10'))
        await state.clear()


    @router.message(Test.d11)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(d11=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 11 задания из "Сделай это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'd11'))
        await state.clear()


    @router.message(Test.d12)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(d12=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 12 задания из "Сделай это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'd12'))
        await state.clear()


    @router.message(Test.d13)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(d13=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 13 задания из "Сделай это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'd13'))
        await state.clear()

    router.message.middleware(AlbumMiddleware())
    @router.message(Test.d14)
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
        await state.update_data(d14=message.from_user)
        await bot.send_media_group(media=media_group, chat_id=-1002250236179)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 14 задания их "Сделай это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'd14'))
        await state.clear()


    @router.message(Test.d15)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(d15=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 15 задания из "Сделай это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'd15'))
        await state.clear()


    @router.message(Test.d16)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(d16=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 16 задания из "Сделай это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'd16'))
        await state.clear()


    @router.message(Test.d17)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(d17=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 17 задания из "Сделай это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'd17'))
        await state.clear()


    @router.message(Test.d18)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(d18=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 18 задания из "Сделай это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'd18'))
        await state.clear()


    @router.message(Test.d19)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(d19=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 19 задания из "Сделай это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'd19'))
        await state.clear()


    @router.message(Test.d20)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(d20=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 20 задания из "Сделай это", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 'd20'))
        await state.clear()


@router.callback_query(F.data == 'choose_quiz')
async def quests_quiz_p1(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"Будь внимателен, ответить можно только 1 раз\n{quiz1_4}", reply_markup=quiz1_4_())
        await  callback_query.answer('')
    else:
      await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')



@router.callback_query(F.data.startswith('next_to_quiz_p'))
async def quests_quiz_next(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if callback_query.data.split('_')[-1] =='p2':
            await callback_query.message.answer(f'{quiz5_8}', reply_markup=quiz5_8_())
            await callback_query.message.delete()
        if callback_query.data.split('_')[-1] =='p3':
            await callback_query.message.answer(f'{quiz9_12}', reply_markup=quiz9_12_())
            await callback_query.message.delete()
        await callback_query.answer('')
    else:
      await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')



@router.callback_query(F.data.startswith('back_to_quiz_p'))
async def quests_quiz_back(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if callback_query.data.split('_')[-1] =='p1':
            await callback_query.message.answer(f'{quiz1_4}', reply_markup=quiz1_4_())
            await callback_query.message.delete()
        if callback_query.data.split('_')[-1] =='p2':
            await callback_query.message.answer(f'{quiz5_8}', reply_markup=quiz5_8_())
            await callback_query.message.delete()
        await callback_query.answer('')
    else:
      await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')



@router.callback_query(F.data.startswith('quiz'))
async def quests_quiz1_4(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='q1':
                await callback_query.message.answer(f"В каком году зародилось движение студенческих отрядов?", reply_markup=quiz1())
            elif callback_query.data.split('_')[-1] =='q2':
                await callback_query.message.answer(f"Сколько направлений студенческих отрядов есть в СПбГУТ?", reply_markup=quiz2())
            elif callback_query.data.split('_')[-1] =='q3':
                await callback_query.message.answer(f"Первый отряд из ныне действующих, который появился в СПбГУТ?", reply_markup=quiz3())
            elif callback_query.data.split('_')[-1] =='q4':
                await callback_query.message.answer(f"Как называется фирменная одежда бойца студенческих отрядов СПбГУТ?", reply_markup=quiz4())
            elif callback_query.data.split('_')[-1] =='q5':
                await callback_query.message.answer(f"Какой студенческий отряд самый молодой в СПбГУТ?", reply_markup=quiz5())
            elif callback_query.data.split('_')[-1] =='q6':
                await callback_query.message.answer(f"Какой должности нет в студенческом отряде?", reply_markup=quiz6())
            elif callback_query.data.split('_')[-1] =='q7':
                await callback_query.message.answer(f"Сколько бойцов студенческих отрядов числится в отрядах СПбГУТ?", reply_markup=quiz7())
            elif callback_query.data.split('_')[-1] =='q8':
                await callback_query.message.answer(f"Как называют участника студенческих отрядов, который выехал на сезон, но еще не стал бойцом?", reply_markup=quiz8())
            elif callback_query.data.split('_')[-1] =='q9':
                await callback_query.message.answer(f"Что изображено помимо скобочек на логотипе Штаба студенческих отрядов СПбГУТ?", reply_markup=quiz9())
            elif callback_query.data.split('_')[-1] =='q10':
                await callback_query.message.answer(f"Сколько действующих студенческих отрядов в Санкт-Петербурге?", reply_markup=quiz10())
        await  callback_query.answer('')
    else:
      await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')



@router.callback_query(F.data.startswith('answer_true'))
async def correct_answer_online_quest2(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer("Верно!")
        await callback_query.answer('')
        await callback_query.message.delete()
        await quiz_reward(callback_query.from_user.id)
        await delete_quiz(callback_query.from_user.id, callback_query.data.split('_')[-1])
    else:
      await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')



@router.callback_query(F.data.startswith('false'))
async def incorrect_answer_quiz(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer("Ответ неверный :(")
        await callback_query.answer('')
        await delete_quiz(callback_query.from_user.id, callback_query.data.split('_')[-1])
        await callback_query.message.delete()
    else:
      await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')



subs1_4 = ('''После выполнения присылай скриншот. Как только модераторы проверят, тебе зачислят БончКоины;)

1. Подписаться на группу в ВК Штаба студенческих отрядов СПбГУТ
2. Подписаться на группу в ВК СПО Северная Венеция
3. Подписаться на группу в ВК СПО Орбита
4. Подписаться на группу в ВК СОП Лотос''')
subs5_8 = ('''5. Подписаться на группу в ВК ССхО Космея
6. Подписаться на группу в ВК ССО Эдем
7. Подписаться на группу в ВК СМедО АТОМ
8. Подписаться на группу в ВК Санкт-Петербургских студенческих отрядов''')
subs9_12 = ('''9. Подписаться на группу в ВК Российскийх студенческих отрядов
10. Подписаться на канал в ТГ Российскийх студенческих отрядов''')

@router.callback_query(F.data == 'subscribe')
async def quests_quiz_p1(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        await callback_query.message.answer(f"{subs1_4}", reply_markup=subs1_4_())
        await  callback_query.answer('')
    else:
      await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время.')



@router.callback_query(F.data.startswith('next_to_subs_p'))
async def quests_quiz_next(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if callback_query.data.split('_')[-1] =='p2':
            await callback_query.message.answer(f'{subs5_8}', reply_markup=subs5_8_())
            await callback_query.message.delete()
        if callback_query.data.split('_')[-1] =='p3':
            await callback_query.message.answer(f'{subs9_12}', reply_markup=subs9_12_())
            await callback_query.message.delete()
        await callback_query.answer('')
    else:
      await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')



@router.callback_query(F.data.startswith('back_to_subs_p'))
async def quests_quiz_back(callback_query: types.CallbackQuery) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if callback_query.data.split('_')[-1] =='p1':
            await callback_query.message.answer(f'{subs1_4}', reply_markup=subs1_4_())
            await callback_query.message.delete()
        if callback_query.data.split('_')[-1] =='p2':
            await callback_query.message.answer(f'{subs5_8}', reply_markup=subs5_8_())
            await callback_query.message.delete()
        if callback_query.data.split('_')[-1] =='p3':
            await callback_query.message.answer(f'{subs9_12}', reply_markup=subs9_12_())
            await callback_query.message.delete()
        await callback_query.answer('')
    else:
      await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')



@router.callback_query(F.data.startswith('subs'))
async def quests_quiz1_4(callback_query: types.CallbackQuery, state: FSMContext, bot: Bot) -> None:
    if datetime.time(hour=8, minute=59) < datetime.datetime.now().time() < datetime.time(hour=21, minute=0):
        if (str(await quiz_exist(callback_query.from_user.id, callback_query.data.split('_')[-1])))[1:-2] == '0':
            await callback_query.message.answer('Ты уже выполнил это задание!')
        else:
            if callback_query.data.split('_')[-1] =='s1':
                await callback_query.message.answer(f'Подписаться на группу в ВК Штаба студенческих отрядов СПбГУТ\nВ ответ пришли скриншот.', reply_markup=shtablink())
                await state.set_state(Test.s1)
            elif callback_query.data.split('_')[-1] =='s2':
                await callback_query.message.answer('Подписаться на группу в ВК СПО Северная Венеция\nВ ответ пришли скриншот.', reply_markup=svlink())
                await state.set_state(Test.s2)
            elif callback_query.data.split('_')[-1] =='s3':
                await callback_query.message.answer('Подписаться на группу в ВК СПО Орбита\nВ ответ пришли скриншот.', reply_markup=orblink())
                await state.set_state(Test.s3)
            elif callback_query.data.split('_')[-1] =='s4':
                await callback_query.message.answer('Подписаться на группу в ВК СОП Лотос\nВ ответ пришли скриншот.', reply_markup=lotoslink())
                await state.set_state(Test.s4)
            elif callback_query.data.split('_')[-1] =='s5':
                await callback_query.message.answer('Подписаться на группу в ВК ССхО Космея\nВ ответ пришли скриншот.', reply_markup=kosmeyalink)
                await state.set_state(Test.s5)
            elif callback_query.data.split('_')[-1] =='s6':
                await callback_query.message.answer('Подписаться на группу в ВК ССО Эдем\nВ ответ пришли скриншот.', reply_markup=edemlink())
                await state.set_state(Test.s6)
            elif callback_query.data.split('_')[-1] =='s7':
                await callback_query.message.answer('Подписаться на группу в ВК СМедО АТОМ\nВ ответ пришли скриншот.', reply_markup=atomlink())
                await state.set_state(Test.s7)
            elif callback_query.data.split('_')[-1] =='s8':
                await callback_query.message.answer('Подписаться на группу в ВК Санкт-Петербургских студенческих отрядов\nВ ответ пришли скриншот.', reply_markup=link1())
                await state.set_state(Test.s8)
            elif callback_query.data.split('_')[-1] =='s9':
                await callback_query.message.answer('Подписаться на группу в ВК Российскийх студенческих отрядов\nВ ответ пришли скриншот.', reply_markup=link2())
                await state.set_state(Test.s9)
            elif callback_query.data.split('_')[-1] =='s10':
                await callback_query.message.answer('Подписаться на канал в ТГ Российскийх студенческих отрядов\nВ ответ пришли скриншот.', reply_markup=link3())
                await state.set_state(Test.s10)
        await  callback_query.answer('')
    else:
      await callback_query.message.answer('Бот спит, приходи с 9:00 до 21:00, в его рабочее время')



    @router.message(Test.s1)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(s1=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 1 задания из "Подпишись", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 's1'))
        await state.clear()


    @router.message(Test.s2)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(s2=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 2 задания из "Подпишись", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 's2'))
        await state.clear()


    @router.message(Test.s3)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(s3=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 3 задания из "Подпишись", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 's3'))
        await state.clear()


    @router.message(Test.s4)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(s4=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 4 задания из "Подпишись", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 's4'))
        await state.clear()


    @router.message(Test.s5)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(s5=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 5 задания из "Подпишись", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 's5'))
        await state.clear()


    @router.message(Test.s6)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(s6=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 6 задания из "Подпишись", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 's6'))
        await state.clear()


    @router.message(Test.s7)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(s7=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 7 задания из "Подпишись", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 's7'))
        await state.clear()


    @router.message(Test.s8)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(s8=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 8 задания из "Подпишись", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 's8'))
        await state.clear()


    @router.message(Test.s9)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(s9=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 9 задания из "Подпишись", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 's9'))
        await state.clear()


    @router.message(Test.s10)
    async def subs_res(message: Message, bot: Bot, state: FSMContext) -> None:
        await state.update_data(s10=message.from_user)
        await bot.forward_message(chat_id=-1002250236179, message_id=message.message_id, from_chat_id=message.chat.id)
        await bot.send_message(chat_id=-1002250236179, text=f'@{message.from_user.username} прислал решение 10 задания из "Подпишись", проверьте его и зачислите ему БончКоинов!', reply_markup=done(message.from_user.id, 's10'))
        await state.clear()

