import requests
from bs4 import BeautifulSoup, Tag


user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) " \
             "AppleWebKit/605.1.15 (KHTML, like Gecko) " \
             "Version/16.3 Safari/605.1.15"
headers = {"user-agent": user_agent}

bbc_domain = "https://www.bbc.com"
category_urls = ["https://www.bbc.com/news/world-60525350"]


def bbc():
    article_info_list = list()
    for category_url in category_urls:
        response = requests.get(url=category_url, headers=headers)
        bs_object = BeautifulSoup(response.content, "lxml")
        article_list = bs_object.find(name="ol", class_="lx-stream__feed").find_all(name="article")
        article_links = get_article_links(article_list=article_list)
        for article_link in article_links:
            try:
                article_info = get_bbc_article_info(article_link=article_link)
                article_info["article_url"] = article_link
                article_info_list.append(article_info)
            except Exception as ex:
                print(f"[ERROR] -> {article_link}: {ex}")
    return article_info_list


def get_article_links(article_list: list) -> list:
    article_h3_tag_list = [article.h3 for article in article_list if article.h3 is not None]
    all_article_links = [bbc_domain + article_h3_tag.a["href"]
                         for article_h3_tag in article_h3_tag_list
                         if article_h3_tag.a is not None]
    article_links = [article_link for article_link in all_article_links if "/live/" not in article_link]
    return article_links


def get_bbc_article_info(article_link):
    response = requests.get(url=article_link, headers=headers)
    bs_object = BeautifulSoup(response.content, "lxml")
    title = bs_object.h1.text.strip()
    date_of_create = bs_object.time["datetime"].replace("T", " ").split(".")[0]
    article_content = get_article_content(bs_object=bs_object)
    text_article_content = BeautifulSoup(article_content, "lxml").text
    article_info = {
        "title": title,
        "article_content": article_content,
        "text_article_content": text_article_content,
        "date": date_of_create,
    }
    return article_info


def get_article_content(bs_object: BeautifulSoup) -> str:
    article_content_list = list()
    text_valid_tags = ["p", "h1", "h2", "h3", "h4", "h5", "h6"]

    article_body = bs_object.find(name="article")
    for article_section in article_body.descendants:
        if isinstance(article_section, Tag):
            if article_section.name in text_valid_tags:
                article_section_text = article_section.text.strip()
                article_section_name = article_section.name
                article_section_content = f"<{article_section_name}> {article_section_text} </{article_section_name}>"
            elif article_section.name == "img":
                article_section_src = article_section["src"]
                article_section_content = f"<img src='{article_section_src}'>"
            else:
                continue
            article_content_list.append(article_section_content)

    article_content = "\n".join(article_content_list)
    return article_content


if __name__ == "__main__":
    result = bbc()
    print(result)
