"""Console script for gotify_cli."""

from dataclasses import dataclass

import click


@dataclass
class Config:
    base_url: str
    app_tokens: dict
    default_app: str | None = None

    @classmethod
    def from_toml(cls) -> "Config":
        from platformdirs import site_config_dir, user_config_dir
        from pathlib import Path
        import tomllib

        locations = [
            Path.cwd(),
            Path.home(),
            Path(user_config_dir(roaming=True)),
            Path(user_config_dir("gotify_cli", roaming=False)),
            Path(site_config_dir()),
        ]
        for location in locations:
            config_file = location / "gotify_cli.toml"
            if config_file.exists():
                with config_file.open("rb") as f:
                    config_data = tomllib.load(f)
                    app_tokens = {
                        k: v["app_token"]
                        for k, v in config_data.items()
                        if isinstance(v, dict) and "app_token" in v
                    }

                    return cls(
                        base_url=config_data["base_url"],
                        default_app=config_data.get("default_app"),
                        app_tokens=app_tokens,
                    )
        raise FileNotFoundError(
            "Configuration file not found in any of the expected locations."
        )


def send_gotify_message(
    title: str, message: str, priority: int, app_name: str | None = None
):
    from gotify import Gotify

    config = Config.from_toml()
    if not app_name:
        app_name = config.default_app
    if app_name not in config.app_tokens:
        raise ValueError(f"App name '{app_name}' not found in configuration.")
    app_token = config.app_tokens[app_name]

    gotify = Gotify(base_url=config.base_url, app_token=app_token)
    gotify.create_message(
        title=title,
        message=message,
        priority=priority,
    )

    click.echo(
        f"Message sent: {title} - {message} (priority: {priority}) for app: {app_name}"
    )


@click.command()
@click.option("--app-name", help="Name of the application", default=None)
@click.option("--title", "-t", prompt="Title", help="Title of the notification")
@click.option("--message", "-m", prompt="Message", help="Body of the notification")
@click.option("--priority", default=1, help="Priority of the notification")
def main(app_name, title, message, priority):
    """Console script for gotify_cli."""
    try:
        send_gotify_message(title, message, priority, app_name)
    except Exception as e:
        click.echo(f"Error: {str(e)}")


if __name__ == "__main__":
    import sys

    sys.exit(main())  # pragma: no cover
