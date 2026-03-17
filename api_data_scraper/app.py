from scraper import fetch_github_repositories
from processor import process_repositories, filter_repositories
from exporter import save_to_csv, save_to_json


def display_repositories(repositories):
    if not repositories:
        print("No repositories found.")
        return

    print("\nTop Processed Repositories:\n")
    for index, repo in enumerate(repositories, start=1):
        print("=" * 80)
        print(f"#{index} {repo['name']}")
        print(f"Owner       : {repo['owner']}")
        print(f"Stars       : {repo['stars']}")
        print(f"Language    : {repo['language']}")
        print(f"URL         : {repo['url']}")
        print(f"Description : {repo['description']}")


def main():
    print("GitHub API Data Scraper")
    print("-" * 80)

    topic = input("Enter a topic to search repositories: ").strip()

    if not topic:
        print("Topic cannot be empty.")
        return

    raw_data = fetch_github_repositories(topic)
    processed_data = process_repositories(raw_data)
    filtered_data = filter_repositories(processed_data, min_stars=5000)

    display_repositories(filtered_data[:10])

    save_to_csv(filtered_data)
    save_to_json(filtered_data)


if __name__ == "__main__":
    main()