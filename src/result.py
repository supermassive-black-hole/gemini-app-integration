import boto3
import json
import urllib.parse as up
import urllib.request as req

ssm = boto3.client('ssm')
X_API_KEY = ssm.get_parameter(Name='/gemini-app-integration/api-key', WithDecryption=True)['Parameter']['Value']


def main(event, context):
    params = up.parse_qs(event['body'])
    request_id = params.get('request_id')

    check = {}
    if request_id:
        request = req.Request('https://info.v2.api.gemini-app.ai/requests/{0}'.format(request_id[0]),
                              headers={'X-Api-Key': X_API_KEY})
        with req.urlopen(request) as f:
            check = json.loads(f.read())

    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {'Content-Type': 'text/html'},
        'body': """<!doctype html>
<html lang=en>
<head>
<meta charset=utf-8/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Gemini Test</title>
<link rel="icon" type="image/png" href="data:image/png;base64,iVBORw0KGgo=">
</head>
<body>
<h1>Facematch result</h1>
<h3>Result from the frontend</h3>
<table>
    <tbody>
        <tr><th>Request id</th><td>{0}</td></tr>
        <tr><th>Result</th><td>{1}</td></tr>
    </tbody>
</table>
<h3>Result from the Gemini API</h3>
<table>
    <tbody>
        <tr><th>Algorithm version</th><td>{2}</td></tr>
        <tr><th>Match status</th><td>{3}</td></tr>
        <tr><th>Probability</th><td>{4}</td></tr>
        <tr><th>Confidence</th><td>{5}</td></tr>
    </tbody>
</table>
<p>
<a href="/">New Match</a>
</p>
</body>
</html>
""".format(request_id, params['match_status'][0], check.get('algorithm_version'), check.get('match_status'),
           check.get('prob'), check.get('conf'))
    }
