# MotoDrive Bikes
Static site (HTML/CSS/JS). Deploy: push to GitHub, import in Vercel (Framework: Other, no build). Or open index.html.
## Photos (do this first)
Run `python get_images.py` once (needs internet). It downloads real photos from Wikimedia Commons into images/ and writes images/CREDITS.txt.
Then verify each photo matches its bike; replace any wrong one manually.

## Manual photos
Put real photos in `images/` named exactly:
hero.jpg, and for each bike: classic-350, hunter-350, mt-15, r15, duke-390, rc-390, cb350, apache-310, ns200, xtreme-160r, gixxer-sf-250 (.jpg)
(extra gallery shots: <bike>-1.jpg, <bike>-2.jpg). Blog images: blog-<blog-id>.jpg (e.g. blog-classic-350-review.jpg).
If a photo is missing, a styled motorcycle placeholder shows instead (never a broken image).
Use official brand press images or Wikimedia Commons / Unsplash (check licences).
