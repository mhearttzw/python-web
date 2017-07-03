import asyncio, logging
import aiomysql


def log(sql, arg=()):
    logging.info('SQL: %s' % sql)

# 创建连接池，每个http请求都从连接池连接到数据库
async def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global  __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minisize', 1),
        loop=loop
    )

# 销毁连接池
async def destroy_pool():
    global __pool
    if __pool is not None:
        __pool.close()
        await  __pool.wait_closed()

# select语句
async def select(sql, args, size=None):
    log(sql, args)
    global __pool
    async with __pool.get() as conn:
        # """A cursor which returns results as a dictionary"""
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sql.replace('?', '%s'), args or ())
            if size:
                # 接收size条返回结果行.如果size的值大于返回的结果行的数量,则会返回cursor.arraysize条数据.
                rs = await cur.fetchmany(size)
            else:
                # 接收全部的返回结果行.
                rs = await cur.fetchall()
        logging.info('rows returned: %s' % len(rs))
        return rs

# insert, update, delete语句
async def execute(sql, args, autocommit=True):
    log(sql)
    async with __pool.get() as conn:
        if not autocommit:
            await conn.begin()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute(sql.replace('?', '%s'), args)
                # 受影响的行数
                affected = cur.rowcount
            if not autocommit:
                await conn.commit()
        except BaseException as e:
            if not autocommit:
                await conn.rollback()
            raise
        return affected

