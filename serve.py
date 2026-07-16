#!/usr/bin/env python3
# a local stand-in for vercel: the site lives in html/, served at the root, with
# cleanUrls — /orient serves html/orient.html, / serves html/index.html.
# run:  python3 serve.py [port]   →  http://localhost:8000
import http.server, os, socketserver, sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'html')

class CleanURLs(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)
    def translate_path(self, path):
        p = super().translate_path(path)
        bare = p.split('?')[0].split('#')[0]
        if not os.path.exists(bare) and os.path.exists(bare + '.html'):
            return bare + '.html'
        return p

with socketserver.TCPServer(('', PORT), CleanURLs) as httpd:
    print(f'dharma.gift, locally → http://localhost:{PORT}')
    httpd.serve_forever()
