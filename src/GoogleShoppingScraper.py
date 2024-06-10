import re
from typing import Dict

import requests
from bs4 import BeautifulSoup
from loguru import logger


class GoogleShoppingScraper:
    def __init__(self):
        print("ENTROU AQUI")
        self.url = "https://shopping.google.com.br/"
        self.search_url = (
            "https://www.google.com/search?q={}&tbm=shop&sclient=products-cc"
        )
        self.user_agent = (
            "Mozilla/5.0 (X11; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0"
        )
        self.headers = {"User-Agent": self.user_agent}

    def get_search_url(self, product_name: str, only_sales: bool = False) -> str:
        formatted_product_name = product_name.replace(" ", "+").lower().strip()
        if only_sales:
            return self.search_url.format(formatted_product_name) + "&tbs=sales:1"
        return self.search_url.format(formatted_product_name)

    def format_price(self, price: str) -> str:
        return price.replace("R$\xa0", "")

    def format_product_link(self, url: str) -> str:
        if url.startswith("/shopping"):
            return f"https://www.google.com{url}"
        elif url.startswith("/url?url="):
            return url.replace("/url?url=", "")
        return url.strip()

    def format_reviews(self, reviews: str) -> Dict[str, str]:
        rating = reviews.split(" ")[0].strip()
        rating = str(round(float(rating), 1))
        amount = reviews.split("estrelas. ")[1].split(" resenhas")[0].strip()
        return {"rating": rating, "amount": amount}

    def get_reviews(self, item) -> dict:
        pattern = re.compile("(\d+(\.\d+)?) de 5 estrelas")
        reviews_element = item.find("div", attrs={"aria-label": pattern})
        if not reviews_element:
            return {}
        reviews = reviews_element.get("aria-label")
        return self.format_reviews(reviews)

    def parse_result_item(self, item):
        item_content = item.find("div", class_="sh-dgr__content")
        product_link = self.format_product_link(
            item_content.find("span").find("a").get("href")
        )
        title = item_content.find("span").find("a").find("h3").text.strip()
        logger.info(f"Title: {title}")
        # image = (
        #     item_content.find("span")
        #     .find("a")
        #     .find("div")
        #     .find("div")
        #     .find("img")
        #     .get("src")
        # )
        image = None
        reviews = {}
        try:
            reviews = self.get_reviews(item_content)
        except Exception:
            logger.warning("No reviews found.")

        price = self.format_price(
            item_content.find("div", class_="sh-dgr__offer-content")
            .find("a")
            .find("span", attrs={"aria-hidden": True})
            .text
        )
        seller = (
            item_content.find("div", class_="sh-dgr__offer-content")
            .find("a")
            .find("div")
            .find_all("div")[-1]
            .text.strip()
        )
        try:
            product_id = str(item.get("data-docid"))
        except Exception:
            product_id = None
        result = {
            "title": title,
            "product_link": product_link,
            "image": image,
            "price": price,
            "seller": seller,
            "reviews_rating": reviews.get("rating", None),
            "reviews_amount": reviews.get("amount", None),
            "product_id": product_id,
        }
        print(result)
        return result

    def parse_search_results(
        self, response: requests.Response, limit: int = 30
    ) -> list[dict]:
        results = []
        self.soup = BeautifulSoup(response.content, "html.parser")
        items = self.soup.find_all("div", class_="sh-dgr__grid-result")

        results_count = 0
        for item in items:
            result = self.parse_result_item(item)
            if not result:
                continue
            results_count += 1
            results.append(result)
            if results_count >= limit:
                break
        return results

    def search_product(
        self, product_name: str, limit: int = 30, only_sales: bool = False
    ):
        search_url = self.get_search_url(product_name, only_sales)
        response = requests.get(search_url, headers=self.headers)
        parsed_results = self.parse_search_results(response, limit)
        parsed_results = [element for element in parsed_results if element]
        return parsed_results
