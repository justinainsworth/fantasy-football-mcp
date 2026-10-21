#!/usr/bin/env python3
"""
Yahoo Fantasy Sports login using an HTTPS redirect URI.

Yahoo no longer accepts `oob` or plain http:// redirect URIs, so register
https://localhost:8000/callback in your Yahoo app. After you approve access,
the browser lands on that address and fails to load (nothing listens there).
Paste the full address from the browser bar here and the tokens are saved
to .env in the repo root.
"""

import os
import sys
import webbrowser
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlparse

import requests
from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
os.chdir(REPO_ROOT)  # save_tokens writes .env relative to cwd
load_dotenv(REPO_ROOT / ".env")

from reauth_yahoo import get_user_guid, save_tokens  # noqa: E402

AUTH_URL = "https://api.login.yahoo.com/oauth2/request_auth"
TOKEN_URL = "https://api.login.yahoo.com/oauth2/get_token"
REDIRECT_URI = os.getenv("YAHOO_REDIRECT_URI", "https://localhost:8000/callback")
# Ask for Fantasy Sports explicitly; apps that also have OpenID otherwise get profile-only tokens.
# Use fspt-w once Yahoo grants Read/Write.
SCOPE = os.getenv("YAHOO_SCOPE", "fspt-r")


def main():
    client_id = os.getenv("YAHOO_CONSUMER_KEY") or os.getenv("YAHOO_CLIENT_ID")
    client_secret = os.getenv("YAHOO_CONSUMER_SECRET") or os.getenv("YAHOO_CLIENT_SECRET")
    if not client_id or not client_secret:
        print("❌ Add YAHOO_CONSUMER_KEY and YAHOO_CONSUMER_SECRET to .env first")
        return 1

    url = AUTH_URL + "?" + urlencode({
        "client_id": client_id,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": SCOPE,
        "language": "en-us",
    })
    print(f"📌 Redirect URI: {REDIRECT_URI} (must match your Yahoo app exactly)\n")
    print("1. Sign in to Yahoo and click Agree. If no browser opens, visit:\n")
    print(f"   {url}\n")
    webbrowser.open(url)
    print("2. The browser will show a page that can't load. That's expected.")
    pasted = input("3. Paste the full address from the browser bar here: ").strip()

    code = parse_qs(urlparse(pasted).query).get("code", [None])[0] or pasted
    response = requests.post(TOKEN_URL, data={
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": REDIRECT_URI,
        "code": code,
        "grant_type": "authorization_code",
    })
    if response.status_code != 200:
        print(f"❌ Token exchange failed ({response.status_code}): {response.text}")
        return 1

    tokens = response.json()
    guid = get_user_guid(tokens["access_token"])
    save_tokens(tokens["access_token"], tokens["refresh_token"], guid)
    print("\n✅ Logged in. Tokens saved to .env" + ("" if guid else " (GUID not found)"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
