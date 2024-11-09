from aiogram import Router, types, F
from aiogram.utils.markdown import hlink
from aiogram.types import FSInputFile
from aiogram.types import URLInputFile
from app.keyboards import orblink, kosmeyalink, shtablink, lotoslink, atomlink, svlink, edemlink

router = Router()


about_orbita = (f'Педагогический отряд "Орбита" объединяет в себе вожатых, которые ежегодно организовывают '
                'каникулярный отдых детей в первую очередь в детских лагерях '
                'Ленинградской области. На счету у коллектива десятки побед '
                'в разных профессиональных конкурсах и тысячи покоренных '
                'детских сердец. Главные слова, которые сопровождают '
                'деятельность отряда — качество, команда, креатив!\nСредняя заработная плата — '
                '25 тысяч за смену*.')


about_venetsia = ('В Педагогическом отряде "Северная Венеция" состоят ребята, которые создают '
                  'настоящую сказку для детей в детских оздоровленных лагерях. '
                  'Вожатые этого отряда подходят к организации каждой смены максимально '
                  'креативно, продумывая и прописывая художественно-ролевую программу, '
                  'чтобы детки смогли погрузиться в атмосферу другого мира от вселенной '
                  '«Гарри Поттера» до тематики «Будущего через 1000 лет»'
                  '\nСредняя заработная плата за одну — 25 тысяч за смену*.')


about_atom = ('Ребята из Медиаотряда "АТОМ" '
              'работают медиа специалистами в детских городских и коммерческих лагерях: '
              'ведут профильные кружки, работают в пресс-центре лагеря, занимаются звуковым и '
              'медиа сопровождением мероприятий. Помимо работы в детских лагерях, медиаотряду '
              'удается работать в качестве фотографов и видеографов на других различных проектах.'
              '\nСредняя заработная плата — 40 тысяч за смену*.')


about_edem = ('Строительный отряд "Эдем" работает на различных строительных объектах нашей страны как регионального, '
              'так и всероссийского масштаба, где выполняют широкий спектр работ в зависимости от '
              'места трудоустройства: бетонные, монтажные, покрасочные и др. Ребята из строительного '
              'отряда покажут настоящую романтику отрядной жизни, а главное вместе вы построите будущее.'
              '\nСредняя заработная плата — 210 тысяч за сезон*.')


about_lotus = ('Отряд проводников "Лотос" работают проводниками пассажирских вагонов на железной дороге.'
               '\nЭто направление для тех, кто любит путешествия и новизну ярких впечатлений. '
               'Постоянная смена пейзажей за окном, калейдоскоп новых лиц, общение с самыми разными '
               'людьми – такова внешняя сторона работы студенческих отрядов проводников, '
               'которую называют романтикой железной дороги.\nСредняя заработная плата — '
               '135 тысяч за сезон*.')


about_kosmeya = ('Сельскохозяйственный отряд "Космея" выполняет работу на сельскохозяйственных землях южных частей России. '
                 'Работа проходит на виноградных полях, где необходимо заниматься '
                 'различной деятельностью по уходу за виноградом, а также собирать спелые фрукты. '
                 'В свободное от работы время, ребята отдыхают на море, покоряют горы и путешествуют '
                 'по разным уголкам того края, где оказались.'
                 '\nСредняя заработная плата — 30 тысяч за сезон*.')


about_headquarter = ('Здесь ты сможешь найти работу, а ещё своих друзей, любовь и путешествия! '
                     'В СПбГУТ отряды действуют с 2018 года по 5 направлениям: вожатые, '
                     'строители, проводники поезда, сборщики урожая и медиа-специалисты. '
                     'Благодаря отрядам летом ты сможешь не только заработать, но и найти настоящих друзей. Чтобы узнать больше, '
                     'скорее подписывайся на группу штаба студенческих отрядов СПбГУТ в ВК')


@router.callback_query(F.data == 'orbita')
async def orbita_peremennaya(callback_query: types.CallbackQuery) -> None:
        photo = FSInputFile('orbita.jpg', filename='orbita.jpg')
        await callback_query.message.answer_photo(photo=photo, caption=f"{about_orbita}", reply_markup=orblink())
        await callback_query.answer("орбита")

@router.callback_query(F.data == 'headquearter')
async def headquarter_peremennaya(callback_query: types.CallbackQuery) -> None:
        photo = FSInputFile('shtab.jpg', filename='shtab.jpg')
        await callback_query.message.answer_photo(photo=photo, caption=f"{about_headquarter}", reply_markup=shtablink())
        await callback_query.answer("штаб")

@router.callback_query(F.data == 'lotos')
async def lotos_peremennaya(callback_query: types.CallbackQuery) -> None:
        photo = FSInputFile('lotos.jpg', filename='lotos.jpg')
        await callback_query.message.answer_photo(photo=photo, caption=f"{about_lotus}", reply_markup=lotoslink())
        await callback_query.answer("лотос")

@router.callback_query(F.data == 'kosmeya')
async def kosmeya_peremennaya(callback_query: types.CallbackQuery) -> None:
        photo = FSInputFile('kosmeya.jpg', filename='kosmeya.jpg')
        await callback_query.message.answer_photo(photo=photo, caption=f"{about_kosmeya}", reply_markup=kosmeyalink())
        await callback_query.answer("космея")

@router.callback_query(F.data == 'edem')
async def edem_peremennaya(callback_query: types.CallbackQuery) -> None:
        photo = FSInputFile('edem.jpg', filename='edem.jpg')
        await callback_query.message.answer_photo(photo=photo, caption=f"{about_edem}", reply_markup=edemlink())
        await callback_query.answer("эдем")

@router.callback_query(F.data == 'venetsia')
async def venetsia_peremennaya(callback_query: types.CallbackQuery) -> None:
        photo = FSInputFile('sv.jpg', filename='sv.jpg')
        await callback_query.message.answer_photo(photo=photo, caption=f"{about_venetsia}", reply_markup=svlink())
        await callback_query.answer("северная венеция")

@router.callback_query(F.data == 'atom')
async def atom_peremennaya(callback_query: types.CallbackQuery) -> None:
        photo = FSInputFile('atom.jpg', filename='atom.jpg')
        await callback_query.message.answer_photo(photo=photo, caption=f"{about_atom}", reply_markup=atomlink())
        await callback_query.answer("атом")

dicti = ('Боец — человек, который уже успел поработать с отрядом на сезоне летом, показал свои '
         'лучшие качества и умение работать в команде. Бойцы – это основной действующий состав. '
         'Они принимают участие во всех мероприятиях и помогают отряду становится лучше.\n\nВетеран — '
         'человек, отработавший в составе отряда три трудовых сезона. Ветераны всегда рады поделиться '
         'своим опытом с более молодыми бойцами, а также рассказать много веселых и поучительных '
         'историй.\n\nКандидат в бойцы — человек, который только вступил в отряд. Ему еще многому '
         'предстоит научиться, показать себя, раскрыть в себе новые таланты, прежде чем стать бойцом.'
         '\n\nКомандир — руководитель студенческого отряда. Он осуществляет трудоустройство своих '
         'бойцов, заботится об их здоровье и следит за внутриотрядной дисциплиной. Несет персональную '
         'ответственность за производственную, общественную и финансово-хозяйственную деятельность '
         'студенческого отряда.\n\nКомиссар — заместитель командира студенческого отряда. Он отвечает '
         'за внутренний климат и атмосферу в отряде, осуществляет участие своих бойцов в спортивных, '
         'социально-значимых и культурно-массовых мероприятиях.\n\nКомендант — заместитель командира '
         'по хозяйственной части. Он является материально ответственным лицом и производит расходы '
         'на внутриотрядные нужды.\n\nМастер (или методист) — заместитель командира студенческого '
         'отряда по производственной деятельности. Отвечает за своевременное и качественное '
         'выполнение отрядом всех работ, за охрану труда, бережное отношение к технике, инвентарю '
         'и материалам.\n\nСезон — время, когда студенческие отряды отправляются на свои места '
         'работы, трудятся на объектах и показывают высокие показатели в работе и творчестве. '
         'Количество рабочих дней на сезоне варьируется от 30 до 45, в зависимости от направления '
         'и объекта работы.\n\nСмена — тоже самое, что сезон, где количество рабочих дней на смене '
         'в детском лагере в строгом интервале от 18 до 21 дня.\n\nСтроевка — основная форма каждого '
         'бойца. Выглядит как легкая куртка с бесчисленным количеством значков, каждый из которых '
         'имеет свое значение.')

@router.callback_query(F.data == 'dicti')
async def dict(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer(f'{dicti}')
    await callback_query.answer("словарь")