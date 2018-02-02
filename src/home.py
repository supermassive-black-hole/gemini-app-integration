import boto3
import json
import urllib.request as req

ssm = boto3.client('ssm')
X_API_KEY = ssm.get_parameter(Name='/gemini-app-integration/api-key', WithDecryption=True)['Parameter']['Value']


def main(event, context):
    request = req.Request(url='https://api.gemini-app.ai/server-compute/token', method='POST',
                          headers={'X-Api-Key': X_API_KEY})
    with req.urlopen(request) as f:
        token = json.loads(f.read())['token']
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {'Content-Type': 'text/html'},
        'body': """<!doctype html>
<html lang=en>
<head>
<meta charset=utf-8/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Gemini App Integration</title>
<link rel="icon" type="image/png" href="data:image/png;base64,iVBORw0KGgo=">
</head>
<body>
  <form action="/Prod/result" method="post">
  <script src="https://api.gemini-app.ai/static-assets/gemini.js" type="text/javascript" class="gemini-button" data-api-token="{0}" data-iframe-path="{1}"></script>
</form>
</body>
</html>
""".format(token, '/Prod/iframe')
    }
