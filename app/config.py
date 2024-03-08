import pydantic
import pydantic_settings


class HTTP(pydantic.BaseModel):
    debug: bool


class Settings(pydantic_settings.BaseSettings):
    http: HTTP = HTTP(debug=True)
    model_config = pydantic_settings.SettingsConfigDict(toml_file="config.toml")

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
