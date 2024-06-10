import unittest
from unittest.mock import patch

from bs4 import BeautifulSoup

from src.MercadoLivreScraper import MercadoLivreScraper


class TestMercadoLivreScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = MercadoLivreScraper()

    @patch("requests.get")
    def test_parse_result_item(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.content = """
        <div class="ui-search-result__wrapper"><div class="andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16 andes-card--animated" id=":R2l5e6:"><div class="ui-search-result__image"><section aria-label="Impressora 3d Fdm Creality K1 Fechada - 1201010168 Bivolt Cor Preto 110V/220V" aria-roledescription="Carrossel" class="andes-carousel-snapped__container andes-carousel-snapped__container--full andes-carousel-snapped__container--with-controls" id=":R2k2l5e6:"><div class="andes-carousel-snapped__header"></div><div class="andes-carousel-snapped__controls-wrapper"><button class="andes-carousel-snapped__control andes-carousel-snapped__control--previous andes-carousel-snapped__control--size-large andes-carousel-snapped__control--disabled swiper-button-disabled" type="button" aria-label="Anterior" disabled=""><span aria-hidden="true" class="andes-carousel-snapped__control__icon-container"><svg aria-hidden="true" width="24" height="24" viewBox="0 0 24 24" fill="rgba(0, 0, 0, 0.9)" style="--darkreader-inline-fill: rgba(232, 230, 227, 0.9);" data-darkreader-inline-fill=""><path d="M14.0656 4.9325L15.1263 5.99316L9.12254 11.9969L15.1325 18.0069L14.0719 19.0676L7.00122 11.9969L14.0656 4.9325Z" fill="rgba(0, 0, 0, 0.9)" style="--darkreader-inline-fill: rgba(232, 230, 227, 0.9);" data-darkreader-inline-fill=""></path></svg></span></button><div class="andes-carousel-snapped ui-search-result__card andes-carousel-snapped--scroll-hidden"><div class="andes-carousel-snapped__wrapper" style="display: flex; will-change: transform; flex-direction: row; transition: transform; transform: translate3d(0px, 0px, 0px);"><div role="group" class="andes-carousel-snapped__slide andes-carousel-snapped__slide--active" aria-label="1 de 6" style="width: 284px; margin-right: 0px;" data-slider="0"><img width="284" height="284" decoding="sync" src="https://http2.mlstatic.com/D_NQ_NP_666433-MLU71216508920_082023-W.webp" class="ui-search-result-image__element" fetchpriority="high" alt="Impressora 3d Fdm Creality K1 Fechada - 1201010168 Bivolt Cor Preto 110V/220V"></div><div role="group" class="andes-carousel-snapped__slide" aria-label="2 de 6" style="width: calc(100% - 0px);"><img decoding="sync" src="https://http2.mlstatic.com/D_749161-MLU71216508930_082023-O.jpg" class="ui-search-result-image__element" fetchpriority="high" alt="Impressora 3d Fdm Creality K1 Fechada - 1201010168 Bivolt Cor Preto 110V/220V"></div><div role="group" class="andes-carousel-snapped__slide" aria-label="3 de 6" style="width: calc(100% - 0px);"><img decoding="sync" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" class="ui-search-result-image__element lazy-loadable" data-src="https://http2.mlstatic.com/D_697734-MLU71216341314_082023-O.jpg" fetchpriority="high" alt="Impressora 3d Fdm Creality K1 Fechada - 1201010168 Bivolt Cor Preto 110V/220V"></div><div role="group" class="andes-carousel-snapped__slide" aria-label="4 de 6" style="width: calc(100% - 0px);"><img decoding="sync" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" class="ui-search-result-image__element lazy-loadable" data-src="https://http2.mlstatic.com/D_612607-MLU71216341320_082023-O.jpg" fetchpriority="high" alt="Impressora 3d Fdm Creality K1 Fechada - 1201010168 Bivolt Cor Preto 110V/220V"></div><div role="group" class="andes-carousel-snapped__slide" aria-label="5 de 6" style="width: calc(100% - 0px);"><img decoding="sync" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" class="ui-search-result-image__element lazy-loadable" data-src="https://http2.mlstatic.com/D_754086-MLU71216508910_082023-O.jpg" fetchpriority="high" alt="Impressora 3d Fdm Creality K1 Fechada - 1201010168 Bivolt Cor Preto 110V/220V"></div><div role="group" class="andes-carousel-snapped__slide" aria-label="6 de 6" style="width: calc(100% - 0px);"><img decoding="sync" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" class="ui-search-result-image__element lazy-loadable" data-src="https://http2.mlstatic.com/D_685558-MLU71216341318_082023-O.jpg" fetchpriority="high" alt="Impressora 3d Fdm Creality K1 Fechada - 1201010168 Bivolt Cor Preto 110V/220V"></div></div></div><button class="andes-carousel-snapped__control andes-carousel-snapped__control--next andes-carousel-snapped__control--size-large" type="button" aria-label="Seguinte"><span aria-hidden="true" class="andes-carousel-snapped__control__icon-container"><svg aria-hidden="true" width="24" height="24" viewBox="0 0 24 24" fill="rgba(0, 0, 0, 0.9)" style="--darkreader-inline-fill: rgba(232, 230, 227, 0.9);" data-darkreader-inline-fill=""><path d="M14.0656 4.9325L15.1263 5.99316L9.12254 11.9969L15.1325 18.0069L14.0719 19.0676L7.00122 11.9969L14.0656 4.9325Z" fill="rgba(0, 0, 0, 0.9)" style="--darkreader-inline-fill: rgba(232, 230, 227, 0.9);" data-darkreader-inline-fill=""></path></svg></span></button></div></section></div><div class="ui-search-result__content"><div class="ui-search-result__content-wrapper"><div class="ui-search-item__group ui-search-item__group--title"><span class="ui-search-item__brand-discoverability ui-search-item__group__element"></span><a href="https://click1.mercadolivre.com.br/mclics/clicks/external/MLB/count?a=GUCOINRkdKaJVYyy%2BnI6ypCWhZGL7dJHCXFHi6L%2BLlpfJk89NeqV04%2FQJqPCHUMO6ipQyXW6YTJUqN9QzpG6i2qDe5vYeyHrhb8m6Xu6ZOCHo%2F37U5SsdRcurdSq6rAyCk65qJL533Jy5%2F4F00HPBJWCZUA4xdW6VnL%2FZs8SOGhgkhqxMGj9AFEMtGlQFBV0SaeEDY5siU39Cs87UZ4qYoUg%2FGen2ytOKe8nxnBPOd%2FIALjhDN9OUo%2BGh1nxQOOJUkpIU8iKmR7wEHc92BGgtt7SDxeiGgO27zE9Gahwi4GidQ5A0DxlDZ7AKnyFF64F4gfk%2B9S4ny%2FEPY9dBLpMaQYYUnCqu%2BnN85dWRghZPUQfmxy3fzkUowv%2BynAS19T%2BlD%2FJXgvexEMYrr18hVaIWDuWUzkGnEZyS3aIf%2FE%2Ff6kmePCqLHg%2BLjH1gY3KH9F%2FeVLMyHVUp9HESMYebPPhmgJzXE20PBDhkeJp%2By3KvhqxZYjUgQYwQwk0qnJG8A%2F1Tj9IolZCoNQZZ1jDUzoHyo2BxNkR%2BAe68oDFugocK8MMUBaJPJgiR0VpIMo4g7mcJ1m3fqRj4PR40w9wGIpEZK1M0oGjTQEhHoGme8ExWeOsTfnz5f8gBvsE2AeoR0wIFrmf2CvBQVp0qY5sW8adbxT5BndXUfNkGJ00i6DuNHlID5r%2Fk99JSVEwYyRUiEpzlkdVR%2FIUJpZ%2FF%2F2rvIf0Ldl29%2Bn5lzt7yQxm9WLxlaR3Y8fvGLiAmO4Jz3I8WBVDA%2BAG4SjCIbe4AqX3A4AQ6jfNbiFI000kkKqAZFc2VoM%2Fv%2FB8btO8fMY5lhh35fkscTyARA%3D%3D&amp;e=mclics%2Fvariant-candidates%2B31710%2Cmclics%2Fadvertising-results-augmenter-on%2B15098%2Cmclics%2Fpseudo-search-pads-buybox%2B7708%2Cmclics%2Fmax-bid-item-factor%2B23928%2Cmclics%2Fsearch-list-ad-algorithm%2BDEFAULT%2Cmclics%2Fbuybox-layout%2B25349%2Cmclics%2Fsearch-btr-score%2B38239%2Cmclics%2Fmax-bid-capped%2B36382%2Cmclics%2Freserve-prices-versions%2B35774%2Cmclics%2Fshow-pads-global-logged-shadow%2B31033%2Cmclics%2Fdummy-search-experiment%2B29111%2Cmclics%2Fpads-score-mla%2B17263%2Cmclics%2Fshow-pads-search-lst%2B27043%2Cmclics%2Flax-top-domain%2B23443&amp;rb=x" class="ui-search-item__group__element ui-search-link__title-card ui-search-link" title="Impressora 3d Fdm Creality K1 Fechada - 1201010168 Bivolt Cor Preto 110V/220V" rel="nofollow,sponsored"><h2 aria-level="3" class="ui-search-item__title">Impressora 3d Fdm Creality K1 Fechada - 1201010168 Bivolt Cor Preto 110V/220V</h2></a><p class="ui-search-official-store-label ui-search-item__group__element ui-search-color--GRAY">por Tec Print<label for="" class="ui-search-official-store-label__cockade ui-search-icon-label"><img decoding="async" src="https://http2.mlstatic.com/frontend-assets/search-nordic/cockade.svg" class="ui-search-icon ui-search-icon--cockade" alt=""></label></p><div class="ui-search-reviews ui-search-item__group__element"><span class="andes-visually-hidden">Avaliação 4.8 de 5. 101 opiniões.</span><span class="ui-search-reviews__rating-number" aria-hidden="true">4.8</span><span class="ui-search-reviews__ratings" aria-hidden="true"><svg class="ui-search-icon ui-search-icon--star ui-search-icon--star-full" width="100%" height="100%" viewBox="0 0 10 10" fill="#3483fa" style="--darkreader-inline-fill: #3f9ffa;" data-darkreader-inline-fill=""><use href="#poly_star_fill"></use></svg><svg class="ui-search-icon ui-search-icon--star ui-search-icon--star-full" width="100%" height="100%" viewBox="0 0 10 10" fill="#3483fa" style="--darkreader-inline-fill: #3f9ffa;" data-darkreader-inline-fill=""><use href="#poly_star_fill"></use></svg><svg class="ui-search-icon ui-search-icon--star ui-search-icon--star-full" width="100%" height="100%" viewBox="0 0 10 10" fill="#3483fa" style="--darkreader-inline-fill: #3f9ffa;" data-darkreader-inline-fill=""><use href="#poly_star_fill"></use></svg><svg class="ui-search-icon ui-search-icon--star ui-search-icon--star-full" width="100%" height="100%" viewBox="0 0 10 10" fill="#3483fa" style="--darkreader-inline-fill: #3f9ffa;" data-darkreader-inline-fill=""><use href="#poly_star_fill"></use></svg><svg class="ui-search-icon ui-search-icon--star ui-search-icon--star-full" width="100%" height="100%" viewBox="0 0 10 10" fill="#3483fa" style="--darkreader-inline-fill: #3f9ffa;" data-darkreader-inline-fill=""><use href="#poly_star_fill"></use></svg></span><span class="ui-search-reviews__amount" aria-hidden="true">(101)</span></div></div><div class="ui-search-item__group ui-search-item__group--price ui-search-item__group--price-grid-container"><div class="ui-search-item__group__element ui-search-price__part-without-link"><div class="ui-search-price ui-search-price--size-medium"><div class="ui-search-price__second-line"><span class="andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript" style="font-size:24px" role="img" aria-label="3062 reais" aria-roledescription="Preço"><span class="andes-money-amount__currency-symbol" aria-hidden="true">R$</span><span class="andes-money-amount__fraction" aria-hidden="true">3.062</span></span><span class="ui-search-price__second-line__label"></span></div></div></div><span class="ui-search-item__group__element ui-search-installments ui-search-color--BLACK"><div class="ui-search-installments-prefix"><span class="">em</span></div>12x <div class="ui-search-price ui-search-price--size-x-tiny ui-search-color--BLACK"><div class="ui-search-price__second-line"><span class="andes-money-amount ui-search-price__part ui-search-price__part--x-tiny andes-money-amount--cents-superscript andes-money-amount--compact" style="font-size:16px" role="img" aria-label="294 reais com 31 centavos" aria-roledescription="Preço"><span class="andes-money-amount__currency-symbol" aria-hidden="true">R$</span><span class="andes-money-amount__fraction" aria-hidden="true">294</span><span class="andes-visually-hidden" aria-hidden="true">,</span><span class="andes-money-amount__cents andes-money-amount__cents--superscript-16" style="font-size:10px;margin-top:1px" aria-hidden="true">31</span></span></div></div></span></div><div class="ui-pb"><div class="ui-pb-container"><p class="ui-meliplus-pill meliplus--actived ui-pb-label-builder ui-meliplus-pill meliplus--actived meli_plus"><span class="ui-pb-highlight-wrapper"><span class="ui-pb-highlight-content"><span class="ui-pb-highlight" style="background: rgb(255, 255, 255); color: rgb(0, 166, 80); padding-left: 0px; padding-right: 0px; --darkreader-inline-bgcolor: #181a1b; --darkreader-inline-bgimage: none; --darkreader-inline-color: #58ffa8;" data-darkreader-inline-bgcolor="" data-darkreader-inline-bgimage="" data-darkreader-inline-color="">Frete grátis</span></span></span></p></div></div></div><div class="ui-search-item__pub-container"><label class="ui-search-styled-label ui-search-item__pub-label" style="color: rgb(115, 115, 115); --darkreader-inline-color: #9f978b;" data-darkreader-inline-color="">Patrocinado</label></div></div><div class="ui-search-result__bookmark"><form action="/search/bookmarks/MLB3521172791" class="ui-search-bookmark" method="POST"><button type="submit" class="ui-search-bookmark__btn" role="switch" aria-checked="false" aria-label="Favorito"><svg class="ui-search-icon ui-search-icon--bookmark ui-search-bookmark__icon-bookmark" viewBox="0 0 22 20" xmlns="http://www.w3.org/2000/svg"><use href="#poly_bookmark"></use></svg><svg class="ui-search-icon ui-search-icon--bookmark ui-search-bookmark__icon-bookmark-fill" viewBox="0 0 22 20" xmlns="http://www.w3.org/2000/svg"><use href="#poly_bookmark"></use></svg></button><input type="hidden" name="logginUrl" value="https://www.mercadolivre.com/jms/mlb/lgz/login?platform_id=ML&amp;go=https%3A%2F%2Flista.mercadolivre.com.br%2Fimpressora-3d&amp;loginType=explicit"><input type="hidden" name="method" value="add"><input type="hidden" name="itemId" value="MLB3521172791"></form></div></div></div>"""
        mock_response.status_code = 200

        result_item = BeautifulSoup(
            mock_response.content,
            "html.parser",
        )
        result = self.scraper.parse_result_item(result_item)

        self.assertEqual(
            result["title"],
            "Impressora 3d Fdm Creality K1 Fechada - 1201010168 Bivolt Cor Preto 110V/220V",
        )
        self.assertEqual(result["price"], "3.062")
        self.assertEqual(result["seller"], "Mercado Livre")
        self.assertEqual(result["product_id"], "MLB3521172791")
        self.assertEqual(result["reviews_rating"], "4.8")
        self.assertEqual(result["reviews_rating"], "101")


if __name__ == "__main__":
    unittest.main()