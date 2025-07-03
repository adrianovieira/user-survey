from environ import config, group, to_config, var


@config
class Config:

    @config
    class APIConfig:
        CORS_ORIGINS: list[str] = var(
            default=[
                "http://localhost",
                "http://localhost:3000",
            ],
            converter=list,
        )

    @config
    class DBConfig:
        USER_NAME: str = var(default="iluminatti")
        USER_PASS: str = var(default="notsecure")
        NAME: str = var(default="iluminatti")
        SCHEMA: str = var(default="inside")
        HOST: str = var(default="localhost")
        PORT: int = var(default=5432, converter=int)
        DRIVER: str = var(default="psycopg")
        TYPE: str = var(default="postgresql")

        @property
        def url(self):
            return f"{self.TYPE}+{self.DRIVER}://{self.USER_NAME}:{self.USER_PASS}@{self.HOST}:{self.PORT}/{self.NAME}"

    DB: DBConfig = group(DBConfig)
    API: APIConfig = group(APIConfig)


CONFIG: Config = to_config(Config)
