# swarna-krishi-api

Help farmers manage their crops.

The frontend of this application lives here: https://github.com/Mithun-750/Swarna-Krishi-app

## Credits

The crop and fertilizer predictions in our app is possible due to this open source project (https://github.com/Gladiator07/Harvestify) by [Atharva Ingle](https://www.linkedin.com/in/atharva-ingle-564430187/)

## Run

```shell
docker run --rm -p 27017:27017 mongo
uvicorn api.main:app --reload --port 8080
```

You can view the autogenerated api docs at the `/docs` endpoint.
