from celery import Celery

app = Celery('tasks', broker='sqs://access_key:secret_key@sqs-docker:9324', backend='redis://redis:6379')


@app.task()
def echo(number):
    return number
