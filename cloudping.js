const request = require('request');

var regions = ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2', 'ca-central-1', 'eu-west-1', 'eu-west-2', 'eu-central-1', 'ap-south-1', 'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'sa-east-1', 'cn-north-1', 'us-gov-west-1'];
var length = regions.length;

doTest();

function doTest() {
  for (var i = 0; i < length; i++) {
    ping_endpoint(regions[i]);
  }
}

async function ping_endpoint(region) {
  var postfix = region.startsWith('cn-') ? '.amazonaws.com.cn/ping' : '.amazonaws.com/ping';
  var endpoint = 'http://dynamodb.' + region + postfix;
  var startTime = currentTimeMillis();
  request(endpoint, { json: true }, (err, res, body) => {
    if (err) { return console.log(err); }
    var endTime = currentTimeMillis();
    var elapsed = endTime - startTime;
    var resultText = elapsed.toString() + " ms";
    console.log(region + ": " + resultText);
  });

}

function currentTimeMillis() {
  return (new Date()).getTime();
}
