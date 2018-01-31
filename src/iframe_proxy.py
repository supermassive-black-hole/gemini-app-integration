import urllib.request as req


def main(event, context):
    with req.urlopen("https://api.gemini-app.ai/static-assets/gemini_app.html") as f:
        iframe = f.read().decode("utf-8")
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {'Content-Type': 'text/html'},
        'body': iframe
    }
