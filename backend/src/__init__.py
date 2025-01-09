from fastapi import FastAPI
from src.inventory.routes import inventory_router
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.main import engine
from src.inventory.operations import InventoryOperations

app = FastAPI()
inv = InventoryOperations()

app.include_router(inventory_router, prefix="/api/inv")


async def daily_expiry_check():
    async with AsyncSession(engine) as session:
        await inv.check_and_insert_expiry(session)

# Scheduler setup
scheduler = AsyncIOScheduler()

# Add the job to the scheduler
scheduler.add_job(
    daily_expiry_check,
    CronTrigger(hour=0, minute=0)  # Run daily at midnight
)

@app.on_event("startup")
async def startup_event():
    """Start the scheduler when the FastAPI app starts."""
    scheduler.start()
    print(f"Scheduled jobs: {scheduler.get_jobs()}")

@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown the scheduler when the FastAPI app stops."""
    scheduler.shutdown()

@app.get("/test-expiry-check")
async def test_expiry_check():
    """Manually trigger the expiry check function."""
    await daily_expiry_check()
    return {"status": "Expiry check executed"}