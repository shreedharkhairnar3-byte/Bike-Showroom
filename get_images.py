"""Downloads REAL motorcycle photos from Wikimedia Commons into ./images (run once, needs internet).
Usage:  python get_images.py      (Python 3, no extra packages)"""
import json, os, shutil, time, urllib.parse, urllib.request
API = "https://commons.wikimedia.org/w/api.php"
UA = {"User-Agent": "MotoDriveBikes-College-Project/1.0 (student project)"}
BIKES = {
 "classic-350": "Royal Enfield Classic 350", "hunter-350": "Royal Enfield Hunter 350",
 "mt-15": "Yamaha MT-15", "r15": "Yamaha YZF-R15", "duke-390": "KTM 390 Duke",
 "rc-390": "KTM RC 390", "cb350": "Honda CB350", "apache-310": "TVS Apache RTR 310",
 "ns200": "Bajaj Pulsar NS200", "xtreme-160r": "Hero Xtreme 160R", "gixxer-sf-250": "Suzuki Gixxer SF 250",
 "hero": "Royal Enfield Bullet motorcycle"}
BLOGS = {"top5-under-2-lakh":"ns200","classic-350-review":"classic-350","best-college-bikes":"mt-15",
 "maintain-motorcycle":"hunter-350","duke-390-vs-mt-15":"duke-390","best-mileage-bikes":"xtreme-160r",
 "used-bike-checklist":"cb350","upcoming-2026":"rc-390"}
def get(url):
    for _ in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r: return r.read()
        except Exception as e: err = e; time.sleep(2)
    raise err
def search(term):
    p = {"action":"query","format":"json","generator":"search","gsrsearch":term+" filetype:bitmap","gsrnamespace":"6",
         "gsrlimit":"15","prop":"imageinfo","iiprop":"url|size|mime|extmetadata","iiurlwidth":"1280"}
    d = json.loads(get(API+"?"+urllib.parse.urlencode(p))).get("query",{}).get("pages",{})
    out = []
    for pg in sorted(d.values(), key=lambda x:x.get("index",99)):
        ii = pg.get("imageinfo",[{}])[0]
        if ii.get("mime")=="image/jpeg" and ii.get("width",0)>=900 and ii.get("width",0)>ii.get("height",0):
            out.append((pg["title"], ii.get("thumburl") or ii["url"], ii.get("descriptionurl","")))
    return out
os.makedirs("images", exist_ok=True); credits = []
for slug, term in BIKES.items():
    try: res = search(term)
    except Exception as e: print("FAILED", slug, e); continue
    if not res: print("NO RESULT for", term, "- add images/%s.jpg manually" % slug); continue
    for i, (title, url, page) in enumerate(res[:3]):
        name = slug + (".jpg" if i == 0 else "-%d.jpg" % i)
        try:
            open("images/"+name, "wb").write(get(url)); credits.append("%s <- %s (%s)" % (name, title, page))
            print("OK  ", name, "<-", title)
        except Exception as e: print("FAIL", name, e)
        time.sleep(1)
for blog, bike in BLOGS.items():
    if os.path.exists("images/%s.jpg" % bike): shutil.copy("images/%s.jpg" % bike, "images/blog-%s.jpg" % blog)
open("images/CREDITS.txt", "w", encoding="utf8").write("Photos from Wikimedia Commons (check each page for licence/attribution):\n" + "\n".join(credits))
print("\nDone. Open index.html. CHECK each photo matches its bike; replace any wrong one by saving a better photo with the same filename.")
