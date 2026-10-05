# Anand Kumar — Academic Website

Minimal static academic website. Shared styling: `assets/css/custom.css`.

## Preview

Run `python3 -m http.server 8000` in this folder and open http://localhost:8000.

## Update news

Open `assets/data/news.json`. Add a new entry at the top, using the same fields:

```json
{
  "date": "Oct 15, 2026",
  "duration": "Oct 15–17, 2026",
  "lead": "I will present ",
  "title": "Title of the work",
  "event": "Name of the event",
  "link": "https://example.org/",
  "suffix": ", City, Country."
}
```

Separate entries with a comma. Keep the newest entries first. The homepage shows the first three; the News page shows all entries. No HTML changes are needed. Use normal text in every field, not HTML, and preserve spaces at the end of `lead` where required. Preview through the local server to see updates.

## Profile photo

The homepage uses the warm editorial portrait in `images/portrait-ambient.png`. To replace it, update the image path in `assets/css/custom.css`. Desktop photo height follows the paragraph automatically, with contact icons outside that row. On small phones the photo stacks below the paragraph.

All pages are plain HTML and can be edited directly. No build step or external font/icon service is required.
