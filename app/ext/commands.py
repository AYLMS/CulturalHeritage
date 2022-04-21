import click
import json
import os

from app.ext.auth import create_user
from app.ext.database import db
from app.models import Object


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    for i in range(1, 16):
        with open(os.path.join('data', f'{i}.json'), encoding='utf-8') as cat_file:
            f = cat_file.read()
            data = json.loads(f)
            temp = []
            b = {
                'нет': False,
                'да': True
            }
            for item in data:
                name = item['nativeName']
                id = item['nativeId']
                region = item['data']['general']['region']['value']
                unesco = item['data']['general']['unesco']['value'] if "value" in item['data']['general'][
                    'unesco'] else "нет"
                try:
                    if 'photo' in item['data']['general'] and item['data']['general']['photo'] and "url" in \
                            item['data']['general']['photo']:
                        photo = item['data']['general']['photo']['url']
                    else:
                        photo = ""
                except:
                    print(item)
                    break

                temp.append(Object(name=name, id=id, region=region, unesco=b[unesco], photo=photo))

    db.session.bulk_save_objects(temp)
    db.session.commit()
    return Object.query.all()
    pass



def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))

    # add a single command
    @app.cli.command()
    @click.option("--username", "-u")
    @click.option("--password", "-p")
    def add_user(username, password):
        """Adds a new user to the database"""
        return create_user(username, password)
