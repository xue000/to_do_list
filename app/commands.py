import click
from faker import Faker
from app import db,app
from app.models import Task, Admin

fake=Faker()

def fake_admin():
    admin = Admin(
        username = "xuedifan",
    )
    admin.set_password('123456')
    db.session.add(admin)
    db.session.commit()

def fake_task(count=10):
    for i in range(count):
        task = Task(title=fake.sentence(),
                    description=fake.sentence(),
                    date=fake.date_this_decade(),
                    status="Uncompleted")
        db.session.add(task)
    db.session.commit()

@app.cli.command()
def forge():
    db.drop_all()
    db.create_all()

    click.echo('Generating administrator...')
    fake_admin()

    click.echo('Generating tasks...')
    fake_task()

    click.echo('Done.')


