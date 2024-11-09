import aiosqlite

async def quest_db(tg_id, user_name, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, irl1, irl2, irl3, irl4, irl5, irl6, irl7, irl8, irl9, oirl1, oirl2, oirl3, oirl4, oirl5, oirl6, ol1, ol2, od1, od2, od3, oq1, oq2, oq3, oq4, oq5, oq6, oq7, oq8, oq9, oq10, lirl1, lirl2, lirl3, lirl4, lirl5, lirl6, ll1, ll2, ld1, ld2, ld3, lq1, lq2, lq3, lq4, lq5, lq6, lq7, lq8, lq9, lq10, kirl1, kirl2, kirl3, kirl4, kirl5, kirl6, kl1, kl2, kd1, kd2, kd3, kq1, kq2, kq3, kq4, kq5, kq6, kq7, kq8, kq9, kq10, svirl1, svirl2, svirl3, svirl4, svirl5, svirl6, svl1, svl2, svd1, svd2, svd3, svq1, svq2, svq3, svq4, svq5, svq6, svq7, svq8, svq9, svq10, eirl1, eirl2, eirl3, eirl4, eirl5, eirl6, el1, el2, ed1, ed2, ed3, eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9, eq10, airl1, airl2, airl3, airl4, airl5, airl6, al1, al2, ad1, ad2, ad3, aq1, aq2, aq3, aq4, aq5, aq6, aq7, aq8, aq9, aq10, dq1, dq2, dq3, dq4, dq5, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10):
    async with aiosqlite.connect('quest_list.db') as db:
        await db.execute('CREATE TABLE IF NOT EXISTS quest_list (tg_id BIGINT, user_name STRING,'
                         'q1 INT, q2 INT, q3 INT, q4 INT, q5 INT, q6 INT, q7 INT,'
                         'q8 INT, q9 INT, q10 INT, q11 INT, q12 INT, q13 INT, q14 INT,'
                         'q15 INT, q16 INT, q17 INT, q18 INT, q19 INT, q20 INT, q21 INT, d1 INT, d2 INT, '
                         'd3 INT, d4 INT, d5 INT, d6 INT, d7 INT, d8 INT, d9 INT, d10 INT, d11 INT, d12 INT, d13 INT, '
                         'd14 INT, d15 INT, d16 INT, d17 INT, d18 INT, d19 INT, d20 INT, l1 INT, l2 INT, l3 INT, '
                         'l4 INT, l5 INT, l6 INT, l7 INT, l8 INT, l9 INT, l10 INT, irl1 INT, irl2 INT, irl3 INT, '
                         'irl4 INT, irl5 INT, irl6 INT, irl7 INT, irl8 INT, irl9 INT, oirl1 INT, oirl2 INT, oirl3 INT, oirl4 INT, oirl5 INT, oirl6 INT, ol1 INT, ol2 INT, od1 INT, od2 INT, od3 INT, oq1 INT, oq2 INT, oq3 INT, oq4 INT, oq5 INT, oq6 INT, oq7 INT, oq8 INT, oq9 INT, oq10 INT, lirl1 INT, lirl2 INT, lirl3 INT, lirl4 INT, lirl5 INT, lirl6 INT, ll1 INT, ll2 INT, ld1 INT, ld2 INT, ld3 INT, lq1 INT, lq2 INT, lq3 INT, lq4 INT, lq5 INT, lq6 INT, lq7 INT, lq8 INT, lq9 INT, lq10 INT, kirl1 INT, kirl2 INT, kirl3 INT, kirl4 INT, kirl5 INT, kirl6 INT, kl1 INT, kl2 INT, kd1 INT, kd2 INT, kd3 INT, kq1 INT, kq2 INT, kq3 INT, kq4 INT, kq5 INT, kq6 INT, kq7 INT, kq8 INT, kq9 INT, kq10 INT, svirl1 INT, svirl2 INT, svirl3 INT, svirl4 INT, svirl5 INT, svirl6 INT, svl1 INT, svl2 INT, svd1 INT, svd2 INT, svd3 INT, svq1 INT, svq2 INT, svq3 INT, svq4 INT, svq5 INT, svq6 INT, svq7 INT, svq8 INT, svq9 INT, svq10 INT, eirl1 INT, eirl2 INT, eirl3 INT, eirl4 INT, eirl5 INT, eirl6 INT, el1 INT, el2 INT, ed1 INT, ed2 INT, ed3 INT, eq1 INT, eq2 INT, eq3 INT, eq4 INT, eq5 INT, eq6 INT, eq7 INT, eq8 INT, eq9 INT, eq10 INT, airl1 INT, airl2 INT, airl3 INT, airl4 INT, airl5 INT, airl6 INT, al1 INT, al2 INT, ad1 INT, ad2 INT, ad3 INT, aq1 INT, aq2 INT, aq3 INT, aq4 INT, aq5 INT, aq6 INT, aq7 INT, aq8 INT, aq9 INT, aq10 INT, dq1 INT, dq2 INT, dq3 INT, dq4 INT, dq5 INT, s1 INT, s2 INT, s3 INT, s4 INT, s5 INT, s6 INT, s7 INT, s8 INT, s9 INT, s10 INT)')
        cursor = await db.execute('SELECT * FROM quest_list WHERE tg_id =?', (tg_id,))
        data = await cursor.fetchone()
        if data is not None:
            return
        async with aiosqlite.connect('quest_list.db') as db:
            await db.execute('INSERT INTO quest_list(tg_id, user_name, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, irl1, irl2, irl3, irl4, irl5, irl6, irl7, irl8, irl9, oirl1, oirl2, oirl3, oirl4, oirl5, oirl6, ol1, ol2, od1, od2, od3, oq1, oq2, oq3, oq4, oq5, oq6, oq7, oq8, oq9, oq10, lirl1, lirl2, lirl3, lirl4, lirl5, lirl6, ll1, ll2, ld1, ld2, ld3, lq1, lq2, lq3, lq4, lq5, lq6, lq7, lq8, lq9, lq10, kirl1, kirl2, kirl3, kirl4, kirl5, kirl6, kl1, kl2, kd1, kd2, kd3, kq1, kq2, kq3, kq4, kq5, kq6, kq7, kq8, kq9, kq10, svirl1, svirl2, svirl3, svirl4, svirl5, svirl6, svl1, svl2, svd1, svd2, svd3, svq1, svq2, svq3, svq4, svq5, svq6, svq7, svq8, svq9, svq10, eirl1, eirl2, eirl3, eirl4, eirl5, eirl6, el1, el2, ed1, ed2, ed3, eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9, eq10, airl1, airl2, airl3, airl4, airl5, airl6, al1, al2, ad1, ad2, ad3, aq1, aq2, aq3, aq4, aq5, aq6, aq7, aq8, aq9, aq10, dq1, dq2, dq3, dq4, dq5, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?, ?, ?, ?,?,?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                             (tg_id, user_name, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, irl1, irl2, irl3, irl4, irl5, irl6, irl7, irl8, irl9, oirl1, oirl2, oirl3, oirl4, oirl5, oirl6, ol1, ol2, od1, od2, od3, oq1, oq2, oq3, oq4, oq5, oq6, oq7, oq8, oq9, oq10, lirl1, lirl2, lirl3, lirl4, lirl5, lirl6, ll1, ll2, ld1, ld2, ld3, lq1, lq2, lq3, lq4, lq5, lq6, lq7, lq8, lq9, lq10, kirl1, kirl2, kirl3, kirl4, kirl5, kirl6, kl1, kl2, kd1, kd2, kd3, kq1, kq2, kq3, kq4, kq5, kq6, kq7, kq8, kq9, kq10, svirl1, svirl2, svirl3, svirl4, svirl5, svirl6, svl1, svl2, svd1, svd2, svd3, svq1, svq2, svq3, svq4, svq5, svq6, svq7, svq8, svq9, svq10, eirl1, eirl2, eirl3, eirl4, eirl5, eirl6, el1, el2, ed1, ed2, ed3, eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9, eq10, airl1, airl2, airl3, airl4, airl5, airl6, al1, al2, ad1, ad2, ad3, aq1, aq2, aq3, aq4, aq5, aq6, aq7, aq8, aq9, aq10, dq1, dq2, dq3, dq4, dq5, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10))
            await db.commit()

async def wallet_value(tg_id):
    db = await aiosqlite.connect('tg_users_wallet.db')
    cursor = await db.execute(f'SELECT wallet FROM users_wallet WHERE tg_id == {tg_id}')
    data = await cursor.fetchone()
    await db.close()
    return data

async def wallet_db(tg_id, wallet, user_name):
    async with aiosqlite.connect('tg_users_wallet.db') as db:
        await db.execute('CREATE TABLE IF NOT EXISTS users_wallet (tg_id BIGINT, wallet INT, user_name STRING)')
        cursor = await db.execute('SELECT * FROM users_wallet WHERE tg_id =?', (tg_id,))
        data = await cursor.fetchone()
        if data is not None:
            return
        async with aiosqlite.connect('tg_users_wallet.db') as db:
            await db.execute('INSERT INTO users_wallet (tg_id, wallet, user_name) VALUES (?,?,?)', (tg_id, wallet, user_name))
            await db.commit()
            await db.close()


async def verify_db(tg_id, verify, user_name):
    async with aiosqlite.connect('verify.db') as db:
        await db.execute('CREATE TABLE IF NOT EXISTS users_verify (tg_id BIGINT, verify INT, user_name STRING)')
        cursor = await db.execute('SELECT * FROM users_verify WHERE tg_id =?', (tg_id,))
        data = await cursor.fetchone()
        if data is not None:
            return
        async with aiosqlite.connect('verify.db') as db:
            await db.execute('INSERT INTO users_verify (tg_id, verify, user_name) VALUES (?,?,?)', (tg_id, verify, user_name))
            await db.commit()
            await db.close()


async def verifying(tg_id):
    db = await aiosqlite.connect('verify.db')
    await db.execute(f'UPDATE users_verify SET verify = 1 WHERE tg_id == {tg_id}')
    await db.commit()
    await db.close()


async def verify_exist(tg_id):
    db = await aiosqlite.connect('verify.db')
    cursor = await db.execute(f'SELECT verify FROM users_verify WHERE tg_id == {tg_id}')
    data = await cursor.fetchone()
    await db.close()
    return data


async def referal_db(tg_id, referal, qr, friend, social, other):
    async with aiosqlite.connect('referal.db') as db:
        await db.execute('CREATE TABLE IF NOT EXISTS referal_table (tg_id BIGINT, referal INT, qr INT, friend INT, social INT, other INT)')
        cursor = await db.execute('SELECT * FROM referal_table WHERE tg_id =?', (tg_id,))
        data = await cursor.fetchone()
        if data is not None:
            return
        async with aiosqlite.connect('referal.db') as db:
            await db.execute('INSERT INTO referal_table (tg_id, referal, qr, friend, social, other) VALUES (?,?,?,?,?,?)', (tg_id, referal, qr, friend, social, other))
            await db.commit()
            await db.close()


async def where_from_user(tg_id, type):
    db = await aiosqlite.connect('referal.db')
    await db.execute(f'UPDATE referal_table SET {type} = 1 WHERE tg_id == {tg_id}')
    await db.commit()
    await db.close()


async def referal_exist(tg_id):
    db = await aiosqlite.connect('referal.db')
    cursor = await db.execute(f'SELECT referal FROM referal_table WHERE tg_id == {tg_id}')
    data = await cursor.fetchone()
    await db.close()
    return data


async def referal_delete(tg_id):
    db = await aiosqlite.connect('referal.db')
    await db.execute(f'UPDATE referal_table SET referal = 0 WHERE tg_id == {tg_id}')
    await db.commit()
    await db.close()


async def quiz_exist(tg_id, quiz):
    db = await aiosqlite.connect('quest_list.db')
    cursor = await db.execute(f'SELECT {quiz} FROM quest_list WHERE tg_id == {tg_id}')
    data = await cursor.fetchone()
    await db.close()
    return data

async def quiz_exist_admin(user_name, quiz):
    db = await aiosqlite.connect('quest_list.db')
    cursor = await db.execute(f'SELECT {quiz} FROM quest_list WHERE user_name == {user_name}')
    data = await cursor.fetchone()
    await db.close()
    return data


async def delete_quiz(tg_id, quiz):
    db = await aiosqlite.connect('quest_list.db')
    await db.execute(f'UPDATE quest_list SET {quiz} = 0 WHERE tg_id == {tg_id}')
    await db.commit()
    await db.close()


async def quiz_reward(tg_id):
    db = await aiosqlite.connect('tg_users_wallet.db')
    await db.execute(f'UPDATE users_wallet SET wallet = wallet + 5 WHERE tg_id = {tg_id}')
    await db.commit()
    await db.close()





async def shop_db(num, friend, social, qr, other, sh1, sh2, sh3, sh4, sh5, sh6, sh7, sh8, sh9, sh10, sh11, sh12, sh13, sh14, sh15, sh16, sh17, sh18, sh19, sh20, sh21, sh22, sh23, sh24, sh25):
    async with aiosqlite.connect('shop.db') as db:
        await db.execute('CREATE TABLE IF NOT EXISTS shop_db (num BIGINT,'
                         ' friend INT, social INT, qr INT, other INT, sh1 INT, sh2 INT, sh3 INT, sh4 INT, sh5 INT, sh6 INT, sh7 INT, sh8 INT, sh9 INT, sh10 INT, sh11 INT, sh12 INT, sh13 INT, sh14 INT, sh15 INT, sh16 INT, sh17 INT, sh18 INT, sh19 INT, sh20 INT, sh21 INT, sh22 INT, sh23 INT, sh24 INT, sh25 INT)')
        cursor = await db.execute('SELECT * FROM shop_db WHERE num =?', (num,))
        data = await cursor.fetchone()
        if data is not None:
            return
        async with aiosqlite.connect('shop.db') as db:
            await db.execute('INSERT INTO shop_db(num'
                             ', friend, social, qr, other, sh1, sh2, sh3, sh4, sh5, sh6, sh7, sh8, sh9, sh10, sh11, sh12, sh13, sh14, sh15, sh16, sh17, sh18, sh19, sh20, sh21, sh22, sh23, sh24, sh25) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                             (num, friend, social, qr, other, sh1, sh2, sh3, sh4, sh5, sh6, sh7, sh8, sh9, sh10, sh11, sh12, sh13, sh14, sh15, sh16, sh17, sh18, sh19, sh20, sh21, sh22, sh23, sh24, sh25))
            await db.commit()


async def add_friend():
    db = await aiosqlite.connect('shop.db')
    await db.execute(f'UPDATE shop_db SET friend = friend + 1 WHERE num = "1"')
    await db.commit()
    await db.close()

async def add_social():
    db = await aiosqlite.connect('shop.db')
    await db.execute(f'UPDATE shop_db SET social = social + 1 WHERE num = "1"')
    await db.commit()
    await db.close()

async def add_qr():
    db = await aiosqlite.connect('shop.db')
    await db.execute(f'UPDATE shop_db SET qr = qr + 1 WHERE num = "1"')
    await db.commit()
    await db.close()

async def add_other():
    db = await aiosqlite.connect('shop.db')
    await db.execute(f'UPDATE shop_db SET other = other + 1 WHERE num = "1"')
    await db.commit()
    await db.close()


async def how_many_friends():
    db = await aiosqlite.connect('shop.db')
    cursor = await db.execute(f'SELECT friend FROM shop_db WHERE num == "1"')
    data = await cursor.fetchone()
    await db.close()
    return data

async def how_many_qr():
    db = await aiosqlite.connect('shop.db')
    cursor = await db.execute(f'SELECT qr FROM shop_db WHERE num == "1"')
    data = await cursor.fetchone()
    await db.close()
    return data

async def how_many_social():
    db = await aiosqlite.connect('shop.db')
    cursor = await db.execute(f'SELECT social FROM shop_db WHERE num == "1"')
    data = await cursor.fetchone()
    await db.close()
    return data

async def how_many_other():
    db = await aiosqlite.connect('shop.db')
    cursor = await db.execute(f'SELECT other FROM shop_db WHERE num == "1"')
    data = await cursor.fetchone()
    await db.close()
    return data


async def get_money(tg_id, cost):
    db = await aiosqlite.connect('tg_users_wallet.db')
    await db.execute(f'UPDATE users_wallet SET wallet = wallet - {cost} WHERE tg_id == {tg_id}')
    await db.commit()
    await db.close()

async def friend_reward(user_name):
    db = await aiosqlite.connect('tg_users_wallet.db')
    await db.execute(f'UPDATE users_wallet SET wallet = wallet + 10 WHERE user_name == "{user_name}"')
    await db.commit()
    await db.close()


async def shop_balance(item):
    db = await aiosqlite.connect('shop.db')
    cursor = await db.execute(f'SELECT {item} FROM shop_db WHERE num == "1"')
    data = await cursor.fetchone()
    await db.close()
    return data

async def purchase(item):
    db = await aiosqlite.connect('shop.db')
    await db.execute(f'UPDATE shop_db SET {item} = {item} - 1 WHERE num = "1"')
    await db.commit()
    await db.close()