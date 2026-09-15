import esd
from fastapi import FastAPI

app = FastAPI(title="Kord SofaScore API")

client = esd.SofascoreClient()


@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Kord SofaScore API is running"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/api/live")
def live_matches():
    events = client.get_events(live=True)

    matches = []

    for event in events:
        matches.append({
            "id": event.id,
            "home": event.home_team.name,
            "away": event.away_team.name,
            "home_score": event.home_score.current,
            "away_score": event.away_score.current,
            "status": event.status.description,
            "tournament": event.tournament.name,
            "minute": event.total_elapsed_minutes
        })

    return {
        "count": len(matches),
        "matches": matches
    }
