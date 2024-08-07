from flask import Flask, request, jsonify, send_file, render_template
import yt_dlp as ytdlp
import os

app = Flask(__name__)
DOWNLOAD_FOLDER = 'downloads'
app.config['UPLOAD_FOLDER'] = DOWNLOAD_FOLDER

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/video_info', methods=['GET'])
def get_video_info():
    url = request.args.get('url')
    ydl_opts = {
        'quiet': True,
        'noplaylist': True,
        'format': 'bestaudio/best',
        'simulate': True,
    }
    try:
        with ytdlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info.get('formats', [])
            return jsonify({'formats': formats})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    format_id = request.form.get('format_id')
    media_type = request.form.get('media-type')

    ydl_opts = {
        'format': format_id,
        'outtmpl': os.path.join(app.config['UPLOAD_FOLDER'], '%(title)s.%(ext)s'),
    }
    
    try:
        with ytdlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)
            return jsonify({'file_path': file_path})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
