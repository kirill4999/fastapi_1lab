from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root_page():
    return {
        "FIO": "Тайлаков Кирилл Николаевич"
    }


@app.get("/tools")
async def tools_page():
    return {
        "description": "Backend-разработчик с опытом в C#, ASP.NET, и базами данных. "
                       "Создавал эффективные API, оптимизировал запросы SQL. "
                       "Знаком с архитектурой микросервисов. "
                       "Работал с .NET Core и интеграцией систем"
    }


@app.get("/users")
async def users_page():
    return {
        "phone": "Телефон: 8 133 714 88 42"
    }