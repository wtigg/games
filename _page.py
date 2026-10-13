"""Generates privacy + support pages for each game. Usage: python3 _page.py <slug> "<App Name>" """
import sys, os
slug, name = sys.argv[1], sys.argv[2]
email = "soubigoupaul@gmail.com"
css = """body{font-family:-apple-system,system-ui,sans-serif;max-width:720px;margin:40px auto;padding:0 20px;line-height:1.6;color:#1b1d3a;background:#f6f7fb}
h1{font-size:28px}h2{font-size:19px;margin-top:28px}a{color:#4c6fff}"""
privacy = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{name} – Privacy Policy</title><style>{css}</style></head><body>
<h1>{name} – Privacy Policy</h1><p>Last updated: October 13, 2026</p>
<p>{name} ("the app") is developed by Paul Soubigou. This policy explains what data is processed when you play.</p>
<h2>Data we collect</h2><p>We do not ask for an account, your name, email or contacts. Game progress (scores, levels, settings) is stored only on your device.</p>
<h2>Advertising</h2><p>The app shows ads served by Google AdMob. AdMob may collect device identifiers (such as the IDFA, only if you allow tracking), approximate location from your IP address, and usage and diagnostic data to show and measure ads. In the EEA, UK and Switzerland you are asked for consent first, and you can change your choice at any time. See Google's policy: <a href="https://policies.google.com/technologies/ads">policies.google.com/technologies/ads</a>.</p>
<h2>In-app purchases</h2><p>Purchases are processed by Apple. We never see your payment details.</p>
<h2>Tracking</h2><p>Personalized ads use the IDFA only if you allow it in the App Tracking Transparency prompt. You can change this in iOS Settings &gt; Privacy &amp; Security &gt; Tracking.</p>
<h2>Children</h2><p>The app is not directed to children under 13 and we do not knowingly collect their data.</p>
<h2>Contact</h2><p>Questions: <a href="mailto:{email}">{email}</a></p></body></html>"""
support = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{name} – Support</title><style>{css}</style></head><body>
<h1>{name} – Support</h1>
<p>Need help, found a bug or have an idea? Email <a href="mailto:{email}?subject={name}">{email}</a> and we'll answer within 48 hours.</p>
<h2>Remove ads</h2><p>The one-time "Remove ads" purchase hides banner and interstitial ads. Already bought it on another device? Open Settings in the game and tap "Restore purchase".</p>
<p><a href="privacy.html">Privacy Policy</a></p></body></html>"""
os.makedirs(slug, exist_ok=True)
open(f"{slug}/privacy.html", "w").write(privacy)
open(f"{slug}/support.html", "w").write(support)
open(f"{slug}/index.html", "w").write(support)
