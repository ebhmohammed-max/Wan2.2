#!/usr/bin/env python3
"""Stream a file into a pre-authorised Google Drive resumable-upload session (runs on CI).

usage: ci_drive_upload.py FILE SESSION_URI_FILE  -> prints the Drive file JSON
The session URI comes from Arena's google_drive.initiate_resumable_upload. It only allows
uploading this one new file, and it expires after 7 days.
The session uses Google's X-Goog-Upload protocol:
  each chunk is PUT with X-Goog-Upload-Command: upload (the last one: "upload, finalize") plus
  X-Goog-Upload-Offset; X-Goog-Upload-Status in the response is active / final.
"""
import json, os, sys, time, urllib.error, urllib.request

CH = 32 * 256 * 1024  # 8 MiB, a multiple of 256 KiB


def call(uri, headers, data=b'', method='PUT'):
    req = urllib.request.Request(uri, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            return r.status, r.headers, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.headers, e.read()


def main():
    path, sess_file = sys.argv[1], sys.argv[2]
    uri = open(sess_file).read().strip()
    total = os.path.getsize(path)
    method = 'PUT'
    st, h, body = call(uri, {'X-Goog-Upload-Command': 'query', 'Content-Length': '0'}, method=method)
    if st == 405:
        method = 'POST'
        st, h, body = call(uri, {'X-Goog-Upload-Command': 'query', 'Content-Length': '0'}, method=method)
    print(f'query: HTTP {st} status={h.get("X-Goog-Upload-Status")} received={h.get("X-Goog-Upload-Size-Received")}',
          file=sys.stderr)
    off = int(h.get('X-Goog-Upload-Size-Received') or 0) if st == 200 else 0
    with open(path, 'rb') as f:
        while off < total:
            f.seek(off)
            data = f.read(CH)
            last = off + len(data) >= total
            hdr = {'X-Goog-Upload-Command': 'upload, finalize' if last else 'upload',
                   'X-Goog-Upload-Offset': str(off), 'X-Goog-Upload-Total-Size': str(total),
                   'Content-Length': str(len(data)), 'Content-Type': 'video/mp4'}
            ok = False
            for k in range(6):
                st, h, body = call(uri, hdr, data, method)
                if st in (200, 201):
                    ok = True
                    break
                if st == 400 and 'X-Goog-Upload-Total-Size' in hdr:
                    print(f'HTTP 400 with Total-Size header, retrying without: {body[:200]}', file=sys.stderr)
                    hdr.pop('X-Goog-Upload-Total-Size')
                    continue
                if k == 5 or (400 <= st < 500 and st not in (408, 429)):
                    raise SystemExit(f'upload failed at {off}: HTTP {st} {body[:300]}')
                time.sleep(2 ** k)
                q = call(uri, {'X-Goog-Upload-Command': 'query', 'Content-Length': '0'}, method=method)
                if q[0] == 200 and q[1].get('X-Goog-Upload-Size-Received'):
                    off = int(q[1]['X-Goog-Upload-Size-Received'])
                    break
            if not ok:
                continue
            status = h.get('X-Goog-Upload-Status')
            if status == 'final' or last:
                print(body.decode('utf-8', 'ignore') or json.dumps({'status': status}))
                return
            off += len(data)
            if (off // CH) % 25 == 0:
                print(f'{off}/{total}', file=sys.stderr)


if __name__ == '__main__':
    main()
