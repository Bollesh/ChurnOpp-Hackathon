from apscheduler.schedulers.background import BackgroundScheduler


hour = 16
minute = 8

def scheduled_job():
    print(f'This job will run at {hour}, {minute}')

scheduler = BackgroundScheduler()
scheduler.add_job(scheduled_job, 'cron', hour=hour, minute=minute)