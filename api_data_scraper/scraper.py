import requests

GITHUB_API_URL = "https://api.github.com/search/repositories"


def fetch_github_repositories(topic, per_page=20):
    params = {
        "q": topic,
        "sort": "stars",
        "order": "desc",
        "per_page": per_page
    }

    try:
        response = requests.get(GITHUB_API_URL, params=params, timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from GitHub API: {e}")
        return None