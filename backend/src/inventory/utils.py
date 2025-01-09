from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import asyncio

# Function to schedule
async def daily_expiry_check():
    async with AsyncSession(engine) as session:
        await check_and_insert_expiry(session)

# Scheduler setup
def start_scheduler():
    scheduler = AsyncIOScheduler()
    # Run daily at midnight
    scheduler.add_job(
        daily_expiry_check,
        CronTrigger(hour=0, minute=0)  # Adjust the timing as needed
    )
    scheduler.start()

# Start the scheduler when the application starts
if __name__ == "__main__":
    start_scheduler()
    asyncio.run(app())
