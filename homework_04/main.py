"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio
from models import Base, User, Post, Session, async_engine
import jsonplaceholder_requests as jsons


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_users(session: Session, users: list[dict]):
    Users_list = []
    for item in users:
        user = User(id=item['id'],
                    name=item['name'],
                    username=item['username'],
                    email=item['email'])
        Users_list.append(user)

    session.add_all(Users_list)
    await session.commit()


async def create_posts(session: Session, posts: list[dict]):
    Posts_list = []
    for item in posts:
        post = Post(id=item['id'],
                    user_id=item['userId'],
                    title=item['title'],
                    body=item['body'])
        Posts_list.append(post)

    session.add_all(Posts_list)
    await session.commit()


async def async_main():
    await create_tables()

    users_data: list[dict]
    posts_data: list[dict]
    users_data, posts_data = await asyncio.gather(
        jsons.fetch_json(jsons.USERS_DATA_URL),
        jsons.fetch_json(jsons.POSTS_DATA_URL)
    )

    async with Session() as session:
        await create_users(session, users_data)
        await create_posts(session, posts_data)
        await session.close()


def main():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
