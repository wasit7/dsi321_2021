from celery import Celery
app = Celery(‘tasks’,broker="redis://localhost:6379/0")
@app.task
def check():
 print("I am checking your stuff")
app.conf.beat_schedule = {
 "run-me-every-ten-seconds": {
 "task": "tasks.check",
 "schedule”: 10.0
 }
}