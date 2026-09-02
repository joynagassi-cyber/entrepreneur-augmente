# -*- coding: utf-8 -*-
"""
Bulk-verify GitHub repositories (license, stars, description, archival status)
via the GitHub REST API, which IS reachable from this sandbox (confirmed, ~5.9k
requests available unauthenticated). Used for Priority-1/Priority-2 verification
of open-source tools in the directory.
"""
import os, json, time, urllib.request, urllib.parse

CACHE_PATH = os.path.join(os.path.dirname(__file__), "output", "github_repos_cache.json")
os.makedirs(os.path.dirname(CACHE_PATH), exist_ok=True)


def load_cache():
    if os.path.exists(CACHE_PATH):
        with open(CACHE_PATH) as f:
            return json.load(f)
    return {}


def save_cache(cache):
    with open(CACHE_PATH, "w") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)


def api_repos(repos, delay=0.15):
    """repos: iterable of 'owner/name'. Returns {repo: {license, stars, desc, archived,...}}."""
    cache = load_cache()
    remaining, limit = 5900, 5900
    for repo in repos:
        if repo in cache:
            continue
        url = "https://api.github.com/repos/" + repo
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "dir-builder", "Accept": "application/vnd.github+json"})
            with urllib.request.urlopen(req, timeout=20) as r:
                d = json.loads(r.read().decode("utf-8"))
            lic = (d.get("license") or {}).get("spdx_id")
            cache[repo] = {
                "license": lic,
                "license_name": (d.get("license") or {}).get("name"),
                "stars": d.get("stargazers_count"),
                "forks": d.get("forks_count"),
                "archived": d.get("archived"),
                "description": (d.get("description") or "")[:200],
                "html_url": d.get("html_url"),
                "created_at": d.get("created_at"),
                "pushed_at": d.get("pushed_at"),
                "topics": (d.get("topics") or [])[:12],
            }
            if remaining is not None and remaining <= 1:
                break
        except urllib.error.HTTPError as e:
            if e.code == 404:
                cache[repo] = {"license": None, "not_found": True}
            elif e.code == 403:
                # rate limited
                print("RATE LIMIT hit, stopping early")
                break
            else:
                cache[repo] = {"error": str(e), "status": e.code}
        except Exception as e:
            cache[repo] = {"error": str(e)}
        time.sleep(delay)
    save_cache(cache)
    return cache


if __name__ == "__main__":
    test = ["ollama/ollama", "langflow-ai/langflow", "n8n-io/n8n"]
    c = api_repos(test)
    for k, v in c.items():
        print(k, v.get("license"), v.get("stars"))
