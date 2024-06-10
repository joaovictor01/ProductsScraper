from fastapi import FastAPI

import controller
from GoogleShoppingScraper import GoogleShoppingScraper
from MercadoLivreScraper import MercadoLivreScraper

app = FastAPI()

ML_SCRAPER = MercadoLivreScraper()
GS_SCRAPER = GoogleShoppingScraper()


@app.get("/")
def read_root():
    return {"Products API": "Procure os preços dos seus produtos favoritos"}


@app.get("/search/{product_name}")
def search_product(product_name: str):
    ml_products = ML_SCRAPER.search_product(product_name)
    controller.insert_list_of_dicts_into_db(ml_products)
    gs_products = GS_SCRAPER.search_product(product_name)
    controller.insert_list_of_dicts_into_db(gs_products)
    all_results = {"MercadoLivre": ml_products, "Google Shopping": gs_products}
    return all_results


@app.get("/product/{product_id}")
def get_product_by_id(product_id: str):
    product = controller.get_product(product_id)
    return product


@app.delete("/product/{product_id}")
def delete_product_by_id(product_id: str):
    controller.delete_product(product_id)
    return {"message": "Product deleted successfully"}


@app.delete("/products")
def delete_all_products_from_db():
    controller.delete_all_products()
    return {"message": "All products deleted successfully"}


# def main():
#     GSScraper = GoogleShoppingScraper()
#     results = GSScraper.search_product("notebook full hd ryzen", only_sales=True)
#     print(results)


# if __name__ == "__main__":
#     main()
