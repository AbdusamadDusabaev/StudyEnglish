import requests
from bs4 import BeautifulSoup, Tag


user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) " \
             "AppleWebKit/605.1.15 (KHTML, like Gecko) " \
             "Version/16.3 Safari/605.1.15"
headers = {"user-agent": user_agent}


def run_forbes_parser():
    article_info_list = list()
    start_url = "https://www.forbes.com/banking-insurance/"
    response = requests.get(url=start_url, headers=headers)
    bs_object = BeautifulSoup(response.content, "lxml")
    article_list = bs_object.find_all(name="h3")
    article_links = [article.a["href"] for article in article_list if "video" not in article.a["href"]]
    for article_link in article_links:
        article_info = get_forbes_article_info(article_link=article_link)
        article_info["article_url"] = article_link
        article_info_list.append(article_info)
    return article_info_list


def get_forbes_article_info(article_link):
    response = requests.get(url=article_link, headers=headers)
    bs_object = BeautifulSoup(response.content, "lxml")
    title = bs_object.find(name="h1").text.strip()
    date_of_create = get_article_date_of_create(bs_object=bs_object)
    article_content = get_article_content(bs_object=bs_object)
    text_article_content = BeautifulSoup(article_content, "lxml").text.strip()
    article_info = {
        "title": title,
        "article_content": article_content,
        "text_article_content": text_article_content,
        "date": date_of_create,
    }
    return article_info


def get_article_date_of_create(bs_object: BeautifulSoup) -> str:
    time_objects = bs_object.find(name="div", class_="contribs").find_all(name="time")
    date_of_create = " ".join([time_object.text for time_object in time_objects])
    return date_of_create


def get_article_content(bs_object: BeautifulSoup) -> str:
    article_content_list = list()
    text_valid_tags = ["p", "h1", "h2", "h3", "h4", "h5", "h6"]

    article_body = bs_object.find(name="div", class_="body-container")
    more_for_you_block = article_body.find(name="div", id="recirc-unit")
    for article_section in article_body.descendants:
        if isinstance(article_section, Tag):
            if more_for_you_block not in article_section.parents:
                if article_section.name in text_valid_tags:
                    article_section_text = article_section.text.strip()
                    article_section_name = article_section.name
                    article_section_content = f"<{article_section_name}>{article_section_text}</{article_section_name}>"
                elif article_section.name == "progressive-image":
                    article_section_src = article_section["src"]
                    article_section_content = f"<img src='{article_section_src}'>"
                else:
                    continue
                article_content_list.append(article_section_content)

    article_content = "\n".join(article_content_list)
    return article_content


if __name__ == "__main__":
    result = run_forbes_parser()
    print(result)
