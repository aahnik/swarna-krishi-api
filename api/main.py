from api.app import app

from api.routers import auth, crop, register, user


app.include_router(auth.router)
app.include_router(register.router)
app.include_router(user.router)
app.include_router(crop.router)

