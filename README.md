# Media Downloader

A Flask web application for downloading video and audio from online platforms supported by [yt-dlp](https://github.com/yt-dlp/yt-dlp). Paste a URL, fetch the list of available formats, pick one, and the server downloads the selected format into a local `downloads/` folder.

## Features

- Fetch metadata and the list of available formats for a media URL
- Choose a specific format (resolution, codec, audio-only, and so on) from a dropdown
- In-page preview for URLs that expose a direct MP4 stream
- Server-side download using the selected format, saved as `<title>.<ext>`
- Works with any site yt-dlp supports (YouTube, Vimeo, SoundCloud, and many others)

## Tech stack

| Component | Version |
|-----------|---------|
| Python    | 3 |
| Flask     | 2.2.2 |
| yt-dlp    | 2024.8.3 |
| jQuery    | 3.6.0 (CDN) |
| Font Awesome | 6.0.0-beta3 (CDN) |

## Getting started

### Prerequisites

- Python 3
- FFmpeg on your `PATH` (yt-dlp needs it to merge separate audio and video streams and for some conversions)

### Install

```bash
cd pytube
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

### Run

```bash
python app.py
```

Open `http://127.0.0.1:5000`. Downloaded files are written to `pytube/downloads/`, which is created on startup.

To list the sites yt-dlp can handle:

```bash
yt-dlp --list-extractors
```

## API

| Method | Path | Description |
|--------|------|-------------|
| GET  | `/` | Web interface |
| GET  | `/api/video_info?url=<url>` | Returns the available formats for the URL as JSON |
| POST | `/download` | Form fields `url`, `format_id`; downloads the format and returns the saved `file_path` |

## Project structure

```
pytube/
├── app.py               # Flask app and yt-dlp integration
├── requirements.txt
├── templates/
│   └── index.html       # UI and client-side logic (jQuery)
└── static/
    ├── css/styles.css
    └── js/scripts.js    # Currently empty
```

## Notes and limitations

- Files are saved on the machine running the server. After a download, the page redirects to `/downloads/<file>`, but the app does not define a route that serves that folder, so retrieve the file from `pytube/downloads/` directly.
- The Video/Audio selector is sent to the server but not used; the format chosen in the format list determines what is downloaded.
- Some platforms require authentication for certain content, and site changes can break extraction. Keep yt-dlp up to date (`pip install -U yt-dlp`).
- Use this tool only for content you have the right to download, and respect each platform's terms of service and applicable copyright law.

## License

No license has been specified for this project.
