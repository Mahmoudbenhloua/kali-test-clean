from prometheus_client import Counter, generate_latest
from fastapi.responses import Response

requests_total = Counter("http_requests_total", "Total HTTP requests")

def register_metrics(app):
    @app.middleware("http")
    async def count_requests(request, call_next):
        response = await call_next(request)
        requests_total.inc()
        return response

    @app.get("/metrics")
    def metrics():
        return Response(generate_latest(), media_type="text/plain")
