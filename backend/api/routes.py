from backend.services.status_service import  get_status_data, get_item_data
from backend.schemas.status_schema import StatusOutSchema
from backend.schemas.item_schema import ItemSchema

def register_routes(app):
    @app.get("/api/status")
    @app.output(StatusOutSchema)
    def api_status():
        return get_status_data()

    @app.get("/api/items")
    @app.output(ItemSchema)
    def api_items():
        return {"items": get_item_data()}