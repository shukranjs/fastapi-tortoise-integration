from fastapi import APIRouter, HTTPException
from app.models.models import MyModel
from app.schemas.schema import MyModelIn, MyModelOut

router = APIRouter()


@router.post("", response_model=MyModelOut)
async def create_model(model_in: MyModelIn):
    model = await MyModel.create(status=model_in.status)
    return model


@router.get("/{model_id}", response_model=MyModelOut)
async def read_model(model_id: int):
    model = await MyModel.get_or_none(id=model_id)
    if model is None:
        raise HTTPException(status_code=404, detail="Model not found")
    return model
