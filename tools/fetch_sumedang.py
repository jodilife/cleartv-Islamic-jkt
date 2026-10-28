import json
import urllib.request
import re
from datetime import datetime, timedelta

months_id = ["Jan", "Feb", "Mac", "Apr", "Mei", "Jun", "Jul", "Ogo", "Sep", "Okt", "Nov", "Dis"]

# Standard Kemenag RI Ihtiyat (Buffer/Pengaman waktu sholat):
# Subuh: +2 min, Dzuhur: +4 min, Ashar: +2 min, Maghrib: +3 min, Isya: 0 min
OFFSETS = {
    "Fajr": 2,
    "Dhuhr": 4,
    "Asr": 2,
    "Maghrib": 3,
    "Isha": 0
}

all_days = []

def add_minutes(time_str, minutes_to_add):
    clean = re.sub(r"[^\d:]", "", time_str).strip()
    parts = clean.split(":")
    h, m = int(parts[0]), int(parts[1])
    t = datetime(2026, 1, 1, h, m) + timedelta(minutes=minutes_to_add)
    return t.strftime("%H:%M:00")

for year in [2026, 2027]:
    for m in range(1, 13):
        url = f"https://api.aladhan.com/v1/calendar/{year}/{m}?latitude=-6.2088&longitude=106.8456&method=20"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        res = urllib.request.urlopen(req)
        data = json.loads(res.read().decode())["data"]
        for day in data:
            g_day = int(day["date"]["gregorian"]["day"])
            g_month = int(day["date"]["gregorian"]["month"]["number"])
            g_year = int(day["date"]["gregorian"]["year"])
            date_str = f"{g_day:02d}-{months_id[g_month-1]}-{g_year}"
            
            h_day = int(day["date"]["hijri"]["day"])
            h_month = int(day["date"]["hijri"]["month"]["number"])
            h_year = int(day["date"]["hijri"]["year"])
            hijri_str = f"{h_year:04d}-{h_month:02d}-{h_day:02d}"

            timings = day["timings"]
            entry = {
                "hijri": hijri_str,
                "date": date_str,
                "fajr": add_minutes(timings["Fajr"], OFFSETS["Fajr"]),
                "dhuhr": add_minutes(timings["Dhuhr"], OFFSETS["Dhuhr"]),
                "asr": add_minutes(timings["Asr"], OFFSETS["Asr"]),
                "maghrib": add_minutes(timings["Maghrib"], OFFSETS["Maghrib"]),
                "isha": add_minutes(timings["Isha"], OFFSETS["Isha"])
            }
            all_days.append(entry)

out_file = r"C:\Users\cyxor\.gemini\antigravity\scratch\cleartv-Islamic\themes\islamik\solat-JKT01.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(all_days, f, separators=(',', ':'))

print(f"Total days: {len(all_days)}, updated with Kemenag Ihtiyat buffer.")
