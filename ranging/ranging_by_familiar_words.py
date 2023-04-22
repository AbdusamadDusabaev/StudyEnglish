from text_analysis.vocabulary_analysis import get_text_vocabulary_analysis


def get_familiar_words_percentage(text_vocabulary_dict: dict, familiar_words: set) -> float:
    unknown_words_percentage = 0
    text_vocabulary_set = set(text_vocabulary_dict.keys())
    for text_word in text_vocabulary_set:
        if text_word not in familiar_words:
            unknown_words_percentage += text_vocabulary_dict[text_word]["percentage"]
    familiar_words_percentage = round(100 - unknown_words_percentage, 2)
    return familiar_words_percentage


def run():
    text = """
    More Bank Failures If Congress & Biden Can’t Cut A Debt Deal.
    Silicon Valley Bank customers listen as FDIC representatives, left, speak with them before the ... [+] opening of a branch SVBs headquarters in Santa Clara, California, on March 13, 2023. (Photo by NOAH BERGER / AFP) (Photo by NOAH BERGER/AFP via Getty Images)
    Treasury Secretary Janet L. Yellen recently tied the failure to raise the debt limit in time to the prospect of more bank failures. The Secretary is absolutely right that if Congress wants to prevent more government bailouts of banks in the short-term, it can ill afford to wait to enact a clean debt limit increase. But in order to help bring down the inflationary pressures that helped undermine Silicon Valley Bank (SVB), President Biden and Democrats must find common ground with Republicans to stabilize the national debt.
    While liberal Democrats point to the 2018 banking regulatory relief law and MAGA Republicans to so-called “woke” investments as the culprit of SVB’s collapse, the reality is that neither were to blame. First, SVB’s commitment to investments in renewable energy, community development, and affordable housing was about $16.2 billion, only 8% of its total assets. And these assets were not the ones “underwater.”
    Second, although SVB was no longer subject to the most stringent of Dodd-Frank requirements as they had been previously, the bank was not investing in high-risk assets, but rather was holding a large portfolio of one of the safest investments in finance, 20- and 30- year Treasuries.
    Unfortunately, SVB had too many of these “safe” assets on its balance sheet when the Federal Reserve began aggressively raising interest rates in 2022 to combat rapidly rising inflation. As a result, higher interest rates reduced the value of SVB’s outstanding bonds and left the bank with insufficient capital. When SVB’s depositors began pulling their money out in response to a decline in the tech sector, the bank sold $21 billion of Treasuries in a 24-hour period (at a loss of $2 billion) — leading to panic (hyper-charged by social media), a run on the bank, and soon after, insolvency.
    But rather than focusing on false narratives of what caused SVB’s failure, Democrats and Republicans should focus on how to prevent additional bank collapses — in the short- and long-term.
    In the coming weeks, Congress must send a clean debt limit increase to the president for his signature. If the U.S. government cannot pay its debts reliably, lenders will demand higher interest rates for Treasuries, leading to more bank failures.
    In addition, without a debt ceiling increase, the lending program that regulators use to keep banks liquid during financial crises (and was utilized to address the SVB collapse) would be put at risk, creating even more financial uncertainty and the potential for depositor panic.
    Once a debt limit increase is enacted, Congress and the president need to come to an agreement to significantly reduce near-term deficits. Doing so would cut demand, help lower inflation, and thereby give the nation’s central bank more flexibility as to the size and timing of future rate hikes.
    Long-term, getting the growing cost of entitlements, tax expenditures, and interest payments on the debt under control will give Congress more fiscal freedom to act in times of crisis. The national debt has jumped 54% since 2017. To restore fiscal stability and reduce the burden on future generations, everything needs to be on the table.
    More bank failures and government bailouts can be avoided. But it will require both parties to use common sense and rediscover fiscal restraint. Let’s hope Democrats and Republicans can find a path forward.
    """
    text_vocabulary_dict = get_text_vocabulary_analysis(text=text)["vocabulary_analysis_dict"]
    result = get_familiar_words_percentage(text_vocabulary_dict=text_vocabulary_dict,
                                           familiar_words={"more", "name", "me", "set"})
    print(result)


if __name__ == "__main__":
    run()
