from itertools import zip_longest

import requests
from bs4 import BeautifulSoup
from pandas import DataFrame


def get_Amazon_product(product: str = "laptop") -> DataFrame:
    """
    Take a product name or category as input and return product information from Amazon
    including title, URL, price, ratings, and the discount available.
    """
    url = f"https://www.amazon.com/laptop/s?k={product}"
    header = {
        "User-Agent": """Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0""",
        "Accept-Language": "en-US, en;q=0.5",
    }
    soup = BeautifulSoup(requests.get(url, headers=header).text,"html.parser")
    # Initialize a Pandas dataframe with the column titles
    data_frame = DataFrame(
        columns=[
            "Product Title",
            "Product Link",
            "Current Price of the product",
            "Product Rating",
            "MRP of the product",
            "Discount",
        ]
    )
    # Loop through each entry and store them in the dataframe
    for item, _ in zip_longest(
        soup.find_all(
            "div",
            attrs={"class": "s-result-item", "data-component-type": "s-search-result"},
        ),
        soup.find_all("div", attrs={"class": "a-row a-size-base a-color-base"}),
    ):
        try:
            product_title = item.h2.text
            product_link = "https://www.amazon.com/" + item.h2.a["href"]
            product_price = item.find("span", attrs={"class": "a-offscreen"}).text
            try:
                product_rating = item.find("span", attrs={"class": "a-icon-alt"}).text
            except AttributeError:
                product_rating = "Not available"
            try:
                product_mrp = (
                    "₹"
                    + item.find(
                        "span", attrs={"class": "a-price a-text-price"}
                    ).text.split("₹")[0]
                )
            except AttributeError:
                product_mrp = ""
            try:
                discount = float(
                    (
                        (
                            float(product_mrp.strip("₹").replace(",", ""))
                            - float(product_price.strip("₹").replace(",", ""))
                        )
                        / float(product_mrp.strip("₹").replace(",", ""))
                    )
                    * 100
                )
            except ValueError:
                discount = float("nan")
        except AttributeError:
            pass
        data_frame.loc[len(data_frame.index)] = [
            product_title,
            product_link,
            product_price,
            product_rating,
            product_mrp,
            discount,
        ]
    data_frame.loc[
        data_frame["Current Price of the product"] > data_frame["MRP of the product"],
        "MRP of the product",
    ] = " "
    data_frame.loc[
        data_frame["Current Price of the product"] > data_frame["MRP of the product"],
        "Discount",
    ] = " "
    data_frame.index += 1
    return data_frame


if __name__ == "__main__":
    product = "smartphone"
    get_Amazon_product(product).to_csv(f"Amazon Product Data for {product}.csv")