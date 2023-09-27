import click


@click.group()
def db():
    pass


@click.command()
def get():
    


def main():
    db()


if __name__ == "__main__":
    main()
