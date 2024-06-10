import requests
import utils
from bs4 import BeautifulSoup
from loguru import logger


class MercadoLivreScraper:
    def __init__(self):
        self.url = "https://www.mercadolivre.com.br/"
        self.search_url = "https://lista.mercadolivre.com.br/"

    def format_name_to_url(self, name: str) -> str:
        return name.replace(" ", "-").lower().strip()

    def get_search_url(self, name: str) -> str:
        formatted_name = self.format_name_to_url(name)
        return f"{self.search_url}{formatted_name}"

    def parse_result_item(self, result_item) -> dict:
        # result = {}
        title = result_item.find("h2", class_="ui-search-item__title").text
        product_link = result_item.find("a", class_="ui-search-link").get("href")
        image = result_item.find("img", class_="ui-search-result-image__element").get(
            "data-src"
        )
        try:
            reviews_rating_number = result_item.find(
                "span", class_="ui-search-reviews__rating-number"
            ).text
        except AttributeError:
            reviews_rating_number = None
            logger.warning("Reviews rating number not found")
        try:
            reviews_amount = utils.str_to_int(
                result_item.find("span", class_="ui-search-reviews__amount").text
            )
        except AttributeError:
            reviews_amount = None
            logger.warning("Reviews amount not found")
        try:
            product_id = (
                result_item.find("form", class_="ui-search-bookmark")
                .get("action")
                .split("/bookmarks/")[1]
                .strip()
            )
        except Exception:
            logger.warning("Error getting product id.")
            product_id = None
        price = result_item.find("span", class_="andes-money-amount__fraction").text
        result = {
            "title": title,
            "product_link": product_link,
            "image": image,
            "reviews_rating": reviews_rating_number,
            "reviews_amount": reviews_amount,
            "price": price,
            "seller": "Mercado Livre",
            "product_id": product_id,
        }
        print(result)
        return result

    def parse_search_results(
        self, response: requests.Response, limit: int = 30
    ) -> list:
        self.soup = BeautifulSoup(response.content, "html.parser")
        results = []
        result_items = self.soup.find_all("li", class_="ui-search-layout__item")

        results_count = 0
        for result_item in result_items:
            result = self.parse_result_item(result_item)
            if not result:
                continue
            results.append(result)
            results_count += 1
            if results_count > limit:
                break

        return results

    def search_product(self, name: str, limit: int = 30) -> list:
        response = requests.get(self.get_search_url(name))
        parsed_results = self.parse_search_results(response)
        while len(parsed_results) < limit:
            next_page = self.soup.find("li", class_="andes-pagination__button--next")
            next_page_link = next_page.find("a").get("href")
            response = requests.get(next_page_link)
            parsed_results += self.parse_search_results(response)
        parsed_results = [element for element in parsed_results if element]
        return parsed_results
