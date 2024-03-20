"""
Application configuration from file and environment variables.
"""

import pydantic
import pydantic_settings
import rich


class HTTP(pydantic.BaseModel):
    """
    HTTP module configuration besides configuration that are passed
    directly to uvicorn.
    """

    debug: bool


class DB(pydantic.BaseModel):
    """
    Database module configuration
    """

    database: str
    echo: bool


class Settings(pydantic_settings.BaseSettings):
    """
    Configuration holder which reads configuration from config.toml
    and environment variables.
    """

    http: HTTP = HTTP(debug=True)
    database: DB = DB(database="database.db", echo=True)
    model_config = pydantic_settings.SettingsConfigDict(
        toml_file="config.toml",
        env_prefix="fastapi101_",
        case_sensitive=False,
        env_nested_delimiter="__",
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[pydantic_settings.BaseSettings],
        init_settings: pydantic_settings.PydanticBaseSettingsSource,
        env_settings: pydantic_settings.PydanticBaseSettingsSource,
        dotenv_settings: pydantic_settings.PydanticBaseSettingsSource,
        file_secret_settings: pydantic_settings.PydanticBaseSettingsSource,
    ) -> tuple[pydantic_settings.PydanticBaseSettingsSource, ...]:
        del init_settings
        del env_settings
        del dotenv_settings
        del file_secret_settings

        return (pydantic_settings.TomlConfigSettingsSource(settings_cls),)


settings = Settings()
rich.print(f"configuration: {settings.model_dump()}")
