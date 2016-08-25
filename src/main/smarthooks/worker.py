import celery
import os

app = celery.Celery('smarthooks',
                    broker=os.environ['REDIS_URL'],
                    include=['smarthooks.geeksforgeeksbot.worker'])

# note: if results are to be stored
# app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
#                 CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])
