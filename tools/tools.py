from langchain.serpapi import SerpAPIWrapper

def get_profile_url(text: str) -> str:
    """
    Search for a Linkedin profile page
    """
    search = SerpAPIWrapper()
    res = search.run(f"{text}")
    
    return res