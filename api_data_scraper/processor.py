def clean_text(text):
    if not text:
        return "N/A"
    return " ".join(text.strip().split())


def process_repositories(api_data):
    if not api_data or "items" not in api_data:
        return []

    processed = []

    for repo in api_data["items"]:
        processed_repo = {
            "name": repo.get("name", "N/A"),
            "owner": repo.get("owner", {}).get("login", "N/A"),
            "stars": repo.get("stargazers_count", 0),
            "language": repo.get("language", "N/A"),
            "url": repo.get("html_url", "N/A"),
            "description": clean_text(repo.get("description"))
        }
        processed.append(processed_repo)

    return processed


def filter_repositories(repositories, min_stars=5000):
    return [repo for repo in repositories if repo["stars"] >= min_stars]