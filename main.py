from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, FileResponse
import random
import os

app = FastAPI(title="Бойцовский клуб API", description="Весёлое API по фильму 'Бойцовский клуб'")

# Цитаты из фильма
quotes = [
    "Первый закон Бойцовского клуба: никому не рассказывать о Бойцовском клубе.",
    "Второй закон Бойцовского клуба: НИКОМУ не рассказывать о Бойцовском клубе.",
    "Ты — не твои деньги.",
    "Мы — поколение, воспитанное женщинами. Нам как-то не хватает мужского начала.",
    "Только потеряв всё, мы обретаем свободу.",
    "Ты — не твоя работа. Ты — не твои деньги. Ты — не твой автомобиль.",
    "Сначала ты покупаешь мебель, потом ты покупаешь дом, а потом ты смотришь на свою жизнь и понимаешь, что она превратилась в рекламу Ikea.",
    "Это твоя жизнь, и она заканчивается с каждой минутой.",
]

# Интересные факты о фильме
facts = [
    "Брэд Питт и Эдвард Нортон действительно дрались в некоторых сценах, чтобы сделать их более реалистичными.",
    "Фильм был снят по одноимённому роману Чака Паланика.",
    "Режиссёр Дэвид Финчер сделал более 1500 дублей для сцены, где Тайлер Дёрден говорит: 'Мы — поколение, воспитанное женщинами.'",
    "Фильм провалился в прокате, но позже стал культовым благодаря DVD-релизам.",
    "Брэд Питт отказался от гонорара, чтобы сыграть роль Тайлера Дёрдена.",
]

# Фотографии (путь к файлам)
photos = [
    "fight_club_1.jpg",
    "fight_club_2.jpg",
    "fight_club_3.jpg",
]


# Генератор случайных правил Бойцовского клуба
def generate_random_rule():
    rule_number = random.randint(1, 10)
    return f"Правило Бойцовского клуба №{rule_number}: {random.choice(['Не рассказывать о Бойцовском клубе.', 'Драться до конца.', 'Никаких рубашек, никаких обуви.'])}"


# Маршруты API
@app.get("/quote", summary="Получить случайную цитату из фильма")
def get_random_quote():
    return JSONResponse(content={"quote": random.choice(quotes)})


@app.get("/fact", summary="Получить интересный факт о фильме")
def get_random_fact():
    return JSONResponse(content={"fact": random.choice(facts)})


@app.get("/photo", summary="Получить случайную фотографию из фильма")
def get_random_photo():
    photo = random.choice(photos)
    if not os.path.exists(photo):
        raise HTTPException(status_code=404, detail="Фотография не найдена")
    return FileResponse(photo)


@app.get("/rule", summary="Получить случайное правило Бойцовского клуба")
def get_random_rule():
    return JSONResponse(content={"rule": generate_random_rule()})


@app.get("/everything", summary="Получить всё: цитату, факт, фото и правило")
def get_everything():
    return JSONResponse(content={
        "quote": random.choice(quotes),
        "fact": random.choice(facts),
        "photo": random.choice(photos),
        "rule": generate_random_rule(),
    })


# Запуск сервера
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


