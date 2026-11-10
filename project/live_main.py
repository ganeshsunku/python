from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from database.database import engine, get_db
from models.database_models import Base, Product
from models.product import Products
from sqlalchemy import select

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post(
    "/create_product",
    response_model=Products,
    status_code=201,
)
def create_product(
    product: Products,
    db: Session = Depends(get_db),
):
    db_product = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        quantity=product.quantity,
    )

    try:
        db.add(db_product)
        db.commit()
    except Exception:
        db.rollback()
        raise

    db.refresh(db_product)

    return db_product

@app.get("/products", response_model=list[Products], response_model_exclude_none=True, status_code=200)
def get_products(db:Session=Depends(get_db)):
    products = db.scalars(
        select(Product).order_by(Product.id)
    ).all()

    return products

