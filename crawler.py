#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Crawler HTML récursif - Projet 1
Découvre toutes les pages d’un site web jusqu’à une certaine profondeur.

Copyright (c) 2025 Virginie Lechene
License: MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

visited = set()

def crawl(url, target, depth=0, max_depth=2):
    """Crawl récursif simple."""
    if depth > max_depth or url in visited:
        return
    visited.add(url)
    print(f"[+] {url}")
    try:
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        for a in soup.find_all("a", href=True):
            link = urljoin(url, a["href"])
            if urlparse(link).netloc == urlparse(target).netloc:
                crawl(link, target, depth + 1, max_depth)
    except Exception:
        pass

if __name__ == "__main__":
    start = "http://192.168.100.10:3000"  # URL cible (Juice Shop)
    crawl(start, start)
    print(f"\nExploration terminée — {len(visited)} pages trouvées.")
