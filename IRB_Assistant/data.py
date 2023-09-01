import time
from datetime import datetime
from urllib.error import HTTPError

from Bio import Entrez


def search_pubmed_articles(
    pubmed_string, email, max_results=10, streamlit_context=False, max_retries=3, delay_seconds=5
):
    """
    The function `search_pubmed_articles` takes a PubMed search string, an email address, and an
    optional maximum number of results, and returns a list of PubMed article IDs that match the search
    criteria.

    Args:
      pubmed_string: The search query string for PubMed.
      email: The email address associated with your NCBI account.
      max_results: Optional; maximum number of results to retrieve (default 10).
      streamlit_context: Optional; a boolean flag indicating whether the code is running within a Streamlit app (default False).
      max_retries: Optional; the maximum number of retry attempts if an HTTP error occurs (default 3).
      delay_seconds: Optional; the number of seconds to wait between retry attempts (default 5).

    Returns:
      A list of PubMed article IDs that match the search criteria.
    """
    Entrez.email = email

    for attempt in range(max_retries + 1):
        try:
            handle = Entrez.esearch(
                db="pubmed", term=pubmed_string, sort="relevance", retmax=max_results
            )
            record = Entrez.read(handle)
            handle.close()
            return record["IdList"]
        except HTTPError as e:
            error_message = f"PubMed didn't respond (attempt {attempt + 1}/{max_retries}): {e}"
            if attempt < max_retries:
                wait_message = f"Waiting {delay_seconds} seconds before trying PubMed again..."
                print(error_message)
                print(wait_message)
                if streamlit_context:
                    import streamlit as st

                    st.warning(error_message)
                    st.warning(wait_message)
                time.sleep(delay_seconds)
            else:
                final_message = "Giving up on PubMed. It was an issue on their end. You may want to try again later."
                print(error_message)
                print(final_message)
                if streamlit_context:
                    import streamlit as st

                    st.warning(error_message)
                    st.warning(final_message)
                return []


import time
from urllib.error import HTTPError


def fetch_article_details(pubmed_ids, max_retries=3, delay_seconds=5, streamlit_context=False):
    """
    The function fetches article details from PubMed using the provided PubMed IDs.

    Args:
      pubmed_ids: A list of strings where each string represents the PubMed ID (PMID)
                  of the article you want to fetch details for.
      max_retries: The maximum number of retry attempts if an HTTP error occurs. Default is 3.
      delay_seconds: The number of seconds to wait between retry attempts. Default is 5.
      streamlit_context: A boolean flag indicating whether the code is running within a Streamlit app. Default is False.

    Returns:
      A list of dictionaries, where each dictionary contains the details of an article with the given PubMed ID.
    """
    ids_string = ",".join(pubmed_ids)

    for attempt in range(max_retries + 1):
        try:
            handle = Entrez.efetch(db="pubmed", id=ids_string, retmode="xml")
            articles = Entrez.read(handle)["PubmedArticle"]
            handle.close()
            return articles
        except HTTPError as e:
            error_message = f"PubMed didn't respond (attempt {attempt + 1}/{max_retries}): {e}"
            if attempt < max_retries:
                wait_message = f"Waiting {delay_seconds} seconds before trying PubMed again..."
                print(error_message)
                print(wait_message)
                if streamlit_context:
                    import streamlit as st

                    st.warning(error_message)
                    st.warning(wait_message)
                time.sleep(delay_seconds)
            else:
                final_message = "Giving up on PubMed. It was an issue on their end. You may want to try again later."
                print(error_message)
                print(final_message)
                if streamlit_context:
                    import streamlit as st

                    st.warning(error_message)
                    st.error(final_message)
                return []


def format_authors(author_list):
    """
    The function `format_authors` takes a list of dictionaries representing authors and returns a
    formatted string of their last names followed by initials.

    Args:
      author_list: A list of dictionaries, where each dictionary represents an author and contains the
    keys "LastName" and "Initials".

    Returns:
      a formatted string of authors' names in the format "Last Name, Initials."
    """
    formatted_authors = []
    for author in author_list:
        last_name = author.get("LastName", "")
        initials = author.get("Initials", "")
        formatted_authors.append(f"{last_name}, {initials}.")
    return ", ".join(formatted_authors)


def format_apa_citation(article, article_id):
    """
    The function `format_apa_citation` takes in an article and its ID and returns a formatted APA
    citation string.

    Args:
      article: The `article` parameter is a dictionary that contains information about a specific
    article. It should have the following structure:
      article_id: The article_id parameter is the unique identifier for the article. It is used to
    include the PMID (PubMed ID) in the APA citation format.

    Returns:
      a formatted APA citation for an article, including the authors, publication year, title, journal,
    volume, pages, and PMID (PubMed ID).
    """
    try:
        authors = format_authors(article["MedlineCitation"]["Article"]["AuthorList"])
    except KeyError:
        authors = ""

    try:
        title = article["MedlineCitation"]["Article"]["ArticleTitle"]
    except KeyError:
        title = ""

    try:
        journal = article["MedlineCitation"]["Article"]["Journal"]["Title"]
    except KeyError:
        journal = ""

    try:
        pub_year = datetime.strptime(
            article["MedlineCitation"]["Article"]["Journal"]["JournalIssue"]["PubDate"]["Year"],
            "%Y",
        ).year
    except KeyError:
        pub_year = ""

    try:
        volume = article["MedlineCitation"]["Article"]["Journal"]["JournalIssue"]["Volume"]
    except KeyError:
        volume = ""

    try:
        pages = article["MedlineCitation"]["Article"]["Pagination"]["MedlinePgn"]
    except KeyError:
        pages = ""

    return f"{authors} ({pub_year}). {title} {journal}, {volume}, {pages}. PMID: {article_id}"
