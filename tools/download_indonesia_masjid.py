import json
import os
import time
import urllib.parse
import urllib.request
import re

UA = {"User-Agent": "clear-tv-islamic/1.0 (TV screensaver; https://github.com/Pokka99/cleartv-Islamic)"}

candidates = [
    {
        "commons": "Masjid Raya Al Jabbar 17.jpg",
        "caption": "Masjid Raya Al-Jabbar, Bandung",
        "author": "Kominfo Kota Bandung",
        "license": "CC BY-SA 4.0"
    },
    {
        "commons": "Istiqlal Mosque 31 March 2017.jpg",
        "caption": "Masjid Istiqlal, Jakarta",
        "author": "Johnstad Di Maria",
        "license": "CC BY-SA 4.0"
    },
    {
        "commons": "Meuseujid Raya Baiturrahman .jpg",
        "caption": "Masjid Raya Baiturrahman, Banda Aceh",
        "author": "Jumadal Kasim",
        "license": "CC BY-SA 3.0"
    },
    {
        "commons": "Masjid Agung Sumedang.jpg",
        "caption": "Masjid Agung Sumedang, Sumedang",
        "author": "Noval Rifaldi",
        "license": "CC BY-SA 4.0"
    },
    {
        "commons": "Masjid Agung Jawa Tengah Indonesia.jpg",
        "caption": "Masjid Agung Jawa Tengah, Semarang",
        "author": "Rizal M",
        "license": "CC BY-SA 3.0"
    },
    {
        "commons": "Masjid Islamic Center Samarinda (3).jpg",
        "caption": "Masjid Islamic Center Samarinda, Samarinda",
        "author": "Bungansanggar",
        "license": "CC BY-SA 4.0"
    },
    {
        "commons": "Sheikh Ahmad Khatib Al-Minangkabawi Grand Mosque Padang Indonesia.jpg",
        "caption": "Masjid Raya Sumatera Barat, Padang",
        "author": "Rangga Putra",
        "license": "CC BY-SA 4.0"
    },
    {
        "commons": "Masjid Raya Al Mashun Medan.jpg",
        "caption": "Masjid Raya Al-Mashun, Medan",
        "author": "Hasnan Habib",
        "license": "CC BY-SA 4.0"
    },
    {
        "commons": "Masjid Nasional Al-Akbar Surabaya-1.jpg",
        "caption": "Masjid Nasional Al-Akbar, Surabaya",
        "author": "Arief Rachman",
        "license": "CC BY 4.0"
    },
    {
        "commons": "Masjid Menara Kudus.jpg",
        "caption": "Masjid Menara Kudus, Kudus",
        "author": "Widodo",
        "license": "CC0"
    }
]

def fetch_bytes(url):
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=30) as res:
                return res.read()
        except Exception as e:
            print(f"  Retry {attempt+1}/5 on {url[:60]}: {e}", flush=True)
            time.sleep(3 * (attempt + 1))
    raise RuntimeError(f"Failed to fetch {url}")

def clean_html(raw_html):
    if not raw_html:
        return ""
    clean = re.sub(r'<.*?>', '', raw_html)
    return clean.strip()

out_dir = r"C:\Users\cyxor\.gemini\antigravity\scratch\cleartv-Islamic\themes\islamik\masjid"
captions_file = os.path.join(out_dir, "captions.json")
with open(captions_file, "r", encoding="utf-8") as f:
    captions = json.load(f)

for idx, item in enumerate(candidates):
    n = 13 + idx
    filename = f"{n:02d}.jpg"
    target_path = os.path.join(out_dir, filename)
    print(f"Processing {filename}: {item['caption']}...", flush=True)

    api = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode({
        "action": "query", "titles": "File:" + item["commons"], "prop": "imageinfo",
        "iiprop": "url|extmetadata", "iiurlwidth": 1920, "format": "json"
    })
    data = json.loads(fetch_bytes(api).decode("utf-8"))
    page = next(iter(data["query"]["pages"].values()))
    ii = page["imageinfo"][0]
    thumburl = ii["thumburl"]

    meta = ii.get("extmetadata", {})
    artist = clean_html(meta.get("Artist", {}).get("value", ""))
    lic = meta.get("LicenseShortName", {}).get("value", item["license"])
    if not artist or len(artist) > 50 or "http" in artist:
        artist = item["author"]

    img_bytes = fetch_bytes(thumburl)
    with open(target_path, "wb") as f_out:
        f_out.write(img_bytes)

    credit = f"Foto: {artist}, {lic}, Wikimedia Commons"
    captions[filename] = {
        "caption": item["caption"],
        "credit": credit
    }
    print(f"  OK {filename} ({len(img_bytes)} bytes): {item['caption']} | {credit}", flush=True)
    time.sleep(2)

with open(captions_file, "w", encoding="utf-8") as f:
    json.dump(captions, f, ensure_ascii=False, indent=1)

print(f"Done! Total photos now: {len(captions)}", flush=True)
